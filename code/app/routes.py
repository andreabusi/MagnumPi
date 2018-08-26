from flask import render_template, redirect, url_for
from app import app
from app.utils import Utils
from app.forms import LcdForm, LedForm
from app.view_models import TaskViewModel
from app.tasks_helpers import TasksHelpers
from mygpio import mygpio


@app.route('/')
@app.route('/index')
def index():
    environment = "Raspberry PI"
    if Utils.is_simulator():
        environment = "Simulator"
    return render_template('index.html', title='Index', env=environment)


@app.route('/gpio')
def gpio():
    return render_template('result.html', title='GPIO', result_text='Not yet implemented :)')


@app.route('/led_blink', methods=['GET', 'POST'])
def led_blink():
    form = LedForm()
    if form.validate_on_submit():
        rq_job = app.task_queue.enqueue('app.tasks.gpio_blink_pin', form.pin.data, form.repetitions.data, 1)
        return render_template('led_blink.html', title='LED Blinking', result_text="Led %s will blink for %s times" % (form.pin.data, form.repetitions.data), form=form)
    return render_template('led_blink.html', title='LED Blinking', form=form)


@app.route('/lcd', methods=['GET', 'POST'])
def lcd():
    form = LcdForm()
    if form.validate_on_submit():
        my_gpio = mygpio.MyGPIO()
        result = my_gpio.lcd_text(form.lcd_text.data)
        if result == True:
            message = "Text sent to display: '%s'" % form.lcd_text.data
            return render_template('lcd.html', title='LCD Display', info_message=message, form=form)
        else:
            error = "Error when sending message to LCD, make sure that is properly connected"
            return render_template('lcd.html', title='LCD Display', error_message=error, form=form)

    my_gpio = mygpio.MyGPIO()
    error = None
    if not my_gpio.is_lcd_connected():
        error = "There is no LCD connected!"
    return render_template('lcd.html', title='LCD Display', error_message=error, form=form)


@app.route('/lcd_clear')
def lcd_clear():
    my_gpio = mygpio.MyGPIO()
    result = my_gpio.lcd_clear()
    error = None
    if not result:
        error = "Error when sending clear command to LCD, make sure that is properly connected"
    form = LcdForm()
    return render_template('lcd.html', title='LCD Display', error_message=error, form=form)


@app.route('/tasks')
def tasks():
    helpers = TasksHelpers(app.config['QUEUE_BACKGROUND_TASKS'], connection=app.redis)

    model = TaskViewModel()
    model.running_jobs = helpers.get_running_jobs()
    model.queued_job_ids = app.task_queue.job_ids
    model.expired_job_ids = helpers.get_expired_jobs()

    return render_template('task.html', title='Background Tasks', model=model)


@app.route('/task/create')
def task_create():
    _ = app.task_queue.enqueue('app.tasks.example', 23)
    return redirect(url_for('tasks'))


@app.route('/task/cancel/<job_id>', methods=['GET'])
def task_cancel(job_id):
    helpers = TasksHelpers(app.config['QUEUE_BACKGROUND_TASKS'], connection=app.redis)
    helpers.cancel_job(job_id)
    return redirect(url_for('tasks'))
