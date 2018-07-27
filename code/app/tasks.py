import time
from rq import get_current_job
from mygpio import gpio


def example(seconds):
    job = get_current_job()
    print('Starting task')
    for i in range(seconds):
        job.meta['progress'] = 100.0 * i / seconds
        job.save_meta()
        print(i)
        time.sleep(1)
    job.meta['progress'] = 100.0
    job.save_meta()
    print('Task completed')


def gpio_blink_pin(pin, repetitions, pause_time):
    my_gpio = gpio.MyGPIO()
    my_gpio.configure()

    for i in range(repetitions):
        my_gpio.turn_on(pin)
        time.sleep(pause_time)
        my_gpio.turn_off(pin)
        time.sleep(pause_time/2)