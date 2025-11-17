# SRQ Example

The following Python example demonstrates how to send SCPI commands to the VNA
to set up a SRQ (Service Request) event.

Some SCPI commands take a long time to complete. These commands are also
called overlapped commands. The most common example is SENS:SWE:MODE SING
(for a slow channel).

There are 3 alternative ways to block on these commands:

  1. The simplest is using *OPC?. In this case, the client is blocked until the command completes.

Disadvantages:

    * Client has to set a long time out. Sometimes, with receiver leveling for instance, it is unclear how long the sweep will take.

    * It is hard to abort the sweep.

  2. Polling. In this case, *OPC is sent and loop the *ESR? until it returns true. This is simple  but not quite as simple as alternative #1.

Disadvantage

    * You have to determine how frequently to send the *ESR?.

    * If you send it too frequently, then the code may slow down. So, a Sleep(X) will be added to the loop. The length of the Sleep(X) will add a slight overhead to the loop.

  3. SRQ Events. This is the best solution, but the most complicated to implement. The following example shows how to implement the SRQ method.

### See Also

[Python Basics](../Learning_about_GPIB/Python_Basics.md)

from time import sleep  
import pyvisa as visa  
from pyvisa import constants  
_# Change this variable to the address of your instrument_  
VISA_ADDRESS = 'TCPIP0::localhost::inst0::INSTR'  
  
_# Create a connection (session) to the instrument_  
resourceManager = visa.ResourceManager()  
session = resourceManager.open_resource(VISA_ADDRESS)  
session.called = False  
  
def handle_event(resource, event, user_handle):  
resource.called = True  
print(f"Handled event {event.event_type} on {resource}\n")  
  
_# Command to preset the instrument and deletes the default trace,
measurement, and window_  
session.write("SYST:FPR")  
  
_# Create and turn on window 1_  
session.write("DISP:WIND1:STAT ON")  
  
_# Create the measurement_  
session.write("CALC1:MEAS1:DEF 'S11'")  
  
_# Displays measurement 1 in window 1 and assigns the next available trace
number to the measurement_  
session.write("DISP:MEAS1:FEED 1")  
  
session.write("SENS:SWE:MODE SING")  
opcCode = session.query("*OPC?") _  
# Type of event we want to be notified about_  
event_type = constants.EventType.service_request  
_# Mechanism that we want to be notified about_  
event_mech = constants.EventMechanism.handler  
wrapped = session.wrap_handler(handle_event)  
user_handle = session.install_handler(event_type, wrapped, 42)  
session.enable_event(event_type, event_mech, None)  
  
_# The following code enables service request_  
_# Turn on the SRQ for operation complete? bit_  
session.write("*SRE 32")  
_# Clear any pending status_  
session.write("*CLS")  
_# Set sweep time to 2 seconds_  
session.write("SENS:SWE:TIME 2")  
print("Sweep Started")  
session.write("SENS:SWE:MODE SING")  
session.write("*OPC")   _# Tell VNA that we are interested in operation
complete status_  
while not session.called:  
print("Waiting")  
sleep(0.01)  
print("Done")  
session.disable_event(event_type, event_mech)  
session.uninstall_handler(event_type, wrapped, user_handle)  
  
---

