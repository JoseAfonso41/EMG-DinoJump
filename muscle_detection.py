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

#def ler(nome_ficheiro):
    #f = open(nome_ficheiro, 'r')
    #capturas = []
    #for line in f:
        #columns = line.split()
        #timestamp = float(columns[0])
        #emg = float(columns[1])
        #print(timestamp)
        #capturas.append([timestamp, emg])
    #return capturas

#def emg_plot(data):
    # criar listas para armazenar os primeiros e segundos elementos
    #x = []
    #y = []

    #t_zero = data[0][0]
    #for array in data:
       #print(array[0]-t_zero, array[1])
       #x.append(array[0]-t_zero)
       #y.append(array[1])

    #plt.plot(x,y)
    #plt.xlabel('Tempo')
    #plt.ylabel('Sinal EMG')
    #plt.show()

#wue = ler('dados1.txt')
#emg_plot(wue)

#######################


def contraction_detection(max_rms):
    # #Resolve an available OpenSignals stream
    print("# Looking for an available OpenSignals stream...")
    os_stream = resolve_stream("name", "OpenSignals")
    # # Create an inlet to receive signal samples from the stream
    inlet = StreamInlet(os_stream[0])
    sample_array = np.full(300, 0)

    jump = False

    while True:
    #  # Receive samples
        sample, timestamp = inlet.pull_sample()
        #retificar amostra
        emg_rectified = abs(sample[1])
        #remover uma amostra antiga e inserir uma nova
        sample_array[:-1] = sample_array[1:]
        sample_array[-1] = emg_rectified
        #calcular rms do sample array
        rms = np.sqrt(np.mean(sample_array**2))

        if rms > 0.4 * float(max_rms) and not jump:
            jump = True
            keyboard.press('space')
            print("Jumping")

        elif jump and rms < 0.2 * float(max_rms):
            print("UnJumping")
            #pygame.event.post(pygame.event.Event(USEREVENT + 2))
            keyboard.release('space')
            jump = False

















