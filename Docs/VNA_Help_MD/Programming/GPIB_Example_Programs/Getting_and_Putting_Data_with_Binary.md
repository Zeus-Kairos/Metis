# Getting and Putting Data with Binary

This Python Program does the following:

  * Getting the data and store as Binary format.

  * Putting back the data.

### See Also

[Python Basics](../Learning_about_GPIB/Python_Basics.md)

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
  
_# ======================== Getting data ========================_  
  
_# Select the measurement_  
session.write("CALC1:MEAS1:DEF 'S21'")  
_# Take a sweep_  
session.write("SENS1:SWE:MODE SING")  
session.query("*OPC?")  
_# Data format suited for large amounts of measurement data (dB)_  
session.write("FORM:DATA REAL,32")  
_# Tells the instrument to use the native endian type when sending binary
data_  
session.write("FORM:BORD SWAP")  
  
_# Ask for the data from the sweep, pick one of the locations to read_  
myMeas = session.query_binary_values('CALC1:MEAS1:DATA:FDATA?', datatype='f')
_# Formatted Meas_ _# myMeas = session.query_binary_values(
"CALC:MEAS1:DATA:SDATA?", datatype='f') # Corrected, Complex Meas_  
_# session.write("CALC:MEAS:MATH:MEM") # Stores a trace into memory, required
if querying with FMEM or SMEM_  
_# myMeas = session.query_binary_values( "CALC:MEAS1:DATA:FMEM?",
datatype='f') # Formatted Memory_  
_# myMeas = session.query_binary_values( "CALC:MEAS1:DATA:SMEM?",
datatype='f') # Corrected, Complex Memory_  
_# myMeas = session.query_binary_values("SENS1:CORR:CSET:ETER:DATA?
'Directivity(1,1)'", datatype='f') # Error-Term Directivity_  
  
print(myMeas)  
  
_# Data format suited for accurate transfer of frequency data (Frequency)_  
session.write("FORM:DATA REAL,64")  
myFreq = session.query_binary_values('CALC1:MEAS1:X?', datatype='d')  
  
_# ======================== Putting data ========================_  
  
_# Preset the instrument and deletes existing traces, measurements, and
windows_  
_# Creates a S11 measurement named "CH1_S11_1"_  
session.write("SYST:PRES")  
  
_# Must set data format and swap again after system preset_  
_# Data format suited for large amounts of measurement data (dB)_  
session.write("FORM:DATA REAL,32")  
_# Tells the instrument to use the native endian type when sending binary
data_ session.write("FORM:BORD SWAP")  
session.write_binary_values("CALC1:MEAS1:DATA:FDATA ",myMeas)  _# Formatted
Meas_  
_# session.write_binary_values( "CALC:MEAS1:DATA:FMEM ",myMeas) # Formatted
Memory_  
_# session.write_binary_values( "CALC:MEAS1:DATA:SDATA ",myMeas) # Corrected,
Complex Meas_  
_# session.write_binary_values( "CALC:MEAS1:DATA:SMEM ",myMeas) # Corrected,
Complex Memory_  
_# session.write_binary_values( "SENS1:CORR:CSET:ETER:DATA
'Directivity(1,1)',", myMeas) # Error-Term Directivity'_  
  
---

