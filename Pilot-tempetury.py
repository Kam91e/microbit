tempetura = 0
basic.show_string("PILOT")
radio.set_group(91)

def on_forever():
    global tempetura
    tempetura = input.temperature()
    radio.send_number(tempetura)
    basic.show_number(tempetura)
    basic.pause(1000)
basic.forever(on_forever)
