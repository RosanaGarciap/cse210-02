from game.cards import Cards


class Player:
    """A player who directs the game.

    The responsibility of the Player is to control the game.

    Attributes:
        currenCard (int): The current card value.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for the game.
    """

    def __init__(self):
        """Constructs a new Player.
        
        Args:
            self (Player): an instance of Player.
        """
        self.currentCard = Cards()
        self.is_playing = True
        self.score = 300

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Player): an instance of Player.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if the next card will be higher or lower than the current card.

        Args:
            self (Player): an instance of Player.
        """
        val = self.currentCard.value
        print("The card is: %d" %val)

        #This will keep looping until the player enters either h or l
        playerIn = ""
        while playerIn != "h" or playerIn != "l":
            playerIn = input("Higher or lower? [h/l]: ")
            oldCard = self.currentCard
            newCard = Cards()
            if(playerIn == "h"):
                self.get_high(oldCard, newCard)
                break

            elif(playerIn == "l"):
                self.get_low(oldCard, newCard)
                break
            else:
                print("Invalid input")
                print()

    def do_updates(self, guess, newCard):
        """Updates the player's score.

        Args:
            self (Player): an instance of Player.
        """
        #updating score
        self.score += guess
        if (self.score <= 0):
            self.is_playing = False
        #updating card
        self.currentCard.value = newCard

        
    def do_outputs(self):
        """Displays the cards and the score. Also asks if the want to keep playing

        Args:
            self (Player): an instance of Player.
        """
        print(f"Your score is: {self.score}")
        print(f"The card was: {self.currentCard.value}")

        if(self.score <= 0):
            self.is_playing = False
            return

        #This will keep looping until the user enters either y or n
        v = ""
        while v != "n" or v != "y":
            v = input("Play again [y/n]: ")
            if(v == "n"):
                self.is_playing = False
                break
            elif(v == "y"):
                print("")
                break
            else:
                print("Invalid input")


    def get_high(self, c1, c2):
        """If player chooses High and gets it right we add 100 points
        But if they get it wrong they lose 75 points."""
        
        if c2.value > c1.value:
            self.do_updates(100, c2.value)
            
        elif c2.value < c1.value:
            self.do_updates(-75, c2.value)


    def get_low(self, c1, c2):
        """If player chooses Low and gets it right we add 100 points
        But if they get it wrong they lose 75 points."""
        if c2.value < c1.value:
            self.do_updates(100, c2.value)
        elif c2.value > c1.value:
            self.do_updates(-75, c2.value)
        else:
            print("")
            return