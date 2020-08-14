def on_button_pressed_a():
    basic.show_number(pins.analog_read_pin(AnalogPin.P0))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Miliwolty
    Miliwolty = Math.round(pins.analog_read_pin(AnalogPin.P0) * 3000 / 1023)
    basic.show_number(Miliwolty)
    if Miliwolty < 1200:
        basic.show_leds("""
            . # . # .
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            """)
    else:
        basic.show_leds("""
            . # . # .
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            """)
input.on_button_pressed(Button.B, on_button_pressed_b)

Miliwolty = 0
basic.show_string("TESTER BATERI")
