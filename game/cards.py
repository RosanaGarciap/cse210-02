import random


class Cards:
    """Please update comments
   
    Attributes:
        Please update comments
    """

    def __init__(self):
        """Please update comments

        Args:
            Please update comments
        """
        self.value = 0
        self.points = 0

    def roll(self):
        """Please update comments
        
        Args:
            Please update comments
        """
        self.value = random.randint(1, 6)
        self.points = 50 if self.value == 5 else 100 if self.value == 1 else 0