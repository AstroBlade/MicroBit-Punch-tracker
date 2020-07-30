from microbit import *
import radio
def shaking():
  if accelerometer.was_gesture("shake"):
    return True
  else:
    return False
def scroll(image):
  display.show(Image(image))
while True:
  Fullsteps = 0
  ministeps = 0
  if button_b.was_pressed():
    display.scroll(str(Fullsteps))
  if button_a.was_pressed():
    ministeps = 1
    i = 0
    previ = i
    while i != 20:
      print(str(i))
      if accelerometer.was_gesture("shake"):
        print("OWO")
        i = i+1
        ministeps = ministeps + 1
        Fullsteps = Fullsteps + 1
      else:
        print("else")
    if i == 20:
      print("You got your goal! Your total punches are " + str(Fullsteps))
        
