# Create a FOM Measurement with Error Handling

The following Python example demonstrates how to create a FOM measurement with
the following attributes:

  * Sweep the Source (input) from 1 GHz to 2 GHz

  * Sweep the Receivers (output) from 2 GHz to 3 GHz

  * Check for VISA connection issue and SCPI errors using error handling code

### See Also

[Python Basics](../Learning_about_GPIB/Python_Basics.md)

import pyvisa as visa  
import sys  
  
_# Change this variable to the address of your instrument_  
VISA_ADDRESS = 'TCPIP0::localhost::inst0::INSTR'  
  
_# Custom Exception class for SCPI Errors_  
class SCPIError(Exception):  
def __init__(self, ex, *args):  
super().__init__(args)  
self.ex = ex  
 _# Display the Error Messag_  
def __str__(self):  
return f'SCPI errors found in the system: {self.ex}'  
  
_# Helper function to check for errors_  
def catchErr():  
numErrors = session.query("SYST:ERR:COUN?")  
if int(numErrors) != 0:  
raise SCPIError(session.query("SYST:ERR?"))  
  
try:  
 _# Create a connection (session) to the instrument_  
resourceManager = visa.ResourceManager()  
session = resourceManager.open_resource(VISA_ADDRESS)  
  
 _# Command to preset the instrument and deletes the default trace,
measurement, and window_  
session.write("SYST:FPR")  
catchErr()  
  
 _# Create and turn on window 1_  
session.write("DISP:WIND1:STAT ON")  
catchErr()  
  
 _# Create a measurement with parameter_  
session.write("CALC1:MEAS1:DEF 'S21'")  
catchErr()  
  
 _# Displays measurement 1 in window 1 and assigns the next available trace
number to the measurement_  
session.write("DISP:MEAS1:FEED 1")  
catchErr()  
  
 _# Set the start and stop frequencies_  
session.write("SENS1:FREQ:START 1e9")  
catchErr()  
  
session.write("SENS1:FREQ:STOP 2e9")  
catchErr()  
  
 _# Set the receivers to be 2e9 - > 3e9_  
 _# See SENS:FOM:RNUM? to find the range number for a specific name_  
session.write("SENS1:FOM:RANG3:FREQ:OFFS 1e9") catchErr()  
  
 _# Turns frequency offset on and enable the freq offset settings_  
session.write("SENS1:FOM ON")  
catchErr()  
  
except visa.Error as ex:  _# Failed to communicate with the instrument_  
print('Couldn\'t connect to \'%s\', exiting now...' % VISA_ADDRESS)  
sys.exit()  
  
except SCPIError as e:  
 _# SCPI Errors in the system_  
print(e)  
sys.exit()  
  
except Exception as e:  
 _# Catches generic errors_  
print(f"Error: {e}")  
  
finally:  
 _# No errors found_  
print("Done")  
  
---

