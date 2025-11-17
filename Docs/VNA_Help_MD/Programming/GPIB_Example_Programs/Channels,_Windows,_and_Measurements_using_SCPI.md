# Channels, Windows, and Measurements using SCPI

* * *

This Python program does the following:

  * Presets the analyzer, deleting the default trace

  * Create 2 windows

  * Create 2 Measurements

  * Feed the measurements to windows / traces

  * Change frequency ranges for channels

  * Select both measurements

  * Turn marker 1 ON for each measurement

The following notes explain the basic structure of the SCPI tree on the
analyzer:

  * SOURce: and most SENSe: commands act on the channel that is specified in the command. Channel 1 is default if not specified.

  * Most DISPlay: commands act on the window and trace specified in the command. Window1 and Trace1 are default if not specified.

  * CALCulate: commands act on the selected measurement in the specified channel. Select the measurement for each channel using  
[CALCulate<channel number>:PARameter:SELect <meas name>](../GP-
IB_Command_Finder/Calculate/Parameter.htm#cps). You can select one measurement
in each channel.

#### See Also:

[Python Basics](../Learning_about_GPIB/Python_Basics.md)

[Traces, Channels, and Windows on the
Analyzer](../../S0_Start/Traces_Channels_and_Windows.htm)

[SCPI Example Programs](SCPI_Example_Programs.md)

import pyvisa as visa  
  
_# Change this variable to the address of your instrument_  
VISA_ADDRESS = 'TCPIP0::localhost::inst0::INSTR'  
  
_# Create a connection (session) to the instrument_  
resourceManager = visa.ResourceManager()  
session = resourceManager.open_resource(VISA_ADDRESS)  
  
_# Command to preset the instrument and deletes the default trace,
measurement, and window_  
session.write("SYST:FPR")  
  
_# Create measurements in two different channels_  
session.write("CALC1:MEAS1:DEF 'S11'")  
session.write("CALC2:MEAS2:DEF 'S21'")  
  
_# Turn on 2 windows_  
session.write("DISP:WIND1:STAT ON")  
session.write("DISP:WIND2:STAT ON")  
  
_# Displays measurement 1 in window 1, measurement 2 in window 2_  
_# The FEED command assigns the next available trace number to the
measurement_  
session.write("DISP:MEAS1:FEED 1")  
session.write("DISP:MEAS2:FEED 2")  
  
_# Change each channel 's frequency span_  
session.write("SENS1:FREQ:SPAN 1e9")  
session.write("SENS2:FREQ:SPAN 2e9")  
  
_# Turn marker 1 ON for measurement 1 and measurement 2_  
session.write("CALC1:MEAS1:MARK1:STAT ON")  
session.write("CALC2:MEAS2:MARK1:STAT ON")  
  
_# Select second measurement as active measurement_  
session.write("CALC2:PAR:MNUM 2")  
---

