import pydirectinput as g
import keyboard as k
from main import GPS
from random import randint
import mouse
import time


def main():
    # SM = input('Singleplayer or Multiplayer (s/m)? ').lower()
    SM = 's'
    go = GPS(gamemode=SM)

    
    while True:
        if go.window_focus():
            print('Starting')
            time.sleep(1)
            break

    # while True:
        # start_time = time.time()

    print(go.xyz2())

        # print(f'--- {1/(time.time() - start_time)} seconds ---' )





if __name__ == '__main__':
    main()
