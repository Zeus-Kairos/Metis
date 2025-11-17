# Set Up Basic Measurements

* * *

This VBScript program sets up four basic s-parameter measurements in four
windows, all in a single channel. Handles are created to the measurement,
channel, and window objects so that subsequent settings can be made for each.

Note: This is only an example. This is not necessarily the most efficient way
to make basic S-parameter measurements.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as Basic.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#Setup)

[See VNA Object Model](../COM_Reference/Objects/The_Analyzer_Object_Model.md)

See
[CreateSParameterEx](../COM_Reference/Methods/Create_SParameterEX_Method.md)

[See Other COM Example Programs](COM_Example_Intro.md)

Set pna = CreateObject("AgilentPNA835x.Application") pna.Preset ' Get a handle
to the preset channel 1, S11 meas, and window(1) set
meas1=pna.ActiveMeasurement set chan1=pna.ActiveChannel set
win1=pna.ActiveNAWindow ' Creates a new S21 measurement in New window(2)
pna.CreateSParameterEx 1,2,1,2,2 set meas2=pna.ActiveMeasurement set
win2=pna.ActiveNAWindow ' Creates a new S12 measurement in New window(3)
pna.CreateSParameterEx 1,1,2,1,3 set meas3=pna.ActiveMeasurement set
win3=pna.ActiveNAWindow ' Creates a new S22 measurement in New window(4)
pna.CreateSParameterEx 1,2,2,2,4 set meas4=pna.ActiveMeasurement set
win4=pna.ActiveNAWindow 'Make settings 'set Stop Frequency for channel
chan1.StopFrequency=1e9 'set Display formats meas1.format=0 'Lin Mag
meas2.format=1 'Log Mag meas3.format=2 'Phase meas4.format=3 'Smith 'Show
title in all windows win1.title="Win #1" win2.title="Win #2" win3.title="Win
#3" win4.title="Win #4"  
---  
  
* * *

