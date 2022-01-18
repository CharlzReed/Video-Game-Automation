import pydirectinput as g
import keyboard as k
from main import GPS
import mouse
import time

def main():
    SM = input('Singleplayer or Multiplayer (s/m)? ').lower()
    # SM = 's'
    go = GPS(gamemode=SM)

    while True:
        if go.window_focus():
            print('\n\nStarting\n\n')
            time.sleep(1)
            break
    
    go.turn(direction_x='keep', direction_y=-55)

    time.sleep(1)
    _, casted = go.fishing()
    if casted == True:
        mouse.right_click()
        time.sleep(3)


    while True:
        if go.window_focus() == False or k.is_pressed('esc'):
            print('\n\nWindow lost focus, exiting.\n\n')
            break

        line, _ = go.fishing()

        if line:
            mouse.right_click()
            print('Fish on!')
            time.sleep(0.65)
            mouse.right_click()
            time.sleep(3)
        else:
            print('|\n |\n  |\n   |\n   |\n  |\n |\n|\n')
        





if __name__ == '__main__':
    main()