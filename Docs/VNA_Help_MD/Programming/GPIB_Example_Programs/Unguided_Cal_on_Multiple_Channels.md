# Perform an Unguided Cal on Multiple Channels

* * *

This VBScript program performs an Unguided Calibration simultaneously on two
channels.

This could be used in the following cases:

  * If you need more than the current number of data points per trace, so the additional points must be added to a different channel.

  * If you need several channels with independent settings, but you want to calibrate all channels with a minimal number of standard connections. This would be especially critical for on wafer calibration.

The SCPI commands in this example are sent over a COM interface using the
SCPIStringParser object. You do NOT need a GPIB connection to run this
example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as Unguided.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm)

Dim app Dim scpi Dim NumberOfActiveChannels NumberOfActiveChannels = 2 '
Create / Get the VNA application. Set app =
CreateObject("AgilentPNA835x.Application") Set scpi = app.ScpiStringParser '
Query the list of connectors that the VNA system recognizes
scpi.Execute("SYST:PRES") 'Wait for successful preset before continuing
done=scpi.Execute("*OPC?") 'The following section sets up 2 channels with
different frequency ranges scpi.Execute("DISP:WIND1:STATE OFF") 'Reset Windows
scpi.Execute("DISP:WIND1:STATE ON") scpi.Execute("DISP:WIND2:STATE ON") ' '
Assign a measurement to the first window scpi.Execute("CALC1:PAR:DEF:EXT
'Meas1', S21") scpi.Execute("DISP:WIND1:TRAC1:FEED 'Meas1'") 'Assign a
measurement to the second window scpi.Execute("CALC2:PAR:DEF:EXT 'Meas2',
S21") scpi.Execute("DISP:WIND2:TRAC1:FEED 'Meas2'") 'Set up two channels with
independent parameters scpi.Execute("SENS1:FREQ:SPAN 1e9")
scpi.Execute("SENS2:FREQ:SPAN 1e6") 'Wait for changes before continuing
done=scpi.Execute("*OPC?") ' 'This section sets the calibration kits for
channel 1 and channel 2 'Select a trace from channel 1 and set calibration
type and cal kit scpi.Execute("CALC1:PAR:SEL 'Meas1'")
scpi.Execute("SENS1:CORR:COLL:METH SPARSOLT")
scpi.Execute("SENS1:CORR:COLL:CKIT 2") '85056D for default settings 'Same
standards for forward and reverse direction scpi.Execute("SENS1:CORR:TST OFF")
'Select a trace from channel 2 and set calibration type and cal kit
scpi.Execute("CALC2:PAR:SEL 'Meas2'") scpi.Execute("SENS2:CORR:COLL:METH
SPARSOLT") scpi.Execute("SENS2:CORR:COLL:CKIT 2") '85056D for default settings
'Same standards for forward and reverse direction scpi.Execute("SENS2:CORR:TST
OFF") 'Set both channels to manual triggering scpi.Execute("INIT1:CONT OFF")
scpi.Execute("INIT2:CONT OFF") ' 'The following assumes female port connector
on port 1 ' and male port connector on port 1 'Step through all active
channels and calibrate and measure all standards.
scpi.Execute("SENS1:CORR:SFOR ON") 'Set acquisition to forward
scpi.Execute("SENS2:CORR:SFOR ON") 'Set acquisition to forward MsgBox("Connect
OPEN standard to port 1") For CurrentChannel = 1 To NumberOfActiveChannels
scpi.Execute("CALC" & CurrentChannel & ":PAR:SEL 'Meas" & CurrentChannel &
"'") scpi.Execute("SENS" & CurrentChannel & ":CORR:COLL stan1") done=
scpi.Execute("*OPC?") Next MsgBox("Connect SHORT standard to port 1") For
CurrentChannel = 1 To NumberOfActiveChannels scpi.Execute("CALC" &
CurrentChannel & ":PAR:SEL 'Meas" & CurrentChannel & "'") scpi.Execute("SENS"
& CurrentChannel & ":CORR:COLL stan2") done=scpi.Execute("*OPC?") Next
MsgBox("Connect LOAD standard to port 1") For CurrentChannel = 1 To
NumberOfActiveChannels scpi.Execute("CALC" & CurrentChannel & ":PAR:SEL 'Meas"
& CurrentChannel & "'") scpi.Execute("SENS" & CurrentChannel & ":CORR:COLL
stan3") done=scpi.Execute("*OPC?") Next scpi.Execute("SENS1:CORR:SFOR OFF")
'Set acquisition to reverse scpi.Execute("SENS2:CORR:SFOR OFF") 'Set
acquisition to forward MsgBox("Connect OPEN standard to port 2") For
CurrentChannel = 1 To NumberOfActiveChannels scpi.Execute("CALC" &
CurrentChannel & ":PAR:SEL 'Meas" & CurrentChannel & "'") scpi.Execute("SENS"
& CurrentChannel & ":CORR:COLL stan1") done=scpi.Execute("*OPC?") Next
MsgBox("Connect SHORT standard to port 2") For CurrentChannel = 1 To
NumberOfActiveChannels scpi.Execute("CALC" & CurrentChannel & ":PAR:SEL 'Meas"
& CurrentChannel & "'") scpi.Execute("SENS" & CurrentChannel & ":CORR:COLL
stan2") done=scpi.Execute("*OPC?") Next MsgBox("Connect LOAD standard to port
2") For CurrentChannel = 1 To NumberOfActiveChannels scpi.Execute("CALC" &
CurrentChannel & ":PAR:SEL 'Meas" & CurrentChannel & "'") scpi.Execute("SENS"
& CurrentChannel & ":CORR:COLL stan3") done=scpi.Execute("*OPC?") Next '
'Measure thru standard for all channels in both forward and reverse direction
MsgBox("Connect THRU between ports 1 and 2") scpi.Execute("SENS1:CORR:SFOR
ON") 'Set acquisition to forward scpi.Execute("SENS2:CORR:SFOR ON") 'Set
acquisition to forward For CurrentChannel = 1 To NumberOfActiveChannels
scpi.Execute("CALC" & CurrentChannel & ":PAR:SEL 'Meas" & CurrentChannel &
"'") scpi.Execute("SENS" & CurrentChannel & ":CORR:COLL stan4")
done=scpi.Execute("*OPC?") Next scpi.Execute("SENS1:CORR:SFOR OFF") 'Set
acquisition to reverse scpi.Execute("SENS2:CORR:SFOR OFF") 'Set acquisition to
reverse For CurrentChannel = 1 To NumberOfActiveChannels scpi.Execute("CALC" &
CurrentChannel & ":PAR:SEL 'Meas" & CurrentChannel & "'") scpi.Execute("SENS"
& CurrentChannel & ":CORR:COLL stan4") done=scpi.Execute("*OPC?") Next For
CurrentChannel = 1 To NumberOfActiveChannels scpi.Execute("CALC" &
CurrentChannel & ":PAR:SEL 'Meas" & CurrentChannel & "'") scpi.Execute("SENS"
& CurrentChannel & ":CORR:COLL:SAVE") done=scpi.Execute("*OPC?") Next 'Set
both channels to continuous triggering scpi.Execute("INIT1:CONT ON")
scpi.Execute("INIT2:CONT ON")  
---

