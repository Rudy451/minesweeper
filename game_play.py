# Verify keyboard import
# Verify keycheck + save + load json files

import keyboard
import jsonpickle
from os import system
import time

from grid import Grid
from ai_player import AIPlayer
from player import Player

class Gameplay(object):

    def __init__(self, player):
        self.board = Grid()
        self.player = player
        self.saved_coords_list = []

    def reload_coords(self):
        for coords in self.saved_coords_list:
            self.board.value_generator(coords[0], coords[1])

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
        else:
            self.board.value_generator(x, y)
            self.saved_coords_list.append([x, y])
            self.execute_flag_choice(self.player.flag_choice())
            time.sleep(1)

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
                time.sleep(1)

def load_game():
    with open("minesweeper.json", "r") as file:
        try:
            my_file = file.read()
            return jsonpickle.decode(my_file)
        except:
            return Gameplay(Player())

def save_game(game):
    with open("minesweeper.json", "w") as file:
        my_file = jsonpickle.encode(game)
        file.write(my_file)

def clear_game():
    with open("minesweeper.json", "w") as file:
        file.truncate(0)


mine = load_game()
if(len(mine.saved_coords_list) == 0):
    pass
else:
    mine.reload_coords()
try:
    mine.play()
    clear_game()
except KeyboardInterrupt:
    save_game(mine)
    exit()
