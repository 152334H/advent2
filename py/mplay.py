from getkey import getkey, keys
from aoc import toGrid
ap = 0
MAP = {0:' ', 1:'#', 2:'@', 3:'H', 4:'o'}
def joystick(grid): #returns a joystick value, or None if to autoplay
    global ap
    print toGrid(grid,MAP)
    print 'Use arrow keys to adjust joystick\nOr use the digits 0-9 to have the machine play for you\nOther characters will repeat the previous move'
    if ap:
        ap -= 1
        k = '>'
    else: k = getkey()
    if k == keys.UP or k == keys.DOWN: return 0
    elif k == keys.LEFT: return -1
    elif k == keys.RIGHT: return 1
    else:   #autoplay
        if k.isdigit(): #press 0-9 to plry 10**k times
            ap += 10**int(k)
        return None
