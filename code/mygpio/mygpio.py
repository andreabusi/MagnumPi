from app.utils import Utils
# when the app runs on a non raspberry environment, a fake library will be imported
if Utils.is_simulator():
    import fakeRPi.GPIO as GPIO
    import fakeRPi.RPi_I2C_driver as RPi_I2C_driver
else:
    import RPi.GPIO as GPIO
    import RPi_I2C_driver


class MyGPIO:
    def __init__(self):
        self.name = "GPIO"
        try:
            self.mylcd = RPi_I2C_driver.lcd(address=0x3f)
        except:
            self.mylcd = None

    def is_lcd_connected(self):
        return self.mylcd is not None

    def lcd_text(self, text):
        if self.is_lcd_connected():
            self.mylcd.lcd_display_string(text, 1)
            return True
        return False

    def lcd_clear(self):
        if self.is_lcd_connected():
            self.mylcd.lcd_clear()
            return True
        return False

    @staticmethod
    def configure():
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    @staticmethod
    def turn_on(pin):
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)

    @staticmethod
    def turn_off(pin):
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    @staticmethod
    def input(pin):
        GPIO.setup(pin, GPIO.IN)
        return GPIO.input(pin)

