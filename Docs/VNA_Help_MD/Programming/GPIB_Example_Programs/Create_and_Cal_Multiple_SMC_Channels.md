# Calibrate Multiple SMC Channels

* * *

This example allows you to calibrate multiple SMC channels while connecting
the power meter and required standards or ECal module only once.

In the example program:

  * Modify chans = 2 to indicate the number of channels to calibrate.

  * You can also change the connector type and cal kit for each port.

The SCPI commands in this example are sent over a COM interface using the
SCPIStringParser object. You do NOT need a GPIB connection to run this
example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as MultChanCal.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

Dim app Dim scpi Dim chans Dim i Dim steps Dim desc ' Create / Get the VNA
application. Set app = CreateObject("AgilentPNA835x.Application") Set scpi =
app.ScpiStringParser app.Preset ' Set number of channels to create chans = 2
ReDim calset(chans - 1) For i = 1 To chans chanStr = CStr(i+1) ' calibrate on
channels 2 and 3 Dim parm, measName, sens, calc parm = "S" & CStr(i) & CStr(i)
measName = "My" & parm sens = "SENS" & chanStr calc = "CALC" & chanStr
scpi.Parse calc & ":CUST:DEF '" & measName & "', 'Scalar Mixer/Converter', '"
& parm & "'" 'Setup the new measurement as the 2nd trace in the active window
scpi.Parse "DISP:WIND:TRAC" & chanStr & ":FEED '" & measName & "'" 'Make the
new trace the active measurement scpi.Parse calc & ":PAR:SEL '" & measName &
"'" '\--------------Perform A FCA Mixer Calibration------------- 'Set ports
and cal kits for 2 port calibration portion scpi.Parse sens &
":CORR:COLL:GUID:CONN:PORT1:SEL ""APC 3.5 male""" scpi.Parse sens &
":CORR:COLL:GUID:CONN:PORT2:SEL ""APC 3.5 female""" scpi.Parse sens &
":CORR:COLL:GUID:CKIT:PORT1:SEL ""85052C""" scpi.Parse sens &
":CORR:COLL:GUID:CKIT:PORT2:SEL ""85052C""" 'ECal modules are specified with
the same command ' scpi.Parse sens & ":CORR:COLL:GUID:CKIT:PORT1:SEL
""N4691-60004 ECal""" ' scpi.Parse sens & ":CORR:COLL:GUID:CKIT:PORT2:SEL
""N4691-60004 ECal""" 'Specify the thru measurement method. scpi.Parse sens &
":CORR:COLL:GUID:PATH:TMET 1,2,""DEFINED THRU""" 'Omit the isolation part of
the 2-port cal scpi.Parse sens & ":CORR:COLL:GUID:ISOL NONE" 'Initialize an
SMC guided calibration. scpi.Parse sens & ":CORR:COLL:GUID:INIT" 'Determine
the number of steps required to complete the calibration. steps = scpi.Parse
(sens & ":CORR:COLL:GUID:STEP?") Next For j = 1 To CInt(steps) 'Display the
prompt for each step desc = scpi.Parse(sens & ":CORR:COLL:GUID:DESC? " &
CStr(j)) MsgBox (desc) 'Measure the same standard for each channel For i = 1
To chans chanStr = CStr(i+1) ' channel number as string scpi.Parse "SENS" &
chanStr & ":CORR:COLL:GUID:ACQ STAN" & CStr(j) opc_comp = scpi.Parse("*OPC?")
Next Next 'Finish the cal and save the calsets For i = 1 To chans calset(i -
1) = scpi.Parse("SENS" & CStr(i+1) & ":CORR:COLL:GUID:SAVE ON") Next MsgBox
("SMC Cals Complete!")  
---  
  
* * *

