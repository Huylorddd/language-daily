import os

class utility:

    # Clear terminal/cmd::
    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')