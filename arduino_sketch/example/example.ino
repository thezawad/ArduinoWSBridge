#include <SoftwareSerial.h>   // We need this even if we're not using a SoftwareSerial object
                              // Due to the way the Arduino IDE compiles
#include "SerialCommand.h"

SerialCommand SCmd;   // The demo SerialCommand object

void setup(){  
  
  Serial.begin(9600); 
  // Setup callbacks for SerialCommand commands 
  SCmd.addCommand("FB_CMD",Facebook_Cmd);       // Send back the data
  
}

void loop(){  
  SCmd.readSerial();     // We don't do much, just process serial commands
}

void Facebook_Cmd(){
  char * arg;
  int PIN_Nbr, Value;
  
  PIN_Nbr=-1;
  Value=-1;
  
  arg = SCmd.next();
  if(arg != NULL)
    PIN_Nbr = atoi(arg);
  
  arg = SCmd.next();
  if(arg != NULL)
    Value = atoi(arg);  
    
  Serial.print("Facebook CMD: ");
  
  //PIN Number  
  Serial.print("PinNbr: ");
  Serial.print(PIN_Nbr); 
 
  //Value
  Serial.print("Value: ");
  Serial.println(Value);  
 
}
