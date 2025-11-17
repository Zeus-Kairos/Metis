# GPIB Pass-Through Example

* * *

The SCPI [SYSTem](../GP-IB_Command_Finder/System.md) commands used in this
example allow you to send GPIB commands to another GPIB device through the
VNA. The other device would typically be connected to the VNA through the
System Controller GPIB port on the VNA rear-panel or alternatively be
connected using a USB/GPIB interface. Uncomment the line in Blue text in the
example to open a session for a USB/GPIB interface.

This VB Script example uses the COM
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. However, this is not critical to the use of these commands; they can
be sent using the normal syntax of your programming environment. Using the
SCPIStringParser over LAN allows you to communicate with GPIB devices without
requiring your remote PC to have a GPIB interface card installed.

Although this method of pass-through works for most applications, there are a
couple of limitations:

  * All data is transferred using ASCII format. Therefore, transferring large blocks of data is very slow.

  * Only read and write functions are possible. Service Interrupts are not supported.

##### [See Other SCPI Example Programs](SCPI_Example_Programs.md)

* * *

option explicit  
dim app  
set app = CreateObject("AgilentPNA835x.Application")  
  
dim p  
set p = app.ScpiStringParser  
  
' Open a new GPIB session on Bus:0 Device:14 Timeout: 100ms  
p.Parse "SYST:COMM:GPIB:RDEV:OPEN 0,14,100"  
' The following commented-out line shows opening the same session but  
' for a USB/GPIB interface with VISA interface number GPIB4  
'p.Parse "SYST:COMM:GPIB:RDEV:OPEN 4,14,100"  
dim handleAsStr  
  
' Retrieve the handle (ID number)  
handleAsStr = p.Parse ("SYST:COMM:GPIB:RDEV:OPEN?")  
  
' Convert the handle to an integer  
dim handleAsInt  
handleAsInt = CInt(handleAsStr)  
  
' Send the "*IDN?" query  
p.Parse "SYST:COMM:GPIB:RDEV:WRITE " & handleAsInt & ",'*IDN?'"  
  
' Read its results  
dim idn  
idn = p.Parse("SYST:COMM:GPIB:RDEV:READ? " & handleAsInt)  
msgbox idn  
  
' Close the GPIB session  
p.Parse "SYST:COMM:GPIB:RDEV:CLOSE " & handleAsInt

* * *

