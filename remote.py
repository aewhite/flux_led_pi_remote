from flux_led import WifiLedBulb
import sys
import gpio_listener


def read_test_input():
    return [True, False, False, False]


def handle_rgb_state(bulbs, state):
    r = 255 if state[1] else 0
    g = 255 if state[2] else 0
    b = 255 if state[3] else 0

    for bulb in bulbs:
        bulb.setRgb(r, g, b)


def handle_custom_states(bulbs, state):
    if not any(state[1:]):
        for bulb in bulbs:
            bulb.setWarmWhite255(255)


def handle_state(bulbs, state):
    if not state[0]:
        handle_rgb_state(bulbs, state)
    else:
        handle_custom_states(bulbs, state)


def main():

    ip_addresses = sys.argv[1:]
    bulbs = [WifiLedBulb(ip_address) for ip_address in ip_addresses]

    prev_state = [False, False, False, False]
    while True:
        state = gpio_listener.read_gpio()
        if state == prev_state:
            continue
            
        handle_state(bulbs, state)
        prev_state = list(state)


if __name__ == "__main__":
    main()
