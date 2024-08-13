# # # Helper classes # # #

# Flags for display entry mode
LCD_ENTRYRIGHT = 0x00
LCD_ENTRYLEFT = 0x02
LCD_ENTRYSHIFTINCREMENT = 0x01
LCD_ENTRYSHIFTDECREMENT = 0x00

# Flags for display on/off control
LCD_DISPLAYON = 0x04
LCD_DISPLAYOFF = 0x00
LCD_CURSORON = 0x02
LCD_CURSOROFF = 0x00
LCD_BLINKON = 0x01
LCD_BLINKOFF = 0x00

class Alignment(object):
    left = LCD_ENTRYLEFT
    right = LCD_ENTRYRIGHT


class ShiftMode(object):
    cursor = LCD_ENTRYSHIFTDECREMENT
    display = LCD_ENTRYSHIFTINCREMENT


class CursorMode(object):
    hide = LCD_CURSOROFF | LCD_BLINKOFF
    line = LCD_CURSORON | LCD_BLINKOFF
    blink = LCD_CURSOROFF | LCD_BLINKON

# # # MAIN # # #

class BaseCharLCD(object):

    # Init, setup, teardown

    def __init__(self, cols=20, rows=4, dotsize=8, charmap='A02', auto_linebreaks=True):
        """
        Character LCD controller. Base class only, you should use a subclass.

        Args:
            cols:
                Number of columns per row (usually 16 or 20). Default 20.
            rows:
                Number of display rows (usually 1, 2 or 4). Default: 4.
            dotsize:
                Some 1 line displays allow a font height of 10px.
                Allowed: 8 or 10. Default: 8.
            charmap:
                The character map used. Depends on your LCD. This must be
                either ``A00`` or ``A02`` or ``ST0B``.  Default: ``A02``.
            auto_linebreaks:
                Whether or not to automatically insert line breaks.
                Default: True.

        """
        pass

    def close(self, clear=False):
        pass

    # Properties

    def _get_cursor_pos(self):
        return self._cursor_pos

    def _set_cursor_pos(self, value):
        self._cursor_pos = value

    cursor_pos = property(_get_cursor_pos, _set_cursor_pos,
            doc='The cursor position as a 2-tuple (row, col).')

    def _get_text_align_mode(self):
        if self._text_align_mode == Alignment.left:
            return 'left'
        elif self._text_align_mode == Alignment.right:
            return 'right'
        else:
            raise ValueError('Internal _text_align_mode has invalid value.')

    def _set_text_align_mode(self, value):
        if value == 'left':
            self._text_align_mode = Alignment.left
        elif value == 'right':
            self._text_align_mode = Alignment.right
        else:
            raise ValueError('Text align mode must be either `left` or `right`')

    text_align_mode = property(_get_text_align_mode, _set_text_align_mode,
            doc='The text alignment (``left`` or ``right``).')

    def _get_write_shift_mode(self):
        if self._display_shift_mode == ShiftMode.cursor:
            return 'cursor'
        elif self._display_shift_mode == ShiftMode.display:
            return 'display'
        else:
            raise ValueError('Internal _display_shift_mode has invalid value.')

    def _set_write_shift_mode(self, value):
        if value == 'cursor':
            self._display_shift_mode = ShiftMode.cursor
        elif value == 'display':
            self._display_shift_mode = ShiftMode.display
        else:
            raise ValueError('Write shift mode must be either `cursor` or `display`.')

    write_shift_mode = property(_get_write_shift_mode, _set_write_shift_mode,
            doc='The shift mode when writing (``cursor`` or ``display``).')

    def _get_display_enabled(self):
        return self._display_mode == LCD_DISPLAYON

    def _set_display_enabled(self, value):
        self._display_mode = LCD_DISPLAYON if value else LCD_DISPLAYOFF

    display_enabled = property(_get_display_enabled, _set_display_enabled,
            doc='Whether or not to display any characters.')

    def _get_cursor_mode(self):
        if self._cursor_mode == CursorMode.hide:
            return 'hide'
        elif self._cursor_mode == CursorMode.line:
            return 'line'
        elif self._cursor_mode == CursorMode.blink:
            return 'blink'
        else:
            raise ValueError('Internal _cursor_mode has invalid value.')

    def _set_cursor_mode(self, value):
        if value == 'hide':
            self._cursor_mode = CursorMode.hide
        elif value == 'line':
            self._cursor_mode = CursorMode.line
        elif value == 'blink':
            self._cursor_mode = CursorMode.blink
        else:
            raise ValueError('Cursor mode must be one of `hide`, `line` or `blink`.')

    cursor_mode = property(_get_cursor_mode, _set_cursor_mode,
            doc='How the cursor should behave (``hide``, ``line`` or ``blink``).')

    # High level commands

    def write_string(self, value):
        """
        Write the specified unicode string to the display.

        To control multiline behavior, use newline (``\\n``) and carriage
        return (``\\r``) characters.

        Lines that are too long automatically continue on next line, as long as
        ``auto_linebreaks`` has not been disabled.

        Make sure that you're only passing unicode objects to this function.
        The unicode string is then converted to the correct LCD encoding by
        using the charmap specified at instantiation time.

        If you're dealing with bytestrings (the default string type in Python
        2), convert it to a unicode object using the ``.decode(encoding)``
        method and the appropriate encoding. Example for UTF-8 encoded strings:

        .. code::

            >>> bstring = 'Temperature: 30°C'
            >>> bstring
            'Temperature: 30\xc2\xb0C'
            >>> bstring.decode('utf-8')
            u'Temperature: 30\xb0C'

        """
        print(f"[LCD MOCK] write string: {value}")

    def clear(self):
        """Overwrite display with blank characters and reset cursor position."""
        print("[LCD MOCK] clear")

    def home(self):
        """Set cursor to initial position and reset any shifting."""
        print("[LCD MOCK] home")

    def shift_display(self, amount):
        """Shift the display. Use negative amounts to shift left and positive
        amounts to shift right."""
        print("[LCD MOCK] shift_display")

    def create_char(self, location, bitmap):
        """Create a new character.

        The HD44780 supports up to 8 custom characters (location 0-7).

        :param location: The place in memory where the character is stored.
            Values need to be integers between 0 and 7.
        :type location: int
        :param bitmap: The bitmap containing the character. This should be a
            tuple of 8 numbers, each representing a 5 pixel row.
        :type bitmap: tuple of int
        :raises AssertionError: Raised when an invalid location is passed in or
            when bitmap has an incorrect size.

        Example:

        .. sourcecode:: python

            >>> smiley = (
            ...     0b00000,
            ...     0b01010,
            ...     0b01010,
            ...     0b00000,
            ...     0b10001,
            ...     0b10001,
            ...     0b01110,
            ...     0b00000,
            ... )
            >>> lcd.create_char(0, smiley)

        """
        print("[LCD MOCK] create char")


    # Mid level commands

    def command(self, value):
        """Send a raw command to the LCD."""
        print(f"[LCD MOCK] command: {value}")

    def write(self, value):  # type: (int) -> None
        """Write a raw byte to the LCD."""
        print(f"[LCD MOCK] write: {value}")

    def cr(self):  # type: () -> None
        """Write a carriage return (``\\r``) character to the LCD."""
        self.write_string('\r')

    def lf(self):  # type: () -> None
        """Write a line feed (``\\n``) character to the LCD."""
        self.write_string('\n')

    def crlf(self):  # type: () -> None
        """Write a line feed and a carriage return (``\\r\\n``) character to the LCD."""
        self.write_string('\r\n')



class CharLCD(BaseCharLCD):
    def __init__(self, i2c_expander, address, expander_params=None, port=1,
                       cols=20, rows=4, dotsize=8,
                       charmap='A02',
                       auto_linebreaks=True,
                       backlight_enabled=True):
        """
        CharLCD via PCF8574 I2C port expander:

            Pin mapping::

            7  | 6  | 5  | 4  | 3  | 2  | 1  | 0
            D7 | D6 | D5 | D4 | BL | EN | RW | RS


        CharLCD via MCP23008 and MCP23017 I2C port expanders:

            Adafruit I2C/SPI LCD Backback is supported.

            Warning: You might need a level shifter (that supports i2c)
            between the SCL/SDA connections on the MCP chip / backpack and the Raspberry Pi.
            Or you might damage the Pi and possibly any other 3.3V i2c devices
            connected on the i2c bus. Or cause reliability issues. The SCL/SDA are rated 0.7*VDD
            on the MCP23008, so it needs 3.5V on the SCL/SDA when 5V is applied to drive the LCD.

            The MCP23008 and MCP23017 needs to be connected exactly the same way as the backpack.

            For complete schematics see the adafruit page at:
            https://learn.adafruit.com/i2c-spi-lcd-backpack/

            4-bit operation. I2C only supported.

            Pin mapping::

            7  | 6  | 5  | 4  | 3  | 2 | 1  | 0
            BL | D7 | D6 | D5 | D4 | E | RS | -


        :param address: The I2C address of your LCD.
        :type address: int
        :param i2c_expander: Set your I²C chip type. Supported: "PCF8574", "MCP23008", "MCP23017".
        :type i2c_expander: string
        :param expander_params: Parameters for expanders, in a dictionary. Only needed for MCP23017
            gpio_bank - This must be either ``A`` or ``B``
                         If you have a HAT, A is usually marked 1 and B is 2
            Example: expander_params={'gpio_bank': 'A'}
        :type expander_params: dictionary
        :param port: The I2C port number. Default: ``1``.
        :type port: int
        :param cols: Number of columns per row (usually 16 or 20). Default: ``20``.
        :type cols: int
        :param rows: Number of display rows (usually 1, 2 or 4). Default: ``4``.
        :type rows: int
        :param dotsize: Some 1 line displays allow a font height of 10px.
            Allowed: 8 or 10. Default: ``8``.
        :type dotsize: int
        :param charmap: The character map used. Depends on your LCD. This must
            be either ``A00`` or ``A02`` or ``ST0B``.
        :type charmap: str
        :param auto_linebreaks: Whether or not to automatically insert line breaks.
            Default: ``True``.
        :type auto_linebreaks: bool
        :param backlight_enabled: Whether the backlight is enabled initially. Default: ``True``.
        :type backlight_enabled: bool

        """

        # Call superclass
        super(CharLCD, self).__init__(cols, rows, dotsize,
                                      charmap=charmap,
                                      auto_linebreaks=auto_linebreaks)

    # Properties

    def _get_backlight_enabled(self):
        return True

    def _set_backlight_enabled(self, value):
        pass

    backlight_enabled = property(_get_backlight_enabled, _set_backlight_enabled,
            doc='Whether or not to enable the backlight. Either ``True`` or ``False``.')

    # Low level commands

    def _send_data(self, value):
        print(f"[LCD MOCK] send data: {value}")

    def _send_instruction(self, value):
        print(f"[LCD MOCK] send instruction: {value}")


    def _pulse_data(self, value):
        """Pulse the `enable` flag to process value."""
        print(f"[LCD MOCK] pulse data: {value}")
