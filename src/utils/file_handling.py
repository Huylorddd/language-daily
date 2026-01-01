class File:
    @staticmethod
    def addFile(fileName):

        # Create datafile in data folder.
        filePath = ".\\data\\" + fileName

        with open(filePath, "a", encoding="utf-8") as file:
            while True:
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
        print("Added successfully !")

    @staticmethod
    def takeOutFile(fileName, output):

        # Create datafile in data folder.
        filePath = ".\\data\\" + fileName

        with open(filePath, "r", encoding="utf-8") as file:
            for line in file:
                # gán key và value thành các giá trị được phân cách bởi dấu ':' đầu tiên
                key, value = line.strip().split(":", 1) 
                output[key.strip()] = value.strip()

# cn = function()
# cn.addFile("fileTest.txt")