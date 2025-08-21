import sensor
import time

while True:
    temp = sensor.readSensor()
    print(temp)
    time.sleep(3)

