# Getting and Putting Data with ASCII

This Python Program does the following:

  * Getting the data and store as an array in ASCII format.

  * Putting back the data.

### See Also

[Python Basics](../Learning_about_GPIB/Python_Basics.md)

import pyvisa as visa  
import numpy as np  
  
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
  
_# ======================== Getting data ========================_  
  
_# Select the measurement_  
session.write("CALC1:MEAS1:DEF 'S21'")  
_# Take a sweep_  
session.write("SENS1:SWE:MODE SING")  
_# Keep the controller and the VNA "synched"_  
session.query("*OPC?")  
_# Default Data Format is ASCII_ session.write("FORM:DATA ASCII,0")  
_  
# Ask for the data from the sweep, pick one of the locations to read_  
myMeas = session.query_ascii_values("CALC1:MEAS1:DATA:FDATA?",
container=np.array)   _# Formatted Meas_ _# myMeas =
session.query_ascii_values( "CALC:MEAS1:DATA:SDATA?", container=np.array) #
Corrected, Complex Meas_  
_# session.write( "CALC:MEAS:MATH:MEM") # Stores a trace into memory, required
if querying with FMEM or SMEM_  
_# myMeas = session.query_ascii_values( "CALC:MEAS1:DATA:FMEM?",
container=np.array) # Formatted Memory_  
_# myMeas = session.query_ascii_values( "CALC:MEAS1:DATA:SMEM?",
container=np.array) # Corrected, Complex Memory_  
_# myMeas = session.query_ascii_values( "SENS1:CORR:CSET:ETER:DATA?
'Directivity(1,1)'", container=np.array) # Error-Term Directivity_ _  
_ print(myMeas)  
_# Measurements are stored as an array, allowing quick and simple Python
commands_  
maxValue = np.max(myMeas) print(f"Max Value: {maxValue}") _  
# # ======================== Putting data ========================_ _  
# # Preset the instrument and deletes existing traces, measurements, and
windows  
# # Creates a S11 measurement named "CH1_S11_1"_  
session.write("SYST:PRES")  
  
_# Put data back in_  
session.write_ascii_values("CALC1:MEAS1:DATA:FDATA ",myMeas)   _# Formatted
Meas  
# session.write_ascii_values("CALC:MEAS1:DATA:FMEM ",myMeas) # Formatted
Memory_ _# session.write_ascii_values( "CALC:MEAS1:DATA:SDATA ",myMeas) #
Corrected, Complex Meas_  
_# session.write_ascii_values( "CALC:MEAS1:DATA:SMEM ",myMeas) # Corrected,
Complex Memory_  
_# session.write_ascii_values( "SENS1:CORR:CSET:ETER:DATA
'Directivity(1,1)',",myMeas) # Error-Term Directivity'_  
  
  
---

