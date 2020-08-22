def on_forever():
    bluetooth.uart_write_value("Celcjusze", input.temperature())
    basic.show_number(input.temperature())
    basic.pause(1000)
basic.forever(on_forever)
