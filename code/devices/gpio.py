import json


def get_pins():
    """Get the pins configuration"""
    configuration = json.load(open("resources/pins.json"))
    pins = configuration['pins']
    return pins


def get_pin_info(pin):
    """Get detailed info for a specific pin"""
    pins = get_pins()
    pin_item = list(filter(lambda x: x['pin'] == pin, pins))
    if pin_item[0]['type'] == 'GND' or pin_item[0]['type'] == 'VCC':
        return None
    return pin_item[0]