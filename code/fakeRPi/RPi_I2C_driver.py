"""
Fake class to simulate RPi_I2C_driver.py library outside a Raspberry PI
"""

class lcd:
    def __init__(self, address):
        self.name = "LCD"
        self.address = address

    # put string function
    def lcd_display_string(self, string, line):
        print("[I2C_LCD] {0}: {1}".format(line, string))

    # define precise positioning
    def lcd_display_string_pos(self, string, line, pos):
        print("[I2C_LCD] {0:1}: {2}".format(line, pos, string))

    # clear lcd and set to home
    def lcd_clear(self):
        print("[I2C_LCD] Clear screen")
