# Perform a Simple Source Power Cal

* * *

This example performs a Source Power Cal using ONE USB Power Sensor, already
connected to the VNA.

A measurement must first be set up with desired frequency range, power, and so
forth, ready to be calibrated.

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do NOT need a GPIB connection to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file, such as Notepad, and save it
on the VNA hard drive as spc.vbs.

[Learn how to setup and run the macro.](../Using_Macros.md#HowToSetup)

[See Source Power Cal SCPI commands](../GP-
IB_Command_Finder/SourceCorrection.htm)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

'Performs a source power cal on channel 1 - port 1 using a USB power sensor
'This example assumes ONE USB power sensor is connected to the VNA Dim app Dim
scpi Dim sensor ' Create / Get the VNA application. Set app =
CreateObject("AgilentPNA835x.Application") Set scpi = app.ScpiStringParser
scpi.parse "SYST:PRES" 'set power accuracy tolerance and iterations scpi.parse
"SOUR1:POW1:CORR:COLL:ITER:NTOL 0.1" scpi.parse
"SOUR1:POW1:CORR:COLL:ITER:COUN 15" 'set power sensor settling tolerance
scpi.parse "SOUR1:POW1:CORR:COLL:AVER:NTOL 0.1" scpi.parse
"SOUR1::POW1:CORR:COLL:AVER:COUN 15" 'set offset value for amp or attenuation
scpi.parse "SOUR1:POW1:CORR:OFFS 0 DB" 'show source power cal dialog
scpi.parse "SOUR1:POW1:CORR:COLL:DISP ON" 'read the usb power sensor ID string
sensor=scpi.parse("SYST:COMM:USB:PMET:CAT?") 'specify that sensor scpi.parse
"SYST:COMM:PSEN usb," \+ sensor 'do the measurement scpi.parse
"SOUR1:POW1:CORR:COLL:ACQ PMR,"ASENSOR"" 'save the source cal and create an
R-Channel response calset scpi.parse "SOUR:POW:CORR:COLL:SAVE RREC"  
---  
  
* * *

