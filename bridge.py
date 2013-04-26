__author__ = 'apolikamixitos'
import libs.serial as serial
import wsplugins.configuration as config
import time, wsplugins.configuration as settings

import imp
from wsplugins.facebook.plugin import FacebookWS



for plugin_name in config.ENABLED_PLUGINS:
    plugin = __import__(plugin_name, fromlist=[''])
    print plugin_name
    print plugin
    PINS = plugin.GETPINS()
    for pin in PINS:

        #ser = serial.Serial(config.DEVICE, config.RATE)
        #ser.write("FREQ:3\n")
        print pin,PINS[pin]

# while True:
#
#
#
#     time.sleep(settings.SLEEP_TIME)