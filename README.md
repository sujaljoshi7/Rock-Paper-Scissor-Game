# Rock, Paper, Scissors Game

Welcome to the Rock, Paper, Scissors Game! This is a simple Python implementation of the classic game where you can play against the computer.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Features](#features)
- [Contributing](#contributing)

## Introduction

Rock, Paper, Scissors is a hand game usually played between two people, in this case, between the player and the computer. The player and the computer simultaneously form one of three shapes with an outstretched hand. The possible outcomes are:

- Rock crushes Scissors
- Scissors cuts Paper
- Paper covers Rock

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/sujaljoshi7/Rock-Paper-Scissor-Game.git
    cd rock-paper-scissors
    ```

2. **Ensure you have Python installed:**

    This game requires Python. You can download it from [python.org](https://www.python.org/).

3. **Install the required modules:**

    There are no external dependencies required for this project.

## How to Play

1. **Run the Game:**

    To start the game, simply run the Python script:

    ```bash
    python rock_paper_scissors.py
    ```

2. **Gameplay:**

    - The game will print the welcome message.
    - You will be prompted to choose your move by typing 0 for Rock, 1 for Paper, or 2 for Scissors.
    - The game will display your choice and the computer's random choice.
    - The game will then display the result: win, lose, or tie.

3. **Example:**

    ```bash
    Welcome to Rock, Paper, Scissors Game
    What do you choose? Type 0 for Rock, 1 for Paper of 2 for Scissors: 0
    You Choose:
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)

    Computer choose:
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)

    You Lose
    ```

## Features

- Simple and easy-to-understand code.
- Random choice for the computer to simulate a fair game.
- ASCII art representation for Rock, Paper, and Scissors.
- Text-based interface.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

---

**Note:** This script does not use any external modules beyond the Python standard library. Ensure you have Python installed and properly configured to run the script.
