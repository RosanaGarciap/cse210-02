# import random and Cards class
from random import random
from game.cards import Cards


class Player:
    """A player who directs the game.

    The responsibility of the Player is to control the game.

    Attributes:
        Please update comments  
    """

    def __init__(self):
        """Please update comments
        
        Args:
            Please update comments
        """
<<<<<<< HEAD
        self.card_number1 = 0
        self.card_number2 = 0

        for i in range(5):
            die = Die()
            self.dice.append(die)
=======
        self.currentCard = Cards()
        self.is_playing = True
        self.score = 300
>>>>>>> c7faf0d854c86c3a4362b15caa471bb590e4d429

    def start_game(self):
        """Please update comments
        
        Args:
            Please update comments
        """
        while self.is_playing:
            self.get_inputs()
            self.do_outputs()

    def get_inputs(self):
        """Please update comments

        Args:
            Please update comments
        """
        val = self.currentCard.value
        print("The card is: %d" %val)
        playerIn = input("Higher or lower? [h/l]: ")
        oldCard = self.currentCard
        newCard = Cards()
        if(playerIn == "h"):
            self.get_high(oldCard, newCard)

        elif(playerIn == "l"):
            self.get_low(oldCard,newCard)

    def do_updates(self, guess, newCard):
        """Please update comments

        Args:
            Please update comments
        """
        #updating score
        
        self.score += guess
        #updating card
        self.currentCard.value = newCard

        
    def do_outputs(self):
        """Please update comments

        Args:
            Please update comments
        """
        print("Your score is: %d" %self.score)
        v = input("Play again [y/n]: ")
        if(v=="n" or self.score <= 0):
            self.is_playing = False
        else:
            print("")

<<<<<<< HEAD
        print(f"You rolled: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)

    def get_high(self):
        """If player chooses High and gets it right we add 100 points
        But if they get it wrong they lose 75 points (Jessica, please update this comment in the way you think it's better)"""
        if self.card_number2 > self.card_number1:
            return +100
        elif self.card_number2 < self.card_number1:
            return -75


    def get_low(self):
        """If player chooses Low and gets it right we add 100 points
        But if they get it wrong they lose 75 points (Jessica, please update this comment in the way you think it's better)"""
        if self.card_number2 < self.card_number1:
            return self.point_total + 100
        elif self.card_number2 > self.card_number1:
            return self.point_total - 75
=======

    def get_high(self,c1,c2):
        """If player chooses High and gets it right we add 100 points
        But if they get it wrong they lose 75 points (Jessica, please update this comment in the way you think it's better)"""
        
        if c2.value > c1.value:
            self.do_updates(100,c2.value)
            
        elif c2.value < c1.value:
            self.do_updates(-75,c2.value)


    def get_low(self,c1,c2):
        """If player chooses Low and gets it right we add 100 points
        But if they get it wrong they lose 75 points (Jessica, please update this comment in the way you think it's better)"""
        if c2.value < c1.value:
            self.do_updates(100,c2.value)
        elif c2.value > c1.value:
            self.do_updates(-75, c2.value)
        else:
            print("")
            return
>>>>>>> c7faf0d854c86c3a4362b15caa471bb590e4d429
