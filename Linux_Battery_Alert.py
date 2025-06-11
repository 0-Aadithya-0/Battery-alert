import time
import psutil as psu
import pulsectl
from playsound import playsound
import  pyvolume


def alert():
    while 1:

            time.sleep(8)
            battery_charged = psu.sensors_battery( ).percent
            print("Precentage check")
            try:
                while (psu.sensors_battery( ).power_plugged and battery_charged >= 90):
                    with pulsectl.Pulse('Pulse_speaker_finder') as pulse:
                        sinks = pulse.sink_list( )
                        ports = sinks[0].port_list
                        if not pulse.sink_default_get() == sinks[0]:
                            pulse.default_set(sinks[0])
                            print(f"sink selected:{ports[0].name}")
                            pulse.sink_port_set(sinks[0].index, "[Out] Speaker")
                            print("speaker selected")
                    pyvolume.increase()
                    playsound('/home/aadithya/Development/Software/battery_alert/alert.mp3')
                    time.sleep(3)


                while not psu.sensors_battery( ).power_plugged and battery_charged <= 20:
                    with pulsectl.Pulse('Pulse_speaker_finder') as pulse:
                        sinks = pulse.sink_list( )
                        ports = sinks[0].port_list
                        if not pulse.sink_default_get() == sinks[0]:
                            pulse.default_set(sinks[0])
                            print(f"sink selected:{ports[0].name}")
                            pulse.sink_port_set(sinks[0].index, "[Out] Speaker")
                            print("speaker selected")
                    pyvolume.increase( )
                    playsound('/home/aadithya/Development/Software/battery_alert/alert.mp3')
                    time.sleep(1)

            except Exception as e:
                print(e)


alert( )
