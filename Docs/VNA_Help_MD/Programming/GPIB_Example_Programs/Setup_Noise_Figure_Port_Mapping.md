# Set Up Noise Figure Port Mapping

* * *

This program demonstrates how to change source and receive ports when
measuring noise figure. It assumes that option 029 ("Fully Corrected Noise
Figure") is installed.

If only option 028 ("Noise figure measurements using standard receivers") is
installed, switching ports is simpler, since only one noise receiver selection
is available.

This program can be run as a macro in the VNA. To do this, copy the code into
a text editor file such as Notepad and save on the VNA hard drive as NF.vbs.
[Learn how to setup and run the macro.](../Using_Macros.md#HowToSetup)

[See the Noise figure commands.](../GP-IB_Command_Finder/Sense/Noise.md)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

**option explicit** **dim app, hostname, parser** **set app = CreateObject(
"Agilentpna835x.application")** **set parser = app.ScpiStringParser** **'
Create Noise Figure measurement** **parser.Parse "*RST"** **parser.Parse
"CALC:PAR:DEL:ALL"** **parser.Parse "CALC:CUST:DEF 'NF', 'Noise Figure Cold
Source', 'NF' "** **parser.Parse "DISP:WIND:TRAC1:FEED 'NF'"** **' To change
from the default input/output port settings of** **' source port = VNA1,
receive port = VNA2, you must first** **' change the noise receiver, then
select the desired ports.** **dim srcPort, rcvPort** **' Set source=VNA port 3
and receiver=VNA port 4** **srcPort = 3** **rcvPort = 4** **' use VNA receiver
for noise measurements** **parser.Parse "SENS:NOIS:REC NORMAL"** **' set port
mapping** **parser.Parse "SENS:NOIS:PMAP " & srcPort & "," & rcvPort ** **' To
revert back to using the noise receiver, the receive port must** **' be set to
the default value VNA2 BEFORE switching to the noise receiver. ** **'
Otherwise, the SCPI error** **' "The noise receiver is not available for the
selected receive port" ** **' will occur.** **parser.Parse "SENS:NOIS:PMAP
3,2"** **' use dedicated noise receiver for noise measurements**
**parser.Parse "SENS:NOIS:REC NOISE" **  
---

