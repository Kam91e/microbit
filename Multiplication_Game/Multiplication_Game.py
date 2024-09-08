from random import *
from microbit import *

game = True
N1 = randint(0, 10)
N2 = randint(0, 10)
PI1 = 0
PI10 = 0
PI = PI10 * 10 + PI1
Wynik = N1 * N2
end = False
happy = Image("09090:"
              "09090:"
              "00000:"
              "90009:"
              "09990")

sad = Image("09090:"
            "09090:"
            "00000:"
            "09990:"
            "90009")

def value1(w = 250):
    if button_b.is_pressed():
        global PI1
        PI1 = PI1 + 1
        sleep(w)
        if PI1 >= 10:
            PI1 = 0

def value10(w = 250):
    if button_a.is_pressed():
        global PI10
        PI10 = PI10 + 1
        sleep(w)
        if PI10 >= 11:
            PI10 = 0

def value_check(w = 250):
    if accelerometer.is_gesture('up'):
        global PI
        global PI10
        global PI1
        PI = PI10 * 10 + PI1 
        display.scroll(PI)
        sleep(w)

def end_game():
    if pin_logo.is_touched():
        global end
        end = True

while game == True:
    if button_a.is_pressed():
        N1 = randint(1, 10)
        N2 = randint(1, 10)
        display.scroll(str(N1) + ' * ' + str(N2))
        Wynik = N1 * N2
        PI1 = 0
        PI10 = 0
        PI = PI10 * 10 + PI1
        end = False
        while end == False:
            value1()
            value10()
            value_check()
            end_game()
        if PI == Wynik:
            display.show(happy)
            sleep(1000)
            display.scroll(Wynik)
        else:
            display.show(sad)
            sleep(1000)
            display.scroll(Wynik)
            display.scroll('T: ' + str(PI))