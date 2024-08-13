from RPLCD.i2c import CharLCD


class Lcd:
    
    def __init__(self):
        try:
            self.lcd = CharLCD(
                i2c_expander='PCF8574',
                address=0x3f,
                port=1,
                cols=20,
                rows=4,
                dotsize=8
            )
            print("LCD OK")
        except:
            print("LCD KABOM")
            self.lcd = None
    

    def is_connected(self):
        """Check if the LCD display is connected to the device"""
        return self.lcd is not None
    

    def clear(self):
        """Reset the text on the current connected LCD display"""
        if self.is_connected():
            self.lcd.clear()
            return True
        return False


    def lcd_text(self, text):
        if self.is_connected():
            self.lcd.write_string(text)
            return True
        return False