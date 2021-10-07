import random

class Square:

    def __init__(self):
        self.mine = True if random.randint(0, 60) % 6 == 0 else False
        self.value = "*"
        self.mine_revealed = False

    def set_value(self, value):
        self.mine_revealed = True if not self.check_mine() else False
        self.value = str(value)

    def get_value(self):
        return self.value

    def check_mine(self):
        return self.mine

    def flagged(self):
        return self.value == "F"
