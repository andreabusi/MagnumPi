from time import sleep
from gpiozero import LED


def turn_led_on(pin, on_time: int = 1000):
    led = LED(pin)
    led.on()
    sleep(on_time)


def turn_led_off(pin, off_time: int = 1000):
    led = LED(pin)
    led.off()
    sleep(off_time)


### TASKS

def blink_led(pin, repetitions, pause_time):
    led = LED(pin)

    sleep_time = pause_time / 1000
    for i in range(repetitions):
        led.on()
        sleep(sleep_time)
        led.off()
        sleep(sleep_time)