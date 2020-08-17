
import cv2
import os
#import pandas as pd
veh_count = [0]
current = os.getcwd()

import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile
import cv2
import numpy as np
import csv
import time
from packaging import version
import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile
import pathlib
import sys
def save_img(source_image):
    cv2.imwrite('/content/detected_vehicles/v'
                + str(len(veh_count)) + '.png', source_image)
    veh_count.insert(0, 1)

def variable_reading(typ):
    result=0
    filename = typ + '.txt'
    if os.path.exists(filename):
        f = open(typ + ".txt", "r")
        for line in f:
            if line[-1:].isdigit() == True:
                result = int(line[-1:])
            else:
                result = 0

    return result


def variable_storing(typ,element):
    filename = typ + '.txt'

    if os.path.exists(filename):
        append_write = 'a'  # append if already exists
    else:
        append_write = 'w'  # make a new file if not

    highscore = open(filename, append_write)
    highscore.write(str(element)+ '\n')
    highscore.close()


veh_detected = [0]
#current_frame_list = [0]
#bottom_of_vehicle = [0]
def speed(top,bottom,right,left,curr_frame_no,crop_img,
    roi_position):
    bottom_of_vehicle=variable_reading('bottom')
    current_frame_list=variable_reading('frame')
    spd = 'n.a.'  # In the startiing speed
    drn = 'n.a.'  # direction
    scale_constant = 1  #
    in_ROI = True  # vehicle in Region Of Interest
    update_csv = False
    if bottom < 120:
        scale_constant = 1
    elif bottom > 120 and bottom < 4000:
        scale_constant = 2
    else:
        in_ROI = False
    result=[]
    if os.path.exists('bottom.txt'):
        f = open( "bottom.txt", "r")
        for line in f:
            if line[-1:].isdigit() == True:
                result.append(int(line[-2:]))
    if len(result) != 0 and bottom - bottom_of_vehicle < 0 and 0 < bottom_of_vehicle and bottom_of_vehicle < 120 and roi_position > bottom:
        veh_detected.insert(0, 1)
        update_csv = True
        save_img(crop_img)
        # for debugging
        # print("bottom_position_of_detected_vehicle[0]: " + str(bottom_position_of_detected_vehicle[0]))
        # print("bottom: " + str(bottom))
    if bottom > bottom_of_vehicle:
        drn = 'up'
    else:
        drn = 'down'

    if in_ROI:

         pixel_length = bottom - bottom_of_vehicle
         scale_real_length = pixel_length * 44  # multiplied by 44 to convert pixel length to real length in meters (chenge 44 to get length in meters for your case)

         total_time_passed = curr_frame_no - current_frame_list
         scale_real_time_passed = total_time_passed * 24 # get the elapsed total time for a vehicle to pass through ROI area (24 = fps)
         if scale_real_time_passed != 0:
            spd = scale_real_length / scale_real_time_passed / scale_constant  # performing manual scaling because we have not performed camera calibration
            #spd = spd / 6 * 40  # use reference constant to get vehicle speed prediction in kilometer unit
            variable_storing('frame',curr_frame_no)
            variable_storing('bottom', bottom)


    return (drn,spd, veh_detected, update_csv)
