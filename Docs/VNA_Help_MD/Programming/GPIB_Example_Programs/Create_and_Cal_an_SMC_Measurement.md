# Create and Cal an SMC Measurement

* * *

This VB Script example creates and calibrates a scalar mixer measurement.

To run this example without modification you need the following:

  * An ECal module that covers the frequency range of the measurement.

  * A power meter must be available to the VNA. This can be accomplished either by attaching the meter to the VNA via a GPIB cable, or by using SCPI over LAN.

By removing the comments ( ' ) at the start of the BLUE code, it can also do
the following:

  * Load a mixer setup file

  * Use ECal characterizations

  * Specify Mechanical Cal Kits

  * Perform manual ECal orientation.

  * Specify the thru measurement method.

  * Omit the isolation part of the 2-port cal.

  * Perform an LO Power Cal.

  * Set LO power level on External Source (MUST be pre-configured either remotely or [using the GUI](../../System/Configure_an_External_Source.md). [See example program](Configure_an_External_Source.md).)

  * Enable and configure phase measurements

The SCPI commands in this example are sent over a COM interface using the
SCPIStringParser object. You do NOT need a GPIB connection to run this
example. However, some modification is necessary to make the program run on a
traditional GPIB Interface. For example, during the power meter portion of
this calibration, scpi.Parse will not process a command until the power meter
routine has completed. Traditional GPIB would require a [serial polling
technique](Status_Reporting.htm) to ensure the routine has completed before
proceeding.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as SMC.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm)

Dim app Dim scpi ' Create / Get the VNA application. Set app =
CreateObject("AgilentPNA835x.Application") Set scpi = app.ScpiStringParser '
Create a Scalar Mixer Forward Measurement 'First, delete all measurements on
the channel scpi.Parse "CALC:PAR:DEL:ALL" 'Create a forward scalar mixer
measurement and configure it in 'channel 1. The first parameter is a unique
'identifying string (specified by the user) to allow subsequent 'commands to
be directed at this specific measurement. scpi.Parse "CALC:CUST:DEF 'My SC21',
'Scalar Mixer/Converter', 'SC21'" 'Setup the new measurement in the active
window scpi.Parse "DISP:WIND:TRAC:FEED 'My SC21'" 'Make the new trace the
active measurement scpi.Parse "CALC:PAR:SEL 'My SC21'" 'The parameters of the
mixer measurement can now be configured. 'This can be done by either using the
SENS:MIX commands 'for each of the parameters or by loading a mixer setup
file. 'Uncomment the following line to load a mixer setup file. The path name
'for the mixer file may be loaded from other mapped drives. 'scpi.Parse
"SENS:MIXer:Load 'c:\users\public\network
analyzer\documents/Mixer/MyMixer.mxr'" ' Setup Stimulus ' Points and IFBW are
channel settings scpi.Parse "SENS:SWEep:POINts 21" scpi.Parse "SENS:BANDwidth
1e3" ' Mixer settings scpi.Parse "SENS:MIX:INPut:FREQ:MODE SWEPt" scpi.Parse
"SENS:MIX:INPut:FREQ:STAR 3.6e9" scpi.Parse "SENS:MIX:INPut:FREQ:STOP 3.9e9"
scpi.Parse "SENS:MIX:LO:FREQ:MODE FIXED" scpi.Parse "SENS:MIX:LO:FREQ:FIX 1e9"
scpi.Parse "SENS:MIX:LO:POW 10" scpi.Parse "SENS:MIX:OUTP:FREQ:SID LOW"
scpi.Parse "SENS:MIX:CALC Output" scpi.Parse "SENS:MIX:APPLY" 'First apply the
settings, then set LO Name scpi.Parse "SENS:MIX:LO:NAME 'Port 3'" scpi.Parse
"SENS:MIX:APPLY" scpi.Parse "SENS:MIX:SAVE "C:\Program
Files(x86)\Keysight\Network Analyzer\Documents\Mixer\MyMixer.mxrx""
'\--------------Perform A Scalar Mixer Calibration----------------------
'Specify the connector types and the cal kits for each of the ports.
scpi.Parse "SENS:CORR:COLL:GUID:CONN:PORT1:SEL ""APC 3.5 male""" scpi.Parse
"SENS:CORR:COLL:GUID:CONN:PORT2:SEL ""APC 3.5 female""" scpi.Parse
"SENS:CORR:COLL:GUID:CKIT:PORT1:SEL ""N4691-60004 ECal""" scpi.Parse
"SENS:CORR:COLL:GUID:CKIT:PORT2:SEL ""N4691-60004 ECal""" ' Non-factory
characterizations are specified as follows: 'scpi.Parse
"sens:corr:coll:guid:ckit:port2 'N4691-60004 User 1 ECal'" ' When two or more
ECal modules with the same model number are connected ' also specify the
serial number as follows: 'scpi.Parse "sens:corr:coll:guid:ckit:port2
'N4691-60004 ECal 01234'" ' When Disk Memory ECal user characterizations are
used, ' specify both the User char and the serial number as follows:
'scpi.Parse "sens:corr:coll:guid:ckit:port2 'N4691-60004 MyDskChar ECal
01234'" ' Uncomment the following lines to manually orient ' the ecal port A
connected to VNA port 1 'scpi.Parse "SENS:CORR:PREF:ECAL:ORI OFF" 'scpi.Parse
"SENS:CORR:PREF:ECAL:PMAP ECAL2 ="A1,B2" ' Specify Mechanical cal kits
'scpi.Parse "sens:corr:coll:guid:ckit:port1 '85033D/E'" 'scpi.Parse
"sens:corr:coll:guid:ckit:port2 '85033D/E'" 'Optional settings 'Specify the
thru measurement method. 'Always send an INIT command before the Thru command.
'scpi.Parse "SENS:CORR:COLL:GUID:INIT" 'scpi.Parse
"SENS:CORR:COLL:GUID:PATH:TMET 1,2,""UNDEFINED THRU""" 'Omit the isolation
part of the 2-port cal (default behavior). 'scpi.Parse
"SENS:CORR:COLL:GUID:ISOL NONE" ' 'Perform LO Power Cal 'scpi.Parse
"SENS:CORR:COLL:GUID:SMC:LO1:PCAL 1" **' Set the LO power level for the cal on
an external PSG source.** **' scpi.Parse "SENS:CORR:COLL:GUID:PSEN1:POW:LEV
10,PSG** ' 'Enable and configure Phase measurements 'scpi.Parse
"SENS:MIX:PHAS 1" 'scpi.Parse "SENS:MIX:NORM:POIN 1" 'Using Fixed delay
'scpi.Parse "SENS:CORR:COLL:GUID:SMC:PHAS:METH FIX" 'scpi.Parse
"SENS:CORR:COLL:GUID:SMC:PHAS:DEL 12e-9" 'Initialize an SMC guided
calibration. scpi.Parse "SENS:CORR:COLL:GUID:INIT" 'Tell the wizard to
generate and report the number of steps in this cal. Dim steps Dim desc
'Determine the number of steps required to complete the calibration. steps =
scpi.Parse ("SENS:CORR:COLL:GUID:STEP?") For i = 1 To steps 'Display the
prompt for each step desc = scpi.Parse ("SENS:CORR:COLL:GUID:DESC? " &
CStr(i)) MsgBox (desc) 'Perform the measurement for each step scpi.Parse
"SENS:CORR:COLL:GUID:ACQ STAN" & CStr(i) Next 'Finish the cal and save the
calset scpi.Parse ("SENS:CORR:COLL:GUID:SAVE ON") Msgbox ("SMC cal saved to
CH1_CALREG")  
---  
  
* * *

