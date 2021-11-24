from sense_hat import SenseHat
import time

sense = SenseHat()

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
grey = (95,95,95)
brown = (139,69,19)

def smiley():
	#fait un smile 
    G = green
    Y = yellow
    B = blue
    O = nothing
    R = red
    P = pink

    logo = [
    O, O, O, Y, Y, O, O, O,
    O, Y, Y, Y, Y, Y, O, O,
    O, Y, P, Y, Y, P, Y, O,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, B, Y, Y, Y, Y, B, Y,
    O, Y, B, B, B, B, Y, O,
    O, O, Y, R, R, Y, O, O,
    O, O, O, Y, Y, O, O, O,
    ]
    sense.set_pixels(logo)

def thermostat():
  	#fait un thermostat
	O = nothing 
	W = white
	R = red
	B = blue
	G = grey
	logo = [
	O, O, O, W, W, O, O, O,
	O, O, O, W, O, O, O, O,
	O, O, O, W, W, O, O, O,
	O, O, O, W, O, O, O, O,
	O, O, O, W, W, O, O, O,
	O, O, O, R, R, W, O, O,
	O, O, W, R, R, W, O, O,
	O, O, O, W, W, O, O, O,
	]
	sense.set_pixels(logo)

def cherry():
    R = red
    B = brown
    O = nothing
    logo = [
    O, O, O, O, B, O, O, O,
    O, O, O, O, B, O, O, O,
    O, O, O, B, O, B, O, O,
    O, O, R, O, O, B, O, O,
    O, R, R, R, O, R, O, O,
    O, O, R, O, R, R, R, O,
    O, O, O, O, O, R, O, O,
    O, O, O, O, O, O, O, O,
    ]
    sense.set_pixels(logo)


