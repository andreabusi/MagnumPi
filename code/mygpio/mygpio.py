from app.utils import Utils
import json
if Utils.is_simulator():
    # on Simulator (or non RaspberryPI environment), a fake library is used to simulate GPIO
    import fakeRPi.GPIO as GPIO
    import fakeRPi.RPi_I2C_driver as RPi_I2C_driver
else:
    import RPi.GPIO as GPIO
    import RPi_I2C_driver


class MyGPIO:
    LCD_ROW_WIDTH = 20
    LCD_ROW_NUMBERS = 4

    def __init__(self):
        self.name = "GPIO"
        configuration = json.load(open("resources/pins.json"))
        self.pins = configuration['pins']
        try:
            self.mylcd = RPi_I2C_driver.lcd(address=0x3f)
        except:
            self.mylcd = None

    # GPIO management

    def get_pin_info(self, pin):
        pin_item = list(filter(lambda x: x['pin'] == pin, self.pins))
        if pin_item[0]['type'] == 'GND' or pin_item[0]['type'] == 'VCC':
            return None
        return pin_item[0]

    def get_pins(self):
        return self.pins

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

    # LCD management

    def is_lcd_connected(self):
        """Check if the LCD display is connected to the device"""
        return self.mylcd is not None

    def lcd_clear(self):
        """Reset the text on the current connected LCD display"""
        if self.is_lcd_connected():
            self.mylcd.lcd_clear()
            return True
        return False

    def lcd_display_rowtext(self, text, row):
        """Display a text on the LCD display for a given row"""
        if row > self.LCD_ROW_WIDTH or not self.is_lcd_connected():
            return False

        self.mylcd.lcd_display_string(text, row)
        return True

    def lcd_display_text(self, text):
        """Display a generic text on the LCD display

        Text will be splitted into multiple lines if required.
        Every line will be max LCD_WIDTH chars long.
        Max rows are LCD_ROWS_NUMBER, so the remaining text will be discarded,
        """
        if not self.is_lcd_connected():
            return False

        lines = []
        words = text.split(" ")
        current_line = ""
        for word in words:
            if len(current_line) + len(word) > self.LCD_ROW_WIDTH and len(lines) < self.LCD_ROW_NUMBERS:
                lines.append(current_line)
                current_line = ""
            current_line += word + " "

        lines.append(current_line)

        for row, line in enumerate(lines):
            self.mylcd.lcd_display_string(line, row + 1)

        return True
