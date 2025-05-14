import os, time, random, pygame, pyttsx3
from datetime import datetime
from pygame import mixer

def limpaTela():
    os.system("cls")

def aguardarTempo(segundos):
    time.sleep(segundos)

def randomizar(minimo, maximo):
    return random.randint(minimo, maximo)

def falar(fala):
    engine = pyttsx3.init()
    engine.say(fala)
    engine.runAndWait()

