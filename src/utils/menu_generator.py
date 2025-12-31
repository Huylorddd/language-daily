from utilities import utility

class Menu:
    def __init__(self):
        pass

    # Menu showcase::
    def show(self):
        utility.clear()
        print ("""
        L A N G U A G E   D A I L Y
            1. Log in
            0. Exit
              """)
        
    def choose(self):
        choice = eval(input(("\t > ")))
        utility.clear()
        match choice:
            case 1:
                pass

            case 0:
                ensure = eval(input(("Are you sure ? [Y/N]\n\t > ")))
                if ensure == 'y' or 'Y':
                    print("See you again !")

            
            case _:
                print("Error: invalid choice !")
                pass