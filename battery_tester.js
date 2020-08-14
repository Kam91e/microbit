//https://www.youtube.com/watch?v=gdlc34nhjK4(   - Doświatczenie tester baterii  -    )

input.onButtonPressed(Button.A, function () {
    basic.showNumber(pins.analogReadPin(AnalogPin.P0))
})
input.onButtonPressed(Button.B, function () {
    Miliwolty = Math.round(pins.analogReadPin(AnalogPin.P0) * 3000 / 1023)
    basic.showNumber(Miliwolty)
    if (Miliwolty < 1200) {
        basic.showLeds(`
            . # . # .
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            `)
    } else {
        basic.showLeds(`
            . # . # .
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            `)
    }
})
let Miliwolty = 0
basic.showString("TESTER BATERI")
