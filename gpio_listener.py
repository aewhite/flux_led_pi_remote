import RPi.GPIO as GPIO
import time

bcm_pins = [25, 8, 7, 11]


def setup_gpio():
    GPIO.setmode(GPIO.BCM)

    for pin in bcm_pins:
        GPIO.setup(pin, GPIO.IN)


def read_gpio():
    prev_states = [False, False, False, False]
    states = [False, False, False, False]

    while True:
        for index, pin in enumerate(bcm_pins):
            states[index] = GPIO.input(pin)

        if any(states) and states == prev_states:
            return states

        prev_states = list(states)
        time.sleep(0.1)

setup_gpio()