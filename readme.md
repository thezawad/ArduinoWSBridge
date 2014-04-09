# ArduinoWSBridge #

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/apolikamixitos/arduinowsbridge/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

**ArduinoWSBridge** (Arduino WebServices Bridge) is a multiplatform app based on Python with which you can easily use the information provided by the API services on the web and that you can easily integrate their with your arduino boards.

## Principle ##

The principle of the application is simple, if you want to use a service, you have to create the plugin that communicates it.

In this version of ArduinoWSBridge, only simple Digits are supported (Number of X : unread notifications, unread messages etc ...)

## Installation ##

ArduinoWSBridge

You can download the latest stable version as an archive directly from the download section or you can clone directly from repository the dev version.

    git clone https://github.com/apolikamixitos/arduinowsbridge


## Plugins ##

You can copy directly the plugin you downloaded to `wsplugins` folder.

`SLEEP_TIME`: seconds to wait before rechecking again.

## Configuration : ##

### Software client : ###

**Plugins**

You can edit the default values of a specific plugin directly in `wsplugins/PLUGIN_NAME/configuration.py`.

Each plugin has some specifics methods that return ONLY integer values, those values are sent to the board later.

If you want to create a plugin, you can refer to this [documentation](http://DOCUMENTATIONLINK).

**Bridge**

In the bridge configuration file you can specify the different configurations that are going to be used with the app.

'`COMx`' for windows or '`/dev/ttyACMx`' for Unix ('x' depends on the affected number by the OS of a free port, not always fixed)

	DEVICE='COM7'   
	RATE = 9600

Those are the enabled plugins that are going to be used:

	#We can specify the enabled plugins that are going to be used with AWSB

	ENABLED_PLUGINS={
	    ('Facebook','wsplugins.facebook','FB_CMD'),
	    #('Youtube','wsplugins.youtube','YT_CMD'),
	}

*Ex:* **Facebook plugin** :

`'Facebook'`: 
> Alias for the plugin that we are going to use to specify the methods in `ENABLED_PINS`.

`'wsplugins.facebook'`: 
> The name of the Python module (it starts with `'wsplugins'`).

`'FB_CMD'`: 
> Command to be sent to the Arduino board. It has 2 arguments the ***PIN number*** defined AND the ***Value*** returned from the method

----

For each declared PIN, we specify a method defined in a specific plugin using its alias, and that returns the value to be sent to the Arduino board:

	#ArduinoUNO Model
	ENABLED_PINS = {
	    'PIN_1':'Facebook.inbox',
	    'PIN_2':'Facebook.notifications',
	    #'PIN_3':'Youtube.views',
	    'PIN_4':None,
		...
	    'PIN_14':None,
	}

### Arduino board : ###

To use the Arduino with the app, you have just to include `SerialCommand` library, which it was forked from this [original project](https://github.com/kroimon/Arduino-SerialCommand).

You can checkout this Arduino [sketch example](https://github.com/apolikamixitos/ArduinoWSBridge/tree/arduino_sketch/arduino_sketch/example) to have a clear view.


#### Some explanations for the sketch example file : ####

In general you have to specify the **SAME** command that you specified in the Arduino configuration file.

`SCmd.addCommand("FB_CMD",Facebook_Cmd);`

`Facebook_Cmd`: the callback function to be executed when the board receives a '`FB_CMD`' command.

	void Facebook_Cmd(){
		//Place your instructions here
		/*
		You turn on the light when you receive a notification
		or even start a party when "someone" adds you on Facebook
		*/
	}

## Usage : ##

The usage of the application is pretty easy, especially for people who haven't experienced some advanced web programming skills.

After the installation and the configuration, you can now run directly the file run.sh for Linux users and run.bat for Windows users.

## Contributions ##

If you are a software developer, an Arduino enthusiastic or even just passing by, please make sure to push this project more, with the power of Arduino, we can now do ANYTHING !

## TODO: ##

- Create documentation for plugin creation
- Create an example plugin for Youtube
- Create a PIP install package