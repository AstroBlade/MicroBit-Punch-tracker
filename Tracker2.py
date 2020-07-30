from microbit import *
import radio
Fullsteps = 0
ministeps = 0
def scroll(image):
  display.show(Image(image))
while True:
  if button_b.was_pressed():
    display.scroll(str(Fullsteps))
  if button_a.was_pressed():
    ministeps = 1
    i = 0
    previ = i
    while i != 20:
      if button_b.was_pressed():
        display.scroll(str(ministeps))
      print(str(i))
      if accelerometer.was_gesture("shake"):
        i = i+1
        ministeps = ministeps + 1
        Fullsteps = Fullsteps + 1
    if i == 20:
      display.scroll("Total punches are " + str(Fullsteps))
        
