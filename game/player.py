from game.cards import Cards


class Player:
    """Please update comments

    Attributes:
        Please update comments  
    """

    def __init__(self):
        """Please update comments
        
        Args:
            Please update comments
        """
        self.dice = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0

        for i in range(5):
            die = Die()
            self.dice.append(die)

    def start_game(self):
        """Please update comments
        
        Args:
            Please update comments
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Please update comments

        Args:
            Please update comments
        """
        roll_dice = input("Roll dice? [y/n] ")
        self.is_playing = (roll_dice == "y")
       
    def do_updates(self):
        """Please update comments

        Args:
            Please update comments
        """
        if not self.is_playing:
            return 

        for i in range(len(self.dice)):
            die = self.dice[i]
            die.roll()
            self.score += die.points 
        self.total_score += self.score

    def do_outputs(self):
        """Please update comments

        Args:
            Please update comments
        """
        if not self.is_playing:
            return
        
        values = ""
        for i in range(len(self.dice)):
            die = self.dice[i]
            values += f"{die.value} "

        print(f"You rolled: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)