from src.utils.utilities import utility
from src.utils.file_handling import File

class Menu:
    # Menu showcase::
    @staticmethod
    def show():
        utility.clear()
        print ("""
        L A N G U A G E   D A I L Y
               - - - - - - -
            1. Add new vocabulary
            2. Review vocabulary
            0. Exit
              """)
    
    # Choice selection for user::
    @staticmethod
    def choose():
        try:
            choice = int(input("\t > "))
        except ValueError:
            print("Error: invalid choice.")
            return True
        utility.clear()
        
        match choice:
            case 1:
                File.addFile()

            case 0:
                ensure = input(("Are you sure ? [Y/N]\n\t > "))
                if ensure == 'y' or ensure == 'Y':
                    print("See you again !")
                    return False
                else:
                    print("Going back to menu...")
                    return True
                    
            case _:
                print("Error: invalid choice.")
                    
            
            