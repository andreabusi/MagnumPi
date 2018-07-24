import random

"""
Fake class to simulate RPi.GPIO library outside a Raspberry PI
"""

BOARD = 1
BCM = 'BCM'
OUT = 'OUT'
IN = 'IN'
HIGH = 1
LOW = 0


def setmode(mode):
    print('[fakeRPi.GPIO] Set mode: ' + mode)


def setup(pin, state):
    print('[fakeRPi.GPIO] Set pin %s as %s' % (pin, state))


def output(pin, state):
    print('[fakeRPi.GPIO] Output %s to pin %s' % (state, pin))


def input(pin):
    state = random.choice([HIGH, LOW])
    print('[fakeRPi.GPIO] Input for pin %s is %s' % (pin, state))
    return state


def cleanup():
    print('[fakeRPi.GPIO] Cleanup')


def setwarnings(flag):
    print('[fakeRPi.GPIO] Set warnings as %s' % flag)

