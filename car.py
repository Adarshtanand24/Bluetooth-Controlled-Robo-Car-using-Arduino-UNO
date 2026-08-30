import serial
import time

# Connect to Bluetooth module
# Change COM5 to your HC-05 Bluetooth port
car = serial.Serial("COM5", 9600)
time.sleep(2)

print("================================")
print(" Bluetooth Controlled Robo Car")
print("================================")
print("F - Forward")
print("B - Backward")
print("L - Left")
print("R - Right")
print("S - Stop")
print("Q - Quit")

while True:
    command = input("Enter command: ").upper()

    if command == "F":
        car.write(b"F")
        print("Car moving forward")

    elif command == "B":
        car.write(b"B")
        print("Car moving backward")

    elif command == "L":
        car.write(b"L")
        print("Car turning left")

    elif command == "R":
        car.write(b"R")
        print("Car turning right")

    elif command == "S":
        car.write(b"S")
        print("Car stopped")

    elif command == "Q":
        car.write(b"S")
        print("Exiting program...")
        break

    else:
        print("Invalid command!")

car.close()