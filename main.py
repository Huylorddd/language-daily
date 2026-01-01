from src.utils.menu_generator import Menu
from src.utils.file_handling import File

def main():
    Menu.show()

    test = {}
    File.addFile("filetext.txt")
    File.takeOutFile("filetext.txt", test)
    print(test)


if __name__ == "__main__":
    main()