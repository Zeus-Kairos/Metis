# Plotting S- Parameter Measurement

This Python program creates a new S21 measurement and plotting the S parameter
measurement.

### See Also

[Python Basics](../Learning_about_GPIB/Python_Basics.md)

import pyvisa as visa  
import matplotlib.pyplot as plt  
  
_# Change this variable to the address of your instrument_  
VISA_ADDRESS = 'TCPIP0::localhost::inst0::INSTR'*  
  
_# Create a connection (session) to the instrument_  
resourceManager = visa.ResourceManager()  
session = resourceManager.open_resource(VISA_ADDRESS)  
  
_# Command to preset the instrument and deletes the default trace,
measurement, and window_  
session.write("SYST:FPR")  
  
_# Create and turn on window 1_  
session.write("DISP:WIND1:STAT ON")  
  
_# Create a S21 measurement_  
session.write("CALC1:MEAS1:DEF 'S21'")  
  
_# Displays measurement 1 in window 1 and assigns the next available trace
number to the measurement_  
session.write("DISP:MEAS1:FEED 1")  
  
_# Set the active measurement to measurement 1_  
session.write("CALC1:PAR:MNUM 1")  
  
_# Set sweep type to linear_  
session.write("SENS1:SWE:TYPE LIN")  
_  
# Perfoms a single sweep_  
session.write("SENS1:SWE:MODE SING")  
opcCode = session.query("*OPC?")  
  
_# Get stimulus and formatted response data_  
results = session.query_ascii_values("CALC1:MEAS1:DATA:FDATA?")  
xValues = session.query_ascii_values("CALC1:MEAS1:X:VAL?")  
  
plt.plot(xValues, results)  
plt.ylabel("dB")  
plt.xlabel("Frequency")  
plt.show()  
  
---

