import pydirectinput as g
import keyboard as k
from main import GPS
import mouse
import time


def main():
    SM = input('Singleplayer or Multiplayer (s/m)? ').lower()
    go = GPS(gamemode=SM)

    while True:
        if go.window_focus():
            print('Starting')
            time.sleep(1)
            break


    go.turn(direction_x='snap', direction_y=837)
    go.turn(direction_x='+450', direction_y='keep')

    g.press('esc')
    time.sleep(0.05)
    g.keyDown('shift')
    g.keyDown('d')
    g.keyDown('s')
    time.sleep(0.05)
    g.press('esc')

    while True:
        if go.window_focus() == False or k.is_pressed('esc'):
            # g.keyUp('shift')
            g.press('esc')
            time.sleep(0.05)
            g.keyUp('d')
            g.keyUp('s')
            time.sleep(0.05) 
            g.press('esc')
            break
        
        time.sleep(1)
        mouse.right_click()
        time.sleep(0.05)
        mouse.right_click()
        time.sleep(0.05)
        mouse.right_click()



        if k.is_pressed('z'):
            g.press('esc')
            time.sleep(0.05)
            g.keyUp('d')
            g.keyUp('s')
            time.sleep(0.05)
            g.press('esc')

            go.turn(word_dir='around')

            g.press('esc')
            time.sleep(0.05)
            g.keyDown('d')
            g.keyDown('s')
            time.sleep(0.05)
            g.press('esc')
        

        if k.is_pressed('o'):
            print('paused, press "i" to continue')
            g.keyUp('d')
            g.keyUp('s')

            while True:
                if k.is_pressed('i'):
                    print('resumed')
                    go.turn(direction_x='snap', direction_y=837)
                    go.turn(direction_x='+450', direction_y='keep')

                    g.press('esc')
                    time.sleep(0.05)
                    g.keyDown('shift')
                    g.keyDown('d')
                    g.keyDown('s')
                    time.sleep(0.05)
                    g.press('esc')
                    break


            


if __name__ == '__main__':
    main()
