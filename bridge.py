__author__ = 'apolikamixitos'

import time, thread
import libs.serial as serial
import configuration as config
from libs.utilities.serial_utilities import list_serial_ports


print list_serial_ports()
class Bridge:

    #Serial variable instance
    serial_ins=None

    def Init(self):
        print 'Openning the serial port ...'
        self.serial_ins = serial.Serial(config.DEVICE,config.RATE,timeout=None)
        print 'Waiting for initialization ...'
        time.sleep(1)

        print 'Loading plugins ...'

        #This file is responsible of the execution
        for plugin_name in config.ENABLED_PLUGINS:
            plugin = __import__(plugin_name[1]+'.plugin', fromlist=[''])
            configuration = __import__(plugin_name[1]+'.configuration', fromlist=[''])
            name = plugin_name[0]
            try:
                print 'Initializing '+name+'\'s plugin thread ...'
                thread.start_new_thread( self.Watch, (plugin,name,configuration.SLEEP_TIME,) )
            except:
                print "Error: unable to start thread"


    def Watch(self,plugin,name,sleeptime):
        while 1:
            print name+' plugin pins checking ...'
            PINS = plugin.WS.GETPINS()
            for pin in PINS:
                self.serial_ins.write("FREQ:"+str(PINS[pin])+"\n")
                #ser = serial.Serial(config.DEVICE, config.RATE)
                #self.serial_ins.write("FREQ:3\n")
                print pin,PINS[pin]
            print name+' plugin updated.'
            time.sleep(sleeptime)


if __name__ == "__main__":
    bridge = Bridge()
    bridge.Init()
    while 1:
        pass
