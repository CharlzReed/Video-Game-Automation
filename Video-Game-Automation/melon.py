import pydirectinput as g
import keyboard as k
from main import GPS
import mouse
import time


def main():
    # SM = input('Singleplayer or Multiplayer (s/m)? ').lower()
    SM = 'm'
    go = GPS(gamemode=SM)

    while True:
        if go.window_focus():
            print('Starting')
            time.sleep(1)
            break

    go.turn(direction_x='snap', direction_y=625)

    for j in range(35):
        print('|',j,'|')

        g.keyDown('w')
        mouse.press(button='left')

        for i in range(3):
            print(i)
            if not go.window_focus() or k.is_pressed('z'):
                g.keyUp('w')
                mouse.release(button='left')
                exit()
            
            g.press('1')
            time.sleep(0.65)
            g.press('2')


        mouse.release(button='left')
        g.keyUp('w')


        go.turn(word_dir='around')


        g.keyDown('w')
        mouse.press(button='left')

        for i in range(3):
            print(i)
            if not go.window_focus() or k.is_pressed('z'):
                g.keyUp('w')
                mouse.release(button='left')
                exit()
            
            g.press('1')
            time.sleep(1)
            g.press('2')


        mouse.release(button='left')
        g.keyUp('w')


        go.turn(direction_x='keep', direction_y='-500')
        g.keyDown('e')
        time.sleep(0.35)

        mouse.move(1006,670, absolute=True)
        time.sleep(0.305)
        mouse.click()
        time.sleep(0.035)
        mouse.move(1006,710, absolute=True)
        time.sleep(0.035)
        mouse.click()
        time.sleep(0.035)
        mouse.move(1043,670, absolute=True)
        time.sleep(0.035)
        mouse.click()
        time.sleep(0.035)
        mouse.move(1043,710, absolute=True)
        time.sleep(0.035)
        mouse.click()
        time.sleep(0.035)
        mouse.move(1078,670, absolute=True)
        time.sleep(0.035)
        mouse.click()
        time.sleep(0.035)
        mouse.move(1078,710, absolute=True)
        time.sleep(0.035)
        mouse.click()
        time.sleep(0.035)
        mouse.move(1115,670, absolute=True)
        time.sleep(0.035)
        mouse.click()
        time.sleep(0.035)
        mouse.move(1115,710, absolute=True)
        time.sleep(0.035)
        mouse.click()
        time.sleep(0.035)
        mouse.move(1152,670, absolute=True)
        time.sleep(0.035)
        mouse.click()
        time.sleep(0.035)
        mouse.move(1152,710, absolute=True)
        time.sleep(0.035)
        mouse.click()
        time.sleep(0.035)
        mouse.move(1189,670, absolute=True)
        time.sleep(0.035)
        mouse.click()
        time.sleep(0.035)
        mouse.move(1189,710, absolute=True)
        time.sleep(0.035)
        mouse.click()
        time.sleep(0.035)
        mouse.move(1226,670, absolute=True)
        time.sleep(0.035)
        mouse.click()
        time.sleep(0.035)
        mouse.move(1226,710, absolute=True)
        time.sleep(0.035)
        mouse.click()
        time.sleep(0.035)
        mouse.move(1263,670, absolute=True)
        time.sleep(0.035)
        mouse.click()
        time.sleep(0.035)
        mouse.move(1263,710, absolute=True)
        time.sleep(0.035)
        mouse.click()
        time.sleep(0.35)



        g.press('e')
        time.sleep(0.35)
        go.turn(direction_x='keep', direction_y='+500')


        go.turn(word_dir='around')

        # g.press('4')
        # time.sleep(0.25)
        # mouse.right_click()
        # time.sleep(0.25)
        # mouse.right_click()
        # time.sleep(0.5)
        # mouse.move(687, 456, absolute=True)
        # g.keyDown('shift')
        # time.sleep(0.25)
        # mouse.click()
        # time.sleep(0.25)
        # mouse.move(1200, 456, absolute=True)
        # time.sleep(0.25)
        # mouse.click()
        # time.sleep(0.25)
        # g.keyUp('shift')

        # time.sleep(0.5)
        # g.press('esc')
        # time.sleep(0.25)
        # g.press('3')
        # time.sleep(0.25)
        # mouse.press(button='left')
        # time.sleep(0.5)
        # mouse.release(button='left')
        # time.sleep(10)


        



if __name__ == '__main__':
    main()
