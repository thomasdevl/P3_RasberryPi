from sense_hat import SenseHat
import time
import random

def opening():
    
    s = SenseHat()
    s.low_light = True

    white = (255,255,255)
    nothing = (0,0,0)
    W = white
    O = nothing

    def spiral1():
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
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    W = (r, g, b)
      
    def spiral1():
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
      
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    a = (r, g, b)
      
    def spiral2():
      
      logo = [
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, W, W, O, O, O,
      O, O, O, a, a, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo
      
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    z = (r, g, b)
      
    def spiral3():
      logo = [
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, z, W, W, O, O, O,
      O, O, z, a, a, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo 
      
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    e = (r, g, b)
      
    def spiral4():
      logo = [
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, e, e, O, O, O, O,
      O, O, z, W, W, O, O, O,
      O, O, z, a, a, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t = (r, g, b)
    
    def spiral5():
      logo = [
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, e, e, t, t, O, O,
      O, O, z, W, W, O, O, O,
      O, O, z, a, a, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo
      
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    y = (r, g, b)
      
    def spiral6():
      logo = [
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, e, e, t, t, O, O,
      O, O, z, W, W, y, O, O,
      O, O, z, a, a, y, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo
      
    def spiral7():
      logo = [
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, e, e, t, t, O, O,
      O, O, z, W, W, y, O, O,
      O, O, z, a, a, y, O, O,
      O, O, O, O, W, W, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo
    def spiral8():
      logo = [
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, e, e, t, t, O, O,
      O, O, z, W, W, y, O, O,
      O, O, z, a, a, y, O, O,
      O, O, a, a, W, W, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo
      
    def spiral9():
      logo = [
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, O, e, e, t, t, O, O,
      O, O, z, W, W, y, O, O,
      O, z, z, a, a, y, O, O,
      O, z, a, a, W, W, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo
    def spiral10():
      logo = [
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      O, e, e, e, t, t, O, O,
      O, e, z, W, W, y, O, O,
      O, z, z, a, a, y, O, O,
      O, z, a, a, W, W, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo
    def spiral11():
      logo = [
      O, O, O, O, O, O, O, O,
      O, t, t, O, O, O, O, O,
      O, e, e, e, t, t, O, O,
      O, e, z, W, W, y, O, O,
      O, z, z, a, a, y, O, O,
      O, z, a, a, W, W, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo
    def spiral12():
      logo = [
      O, O, O, O, O, O, O, O,
      O, t, t, y, y, O, O, O,
      O, e, e, e, t, t, O, O,
      O, e, z, W, W, y, O, O,
      O, z, z, a, a, y, O, O,
      O, z, a, a, W, W, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo
    def spiral13():
      logo = [
      O, O, O, O, O, O, O, O,
      O, t, t, y, y, W, W, O,
      O, e, e, e, t, t, O, O,
      O, e, z, W, W, y, O, O,
      O, z, z, a, a, y, O, O,
      O, z, a, a, W, W, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo
    def spiral14():
      logo = [
      O, O, O, O, O, O, O, O,
      O, t, t, y, y, W, W, O,
      O, e, e, e, t, t, a, O,
      O, e, z, W, W, y, a, O,
      O, z, z, a, a, y, O, O,
      O, z, a, a, W, W, O, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo
    def spiral15():
      logo = [
      O, O, O, O, O, O, O, O,
      O, t, t, y, y, W, W, O,
      O, e, e, e, t, t, a, O,
      O, e, z, W, W, y, a, O,
      O, z, z, a, a, y, z, O,
      O, z, a, a, W, W, z, O,
      O, O, O, O, O, O, O, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo
    def spiral16():
      logo = [
      O, O, O, O, O, O, O, O,
      O, t, t, y, y, W, W, O,
      O, e, e, e, t, t, a, O,
      O, e, z, W, W, y, a, O,
      O, z, z, a, a, y, z, O,
      O, z, a, a, W, W, z, O,
      O, O, O, O, O, e, e, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo
    def spiral17():
      logo = [
      O, O, O, O, O, O, O, O,
      O, t, t, y, y, W, W, O,
      O, e, e, e, t, t, a, O,
      O, e, z, W, W, y, a, O,
      O, z, z, a, a, y, z, O,
      O, z, a, a, W, W, z, O,
      O, O, O, t, t, e, e, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo
    def spiral18():
      logo = [
      O, O, O, O, O, O, O, O,
      O, t, t, y, y, W, W, O,
      O, e, e, e, t, t, a, O,
      O, e, z, W, W, y, a, O,
      O, z, z, a, a, y, z, O,
      O, z, a, a, W, W, z, O,
      O, y, y, t, t, e, e, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo
    def spiral19():
      logo = [
      O, O, O, O, O, O, O, O,
      O, t, t, y, y, W, W, O,
      O, e, e, e, t, t, a, O,
      O, e, z, W, W, y, a, O,
      O, z, z, a, a, y, z, O,
      W, z, a, a, W, W, z, O,
      W, y, y, t, t, e, e, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo
    def spiral20():
      logo = [
      O, O, O, O, O, O, O, O,
      O, t, t, y, y, W, W, O,
      O, e, e, e, t, t, a, O,
      a, e, z, W, W, y, a, O,
      a, z, z, a, a, y, z, O,
      W, z, a, a, W, W, z, O,
      W, y, y, t, t, e, e, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo
    def spiral21():
      logo = [
      O, O, O, O, O, O, O, O,
      z, t, t, y, y, W, W, O,
      z, e, e, e, t, t, a, O,
      a, e, z, W, W, y, a, O,
      a, z, z, a, a, y, z, O,
      W, z, a, a, W, W, z, O,
      W, y, y, t, t, e, e, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo
    def spiral22():
      logo = [
      e, e, O, O, O, O, O, O,
      z, t, t, y, y, W, W, O,
      z, e, e, e, t, t, a, O,
      a, e, z, W, W, y, a, O,
      a, z, z, a, a, y, z, O,
      W, z, a, a, W, W, z, O,
      W, y, y, t, t, e, e, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo
    def spiral23():
      logo = [
      e, e, t, t, O, O, O, O,
      z, t, t, y, y, W, W, O,
      z, e, e, e, t, t, a, O,
      a, e, z, W, W, y, a, O,
      a, z, z, a, a, y, z, O,
      W, z, a, a, W, W, z, O,
      W, y, y, t, t, e, e, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo
    def spiral24():
      logo = [
      e, e, t, t, y, y, O, O,
      z, t, t, y, y, W, W, O,
      z, e, e, e, t, t, a, O,
      a, e, z, W, W, y, a, O,
      a, z, z, a, a, y, z, O,
      W, z, a, a, W, W, z, O,
      W, y, y, t, t, e, e, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo
    def spiral25():
      logo = [
      e, e, t, t, y, y, W, W,
      z, t, t, y, y, W, W, O,
      z, e, e, e, t, t, a, O,
      a, e, z, W, W, y, a, O,
      a, z, z, a, a, y, z, O,
      W, z, a, a, W, W, z, O,
      W, y, y, t, t, e, e, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo
    def spiral26():
      logo = [
      e, e, t, t, y, y, W, W,
      z, t, t, y, y, W, W, a,
      z, e, e, e, t, t, a, a,
      a, e, z, W, W, y, a, O,
      a, z, z, a, a, y, z, O,
      W, z, a, a, W, W, z, O,
      W, y, y, t, t, e, e, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo
    def spiral27():
      logo = [
      e, e, t, t, y, y, W, W,
      z, t, t, y, y, W, W, a,
      z, e, e, e, t, t, a, a,
      a, e, z, W, W, y, a, z,
      a, z, z, a, a, y, z, z,
      W, z, a, a, W, W, z, O,
      W, y, y, t, t, e, e, O,
      O, O, O, O, O, O, O, O,
      ]
      return logo
    def spiral28():
      logo = [
      e, e, t, t, y, y, W, W,
      z, t, t, y, y, W, W, a,
      z, e, e, e, t, t, a, a,
      a, e, z, W, W, y, a, z,
      a, z, z, a, a, y, z, z,
      W, z, a, a, W, W, z, e,
      W, y, y, t, t, e, e, e,
      O, O, O, O, O, O, O, O,
      ]
      return logo
    def spiral29():
      logo = [
      e, e, t, t, y, y, W, W,
      z, t, t, y, y, W, W, a,
      z, e, e, e, t, t, a, a,
      a, e, z, W, W, y, a, z,
      a, z, z, a, a, y, z, z,
      W, z, a, a, W, W, z, e,
      W, y, y, t, t, e, e, e,
      O, O, O, O, O, O, t, t,
      ]
      return logo
    def spiral30():
      logo = [
      e, e, t, t, y, y, W, W,
      z, t, t, y, y, W, W, a,
      z, e, e, e, t, t, a, a,
      a, e, z, W, W, y, a, z,
      a, z, z, a, a, y, z, z,
      W, z, a, a, W, W, z, e,
      W, y, y, t, t, e, e, e,
      O, O, O, O, y, y, t, t,
      ]
      return logo
    def spiral31():
      logo = [
      e, e, t, t, y, y, W, W,
      z, t, t, y, y, W, W, a,
      z, e, e, e, t, t, a, a,
      a, e, z, W, W, y, a, z,
      a, z, z, a, a, y, z, z,
      W, z, a, a, W, W, z, e,
      W, y, y, t, t, e, e, e,
      O, O, W, W, y, y, t, t,
      ]
      return logo
    def spiral32():
      logo = [
      e, e, t, t, y, y, W, W,
      z, t, t, y, y, W, W, a,
      z, e, e, e, t, t, a, a,
      a, e, z, W, W, y, a, z,
      a, z, z, a, a, y, z, z,
      W, z, a, a, W, W, z, e,
      W, y, y, t, t, e, e, e,
      a, a, W, W, y, y, t, t,
      ]
      return logo

    images = [spiral1, spiral2, spiral3, spiral4, spiral5, spiral6, spiral7, spiral8, spiral9, spiral10, spiral11, spiral12, spiral13, spiral14, spiral15, spiral16, spiral17, spiral18, spiral19, spiral20, spiral21, spiral22, spiral23, spiral24, spiral25, spiral26, spiral27, spiral28, spiral29, spiral30, spiral31, spiral32]
    count = 0

    while True:
      for count in range(len(images)):
        s.set_pixels(images[count % len(images)]())
        
        time.sleep(.03)
      break
    
  
opening()