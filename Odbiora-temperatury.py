def on_received_number(receivedNumber):
    led.plot(4, 4)
    serial.write_value("Celcjusz", receivedNumber)
radio.on_received_number(on_received_number)

basic.show_string("ODBIORCA")
radio.set_group(91)
