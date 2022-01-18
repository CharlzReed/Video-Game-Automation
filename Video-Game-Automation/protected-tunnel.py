import pydirectinput as g
import keyboard as k
from main import GPS
import mouse
import time


def main():
    SM = input('Singleplayer or Multiplayer (s/m)? ').lower()
    go = GPS(gamemode=SM)

    out = 30

    while True:
        if go.window_focus():
            print('Starting')
            time.sleep(1)
            break

    go.turn(direction_x='snap', direction_y=800)
    g.keyDown('shift')
    g.keyDown('s')
    time.sleep(1.5)
    g.keyUp('s')

    for _ in range(out+1):
        if go.window_focus() == False or k.is_pressed('esc'):
            g.keyUp('s')
            g.press('w')
            g.keyUp('shift')
            break

        g.keyDown('shift')
        g.keyDown('s')
        time.sleep(0.75)
        g.keyUp('s')

        go.turn(direction_x='-380', direction_y='-570')
        mouse.right_click()
        go.turn(direction_x='keep', direction_y='-305')
        mouse.right_click()
        go.turn(direction_x='+380', direction_y='-350')
        mouse.right_click()
        go.turn(direction_x='+360', direction_y='+360')
        mouse.right_click()
        go.turn(direction_x='keep', direction_y='+305')
        mouse.right_click()
        go.turn(direction_x='snap', direction_y=800)
        mouse.right_click()
        

    g.keyUp('s')
    g.keyDown('w')
    time.sleep(1)
    g.keyUp('w')
    g.keyUp('shift')



if __name__ == '__main__':
    main()
