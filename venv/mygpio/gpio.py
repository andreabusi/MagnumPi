from app.utils import Utils
# when the app runs on a non raspberry environment, a fake library will be imported
try:
    import RPi.GPIO as GPIO
except ImportError:
    import fakeRPi.GPIO as GPIO
try:
    import I2C_LCD_driver # TODO: come faccio a farla puntare alla libreria corretta?
except ImportError:
    import fakeRPi.I2C_LCD_driver as I2C_LCD_driver


class MyGPIO:
    def __init__(self):
        self.name = "GPIO"
        self.mylcd = I2C_LCD_driver.lcd()

    def lcd_text(self, text):
        self.mylcd.lcd_display_string(text, 1)

    @staticmethod
    def configure():
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    @staticmethod
    def turn_on(pin):
        GPIO.output(pin, GPIO.HIGH)

    @staticmethod
    def turn_off(pin):
        GPIO.output(pin, GPIO.LOW)

