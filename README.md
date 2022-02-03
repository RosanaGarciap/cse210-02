# Python Program: Hilo Game 🂡

## Description
Hilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than the previous one. Points are won or lost based on whether or not the player guessed correctly. The objetive of this project is to use class definitions to simulate an actual game of Hilo according to the rules given in the documentation (see link below).

For further information please visit the following [link](https://byui-cse.github.io/cse210-course-competency/abstraction/materials/hilo-specification.html)

### Python Version:
To run this script `python>3.5` is recommended

## Getting Started 🔥

- Download and extract the repository.
- Open a terminal and move to the with the cd command to the path where the folder was extract: $ cd "/path/to/project/folder"
- From within the repo directory run the command
  $ python __main__.py (for old versions of python3 run $ python3 __main__.py)

### Example

```
$ cd /my/path/to/cse210-02
$ python __main__.py
The card is: 13
Higher or lower? [h/l]: h
Your score is: 225
Play again [y/n]: y

The card is: 10
Higher or lower? [h/l]: h
Your score is: 325
Play again [y/n]: y

The card is: 12
Higher or lower? [h/l]: h
Your score is: 250
Play again [y/n]: n
$

```

## Classes

### Class Cards
Hilo Game is played using cards, each card have a number from 1 to 13. The class Cards contains a value attribute assigned randomly. The Player starts with a card take a second from a deck of cards and guess if it is greater or lower than the current card. The player earns 100 points if they guessed correctly, loses 75 points if they guessed incorrectly, and lose the game if 0 points are reached.
### Class Player
Following the logic of the real game, every game has a "player" and this player is responsible of start and manage the game and keep control of it during it's development, therefore, the class Player is the responsible of start the game, take the cards values and compare them.

## Programming Logic decisions
- Since the rules don't specify if there are only 13 different cards or an unlimited number, it was decided that the current implementation will considerate an unlimited number of cards with possible values between 1 and 13.

- The game logic was divided in four steps and each one was handled with its own function, those steps consist of:
1- Ask for inputs
2- compare values
3- Update results
4- show outputs
