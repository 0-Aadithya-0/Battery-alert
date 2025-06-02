import time
import psutil as psu
import pygame

pygame.mixer.pre_init(devicename='Speaker (Realtek(R) Audio)')
pygame.mixer.init()


def alert():
    while 1:
        time.sleep(8)
        battery_charged = psu.sensors_battery().percent
        try:
            while psu.sensors_battery().power_plugged and battery_charged >= 90:
                pygame.mixer.music.load('alert.mp3')
                pygame.mixer.music.set_volume(1.0)
                pygame.mixer.music.play()
                time.sleep(4)
            while not psu.sensors_battery().power_plugged and battery_charged <= 20:
                pygame.mixer.music.load('alert.mp3')
                pygame.mixer.music.set_volume(1.0)
                pygame.mixer.music.play()
                time.sleep(2)
            else:
                pygame.mixer.music.stop()
        except Exception as e:
            print(e)


alert()
