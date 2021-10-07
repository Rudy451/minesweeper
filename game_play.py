from os import system
import time

from grid import Grid

class Gameplay:

    def __init__(self):
        self.board = Grid()

    def solved(self):
        return self.board.total_mines_calculator() == self.board.total_mines_revealed_calculator()

    def make_guess(self):
        return input(
            "\nPlease enter the your target position (e.g., '2,3')"
            + "\n"
            + "> "
        )

    def validate_input_value(self, pos):
        target = "012345678"
        if len(pos) == 3:
            pos_1 = target.find(pos[0]) != -1
            pos_2 = target.find(pos[2]) != -1
            return pos_1 and pos_2
        return False

    def execute_guess(self, x, y):
        if self.board.grid[x][y].check_mine():
            print("BLAST!!!!")
        else:
            self.board.value_generator(x, y)

    def flag_choice(self):
        choice = input(
            "Would you like to flag a square?"
            + "\n"
            + "> "
        )

        if self.validate_flag_choice(choice):
            result = self.make_guess()
            self.board.grid[int(result[0])][int(result[1])].set_value("F")

    def validate_flag_choice(self, choice):
       return choice.upper() == "Y" or choice.upper() == "YES"

    def play(self):
        while not self.solved():
            system("cls")
            self.board.display_grid()
            result = self.make_guess()
            if self.validate_input_value(result):
                self.execute_guess(int(result[0]), int(result[2]))
                self.flag_choice()
                time.sleep(1)

mine = Gameplay()
mine.play()
