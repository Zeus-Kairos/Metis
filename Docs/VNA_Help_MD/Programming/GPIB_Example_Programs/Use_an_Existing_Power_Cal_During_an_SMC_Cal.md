# Use an Existing Power Cal During an SMC Cal

* * *

This example shows how to use an existing Source Power Cal instead of the
power cal that is performed during an SMC calibration. To run this program
without modification, you need the following:

  * A Mixer setup file saved on the VNA: C:\Program Files(x86)\Keysight\Network Analyzer\Documents\Mixer\MyMixer.mxr.

  * If the mixer file uses an external LO source, it must also be attached and configured.

  * An ECAL module that covers the frequency range of the measurement.

  * An SMC cal set named "SMC_CAL". This is the cal set that source power correction data will be imported from. The input and output frequency ranges of the cal set must cover the corresponding ranges used during calibration, or guided cal initialization will fail.

### Error Messages

  * If you attempt to import power cal data from an SMC calset that uses different ports than the ones currently in use, the message The necessary calibration standards were not found. will appear.

  * If the imported Cal Set does not cover the frequency range of the current cal, the message Interpolation target is out of range. Cannot interpolate. will appear.

### See Also

[Sens:Corr:Coll:Guid:SMC](../GP-IB_Command_Finder/Sense/CorrCollGuidSMC.md)
commands

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save on
the VNA hard drive as SMC.vbs. Learn how to setup and run the macro.

Dim app Dim scpi ' Create / Get the VNA application. Set app =
CreateObject("AgilentPNA835x.Application") Set scpi = app.ScpiStringParser
'\---Create a Scalar Mixer Forward Measurement 'First, delete all measurements
on the channel scpi.Parse "CALC:PAR:DEL:ALL" 'Create a forward scalar mixer
measurement and configure it in 'channel 1. The first parameter is a unique
'identifying string (specified by the user) to allow subsequent 'commands to
be directed at this specific measurement. scpi.Parse "CALC:CUST:DEF 'My SC21',
'Scalar Mixer/Converter', 'SC21'" 'Setup the new measurement as the 2nd trace
in the active window scpi.Parse "DISP:WIND:TRAC2:FEED 'My SC21'" 'Make the new
trace the active measurement scpi.Parse "CALC:PAR:SEL 'My SC21'" 'The
parameters of the mixer measurement can now be configured. 'This can be done
by either using the individual SENS:MIX commands 'for each of the parameters
or by loading a mixer setup file. This 'example loads a mixer setup file. The
path name 'for the mixer file may be loaded from other mapped drives
scpi.Parse "SENS:MIXer:Load ""C:\Program Files(x86)\Keysight\Network
Analyzer\Documents\Mixer\MyMixer.mxr""" '\--------------Perform A Scalar Mixer
Calibration---------------------- 'Specify the connector types and the cal
kits for each of the ports. scpi.Parse "SENS:CORR:COLL:GUID:CONN:PORT1:SEL
""APC 3.5 male""" scpi.Parse "SENS:CORR:COLL:GUID:CONN:PORT2:SEL ""APC 3.5
female""" scpi.Parse "SENS:CORR:COLL:GUID:CKIT:PORT1:SEL ""N4691-60004 ECal"""
scpi.Parse "SENS:CORR:COLL:GUID:CKIT:PORT2:SEL ""N4691-60004 ECal""" 'Import
power cal data from the existing SMC calset "MySMC" scpi.Parse
"SENS:CORR:COLL:GUID:SMC:IMP ""SMC_CAL"",""POWER_STEP""" 'Specify the thru
measurement method. This applies to both ECal 'and mechanical calibrations.
'Always send the init command before the Thru method command scpi.Parse
"SENS:CORR:COLL:GUID:INIT" scpi.Parse "SENS:CORR:COLL:GUID:PATH:TMET
1,2,""DEFINED THRU""" 'Omit the isolation part of the 2-port cal (default
behavior). scpi.Parse "SENS:CORR:COLL:GUID:ISOL NONE" 'Turn on auto
orientation for the ECal (default behavior). scpi.Parse
"SENS:CORR:PREF:ECAL:ORI ON" 'Initialize an SMC guided calibration. scpi.Parse
"SENS:CORR:COLL:GUID:INIT" 'Tell the wizard to generate and report the number
of steps in this cal. Dim steps Dim desc 'Determine the number of steps
required to complete the calibration. steps = scpi.Parse
("SENS:CORR:COLL:GUID:STEP?") For i = 1 To steps 'Display the prompt for each
step desc = scpi.Parse ("SENS:CORR:COLL:GUID:DESC? " & CStr(i)) MsgBox (desc)
'Perform the measurement for each step scpi.Parse "SENS:CORR:COLL:GUID:ACQ
STAN" & CStr(i) Next Dim calset 'Finish the cal and save the calset calset =
scpi.Parse ("SENS:CORR:COLL:GUID:SAVE OFF") Msgbox ("SMC cal saved to cal
register")  
---  
  
* * *

