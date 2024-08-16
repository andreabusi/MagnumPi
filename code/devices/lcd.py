from app.utils import Utils
if Utils.is_simulator():
    from devices.mock.mock_rplcd import CharLCD
else:
    from RPLCD.i2c import CharLCD


class Lcd:
    
    def __init__(self):
        self.columns = 20
        self.rows = 4

        try:

            self.lcd = CharLCD(
                i2c_expander='PCF8574',
                address=0x3f,
                port=1,
                cols=self.columns,
                rows=self.rows,
                dotsize=8
            )
        except:
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


    def write_text(self, text: str, new_line: bool = False) -> bool:
        """Write text to display"""
        if self.is_connected():
            if new_line:
                self.lcd.crlf()
            self.lcd.write_string(text)
            return True
        return False
    

    def write_rows(self, rows: list):
        """Write multiple text rows"""
        if not self.is_connected():
            return False

        self.lcd.clear()
        for i in range(0, len(rows)):
            row = rows[i]
            if len(row) > self.columns:
                row = f"{row[:self.columns - 1]}…"
            self.lcd.cursor_pos = (i, 0)
            self.lcd.write_string(row)
        return True
