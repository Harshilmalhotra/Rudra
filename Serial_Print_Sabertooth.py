import serial
import time
ser = serial.Serial('/dev/ttyUSB0', 9600)  
motor1_speed = 100 

clearMotor 1
ser.write(bytes([motor1_speed]))
print(bytes([motor1_speed]))
time.sleep(3)

ser.write(bytes([0]))
ser.close()

