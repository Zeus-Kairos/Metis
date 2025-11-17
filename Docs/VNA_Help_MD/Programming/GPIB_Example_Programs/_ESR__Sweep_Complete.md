# Poll for Sweep Complete

* * *

This Python example program polls for the completion of a sweep.

### See Also

[Python Basics](../Learning_about_GPIB/Python_Basics.md)

import time import pyvisa as visa def
write_with_stb_polling(session,command,timeout): # Enable operation complete
status register session.write("*ESE 1") # Clear the existing status state
session.query("*ESR?") # Send asynchronous command session.write(command) #
*OPC indicates that we want to be notified when the asyn command is completed
# Note that we are NOT using the query form, so this does not block
session.write("*OPC") # Check if the asyn operation has completed by checking
bit 5 (32) isDone = session.read_stb() & 32 end_time = time.time() + timeout
while (not isDone and time.time() < end_time): time.sleep(0.1) # sleep for 100
ms to avoid working the CPU isDone = session.read_stb() & 32 # If still not
done, then it is because the timeout was hit # Report it as an exception if
(not isDone): raise Exception(f"Timeout exceeded ({timeout}s) with {command}")  
  
# Change this variable to the address of your instrument # or leave this alone
when using the simulator VISA_ADDRESS = 'TCPIP0::localhost::inst0::INSTR' #
Create a connection (session) to the instrument resourceManager =
visa.ResourceManager() session = resourceManager.open_resource(VISA_ADDRESS) #
Command to preset the instrument and deletes the default trace, measurement,
and window session.write("SYST:FPR") # Create and turn on window 1
session.write("DISP:WIND1:STAT ON") # Create the measurement
session.write("CALC1:MEAS1:DEF 'S11'") # Displays measurement 1 in window 1
and assigns the next available trace number to the measurement
session.write("DISP:MEAS1:FEED 1") # Set the channel into hold mode
session.write("SENS:SWE:MODE HOLD") # Set sweep time to 2 seconds to simulate
a slow sweep session.write("SENS:SWE:TIME 2") print("Start Sweep")
timeoutForCommand = 10 # 10 seconds timeout
write_with_stb_polling(session,"SENS:SWE:MODE SING",timeoutForCommand)
print("Stop Sweep")  
---

