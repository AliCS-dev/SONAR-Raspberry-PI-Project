from gpiozero import DistanceSensor
ultrasonic = DistanceSensor(echo=17,trigger=4, max_distance=4) #4m max range

while True:
      ultrasonic.wait_for_in_range()
      print("In range")
      ultrasonic.wait_for_out_of_range()
      print("Out of range")