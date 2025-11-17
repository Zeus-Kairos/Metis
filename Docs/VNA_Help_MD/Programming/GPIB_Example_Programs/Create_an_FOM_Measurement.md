# Create a FOM Measurement

* * *

All Python examples in this topic create a FOM measurement with the following
attributes:

  * Sweep the Source (input) from 1 GHz to 2 GHz

  * Sweep the Receivers (output) from 2 GHz to 3 GHz

  * You provide an LO at 1 GHz

### See Also

[Python Basics](../Learning_about_GPIB/Python_Basics.md)

[Learn more about Frequency Offset
Mode](../../FreqOffset/Frequency_Offset_Mode.htm)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

The following Python example will run on any VNA model with FOM (opt S93080A).
However, these commands have no provisions for internal second source. It uses
[Sens:Offset commands](../GP-IB_Command_Finder/Sense/Offset_SCPI.md).

import pyvisa as visa  
  
_# Change this variable to the address of your instrument_  
VISA_ADDRESS = 'TCPIP0::localhost::inst0::INSTR'  
  
_# Create a connection (session) to the instrument_  
resourceManager = visa.ResourceManager()  
session = resourceManager.open_resource(VISA_ADDRESS)  
  
_# Command to preset the instrument and deletes the default trace,
measurement, and window_  
session.write("SYST:FPR")  
  
_# Create and turn on window 1_  
session.write("DISP:WIND1:STAT ON")  
  
_# Create a measurement with parameter_  
session.write("CALC1:MEAS1:DEF 'S21'")  
  
_# Displays measurement 1 in window 1 and assigns the next available trace
number to the measurement_  
session.write("DISP:MEAS1:FEED 1")  
  
_# Set the start and stop frequencies_  
session.write("SENS1:FREQ:START 1e9")  
session.write("SENS1:FREQ:STOP 2e9")  
  
_# Set the receivers to be 2e9 - > 3e9_  
_# See SENS:FOM:RNUM? to find the range number for a specific name_  
session.write("SENS1:FOM:RANG3:FREQ:OFFS 1e9")  
  
_# Turns frequency offset on and enable the freq offset settings_
session.write("SENS1:FOM ON")  
  
---  
  
The following example can be run ONLY on a VNA with FOM (opt S93080A). It uses
the internal 2nd source for the fixed LO frequency.

import pyvisa as visa  
  
_# Change this variable to the address of your instrument_  
VISA_ADDRESS = 'TCPIP0::localhost::inst0::INSTR'  
  
_# Create a connection (session) to the instrument_  
resourceManager = visa.ResourceManager()  
session = resourceManager.open_resource(VISA_ADDRESS)  
  
_# Command to preset the instrument and deletes the default trace,
measurement, and window_  
session.write("SYST:FPR")  
  
_# Create and turn on window 1_  
session.write("DISP:WIND1:STAT ON")  
  
_# Create a measurement with parameter_  
session.write("CALC1:MEAS1:DEF 'S21'")  
  
_# Displays measurement 1 in window 1 and assigns the next available trace
number to the measurement_  
session.write("DISP:MEAS1:FEED 1")  
session.write("SENS1:FREQ:START 1e9")  
session.write("SENS1:FREQ:STOP 2e9")  
  
_# set the receivers to be 2e9 - > 3e9_  
session.write("SENS1:FOM:RANG3:FREQ:OFFS 1e9")  
  
_# setup the 2nd source frequencies_  
session.write("SENS1:FOM:RANG4:COUP 0")  
session.write("SENS1:FOM:RANG4:FREQ:START 1e9")  
session.write("SENS1:FOM:RANG4:FREQ:STOP 1e9")  
  
_# turn off coupling_  
session.write("SOUR1:POW:COUP 0")  
  
_# set LO power to 10dBm_  
session.write("SOUR1:POW3 10")  
  
_# turn ON port 3, our LO signal_  
session.write("SOUR1:POW3:MODE ON")  
session.write("SENS1:FOM:STAT ON")  
  
  
---  
  
* * *

