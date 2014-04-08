__author__ = 'apolikamixitos'

import wsplugins.facebook.configuration as FB

#DEVICE = '/dev/ttyACM0' #For UNIX
DEVICE='COM7' #Windows
RATE = 9600

#Tuples where we define the name, the module path and the arduino command
ENABLED_PLUGINS={
    ('Facebook','wsplugins.facebook','FB_CMD'),
    #('Twitter','wsplugins.twitter'),
}

#ArduinoUNO Model
ENABLED_PINS = {
    'PIN_1':'Facebook.inbox',
    'PIN_2':'Facebook.notifications',
    #'PIN_3':'Twitter.notifications',
    'PIN_4':None,
    'PIN_5':None,
    'PIN_6':None,
    'PIN_7':None,
    'PIN_8':None,
    'PIN_9':None,
    'PIN_10':None,
    'PIN_11':None,
    'PIN_12':None,
    'PIN_13':None,
    'PIN_14':None,
}