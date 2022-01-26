import random

class Cards:

    def __init__(self):

        self.card_is = random.randint(1, 13)
        self.next_card = 0

    def pull(self):

        self.next_card = self.card_is
        self.card_is = random.randint(1, 13)

    def compare(self):

        if self.card_is > self.next_card:
            return "h"
        elif self.card_is < self.next_card:
            return "l"
