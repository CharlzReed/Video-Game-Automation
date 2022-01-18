# Minecraft Auto-Mine
# Charlie Reed
# 5/3/2021
#==========================

from more_itertools import consecutive_groups
import win32gui, win32ui, win32con
from PIL import ImageGrab, Image
from random import randint
import pydirectinput as g
import pyperclip as clip
import pyautogui as f
import keyboard as k
from cv2 import cv2
import numpy as np
import mouse
import math
import time
import csv
import ast
import mss
import os

################################################################################
class GPS:
    def __init__(self, gamemode='s'):
        self.current_x = 0
        self.current_y = 0
        self.current_z = 0

        self.targetedBlock_x = 0
        self.targetedBlock_y = 0
        self.targetedBlock_z = 0

        self.facing_x = 0
        self.difference_x = 0
        self.facing_y = 0
        self.difference_y = 0


        self.history = [self.xyz()]

        if gamemode == 's':
            # self.xyz_box = (46, 206, 400, 222)
            # self.facing_box = (340, 260, 525, 276)
            # self.targeted_block_box = (1739, 206, 1916, 222)
            self.xyz_box = (22, 114, 203, 123)
            self.facing_box = (340, 260, 525, 276)
            self.targeted_block_box = (1739, 206, 1916, 222)
        elif gamemode == 'm':
            self.xyz_box = (46, 188, 400, 204)
            self.facing_box = (337, 242, 525, 258)
            self.targeted_block_box = (1775, 206, 1917, 222)


        self.locations = {}
        with open('locations.csv', newline='') as csvfile:
            reader = dict(csv.reader(csvfile, delimiter='#'))
            for name,coords in reader.items():
                # self.locations[name] = ast.literal_eval(str(coords))
                self.locations[name] = eval(coords)
        


    def window_focus(self):
        if 'Minecraft 1' in win32gui.GetWindowText(win32gui.GetForegroundWindow()):
            return True
        else:
            return False



#1739, 205, 1918, 222

    def xyz(self):
        try:
            start_time = time.time()
            # ocr_img = ImageGrab.grab(bbox=(46, 206, 400, 222)) # SINGLE PLAYER
            # ocr_img = ImageGrab.grab(bbox=(46, 188, 400, 204)) # MULTIPLAYER
            ocr_img = ImageGrab.grab(bbox=self.xyz_box) # MULTIPLAYER
            # ocr_img.save('xyz.png')
            width, height = ocr_img.size
            char_box = {}

            for x in range(0, width):
                temp = []
                for y in range(0, height):
                    rgb = ocr_img.getpixel((x, y))
                    if rgb == (221,221,221):
                        temp.append(y)

                if len(temp) > 0:
                    sum_y = sum(temp)
                    char_box[x] = [sum_y]

            keys = list(char_box.keys())

            data2 = {       
                570 : '0',
                440 : '1',
                528 : '2',
                420 : '3',
                434 : '4',
                454 : '5',
                498 : '6',
                248 : '7',
                510 : '8',
                402 : '9',
                150 : '-',
                210 : '/',
                54 : '.',
            }

            consecutive = consecutive_groups(keys)
            chars = []
            for i in consecutive:
                temp = 0
                for j in list(i):
                    temp += int(char_box[j][0])
                if temp in data2.keys():
                    chars.append(data2[temp])
                else:
                    pass
            if len(chars) != 0:
                chars = ''.join(chars)
                chars = chars.split('/')
                chars = [int(float(i)*10) for i in chars]
                self.current_x = chars[0]
                self.current_y = chars[1]
                self.current_z = chars[2]
                print('--- %s seconds ---' % (time.time() - start_time))
                return [self.current_x, self.current_y, self.current_z]
            return [0,0,0]
        except:
            return [0,0,0]



    def xyz2(self):
        # with Image.open('xyz-22.png') as ocr_img:
        try:

            # with mss.mss() as sct:
            #     monitor = {"top": self.xyz_box[0], "left": self.xyz_box[1], "width": self.xyz_box[2], "height": self.xyz_box[3]}
            #     ocr_img1 = np.array(sct.grab(monitor))

            ocr_img = ImageGrab.grab(bbox=self.xyz_box) # MULTIPLAYER USE THISSSSSSSSSSSSSSSSSS
            # ocr_img.save('xyz-227.png')

            ocr_img = np.array(ocr_img)
        # take the nth item in each sub array and turn it into its own array
            ocr_img = np.array([[ocr_img[i][j] for i in range(0,len(ocr_img),2)] for j in range(0,len(ocr_img[0]),2)]).tolist()


            # accociations = {
            #     3768: '1',
            #     5392: '2',
            #     5092: '3',
            #     6034: '4',
            #     5350: '5',
            #     4306: '6',
            #     4088: '7',
            #     5406: '8',
            #     5234: '9',
            #     6042: '0',
            #     2226: '/',
            #     86: '.'}

            accociations = {
                242: '1',
                342: '2',
                320: '3',
                378: '4',
                333: '5',
                274: '6',
                250: '7',
                340: '8',
                326: '9',
                6042: '0',
                140: '/',
                7: '.'}

            chars = []
            temp = []
            for i in ocr_img:
                # print(i)
                if [221,221,221] in i:
                    for j in i:
                        temp.append(j)

                else:
                    if len(temp) > 0:
                        total = 0
                        for indx,k in enumerate(temp):
                            if k == [221,221,221]:
                                total += indx

                        print(total)
                        try:
                            chars.append(accociations[total])
                        except:
                            pass
                        temp = []


                    else:
                        temp = []
                        pass
            
                
            if len(chars) > 0:
                chars = ''.join(chars)
                chars = chars.split('/')
                chars = [int(float(i)*10) for i in chars]
                self.current_x = chars[0]
                self.current_y = chars[1]
                self.current_z = chars[2]

                return [chars[0],chars[1],chars[2]]
        except:
            return [0,0,0]



    
    def xyz_f3c(self):
        # k.press('f3')
        # k.press('i')
        # k.release('f3')
        # k.release('i')
        k.send('f3+i')
        #hotkey f3 and c

        # read what is on the clipboard
        xyz = clip.paste()
        xyz = xyz.split(' ')
        if 'minecraft:player' in xyz:
            # print('plyer')
            mouse.click()


    
    def facing(self):
        try:
            # with Image.open('facing.png') as ocr_img:
            # ocr_img = ImageGrab.grab(bbox=(340, 260, 525, 276)) # SINGLE PLAYER
            # ocr_img = ImageGrab.grab(bbox=(337, 242, 525, 258)) # MULTIPLAYER
            ocr_img = ImageGrab.grab(bbox=self.facing_box) # MULTIPLAYER
            # ocr_img.save('facing.png')
            # exit()
            width, height = ocr_img.size
            char_box = {}

            for x in range(0, width):
                temp = []
                for y in range(0, height):
                    rgb = ocr_img.getpixel((x, y))
                    if rgb == (221,221,221):
                        temp.append(y)

                if len(temp) > 0:
                    sum_y = sum(temp)
                    char_box[x] = [sum_y]

            keys = list(char_box.keys())

            data2 = {       
                570 : '0',
                440 : '1',
                528 : '2',
                420 : '3',
                434 : '4',
                454 : '5',
                498 : '6',
                248 : '7',
                510 : '8',
                402 : '9',
                150 : '-',
                210 : '/',
                54 : '.',
            }

            consecutive = consecutive_groups(keys)
            chars = []
            for i in consecutive:

                temp = 0
                for j in list(i):
                    temp += int(char_box[j][0])
                
                if temp in data2.keys():
                    chars.append(data2[temp])
                else:
                    pass

            if len(chars) != 0:
                if chars.count('/') == 3:
                    chars = ''.join(chars[1:-1])
                    chars = chars.split('/')
                elif chars.count('/') == 4:
                    chars = ''.join(chars[2:-1])
                    chars = chars.split('/')
                
                x = int(float(chars[0]) * 10)
                y = int(float(chars[1]) * 10)

                # output = []
                # if float(chars[0]) < 0:
                #     output.append(round(360 + float(chars[0]), 1))
                # else:
                #     output.append(round(float(chars[0]), 1))
                # if float(chars[1]) < 0:
                #     output.append(round(180 - (90 + float(chars[1])), 1))
                # else:
                #     output.append(round(90 - float(chars[1]), 1))
                # output.append(round(float(chars[0]), 1))
                # output.append(round(float(chars[1]), 1))
    
                diff_x = x - self.difference_x
                if diff_x > 1800:
                    diff_x = diff_x - 3600
                elif diff_x < -1800:
                    diff_x = diff_x + 3600
                diff_y = y - self.difference_y
                self.difference_x = x
                self.difference_y = y
                self.facing_x += diff_x
                self.facing_y += diff_y
                # print(self.facing_x, self.facing_y)
                # self.facing_x += self.facing_x - output[0]
                # self.facing_y += self.facing_y - output[1]
                return [self.facing_x, self.facing_y]
            return [0,0]

        except:
            return [0,0]




    def targeted_block(self):
        try:
            # with Image.open('facing.png') as ocr_img:
            # ocr_img = ImageGrab.grab(bbox=(1739, 206, 1916, 222)) # SINGLE PLAYER
            # ocr_img = ImageGrab.grab(bbox=(1775, 206, 1917, 222)) # MULTIPLAYER
            ocr_img = ImageGrab.grab(bbox=self.targeted_block_box) # MULTIPLAYER
            ocr_img.save('targetedBlock.png')
            # exit()
            width, height = ocr_img.size
            char_box = {}

            for x in range(0, width):
                temp = []
                for y in range(0, height):
                    rgb = ocr_img.getpixel((x, y))
                    if rgb == (221,221,221):
                        temp.append(y)

                if len(temp) > 0:
                    sum_y = sum(temp)
                    char_box[x] = [sum_y]

            keys = list(char_box.keys())

            data2 = {       
                570 : '0',
                440 : '1',
                528 : '2',
                420 : '3',
                434 : '4',
                454 : '5',
                498 : '6',
                248 : '7',
                510 : '8',
                402 : '9',
                150 : '-',
                210 : '/',
                54 : '.',
                84 : ',',
                
            }

            consecutive = consecutive_groups(keys)
            chars = []
            for i in consecutive:

                temp = 0
                for j in list(i):
                    temp += int(char_box[j][0])
                
                if temp in data2.keys():
                    if data2[temp] != '/':
                        chars.append(data2[temp])
                else:
                    pass

            if len(chars) != 0:
                chars = ''.join(chars)
                chars = chars.split(',')
                chars = [int(i)*10 for i in chars]
                    
                self.targetedBlock_x = chars[0]
                self.targetedBlock_y = chars[1]
                self.targetedBlock_z = chars[2]

                return [self.targetedBlock_x, self.targetedBlock_y, self.targetedBlock_z]
            return [0,0,0]
        except:
            return [0,0,0]
        




    def see_lava(self):
        cap = ImageGrab.grab(bbox = (0, 30, 1919, 1010))
        frame = np.array(cap)
        before = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

        lower_range_lava = np.array([8, 210, 185])
        upper_range_lava = np.array([14, 252, 230])

        lava_mask = cv2.inRange(before, lower_range_lava, upper_range_lava)
        lava_pixels = cv2.countNonZero(lava_mask)

        if lava_pixels > 50:
            return True
        else:
            return False
    



    def go_to(self, pos=[0,0,0]):
        # self.turn(0)

        pulse_x = False
        pulse_z = False
        
        if pos == 'last_pos':
            starting_x = self.history[-1][0]
            starting_z = self.history[-1][2]
        elif type(pos) == list:
            starting_x = pos[0]
            starting_z = pos[2]


            k.release('w')
            k.release('a')
            k.release('s')
            k.release('d')
            k.release('shift')

            while True:
                time.sleep(0.01)
                # print(pulse_x, pulse_z)
                self.xyz()

                if -2<=(self.current_x-starting_x)<=2 and -2<=(self.current_z-starting_z)<=2 or self.window_focus() == False or k.is_pressed('esc'):
                    k.release('w')
                    k.release('a')
                    k.release('s')
                    k.release('d')
                    k.release('shift')
                    print('done')
                    # time.sleep(1)
                    break
                else:
                    # print((self.current_x-starting_x),(self.current_z-starting_z))
                    if -10<=(self.current_x-starting_x)<=10 and -10<=(self.current_z-starting_z)<=10:
                        pulse_x = True
                        pulse_z = True
                        # print('close')
                        # if k.is_pressed('w') or k.is_pressed('a') or k.is_pressed('s') or k.is_pressed('d'):
                        k.release('w')
                        k.release('a')
                        k.release('s')
                        k.release('d')
                        k.press('shift')
                    
                        # condition1 = (self.current_x-starting_x)<=-20 or 20<=(self.current_x-starting_x)
                        # condition2 = -20<=(self.current_z-starting_z)<= -3 or 3 <=(self.current_z-starting_z)<= 20

                    elif not(-20<=(self.current_x-starting_x)<=-2 or 2<=(self.current_x-starting_x)<=20) and not(-20<=(self.current_z-starting_z)<=-2 or 2<=(self.current_z-starting_z)<=20):
                        # print('shift UP')
                        pulse_x = False
                        pulse_z = False
                        k.release('shift')
                    
                    else:
                        if -1<=(self.current_x-starting_x)<=1:
                            # if k.is_pressed('shift'):
                            k.release('w')
                            k.release('a')
                            k.release('s')
                            k.release('d')
                            k.release('shift')
                            pulse_x = True
                            print('shift UP')

                        if -20<=(self.current_x-starting_x)<=-1 or 1<=(self.current_x-starting_x)<=20:
                            # if not k.is_pressed('shift'):
                            k.press('shift')
                            pulse_x = True
                            print('shift')

                        if -1<=(self.current_z-starting_z)<=1:
                            # if k.is_pressed('shift'):
                            k.release('w')
                            k.release('a')
                            k.release('s')
                            k.release('d')
                            k.release('shift')
                            pulse_z = True
                            print('shift UP')

                        if -20<=(self.current_z-starting_z)<=-2 or 2<=(self.current_z-starting_z)<=20:
                            # if not k.is_pressed('shift'):
                            k.press('shift')
                            pulse_z = True
                            print('shift')

                                


                    # if self.current_x + 16 < starting_x:
                    if self.current_x < starting_x and not(-2<(self.current_x-starting_x)<2):
                        # if k.is_pressed('d'):
                        k.release('d')

                        # if not k.is_pressed('a') and pulse_x == False:
                        if pulse_x == False:
                            # if not k.is_pressed('a'):
                            k.press('a')
                        # elif not k.is_pressed('a') and pulse_x == True:
                        elif pulse_x == True:
                            # if k.is_pressed('a'):
                            k.release('a')
                            k.press('a')
                            time.sleep(0.075)
                            k.release('a')
                        # elif not k.is_pressed('a') and pulse_x == True:
                        #     k.press('a')
                        #     time.sleep(0.075)
                        #     k.release('a')
                        # elif k.is_pressed('a') and pulse_x == True:
                        #     k.release('a')
                        #     k.press('a')
                        #     time.sleep(0.075)
                        #     k.release('a')
                        # print('left')

                    # elif self.current_x - 16 > starting_x:
                    elif self.current_x > starting_x and not(-2<(self.current_x-starting_x)<2):
                        # if k.is_pressed('a'):
                        k.release('a')

                        # if not k.is_pressed('d') and pulse_x == False:
                        if pulse_x == False:
                            # if not k.is_pressed('d'):
                            k.press('d')
                        # elif not k.is_pressed('d') and pulse_x == True:
                        elif pulse_x == True:
                            # if k.is_pressed('d'):
                            k.release('d')
                            k.press('d')
                            time.sleep(0.075)
                            k.release('d')
                        # elif not k.is_pressed('d') and pulse_x == True:
                        #     k.press('d')
                        #     time.sleep(0.075)
                        #     k.release('d')
                        # elif k.is_pressed('d') and pulse_x == True:
                        #     k.release('d')
                        #     k.press('d')
                        #     time.sleep(0.075)
                        #     k.release('d')
                        # print('right')

                    # if self.current_z - 16 < starting_z:
                    if self.current_z < starting_z and not(-2<(self.current_z-starting_z)<2):
                        # if k.is_pressed('s'):
                        k.release('s')

                        # if not k.is_pressed('w') and pulse_z == False:
                        if pulse_z == False:
                            # if not k.is_pressed('w'):
                            k.press('w')
                        # elif not k.is_pressed('w') and pulse_z == True:
                        elif pulse_z == True:
                            # if k.is_pressed('w'):
                            k.release('w')
                            k.press('w')
                            time.sleep(0.075)
                            k.release('w')
                        # elif not k.is_pressed('w') and pulse_z == True:
                        #     k.press('w')
                        #     time.sleep(0.075)
                        #     k.release('w')
                        # elif k.is_pressed('w') and pulse_z == True:
                        #     k.release('w')
                        #     k.press('w')
                        #     time.sleep(0.075)
                        #     k.release('w')
                        # print('forward')

                    # elif self.current_z + 16 > starting_z:
                    elif self.current_z > starting_z and not(-2<(self.current_z-starting_z)<2):
                        # if k.is_pressed('w'):
                        k.release('w')

                        # if not k.is_pressed('s') and pulse_z == False:
                        if pulse_z == False:
                            # if not k.is_pressed('s'):
                            k.press('s')
                        # elif not k.is_pressed('s') and pulse_z == True:
                        elif pulse_z == True:
                            # if k.is_pressed('s'):
                            k.release('s')
                            k.press('s')
                            time.sleep(0.075)
                            k.release('s')
                        # elif not k.is_pressed('s') and pulse_z == True:
                        #     k.press('s')
                        #     time.sleep(0.075)
                        #     k.release('s')
                        # elif k.is_pressed('s') and pulse_z == True:
                        #     k.release('s')
                        #     k.press('s')
                        #     time.sleep(0.075)
                        #     k.release('s')
                        # print('backward')



    def walk_to(self, pos=[0,0,0]):
        
        if pos == 'last_pos':
            starting_x = self.history[-1][0]
            starting_z = self.history[-1][2]
        elif type(pos) == list:
            starting_x = pos[0]
            starting_z = pos[2]

            self.face_coords(pos)

            k.release('w')
            k.release('s')
            k.release('shift')

            counter = 0
            while True:
                time.sleep(0.01)

                counter += 1
                if counter % 100 == 0:
                    self.face_coords(pos)


                self.xyz()
                self.targeted_block()

                print(self.targetedBlock_y, self.current_y)

                if self.targetedBlock_y >= self.current_y:
                    k.press('space')
                    time.sleep(0.075)
                    k.release('space')
                    self.face_coords(pos)

                if self.targetedBlock_y + 20 < self.current_y:
                    k.press('shift')
                    k.release('w')

                # if -1.5<=(self.current_x-starting_x)<=1.5 and -1.5<=(self.current_z-starting_z)<=1.5 or self.window_focus() == False or k.is_pressed('esc'):
                #     k.release('w')
                #     k.release('a')
                #     k.release('s')
                #     k.release('d')
                #     k.release('shift')
                #     print('done')
                #     # time.sleep(1)
                #     break
                # else:
                #     # print((self.current_x-starting_x),(self.current_z-starting_z))
                #     if -10<=(self.current_x-starting_x)<=10 and -10<=(self.current_z-starting_z)<=10:
                #         k.release('w')
                #         self.face_coords(pos)
                #         k.press('w')
                #         time.sleep(0.075)
                #         k.release('w')
                #         k.press('shift')
                #         time.sleep(0.025)

                #     else:
                #         k.release('shift')
                #         k.press('w')



    def snap_to_90(self):
        self.facing()

        remainder = (self.facing_x % 900)
        # print(remainder)
        if 0 <= remainder <= 450:
            snap_dir_x = self.facing_x - remainder
            # print('left')
        elif 450 < remainder <= 900:
            snap_dir_x = self.facing_x - remainder + 900
            # print('right')
        elif -900 <= remainder <= -450:
            snap_dir_x = self.facing_x - remainder + 450
            # print('left')
        elif -450 < remainder <= 0:
            snap_dir_x = self.facing_x - remainder
            # print('right')
        
        snap_dir_y = 900
        
        return snap_dir_x, snap_dir_y


    
    def turn(self, direction_x=0, direction_y=0, word_dir=None):
        self.facing()


        if direction_x == 0 and direction_y == 0 and word_dir != None:
            if word_dir.lower() == 'left':
                snap_dir_x = self.facing_x - 900
                snap_dir_y = self.facing_y
            elif word_dir.lower() == 'right':
                snap_dir_x = self.facing_x + 900
                snap_dir_y = self.facing_y
            elif word_dir.lower() == 'around':
                snap_dir_x = self.facing_x + 1800
                snap_dir_y = self.facing_y
        else:
            if type(direction_x) == str:
                if direction_x.lower() == 'keep':
                    snap_dir_x = self.facing_x
                elif direction_x.lower() == 'snap':
                    snap_dir_x = self.snap_to_90()[0]
                elif direction_x.lower()[0] == '+':
                    snap_dir_x = self.facing_x + int(direction_x[1:])
                elif direction_x.lower()[0] == '-':
                    snap_dir_x = self.facing_x - int(direction_x[1:])
            
            if type(direction_y) == str:
                if direction_y.lower() == 'keep':
                    snap_dir_y = self.facing_y
                elif direction_y.lower() == 'snap':
                    snap_dir_y = self.snap_to_90()[1]
                elif direction_y.lower()[0] == '+':
                    snap_dir_y = self.facing_y + int(direction_y[1:])
                elif direction_y.lower()[0] == '-':
                    snap_dir_y = self.facing_y - int(direction_y[1:])
            
            if type(direction_x) == int:
                snap_dir_x = direction_x
            if type(direction_y) == int:
                snap_dir_y = direction_y

        # print(direction_x, direction_y)
 
        # flop = 5
        while True:
            time.sleep(.01)
            self.facing()

            if self.window_focus() == False or k.is_pressed('esc'):
                break


            # print((self.facing_x, snap_dir_x), (self.facing_y, snap_dir_y))

            gap_x = (snap_dir_x - self.facing_x)
            gap_y = (snap_dir_y - self.facing_y)


            if (gap_x==0) and (gap_y==0):
                break

            # gap_x = math.floor(gap_x/5) if -1<gap_x<0 else math.ceil(gap_x/5) if 0<gap_x<1 else gap_x
            # gap_y = math.floor(gap_y/5) if gap_y>0 else math.ceil(gap_y/5) if gap_y<0 else gap_y
            # print(snap_dir_x, snap_dir_y, self.facing_x, self.facing_y,'|', gap_x, gap_y)

            # gap_x = gap_x if gap_x<1 else math.ceil(gap_x/5)
            # gap_y = math.floor(gap_y/5) if gap_y<1 else math.ceil(gap_y/5)
            


            # gap_x = math.floor(gap_x) if gap_x<0 else math.ceil(gap_x) if gap_x>0 else 0
            # gap_y = math.floor(gap_y) if gap_y<0 else math.ceil(gap_y) if gap_y>0 else 0


            # gap_x = 1 if 0<gap_x<1 else -1 if -1<gap_x<0 else int(gap_x)
            # gap_y = 1 if 0<gap_y<1 else -1 if -1<gap_y<0 else int(gap_y)


            mouse.move(gap_x, gap_y, absolute=False)
            # flop = 1

            
    

    def face_coords(self, end_coords):
        self.xyz()
        self.facing()

        x_diff = end_coords[0] - self.current_x
        z_diff = end_coords[2] - self.current_z

        if x_diff == 0:
            if z_diff > 0:
                angle = 90
            else:
                angle = -90
        elif z_diff == 0:
            if x_diff > 0:
                angle = 0
            else:
                angle = 180
        
        elif abs(x_diff) == abs(z_diff):
            if x_diff > 0 and z_diff > 0:
                angle = 45
            elif x_diff > 0 and z_diff < 0:
                angle = -45
            elif x_diff < 0 and z_diff < 0:
                angle = -135
            elif x_diff < 0 and z_diff > 0:
                angle = 135


        else:
            angle = math.degrees(math.atan(z_diff/x_diff))
            if x_diff > 0 and z_diff > 0:
                angle += 0
            elif x_diff < 0 and z_diff > 0:
                angle += 180
            elif x_diff < 0 and z_diff < 0:
                angle -= 180
            elif x_diff > 0 and z_diff < 0:
                angle += 0

        angle = int(round((angle*10), 0))

        # if angle<0:
        #     angle = str(angle)
        # else:
        #     angle = '+' + str(angle)

        self.turn(direction_x=-900+angle, direction_y=275)
        # self.turn(direction_x=angle, direction_y='keep')
        # time.sleep(0.25)

        return -900+angle

    
    def fishing(self):
        try:
            line = f.pixel(1432, 593) != (0, 0, 0)
            casted_rgb = f.pixel(1440, 1020)
            casted = sum(casted_rgb) >= 760

            return line, casted


            # j = f.pixel(1432, 594)# != (0, 0, 0)
            # k = f.pixel(1432, 595)# != (0, 0, 0)
            # l = f.pixel(1432, 596)# != (0, 0, 0)
            # a = f.pixel(1432, 597)# != (0, 0, 0)

            # print(h, j, k, l, a)

            # if h or j or k or l or a:
            # if line and casted:
            #     return True
            # else:
            #     return False

        except:
            return False, False
    

    # def jump(self):
    #     # self.facing()
    #     # self.snap_to_90()
    #     self.targeted_block()
    #     self.xyz()
    #     if self.targetedBlock_y == self.current_y:
    #         k.press('spa
    # time.sleep(0.075)
    # k.release('a')ce')

    
    # def falling(self):
    #     a = self.xyz()[1]
    #     t1 = time.time()
    #     b = self.xyz()[1]
    #     t2 = time.time()
    #     speed = int((a-b)/(t2-t1)) if a != [0,0,0] and b != [0,0,0] else 0

    #     if speed >= 22:
    #         #mouse.move(0, 1000, absolute=False)
    #         k.release('ctrl') if k.is_pressed('ctrl') else None
    #         k.press('esc
    # time.sleep(0.075)
    # k.release('a')')
    #         mouse.move(0, -15, absolute=False)
    #         mouse.click()
    #         return True
        

        




    # def log_pos(self):
    #     self.history.append(self.xyz())

    def get_locations(self):
        return self.locations
    
    # def get_history(self):
    #     return self.history
