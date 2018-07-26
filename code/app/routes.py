from flask import render_template, redirect, url_for
from app import app
from app.utils import Utils
from app.forms import LcdForm
from app.view_models import TaskViewModel
from mygpio import gpio
from rq.registry import StartedJobRegistry
import redis
import rq
import time


@app.route('/')
@app.route('/index')
def index():
    environment = "Raspberry PI"
    if Utils.is_simulator():
        environment = "Simulator"
    return render_template('index.html', title='Index', env=environment)


@app.route('/gpio')
def route_gpio():
    my_gpio = gpio.MyGPIO()
    my_gpio.configure()
    state = my_gpio.input(25)
    return render_template('result.html', title='Sample GPIO', result_text="State for pin %s is %s" % (25, state))


@app.route('/sample_gpio')
def sample_gpio():
    # sample
    PIN_LED_RED = 17
    PIN_LED_GREEN = 19

    my_gpio = gpio.MyGPIO()
    my_gpio.configure()

    for i in range(3):
        my_gpio.turn_on(PIN_LED_RED)
        time.sleep(1)
        my_gpio.turn_off(PIN_LED_RED)
        time.sleep(1)

    return render_template('result.html', title='Sample GPIO', result_text="GPIO commands executed!")


@app.route('/lcd', methods=['GET', 'POST'])
def lcd():
    form = LcdForm()
    if form.validate_on_submit():
        my_gpio = gpio.MyGPIO()
        my_gpio.lcd_text(form.lcd_text.data)
        return render_template('lcd.html', title='LCD Display', previous_text=form.lcd_text.data, form=form)
    return render_template('lcd.html', title='LCD Display', form=form)


@app.route('/lcd_clear')
def lcd_clear():
    my_gpio = gpio.MyGPIO()
    my_gpio.lcd_clear()
    form = LcdForm()
    return render_template('lcd.html', title='LCD Display', form=form)


@app.route('/tasks')
def tasks():
    registry = StartedJobRegistry(app.config['QUEUE_BACKGROUND_TASKS'], connection=app.redis)

    model = TaskViewModel()
    model.running_job_ids = registry.get_job_ids()
    model.queued_job_ids = app.task_queue.job_ids
    model.expired_job_ids = registry.get_expired_job_ids()

    return render_template('task.html', title='Background Tasks', model=model)


@app.route('/task/create')
def create_task():
    rq_job = app.task_queue.enqueue('app.tasks.example', 23)
    return redirect(url_for('tasks'))


@app.route('/task/<job_id>', methods=['GET'])
def get_rq_job(job_id):
    try:
        rq_job = rq.job.Job.fetch(job_id, connection=app.redis)
    except (redis.exceptions.RedisError, rq.exceptions.NoSuchJobError):
        rq_job = None
    percentage = rq_job.meta.get('progress', 0) if rq_job is not None else 100
    result = 'Completion percentage: %s' % percentage
    return render_template('result.html', title='Background Task', result_text=result)
