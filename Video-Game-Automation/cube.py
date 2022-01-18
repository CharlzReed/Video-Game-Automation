import pydirectinput as g
import keyboard as k
from main import GPS
import mouse
import time


def main():
    SM = input('Singleplayer or Multiplayer (s/m)? ').lower()
    #SM = 's'
    time.sleep(1)
    go = GPS(gamemode=SM)

    while True:
        if go.window_focus():
            print('Starting')
            time.sleep(1)
            break

    STOP = 7
    height = 50

    counter = 1
    set_height = 1
    corner = 1

    go.turn(direction_x='snap', direction_y=855)

    while True:
        if go.window_focus() == False or k.is_pressed('esc'):
            g.keyUp('shift')
            g.keyUp('s')
            break


        g.keyDown('shift')
        g.keyDown('s')

        print(counter, set_height)

        if height == set_height:
            g.keyUp('s')
            g.keyUp('shift')
            break
        
        time.sleep(0.5)
    
        if counter != STOP:
            time.sleep(0.25)
            mouse.right_click()
            time.sleep(0.1)
            mouse.right_click()
            time.sleep(0.1)
            mouse.right_click()
            counter += 1
        
        elif counter == STOP-1 and corner == 4:
            time.sleep(0.5)
            counter += 1

        elif counter == STOP and corner != 4:
            set_height += 1
            corner += 1
            counter = 1

            g.keyUp('s')
            time.sleep(0.1)
            g.press('w')
            time.sleep(0.1)
            g.press('w')
            time.sleep(0.1)
            g.press('w')
            time.sleep(0.1)
            g.press('w')
            time.sleep(0.1)
            g.press('w')
            time.sleep(0.1)

            go.turn(word_dir='left')   


        elif counter == STOP and corner == 4:
            set_height += 1
            corner = 1
            counter = 1

            time.sleep(1)

            g.keyUp('s')
            time.sleep(0.1)
            g.press('w')
            time.sleep(0.1)
            g.press('w')
            time.sleep(0.1)
            g.press('w')
            time.sleep(0.1)
            g.press('w')
            time.sleep(0.1)
            g.press('w')
            time.sleep(0.25)
            g.press('space')
            mouse.right_click()
            time.sleep(0.25)
            g.press('space')
            mouse.right_click()
            time.sleep(0.25)
            g.press('space')
            mouse.right_click()

            time.sleep(0.25)

            go.turn(word_dir='left')


            


if __name__ == '__main__':
    main()
