from square import Square

class Grid:

    def __init__(self):
        self.grid = [[]] * 9
        self.build_grid()

    def build_grid(self):
        self.grid = [[Square(), Square(), Square(),
                      Square(), Square(), Square(),
                      Square(), Square(), Square()
                    ] for spot in self.grid]

    def total_mines_calculator(self):
        return sum([sum([int(val.check_mine()) for val in row]) for row in self.grid])

    def total_mines_revealed_calculator(self):
        return sum([sum([int(val.mine_revealed) for val in row]) for row in self.grid])

    def value_generator(self, x, y):
        self.grid[x][y].set_value(self.adjacent_square_checker(x, y) + self.diagonal_square_checker(x, y)) if not self.grid[x][y].flagged() else 0
        self.grid[x - 1][y].set_value(self.adjacent_square_checker(x - 1, y) + self.diagonal_square_checker(x - 1, y)) if x - 1 >= 0 and not self.grid[x - 1][y].flagged() else 0
        self.grid[x + 1][y].set_value(self.adjacent_square_checker(x + 1, y) + self.diagonal_square_checker(x + 1, y)) if x + 1 < 9 and not self.grid[x + 1][y].flagged()else 0
        self.grid[x][y - 1].set_value(self.adjacent_square_checker(x, y - 1) + self.diagonal_square_checker(x, y - 1)) if y - 1 >= 0 and not self.grid[x][y - 1].flagged()else 0
        self.grid[x][y + 1].set_value(self.adjacent_square_checker(x, y + 1) + self.diagonal_square_checker(x, y +  1)) if y + 1 < 9  and not self.grid[x][y + 1].flagged()else 0
        self.grid[x - 1][y - 1].set_value(self.adjacent_square_checker(x - 1, y - 1) + self.diagonal_square_checker(x - 1, y - 1)) if x - 1 >= 0 and y - 1 >= 0 and not self.grid[x - 1][y - 1].flagged() else 0
        self.grid[x + 1][y - 1].set_value(self.adjacent_square_checker(x + 1, y - 1) + self.diagonal_square_checker(x + 1, y - 1)) if x + 1 < 9 and y - 1 >= 0 and not self.grid[x + 1][y - 1].flagged() else 0
        self.grid[x - 1][y + 1].set_value(self.adjacent_square_checker(x - 1, y + 1) + self.diagonal_square_checker(x - 1, y + 1)) if x - 1 >= 0 and y + 1 < 9 and not self.grid[x - 1][y + 1].flagged() else 0
        self.grid[x + 1][y + 1].set_value(self.adjacent_square_checker(x + 1, y + 1) + self.diagonal_square_checker(x + 1, y + 1)) if x + 1 < 9 and y + 1 < 9 and not self.grid[x + 1][y + 1].flagged() else 0

    def adjacent_square_checker(self, x, y):
        total = 0
        total += 1 if x - 1 >= 0 and self.grid[x - 1][y].check_mine() else 0
        total += 1 if x + 1 < 9 and self.grid[x + 1][y].check_mine() else 0
        total += 1 if y - 1 >= 0 and self.grid[x][y - 1].check_mine() else 0
        total += 1 if y + 1 < 9 and self.grid[x][y + 1].check_mine() else 0
        return total

    def diagonal_square_checker(self, x, y):
        total = 0
        total += 1 if x - 1 >= 0 and y - 1 >= 0 and self.grid[x - 1][y - 1].check_mine() else 0
        total += 1 if x + 1 < 9 and y - 1 >= 0 and self.grid[x + 1][y - 1].check_mine() else 0
        total += 1 if x - 1 >= 0 and y + 1 < 9 and self.grid[x - 1][y + 1].check_mine() else 0
        total += 1 if x + 1 < 9 and y + 1 < 9 and self.grid[x + 1][y + 1].check_mine() else 0
        return total

    def flag_square(self, x, y):
        self.grid[x][y].set_value("F")

    def display_grid(self):
        [print([row[0].get_value(), row[1].get_value(), row[2].get_value(),
                row[3].get_value(), row[4].get_value(), row[5].get_value(),
                row[6].get_value(), row[7].get_value(), row[8].get_value()
              ]) for row in self.grid]
