import serial

ser = serial.Serial("COM5", 921600)
inputData = "AT\r"
ser.write(inputData.encode())
discardData = ser.readline() # This statement is used to discard receive data's first line
receiveData = ser.readline()
print(receiveData.decode())
