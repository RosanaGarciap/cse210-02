import random


class Cards:
    """A deck of cards. Cards included are 1-13.

    The value of the card is used for the main function of the game.
   
    Attributes:
        value (int): The number of the card drawn.
    """

    def __init__(self):
        """Constructs instances of cards.

        Args:
            self (card): an instance of a card. 
        """
        self.card_is = random.randint(1, 13)
        self.next_card = 0

    def pull(self):

        """Sets the value of the first card and generates a random number for the second comparison card.

        Args:
            self (card): an instance of a card.
        """
        self.next_card = self.card_is
        self.card_is = random.randint(1, 13)

    def compare(self):

        """Sets comparison function for the game. Sets the return of 'h' or 'l' to compare to user input.
        
        Args:
            self (card): an instance of a card. """

        if self.card_is > self.next_card:
            return "h"
        elif self.card_is < self.next_card:
            return "l"