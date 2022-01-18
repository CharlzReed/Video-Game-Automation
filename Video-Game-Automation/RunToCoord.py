import pydirectinput as g
import keyboard as k
from main import GPS
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

    while True:
        print(go.see_lava())
    


    # go.turn(direction_x=-0, direction_y=140)
    # time.sleep(0.25)
    # g.press('t')
    # time.sleep(0.25)
    # k.write('/tp cer_26 -98.5 ~ 262.5')
    # k.press('enter')
    # time.sleep(0.25)

    # go.angle_between_coords([-915, 40, 2625])

    # go.walk_to([-915, 40, 2625])
    # print(go.angle_between_coords([-935, 40, 2675]))
    # print(go.angle_between_coords([-985, 40, 2695]))
    # print(go.angle_between_coords([-1035, 40, 2675]))
    # print(go.angle_between_coords([-1055, 40, 2625]))
    # print(go.angle_between_coords([-1035, 40, 2575]))
    # print(go.angle_between_coords([-985, 40, 2555]))
    # print(go.angle_between_coords([-935, 40, 2575]))


    # for i in go.locations['PATH1']:
    #     go.walk_to(i)
    # for i in go.locations['PATH2']:
    #     go.walk_to(i)






if __name__ == '__main__':
    main()