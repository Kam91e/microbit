def on_button_pressed_a():
    global Kliknięte, Kliknąć
    Kliknięte = 1
    if Kliknąć == Kliknięte:
        basic.show_icon(IconNames.YES)
    else:
        basic.show_icon(IconNames.NO)
    Kliknąć = randint(1, 2)
    if Kliknąć == 1:
        basic.show_string("A")
        basic.pause(100)
        basic.clear_screen()
    else:
        basic.show_string("B")
        basic.pause(100)
        basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Kliknięte, Kliknąć
    Kliknięte = 2
    if Kliknąć == Kliknięte:
        basic.show_icon(IconNames.YES)
    else:
        basic.show_icon(IconNames.NO)
    Kliknąć = randint(1, 2)
    if Kliknąć == 1:
        basic.show_string("A")
        basic.pause(100)
        basic.clear_screen()
    else:
        basic.show_string("B")
        basic.pause(100)
        basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

Kliknięte = 0
Kliknąć = 0
Kliknąć = randint(1, 2)
if Kliknąć == 1:
    basic.show_string("A")
    basic.pause(100)
    basic.clear_screen()
else:
    basic.show_string("B")
    basic.pause(100)
    basic.clear_screen()
