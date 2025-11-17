# Advanced Programming Practices

## Error Handling

It's best practice to implement error handling code to make using and
maintaining your script easier.

  1. Connecting to the Instrument: Add a try-except to catch connection issues instead of assuming that the instrument address is correct.

# Module for sys.exit(), add to top of script import sys try: # Create a
connection (session) to the instrument resourceManager =
visa.ResourceManager() session = resourceManager.open_resource(VISA_ADDRESS)
except visa.Error as ex: # Failed to communicate with the instrument
print('Couldn\'t connect to \'%s\', exiting now...' % VISA_ADDRESS) sys.exit()  
---  

  2. Check for SCPI errors using SYST:ERR?

sysErrors = session.query("SYST:ERR?") print(f"Errors: {sysErrors}")  
---  

  3. Example that implements these two practices: [Error Handling for FOM Measurement Script](FOM_Measurement_with_Error_Handling.md)

## Close the Instrument

#Close the connection to the instrument session.close()
resourceManager.close()  
---  
  
## Custom Timeout

  1. After setting a timeout, every operation that continues for longer than the timeout will be aborted, and this raises an exception to the program.

  2. Timeouts are given in milliseconds.

  3. For PyVISA objects, timeouts can be set using the property my_device.timeout = desired_timeout.

  4. If your script returns a timeout issue, this could be potentially fixed by increasing your timeout.

  5. * For an infinite timeout, the timeout value could be set to None or float('+inf'), or simply use the del command, ex: del my_device.timeout.

  6. In the following example, session is the connection to the instrument and its timeout is now set to 25000 milliseconds (25 seconds)

session.timeout = 25000  
---  
  7. For additional details, refer to <https://pyvisa.readthedocs.io/en/latest/introduction/resources.html#:~:text=For%20all%20PyVISA%20objects%2C%20a%20timeout%20is%20set,and%20its%20timeout%20is%20set%20to%2025%20seconds>

