import time
import random

class AIPlayer:

    def __init__(self):
        pass

    def make_guess(self):
        print(
            "\nPlease enter the your target position (e.g., '2,3')"
            + "\n"
            + "> "
        )

        time.sleep(1)

        return str(random.randint(0, 8)) + "," + str(random.randint(0, 8))


    def flag_choice(self):
        print(
            "Would you like to flag a square?"
            + "\n"
            + "> "
        )

        time.sleep(1)

        return "Yes" if random.randint(0, 1) == 1 else "No"
