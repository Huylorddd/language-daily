from src.utils.utilities import utility
import time

class File:

    # Create datafile in data folder with saved vocab.
    @staticmethod
    def addFile(fileName):

        filePath = ".\\data\\" + fileName

        with open(filePath, "a", encoding="utf-8") as file:
            while True:
                utility.clear()
                ENG = input("Add English words : ")
                VIE = input("Add meaning : ")
                file.write(ENG + ":" + VIE + "\n")

                # Avoiding invalid inputs::
                while True:
                    stop = input("Do you want to continue (y/n) --> ")
                    if stop in ("y","Y","n","N"):
                        break
                    else:
                        print("Error: Invalid input.")

                if stop == 'n' or 'N': break

        utility.clear()
        print("Added successfully !")
        time.sleep(1)
        

    # Transfer data from datafile to output variable.
    @staticmethod
    def takeOutFile(fileName, output):

        filePath = ".\\data\\" + fileName

        with open(filePath, "r", encoding="utf-8") as file:
            for line in file:
                # gán key và value thành các giá trị được phân cách bởi dấu ':' đầu tiên
                key, value = line.strip().split(":", 1) 
                output[key.strip()] = value.strip()

# cn = function()
# cn.addFile("fileTest.txt")