#Autor: Jacek Piotrowski
#ver: 0.1

from sense_hat import SenseHat
import random
from time import sleep
def clrscr():
    y=(255,254,27)
    blk=(0,0,0)
    for x in range(8):
        for y in range(8):
            sense.set_pixel(x,y,212,206,50)
            sleep(0.05)
            sense.set_pixel(x,y,49,49,142)
    
    
def rand_pixels():
    for i in range(30):
        sense.set_pixel(random.randint(0,7),random.randint(0,7),random.randint(0,255),random.randint(0,255),random.randint(0,255))
        sleep(random.random())
        
    
    
    
sense = SenseHat()
sense.clear()
w = (150, 150, 150)
b = (0, 0, 255)
e = (0, 0, 0)
y=(255,254,27)
o=(255,182,27)
r=(255,74,27)
fig1 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,y,y,e,e,e,
e,e,e,y,y,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]
fig2 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,o,o,o,o,e,e,
e,e,o,e,e,o,e,e,
e,e,o,e,e,o,e,e,
e,e,o,o,o,o,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]
fig3 = [
e,e,e,e,e,e,e,e,
e,o,o,o,o,o,o,e,
e,o,e,e,e,e,o,e,
e,o,e,y,y,e,o,e,
e,o,e,y,y,e,o,e,
e,o,e,e,e,e,o,e,
e,o,o,o,o,o,o,e,
e,e,e,e,e,e,e,e
]
fig4 = [
r,r,r,r,r,r,r,r,
r,e,e,e,e,e,e,r,
r,e,o,o,o,o,e,r,
r,e,o,e,e,o,e,r,
r,e,o,e,e,o,e,r,
r,e,o,o,o,o,e,r,
r,e,e,e,e,e,e,r,
r,r,r,r,r,r,r,r
]

temp = sense.get_temperature()
t = sense.get_temperature()
p = sense.get_pressure()
h = sense.get_humidity()

  # Round the values to one decimal place
t = round(t, 2)
p = round(p, 2)
h = round(h, 2)
 
message_temp = "Temperature: " + str(t) 
message_pres = " Pressure: " + str(p) 
message_humi = " Humidity: " + str(h)

while True:
    rand_pixels()          
    sleep(0.5)
    clrscr()
    sleep(0.5)
    sense.set_pixels(fig1)
    sleep(0.5)    
    sense.set_pixels(fig2)
    sleep(0.5)
    sense.set_pixels(fig3)
    sleep(0.5)
    sense.set_pixels(fig4)
    sleep(0.5)
    sense.show_message(message_temp,scroll_speed=0.1,text_colour=[255,0,0])
    sense.show_message(message_pres,scroll_speed=0.1,text_colour=[0,255,0])
    sense.show_message(message_humi,scroll_speed=0.1,text_colour=[0,0,255])
    
