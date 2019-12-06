from flask import jsonify
from app.api import bp
from app.api.errors import bad_request
from mygpio import mygpio


@bp.route('/display/<string:text>', methods=['PUT'])
def show_text(text):
    my_gpio = mygpio.MyGPIO()
    if not my_gpio.is_lcd_connected():
        return bad_request('LCD display is not available')

    result = my_gpio.lcd_display_text(text)
    if result:
        return jsonify({'result': 'true'})
    return bad_request('Error when sending text to display')
