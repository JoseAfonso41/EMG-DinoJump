#Imports
from pylsl import StreamInlet, resolve_stream
import queue
import numpy as np
import time
import pygame
from pygame.locals import *
import os
import random
import keyboard


def calibration():
    count = 3

    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)  # Pausa de 1 segundo

    # #Resolve an available OpenSignals stream
    print("# Looking for an available OpenSignals stream...")
    os_stream = resolve_stream("name", "OpenSignals")
    # # Create an inlet to receive signal samples from the stream
    inlet = StreamInlet(os_stream[0])
    sample_array = np.full(300, 0)

    rectified_values = np.array([])

    start_time = time.time()

    print("Calibrating...")

    while (time.time() - start_time) < 5:
    #  # Receive samples
        sample, timestamp = inlet.pull_sample()
        #print(timestamp, sample)
        #retificar amostra
        emg_rectified = abs(sample[1])
        #remover uma amostra antiga e inserir uma nova
        ##sample_array[:-1] = sample_array[1:]
        ##sample_array[-1] = emg_rectified
        #calcular rms do sample array
        rectified_values = np.append(rectified_values, emg_rectified)
        if len(rectified_values) % 1000 == 0:
            print(len(rectified_values) / 1000)
    print(len(rectified_values))
    rms = np.sqrt(np.mean(sample_array**2))

    array_size = 300
    max_rms = float("-inf")
    max_rms_array = None

    for i in range(len(rectified_values) - array_size + 1):
        array = rectified_values[i:i + array_size]
        array_rms = np.sqrt(np.mean(array**2))
        array_rms_round = round(array_rms, 2)

        if array_rms_round > max_rms:
            max_rms = array_rms_round

    arquive = open("max_rms.txt", "w+")
    print(max_rms, file=arquive)
    arquive.close()
    print(max_rms)
    return max_rms


calibration()