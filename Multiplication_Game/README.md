# Micro:bit Multiplication Game

This project is a simple multiplication game for the BBC micro:bit. The game challenges players to compute the product of two random numbers and input the result using the micro:bit's buttons. The game provides visual feedback based on the player's answer.

## Features

- **Random Multiplication Problems**: The game generates two random numbers between 1 and 10. The player must find their product.
- **User Input**: The player inputs their answer by adjusting the tens and ones digits using button A and button B.
- **Display Current Input**: Tilt the micro:bit upwards (gesture 'up') to display the current input value.
- **End Round**: Touch the micro:bit's logo to finalize the answer and conclude the current round.
- **Feedback**: The game shows a happy face for a correct answer and a sad face for an incorrect one. The correct answer is then displayed.

## How to Play

1. **Start the Game**: Press button A to initiate a new round. Two random numbers and the multiplication sign (`*`) will appear on the screen.
2. **Input the Answer**:
   - Use button A to increment the tens digit.
   - Use button B to increment the ones digit.
3. **Display Current Input**: Tilt the micro:bit upwards to see the current input value you have set.
4. **End the Round**: Touch the micro:bit's logo to submit your answer and end the round.
5. **Check the Result**:
   - If the answer is correct, the micro:bit will show a happy face and display the correct result.
   - If the answer is incorrect, a sad face will appear, and the micro:bit will show the correct result along with the entered value.

## Installation

1. Install the [Micro:bit Python Editor](https://python.microbit.org/).
2. Copy the code provided in `main.py` into the editor.
3. Connect your BBC micro:bit via USB and flash the code onto the device.

## Code Explanation

- **Random Number Generation**: Randomly generates two numbers between 1 and 10 for the multiplication problem using `randint(1, 10)`.
- **Input Handling**: Button A increments the tens digit, and button B increments the ones digit. Adjust these buttons to set your answer.
- **Display Current Input**: Tilt the micro:bit upwards to display the current input value.
- **End the Round**: Touch the micro:bit’s logo to finalize your answer and conclude the round.
- **Game Feedback**: Displays a happy face if the answer is correct and a sad face if it is incorrect. Shows both the correct result and the player’s entered value.

## Future Improvements

- **Scoring System**: Add a score counter to track correct answers over time.
- **Time Limit**: Introduce a timer for each round to add a time challenge.
- **Difficulty Levels**: Include difficulty settings for single-digit versus multi-digit multiplication.
- **Sound Feedback**: Incorporate sound effects for correct and incorrect answers.

## Requirements

- BBC Micro:bit
- Python Editor or an equivalent environment for running Micro:bit Python code.

## Contributing

Contributions are welcome! Please submit issues, feature requests, or pull requests to help improve this project.

## License

This project is open source and available under the [MIT License](LICENSE).
