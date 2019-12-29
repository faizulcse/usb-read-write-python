import serial

ser = serial.Serial("COM5", 921600)
inputData = "AT + CMGL = \"ALL\"\r"
ser.write(inputData.encode())
discardData = ser.readline()  # This statement is used to discard receive data's first line
# print(discardData.rstrip().decode())
smsCnt = 0
while True:
    receiveData = ser.readline().rstrip().decode()
    if (receiveData.__len__() != 0):
        if (receiveData != "OK"):
            if (receiveData.__contains__("+CMGL:")):
                smsCnt = smsCnt + 1
            else:
                print(receiveData)
        else:
            print("Total SMS Count: " + smsCnt.__str__())
            break
