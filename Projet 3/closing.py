from sense_hat import SenseHat
import time


def closing():
    s = SenseHat()
    s.low_light = True

    white = (255,255,255)
    nothing = (0,0,0)


    def twosquare():
        W = white
        O = nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def threesquare():
        O = nothing
        W = white
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, W, W, O, O, O,
        O, O, O, W, W, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def foursquare():
        W = white
        O = nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, W, W, W, W, O, O,
        O, O, W, W, W, W, O, O,
        O, O, W, W, W, W, O, O,
        O, O, W, W, W, W, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def fivesquare():
        W = white
        O = nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def fullsquare():
        O = nothing
        W = white
        logo = [
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        ]
        return logo

    images = [fullsquare, fivesquare, foursquare, threesquare, twosquare]


    while True: 
        for count in range(len(images)):
          s.set_pixels(images[count % len(images)]())
          time.sleep(.25)
        break