# 4 S- Parameter Measurement

The following Python program demonstrates how to set up 4 S-Parameter
measurement and display it on the VNA screen.

#### See Also:

[Python Basics](../Learning_about_GPIB/Python_Basics.md)

import pyvisa as visa  
  
_# Change this variable to the address of your instrument_  
VISA_ADDRESS = 'TCPIP0::localhost::inst0::INSTR'  
  
_# Create a connection (session) to the instrument_  
resourceManager = visa.ResourceManager()  
session = resourceManager.open_resource(VISA_ADDRESS)  
  
session.timeout = 25000  
  
_# Command to preset the instrument and deletes the default trace,
measurement, and window_  
session.write("SYST:FPR")  
  
_# Create and turn on window 1_  
session.write("DISP:WIND1:STAT ON")  
  
_# ======================== Set up 4 S-Parameters ========================_  
_# Create a S11 measurement_  
session.write("CALC1:MEAS1:DEF 'S11'")  
  
_# Displays measurement 1 in window 1 and assigns the next available trace
number to the measurement_  
session.write("DISP:MEAS1:FEED 1")  
  
_# Create a S21 measurement_  
session.write("CALC1:MEAS2:DEF 'S21'")  
  
_# Displays measurement 2 in window 1 and assigns the next available trace
number to the measurement_  
session.write("DISP:MEAS2:FEED 1")  
  
_# Create a S12 measurement_  
session.write("CALC1:MEAS3:DEF 'S12'")  
  
_# Displays measurement 3 in window 1 and assigns the next available trace
number to the measurement_  
session.write("DISP:MEAS3:FEED 1")  
  
_# Create a S22 measurement_ __  
session.write("CALC1:MEAS4:DEF 'S22'")  
  
_# Displays measurement 4 in window 1 and assigns the next available trace
number to the measurement_  
session.write("DISP:MEAS4:FEED 1")  
  
_# ======================== Set start and stop ========================_  
session.write("SENS1:FREQ:START 1e9")  
  
session.write("SENS1:FREQ:STOP 2e9")  
  
_# ======================== Change the number of points
========================_  
session.write("SENS1:SWE:POIN 51")  
  
_# ======================== Set IFBW ========================_  
_# Set IF Bandwidth to 700 Hz_  
session.write("SENS1:BAND 700")  
  
_# ======================== Take a sweep and read back data
========================_  
_# Perfoms a single sweep_  
session.write("SENS1:SWE:MODE SING")  
opcCode = session.query("*OPC?")  
results1 = session.query_ascii_values("CALC1:MEAS1:DATA:FDATA?")  
results2 = session.query_ascii_values("CALC1:MEAS2:DATA:FDATA?")  
results3 = session.query_ascii_values("CALC1:MEAS3:DATA:FDATA?")  
results4 = session.query_ascii_values("CALC1:MEAS4:DATA:FDATA?")  
---

