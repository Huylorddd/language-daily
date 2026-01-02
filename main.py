from src.utils.menu_generator import Menu
from src.utils.file_handling import File

def main():
    while True:
        Menu.show()
        # Ensuring the exit command from user::
        if Menu.choose() == False:
            break


if __name__ == "__main__":
    main()