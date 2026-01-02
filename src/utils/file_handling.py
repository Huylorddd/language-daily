from src.utils.utilities import utility
import time
import glob
import os

filePath = ".\\data\\"

class File:

    # Counting how many .txt files are there in data directory::
    @staticmethod
    def countFile():
        file_pattern = "*.txt"

        search_path = os.path.join(filePath, file_pattern)
        txt_files = glob.glob(search_path)
        count = len(txt_files)
        return count


    # Create datafile in data folder with saved vocab.
    @staticmethod
    def addFile():
        # Auto add new .txt file without duplication.
        fileName = os.path.join(filePath, f"daily_vocab{File.countFile()}.txt")

        with open(fileName, "w", encoding="utf-8") as file:
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

                if stop.lower() == 'n': break

        utility.clear()
        print("Added successfully !")
        time.sleep(1)
        

    # Transfer data from datafile to output variable.
    @staticmethod
    def takeOutFile(fileName, output):
        filePath += fileName

        with open(filePath, "r", encoding="utf-8") as file:
            for line in file:
                # gán key và value thành các giá trị được phân cách bởi dấu ':' đầu tiên
                key, value = line.strip().split(":", 1) 
                output[key.strip()] = value.strip()

# cn = function()
# cn.addFile("fileTest.txt")