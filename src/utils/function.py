class function:
    def addFile(self,fileName):
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

# cn = function()
# cn.addFile("fileTest.txt")