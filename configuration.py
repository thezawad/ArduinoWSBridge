__author__ = 'apolikamixitos'

import wsplugins.facebook.configuration as FB

#DEVICE = '/dev/ttyACM0' #For UNIX
DEVICE='COM7' #Windows
RATE = 9600

ENABLED_PLUGINS={
    ('Facebook','wsplugins.facebook'),
    #('Twitter','wsplugins.twitter'),
}


ENABLED_PINS = {
    FB.PIN_FRIENDREQUESTS, #PIN 12
    FB.PIN_NOTIFICATIONS, #PIN 10
}