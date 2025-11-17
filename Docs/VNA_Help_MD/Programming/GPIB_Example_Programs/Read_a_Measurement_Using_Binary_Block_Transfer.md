# Read a Measurement Using Binary Block Transfer

The following Python example demonstrates how to transfer data using binary #
block transfers (most efficient) within the Python environment.

### See Also

[Python Basics](../Learning_about_GPIB/Python_Basics.md)

# This example demonstrates how to transfer data using binary  
# block transfers (most efficient) within the Python environment  
  
import pyvisa as visa  
  
# Change this variable to the address of your instrument  
VISA_ADDRESS = 'TCPIP0::localhost::inst0::INSTR'  
  
# Create a connection (session) to the instrument  
resourceManager = visa.ResourceManager()  
session = resourceManager.open_resource(VISA_ADDRESS)  
  
# Command to preset the instrument and deletes the default trace, measurement,
and window  
session.write("SYST:FPR")  
  
# Create and turn on window 1  
session.write("DISP:WIND1:STAT ON")  
# ======================== Set up a measurement ========================  
  
# Create a S11 measurement  
session.write("CALC1:MEAS1:DEF 'S11'")  
  
# Displays measurement 1 in window 1 and assigns the next available trace
number to the measurement  
session.write("DISP:MEAS1:FEED 1")  
  
# Take a single sweep of data  
session.write("SENS:SWE:MODE SING")  
session.query("*OPC?")  
  
# Setup to transfer the data in the most efficient way  
session.write("FORM:BORD SWAP") # On Windows, we are little endian. This
avoids an unnecessary swap operation  
session.write("FORM:DATA REAL,32") # The native format for data arrays is 32
bit float  
  
# Query an array of formatted data using binary transfers  
values = session.query_binary_values("CALC:MEAS:DATA:FDATA?",datatype='f',
is_big_endian=False)  
  
# print the first element of the array  
# This is the first data point in logmag formatted  
print(values[0])  
  
---

