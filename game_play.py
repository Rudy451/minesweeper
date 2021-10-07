from os import system
import time

from grid import Grid
from ai_player import AIPlayer
from player import Player

class Gameplay:

    def __init__(self, player):
        self.board = Grid()
        self.player = player

    def solved(self):
        return self.board.total_mines_calculator() == self.board.total_mines_revealed_calculator()

    def validate_input_value(self, pos):
        target = "012345678"
        if len(pos) == 3:
            pos_1 = target.find(pos[0]) != -1
            pos_2 = target.find(pos[2]) != -1
            return pos_1 and pos_2
        return False

    def execute_guess(self, x, y):
        if self.board.grid[x][y].check_mine():
            system("cls")
            print("BLAST!!!!")
            time.sleep(2)
            system("cls")
            self.board.display_grid()
        else:
            self.board.value_generator(x, y)

    def execute_flag_choice(self, choice):
        if self.validate_flag_choice(choice):
            result = self.player.make_guess()
            self.board.grid[int(result[0])][int(result[2])].set_value("F")

    def validate_flag_choice(self, choice):
       return choice.upper() == "Y" or choice.upper() == "YES"

    def play(self):
        while not self.solved():
            system("cls")
            self.board.display_grid()
            result = self.player.make_guess()
            if self.validate_input_value(result):
                self.execute_guess(int(result[0]), int(result[2]))
                self.execute_flag_choice(self.player.flag_choice())
                time.sleep(1)

mine = Gameplay(AIPlayer())
mine.play()
