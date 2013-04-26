__author__ = 'apolikamixitos'


import libs.serial as serial
import wsplugins.configuration as config

ser = serial.Serial(config.DEVICE, config.RATE)
ser.write("FREQ:3\n")