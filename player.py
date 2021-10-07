class Player:

    def __init__(self):
        pass

    def make_guess(self):
        return input(
            "\nPlease enter the your target position (e.g., '2,3')"
            + "\n"
            + "> "
        )

    def flag_choice(self):
        choice = input(
            "Would you like to flag a square?"
            + "\n"
            + "> "
        )

        return choice
