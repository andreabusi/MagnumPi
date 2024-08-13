from time import sleep
from rq import get_current_job
from gpiozero import LED


def example(seconds):
    job = get_current_job()
    print('Starting task')
    for i in range(seconds):
        job.meta['progress'] = 100.0 * i / seconds
        job.save_meta()
        print(i)
        sleep(1)
    job.meta['progress'] = 100.0
    job.save_meta()
    print('Task completed')


def gpio_blink_pin(pin, repetitions, pause_time):
    led = LED(pin)

    sleep_time = pause_time / 1000
    for i in range(repetitions):
        led.on()
        sleep(sleep_time)
        led.off()
        sleep(sleep_time)
