class function:
    @staticmethod
    def addFile(fileName):
        with open(fileName,"a",encoding = "utf-8") as file:
            while True:
                EL = input("Add English words :")
                VN = input("Add meaning :")
                file.write(EL + ":" + VN + "\n")

                #Tránh nhận những giá trị không hợp lệ
                while True:
                    stop = input("Do you want to continue (y/n) --> ")
                    if stop in ("y","Y","n","N"):break
                    
                if stop == 'n' or stop == 'N':break
        print("Add success!")

    @staticmethod
    def takeOutFile(filename,data):
        with open(filename,"r",encoding = "utf-8") as file:
            for line in file:
                line = line.strip()
                # gán key và value thành các giá trị được phân cách bởi dấu ':' đầu tiên
                key, value = line.split(":",1) 
                data[key.strip()] = value.strip()
# cn = function()
# cn.addFile("fileTest.txt")