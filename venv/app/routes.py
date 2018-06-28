from flask import render_template
from app import app
from app.utils import Utils
from app.forms import LcdForm
from mygpio import gpio
import time


@app.route('/')
@app.route('/index')
def index():
    environment = "Raspberry PI"
    if Utils.is_simulator():
        environment = "Simulator"
    return render_template('index.html', title='Index', env=environment)


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


@app.route('/sample_lcd')
def sample_lcd():
    my_gpio = gpio.MyGPIO()
    my_gpio.lcd_text('Ciao mondo!')
    return render_template('result.html', title='Sample LCD Display', result_text="Command sent to LCD Display")


@app.route('/lcd')
def lcd():
    form = LcdForm()
    return render_template('lcd.html', title='LCD Display', form=form)

