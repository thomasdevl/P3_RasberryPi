from sense_hat import SenseHat
import time

def opening():
    
    s = SenseHat()
    s.low_light = True

    white = (255,255,255)
    nothing = (0,0,0)

    def spiral1():
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

    def spiral1():
        W = white
        O = nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, W, W, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo


    def spiral2():
        W = white
        O = nothing
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

    def spiral3():
        W = white
        O = nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, W, W, W, O, O, O,
        O, O, W, W, W, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo    
      
    def spiral4():
        W = white
        O = nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, W, W, O, O, O, O,
        O, O, W, W, W, O, O, O,
        O, O, W, W, W, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def spiral5():
        W = white
        O = nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, W, W, W, W, O, O,
        O, O, W, W, W, O, O, O,
        O, O, W, W, W, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def spiral6():
        W = white
        O = nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, W, W, W, W, O, O,
        O, O, W, W, W, W, O, O,
        O, O, W, W, W, W, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def spiral7():
        W = white
        O = nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, W, W, W, W, O, O,
        O, O, W, W, W, W, O, O,
        O, O, W, W, W, W, O, O,
        O, O, O, O, W, W, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def spiral8():
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
        
    def spiral9():
        W = white
        O = nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, W, W, W, W, O, O,
        O, O, W, W, W, W, O, O,
        O, W, W, W, W, W, O, O,
        O, W, W, W, W, W, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def spiral10():
        W = white
        O = nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, W, W, W, W, W, O, O,
        O, W, W, W, W, W, O, O,
        O, W, W, W, W, W, O, O,
        O, W, W, W, W, W, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def spiral11():
        W = white
        O = nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, W, W, O, O, O, O, O,
        O, W, W, W, W, W, O, O,
        O, W, W, W, W, W, O, O,
        O, W, W, W, W, W, O, O,
        O, W, W, W, W, W, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def spiral12():
        W = white
        O = nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, W, W, W, W, O, O, O,
        O, W, W, W, W, W, O, O,
        O, W, W, W, W, W, O, O,
        O, W, W, W, W, W, O, O,
        O, W, W, W, W, W, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def spiral13():
        W = white
        O = nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, O, O,
        O, W, W, W, W, W, O, O,
        O, W, W, W, W, W, O, O,
        O, W, W, W, W, W, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def spiral14():
        W = white
        O = nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, O, O,
        O, W, W, W, W, W, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def spiral15():
        W = white
        O = nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def spiral16():
        W = white
        O = nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, O, O, O, O, W, W, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def spiral17():
        W = white
        O = nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, O, O, W, W, W, W, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def spiral18():
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

    def spiral19():
        W = white
        O = nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def spiral20():
        W = white
        O = nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def spiral21():
        W = white
        O = nothing
        logo = [
        O, O, O, O, O, O, O, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def spiral22():
        W = white
        O = nothing
        logo = [
        W, W, O, O, O, O, O, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def spiral23():
        W = white
        O = nothing
        logo = [
        W, W, W, W, O, O, O, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def spiral24():
        W = white
        O = nothing
        logo = [
        W, W, W, W, W, W, O, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def spiral25():
        W = white
        O = nothing
        logo = [
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def spiral26():
        W = white
        O = nothing
        logo = [
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def spiral27():
        W = white
        O = nothing
        logo = [
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def spiral28():
        W = white
        O = nothing
        logo = [
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def spiral29():
        W = white
        O = nothing
        logo = [
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        O, O, O, O, O, O, W, W,
        ]
        return logo

    def spiral30():
        W = white
        O = nothing
        logo = [
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        O, O, O, O, W, W, W, W,
        ]
        return logo

    def spiral31():
        W = white
        O = nothing
        logo = [
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        O, O, W, W, W, W, W, W,
        ]
        return logo

    def spiral32():
        W = white
        O = nothing
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


    images = [spiral1, spiral2, spiral3, spiral4, spiral5, spiral6, spiral7, spiral8, spiral9, spiral10, spiral11, spiral12, spiral13, spiral14, spiral15, spiral16, spiral17, spiral18, spiral19, spiral20, spiral21, spiral22, spiral23, spiral24, spiral25, spiral26, spiral27, spiral28, spiral29, spiral30, spiral31, spiral32]
    count = 0

    while True:
      for count in range(len(images)):
        s.set_pixels(images[count % len(images)]())
        time.sleep(.03)
      break
