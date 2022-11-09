import os
import time
import urllib.request
import threading
from fileinput import filename
import ffmpy

def compressfile(fname):
    input_name = fname
    crf = 24 #crf can range from 18 to 24 with 24 being the greatest level of compression
    output_name = "output.mp4"
    inp={input_name:None}
    outp = {output_name:'-vcodec libx264 -crf %d'%crf}
    ff=ffmpy.FFmpeg(executable='C:\\FFmpeg\\bin\\ffmpeg.exe', inputs=inp,outputs=outp)
    print(ff.cmd) # just to verify that it produces the correct ffmpeg command
    ff.run()
    print('done!')

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host, None, 20) #Python 3.x
        print("Connected to the internet !")
        return True
    except:
        print("Not connected to the internet :(")
        return False

def configure_wifi(ssid, password):
    config_lines = [
        'ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev',
        'update_config=1',
        'country=US',
        '\n',
        'network={',
        '\tssid="{}"'.format(ssid),
        '\tpsk="{}"'.format(password),
        '}'
        ]
    config = '\n'.join(config_lines)
    
    #give access and writing. may have to do this manually beforehand
    os.popen("sudo chmod a+w /etc/wpa_supplicant/wpa_supplicant.conf")
    
    #writing to file
    with open("/etc/wpa_supplicant/wpa_supplicant.conf", "w") as wifi:
        wifi.write(config)
    
    print("Wifi config added. Refreshing configs")
    ## refresh configs
    os.popen("sudo wpa_cli -i wlan0 reconfigure")




if __name__ == "__main__":
    # Server_name is a case insensitive string, and/or regex pattern which demonstrates
    # the name of targeted WIFI device or a unique part of it.
    ssid = "vunganai"
    password = "12345687"

    ssid1 = "UNIT218THEPARAGONFTTA"
    password1 = "caehqbg8@3@"

    ssid2 = "Bhudh_ooouuuu"
    password2 = "Dzaddy123"

    ssid3 = "Bhudhaldinhos iPhone"
    password3 = "bhudhu99"

    #print(ssid)
    #configure_wifi(ssid2, password2)
    
    #print("Establishing connection to wifi network")
    #time.sleep(15)
    #print("Checking internet connection...")
    #connected = connect()
    
    connected = False
    while not connected:
        print("Probing for network...")
        configure_wifi(ssid1,password1)
        print("Establishing connection to wifi network...")
        time.sleep(15)
        print("Checking internet connection...")
        connected = connect()
    
    #print("Turning off wifi after 7 seconds")
    #time.sleep(7)
    #cmd = 'ifconfig wlan0 down'
    #os.system(cmd)
    
    #print("Turning on wifi on after 5 seconds")
    #time.sleep(5)
    #cmd = 'ifconfig wlan0 up'
    #print("Doneeeeee")

