# Show Custom Cal Windows during a Guided Calibration

* * *

This VBScript program shows how to send commands that allow you to view
specific 'custom' windows, and sweep specific channels, during a UI (Cal
Wizard) or remote calibration.

The SCPI commands in this example are sent over a COM interface using the
SCPIStringParser object. You do NOT need a GPIB connection to run this
example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as CalWindow.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#Setup)

These commands are used to show and sweep windows and channels:

  * [SENS:CORR:COLL:DISP:WIND](../GP-IB_Command_Finder/Sense/Sense_Correction.md#CalWindowState)

  * [SENS:CORR:COLL:SWE:CHAN](../GP-IB_Command_Finder/Sense/Sense_Correction.md#CalWinSweepChan)

  * [SENS:CORR:COLL:DISP:WIND:AOFF](../GP-IB_Command_Finder/Sense/Sense_Correction.md#CalWindowAoff)

  * [SENS:CORR:COLL:SWE:CHAN:AOFF](../GP-IB_Command_Finder/Sense/Sense_Correction.md#CalWindowSweepAoff)

  * [SENS:CORR:COLL:GUID:PACQuire](../GP-IB_Command_Finder/Sense/CorrGuided.md#previewAcquire)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

Dim app Dim scpi ' Create / Get the PNA application. Set app =
CreateObject("AgilentPNA835x.Application") Set scpi = app.ScpiStringParser ' A
comment 'Preset the analyzer 'This creates an S11 measurement in channel 1,
window 1 scpi.Execute "SYST:PReset" ' Create and turn on window 2 scpi.Execute
"DISPlay:WINDow2:STATE ON" 'Define an S21 measurement in channel 2
scpi.Execute "CALCulate2:PARameter:DEFine:EXT 'MyMeas',S21" 'Associate
("FEED") the measurement name ('MyMeas') to WINDow2 'and give the new TRACe a
number (1). scpi.Execute "DISPlay:WINDow2:TRACe1:FEED 'MyMeas'" 'The following
lines are all you need in order to: 'show and sweep the custom Cal windows
during a UI Calibration 'If sending ONLY these commands, make sure you know
the 'correct window and channel numbers to show and sweep. 'Flag windows 1 and
2 to show during Ch1 calibration scpi.Execute "SENS:CORR:COLL:DISP:WIND1 ON"
scpi.Execute "SENS:CORR:COLL:DISP:WIND2 ON" 'Flag channels 1 and 2 to sweep
during Ch1 calibration scpi.Execute "SENS1:CORR:COLL:SWE:CHAN1 ON"
scpi.Execute "SENS1:CORR:COLL:SWE:CHAN2 ON" '
=========================================================== ' The following
code performs a remote guided Cal on Ch1. ' From a remote cal, the Cal window
does not normally show and sweep ' after the previous standard has been
acquired. ' This shows how to include the PACQuire (preview) to view and sweep
the Cal Window. ' The Custom window also shows and sweeps due to the flag
commands above. ' The flags are cleared at the end of this section. ' Specify
the DUT connectors scpi.Execute "sens:corr:coll:guid:conn:port1 ""APC 3.5
female"" " scpi.Execute "sens:corr:coll:guid:conn:port2 ""APC 3.5 male"" " '
Select the Cal Kit for each port being calibrated. scpi.Execute
"sens:corr:coll:guid:ckit:port1 ""85052D"" " scpi.Execute
"sens:corr:coll:guid:ckit:port2 ""85052D"" " ' Initiate the calibration and
query the number of steps scpi.Execute "sens:corr:coll:guid:init" numSteps =
scpi.Execute("sens:corr:coll:guid:steps?") MsgBox "Number of steps is " \+
CStr(numSteps) ' Measure the standards For i = 1 to numSteps step = "Step " \+
CStr(i) + " of " \+ CStr(numSteps) strPrompt =
scpi.Execute("sens:corr:coll:guid:desc? " \+ CStr(i)) 'send the Preview
Acquire command, then prompt scpi.Execute "sens:corr:coll:guid:PACquire STAN"
\+ CStr(i) ' Do NOT send any Guided Cal commands here or the cal window will
not sweep MsgBox strPrompt, vbOKOnly, step scpi.Execute
"sens:corr:coll:guid:acq STAN" \+ CStr(i) Next ' Conclude the calibration
scpi.Execute "sens:corr:coll:guid:save" MsgBox "Cal is done!" 'Remove the
Custom Window flags scpi.Execute "SENS:CORR:COLL:DISP:WIND:AOFF" 'Remove the
channel sweep flags scpi.Execute "SENS:CORR:COLL:SWE:CHAN:AOFF"  
---  
  
* * *

