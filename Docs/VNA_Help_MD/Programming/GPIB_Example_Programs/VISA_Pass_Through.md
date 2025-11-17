# VISA Pass-Through Example

* * *

The VISA (Virtual Instrument Software Architecture) [System
Communicate](../GP-IB_Command_Finder/SystCommunicate.htm) commands used in
this example allow you to send SCPI commands to another device through the
VNA. VISA is used to communicate with most instrumentation buses including the
following:

  * GPIB
  * USB
  * Serial
  * Ethernet

##### [See Other SCPI Example Programs](SCPI_Example_Programs.md)

* * *

option explicit  
dim app  
set app = CreateObject("AgilentPNA835x.Application")  
  
set scpi = app.ScpiStringParser  
  
' Open a new VISA session and set timeout to 10 ms  
scpi.Parse "SYST:COMM:VISA:RDEV:OPEN
'TCPIP0::A-N5242A-10096::hislip1::INSTR',10"  
  
' Retrieve the session ID number  
sessionNum = scpi.Parse "SYST:COMM:VISA:RDEV:OPEN?"  
  
' Send session ID number and send RBW command to the device  
scpi.Parse "SYST:COMM:VISA:RDEV:WRIT & sessionNum & 'RBW:ARB 1'"  
  
' Send the "*IDN?" query  
scpi.Parse "SYST:COMM:VISA:RDEV:WRITE & sessionNum & '*IDN?'"  
  
' Read its results  
idnstr = scpi.Parse "SYST:COMM:VISA:RDEV:READ?" & sessionNum  
  
' Close the VISA session  
scpi.Parse "SYST:COMM:VISA:RDEV:CLOSE" & sessionNum

* * *

