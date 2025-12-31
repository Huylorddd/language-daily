import os
from src.utils.menu_generator import Menu

"""
HELPER
"""
# Clean terminal::
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    clear()
    menu = Menu()
    menu.show()

if __name__ == "__main__":
    main()