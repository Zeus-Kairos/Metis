# Perform a Guided Cal using Multiple Power Sensors

* * *

This example performs a Guided Calibration using TWO power sensors that are
setup as PMAR devices. Use of two power sensors is necessary when the
frequency range of the measurement is greater than can be attained with a
single sensor.

A measurement must first be set up with desired frequency range, power, and so
forth, ready to be calibrated.

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do not need to control the VNA via GPIB to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file, such as Notepad, and save it
on the VNA hard drive as mps.vbs.

[Learn how to setup and run the macro.](../Using_Macros.md#HowToSetup)

[See Guided Power Sensor SCPI commands](../GP-
IB_Command_Finder/Sense/CorrCollGuidPSens.htm)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

set app = CreateObject("Agilentpna835x.application") set s =
app.ScpiStringParser s.Parse "SYST:PRES" s.Parse "SENS:FREQ:START 1E9" s.parse
"SENS:FREQ:STOP 2E9" s.Parse "sens:corr:coll:guid:conn:port1 'APC 3.5 female'"
s.Parse "sens:corr:coll:guid:conn:port2 'APC 3.5 male'" s.Parse
"sens:corr:coll:guid:ckit:port1 'N4691-60004 ECal'" s.Parse
"sens:corr:coll:guid:ckit:port2 'N4691-60004 ECal'" s.Parse
"SENS:CORR:COLL:GUID:PSEN2 ON" 'turn on power cal at port #2 s.Parse
"SENS:CORR:COLL:GUID:PSEN2:MULT ON" s.Parse
"SENS:CORR:COLL:GUID:PSEN2:MULT:NAME 'pmar1'" s.Parse
"SENS:CORR:COLL:GUID:PSEN2:MULT:FREQ:STARt 1e9" s.Parse
"SENS:CORR:COLL:GUID:PSEN2:MULT:FREQ:STOP 1.5e9" s.Parse
"SENS:CORR:COLL:GUID:PSEN2:MULT:ADD 'PMAR2'" s.Parse
"SENS:CORR:COLL:GUID:PSEN2:MULT2:FREQ:STARt 1.5e9" s.Parse
"SENS:CORR:COLL:GUID:PSEN2:MULT2:FREQ:STOP 2e9" s.Parse
"SENS:CORR:COLL:GUID:INIT" numSteps = s.Parse("SENS:CORR:COLL:GUID:STEPS?")
for i = 0 to numSteps-1 desc = s.parse("SENS:CORR:COLL:GUID:DESC? " &
CStr(i+1)) msgbox desc s.parse "SENS:CORR:COLL:GUID:ACQ STAN" & CStr(i+1) next
s.parse "SENS:CORR:COLL:GUID:SAVE"  
---

