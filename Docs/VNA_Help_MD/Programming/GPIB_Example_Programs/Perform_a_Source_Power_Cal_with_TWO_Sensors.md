# Perform a Source Power Cal with TWO Sensors

* * *

This example performs a Source Power Cal using TWO power sensors on a Dual-
Channel Power Meter connected to the VNA via GPIB. Use of two power sensors is
necessary when the frequency range of the measurement is greater than can be
attained with a single sensor.

A measurement must first be set up with desired frequency range, power, and so
forth, ready to be calibrated.

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do not need to control the VNA via GPIB to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file, such as Notepad, and save it
on the VNA hard drive as spc.vbs.

[Learn how to setup and run the macro.](../Using_Macros.md#HowToSetup)

[See Source Power Cal SCPI commands](../GP-
IB_Command_Finder/SourceCorrection.htm)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

'Performs a source power cal on channel 1 - port 1 using TWO USB power
sensors. Dim app Dim scpi Dim sensor ' Create / Get the VNA application. Set
app = CreateObject("AgilentPNA835x.Application") Set scpi =
app.ScpiStringParser scpi.parse "SYST:PRES" 'set power accuracy tolerance and
iterations scpi.parse "SOUR1:POW1:CORR:COLL:ITER:NTOL 0.1" scpi.parse
"SOUR1:POW1:CORR:COLL:ITER:COUN 15" 'set power sensor settling tolerance
scpi.parse "SOUR1:POW1:CORR:COLL:AVER:NTOL 0.1" scpi.parse
"SOUR1::POW1:CORR:COLL:AVER:COUN 15" 'set offset value for amp or attenuation
scpi.parse "SOUR1:POW1:CORR:OFFS 0 DB" 'show source power cal dialog
scpi.parse "SOUR1:POW1:CORR:COLL:DISP ON" 'set frequency ranges for two power
sensors scpi.parse "SOUR:POW:CORR:COLL:ASEN 100E3, 3E9" scpi.parse
"SOUR:POW:CORR:COLL:BSEN 3E9,6E9" 'enable frequency check scpi.parse
"SOUR1:POW:CORR:COLL:FCHeck ON" 'specify the address of the power meter
scpi.parse "SYST:COMM:PSEN GPIB,14" 'do the measurements MsgBox "Connect
Sensor A to Port 1" scpi.parse "SOUR1:POW1:CORR:COLL:ACQ PMR,'ASENSOR'" MsgBox
"Disconnect Sensor A from Port 1 and connect Sensor B to Port 1" scpi.parse
"SOUR1:POW1:CORR:COLL:ACQ PMR,'BSENSOR'" 'save the source cal and create an
R-Channel response calset scpi.parse "SOUR:POW:CORR:COLL:SAVE RREC"  
---  
  
* * *

