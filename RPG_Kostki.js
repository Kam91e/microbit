input.onButtonPressed(Button.A, function () {
    kostka = 4
    kliknięcia = 0
    basic.clearScreen()
    basic.showNumber(4)
})
input.onButtonPressed(Button.B, function () {
    kliknięcia += 1
    if (kliknięcia == 1) {
        kostka = 6
        basic.showNumber(6)
    } else if (kliknięcia == 2) {
        kostka = 8
        basic.showNumber(8)
    } else if (kliknięcia == 3) {
        kostka = 10
        basic.showLeds(`
            . # . # .
            # # # . #
            . # # . #
            . # # . #
            . # . # .
            `)
    } else if (kliknięcia == 4) {
        kostka = 12
        basic.showLeds(`
            . # . # .
            # # # . #
            . # . # .
            . # # . .
            . # # # #
            `)
    } else if (kliknięcia == 5) {
        kostka = 20
        basic.showLeds(`
            . # . # .
            # . # . #
            . # # . #
            # . # . #
            # # # # .
            `)
    }
})
input.onGesture(Gesture.Shake, function () {
    for (let index = 0; index < 3; index++) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            `)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            `)
    }
    basic.showNumber(Math.randomRange(1, kostka))
    basic.pause(3000)
    basic.clearScreen()
    basic.showNumber(kostka)
})
let kliknięcia = 0
let kostka = 0
kostka = 4
basic.showNumber(4)
