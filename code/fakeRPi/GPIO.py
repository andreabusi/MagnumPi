"""
Fake class to simulate RPi.GPIO library outside a Raspberry PI
"""

BOARD = 1
BCM = 'BCM'
OUT = 'OUT'
IN = 'IN'
HIGH = 1
LOW = 0


def setmode(a):
    print('Set mode: ' + a)


def setup(a, b):
    print('Set pin %s as %s' % (a, b))


def output(a, b):
    print('Output %s to pin %s' % (b, a))

def input(pin):
    state = random.choice([HIGH, LOW])
    print('Input for pin %s is %s' % (pin, state))
    return state


def cleanup():
    print('a')


def setwarnings(flag):
    print('Set warnings as %s' % flag)
