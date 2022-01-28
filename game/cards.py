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
        self.value = random.randint(1, 13)

    def getValue(self):
        """Returns The value of the card.
        
        Args:
            self (card): an instance of a card.
        """
        return self.value
