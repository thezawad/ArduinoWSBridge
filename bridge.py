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
            arduino_cmd = plugin_name[2]
            try:
                print_output(name,'Initializing plugin thread ...')
                thread.start_new_thread( self.Watch, (plugin,name,configuration.SLEEP_TIME,arduino_cmd,) )
            except:
                print "Error: unable to start thread"


    def Watch(self,plugin,name,sleeptime,arduino_cmd):
        while 1:
            print_output(name,'Updating the values ...')

            ws = plugin.WS.update_values()

            for pin in config.ENABLED_PINS:
                if config.ENABLED_PINS[pin] is not None:
                    #Check if the current PIN is related with the plugin
                    info = config.ENABLED_PINS[pin].split('.')

                    #Get the first part ex: 'Facebook.inbox' => first part : 'Facebook'
                    part_name = info[0]
                    method = info[1]

                    #Call the method from the instance
                    if part_name == name:
                        value = getattr(ws, method)()
                        pin_number = pin.replace('PIN_','')
                        #print 'Pin '+str(pin_number)+' Val: '+str(value)

                        #Send the value and the command to the pin
                        self.serial_ins.write(arduino_cmd+" "+str(pin_number)+" "+str(value)+"\n")
                        print_output(name,'Response : '+self.serial_ins.readline()[:-1])

            print_output(name,'Values updated.')
            time.sleep(sleeptime)

def print_output(name,message):
    print '['+name+']: '+message

if __name__ == "__main__":
    bridge = Bridge()
    bridge.Init()
    while 1:
        pass
