# Create and Cal a VMC Measurement

* * *

The following example program sets up a 1-stage mixer, then performs a full
VMC calibration.

By removing the comments ( ' ) at the start of the BLUE code, it can also do
the following:

  * Load a mixer setup file

  * Use an ECal Module

  * Perform manual ECal orientation

  * Load a Mixer Characterization

### See Also

[Setup Converter commands](../GP-IB_Command_Finder/Sense/MIXerSCPI.md)

[VMC Cal commands](../GP-IB_Command_Finder/Sense/CorrCollGuidVMC.md)

[All Guided Cal commands](../GP-IB_Command_Finder/Sense/CorrGuided.md)

Example - [Perform a Mixer Characterization
ONLY](Perform_a_VMC_Mixer_Characterization.htm)

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as VMC.vbs. [Learn how to setup and run the
macro](../Using_Macros.htm).

Dim app Dim scpi ' Create / Get the VNA application. Set app =
CreateObject("AgilentPNA835x.Application") Set scpi = app.ScpiStringParser
scpi.Parse "SYSTem:PRESet" 'Create a Vector Mixer Measurement 'First, delete
all measurements on the channel scpi.Parse "CALC:PAR:DEL:ALL" 'Create a
forward scalar mixer measurement and configure it in channel 1. 'The first
parameter is a unique identifying string to allow subsequent 'commands to be
directed at this specific measurement. scpi.Parse "CALC:CUST:DEF 'My VC21',
'Vector Mixer/Converter', 'VC21'" 'Setup the new measurement as the 2nd trace
in the active window scpi.Parse "DISP:WIND:TRAC2:FEED 'My VC21'" 'Make the new
trace the active measurement scpi.Parse "CALC:PAR:SEL 'My VC21'" 'The
parameters of the mixer measurement can now be configured. 'This can be done
by either using the SENS:MIX commands 'for each of the parameters or by
loading a mixer setup file. 'Uncomment the following line to load a mixer
setup file. The path 'name for the mixer file may be loaded from other mapped
drives. 'scpi.Parse "SENS:MIXer:Load 'c:\users\public\network
analyzer\documents/Mixer/MyMixer.mxr'" ' Setup Stimulus ' Points and IFBW are
channel settings scpi.Parse "SENS:SWEep:POINts 21" scpi.Parse "SENS:BANDwidth
1e3" ' The rest are mixer settings scpi.Parse "SENS:MIX:LO:FREQ:MODE SWEPt"
scpi.Parse "SENS:MIX:INPut:FREQ:STAR 3.6e9" scpi.Parse
"SENS:MIX:INPut:FREQ:STOP 3.9e9" scpi.Parse "SENS:MIX:LO:FREQ:MODE FIXED"
scpi.Parse "SENS:MIX:LO:FREQ:FIX 1e9" scpi.Parse "SENS:MIX:LO:POW 10"
scpi.Parse "SENS:MIX:OUTP:FREQ:SID LOW" scpi.Parse "SENS:MIX:CALC Output"
scpi.Parse "SENS:MIX:LO:NAME 'Port 3'" scpi.Parse "SENS:MIX:APPLY" ' Perform
Cal ' Define the DUT connectors for at ports 1 and 2 of the VNA scpi.Parse
"sens:corr:coll:guid:conn:port1 'APC 3.5 female'" scpi.Parse
"sens:corr:coll:guid:conn:port2 'APC 3.5 male'" scpi.Parse
"sens:corr:coll:guid:conn:port3 'Not used'" scpi.Parse
"sens:corr:coll:guid:conn:port4 'Not used'" ' Specify Mechanical cal kits
scpi.Parse "sens:corr:coll:guid:ckit:port1 '85033D/E'" scpi.Parse
"sens:corr:coll:guid:ckit:port2 '85033D/E'" ' Specify an ECal module the same
way 'scpi.Parse "sens:corr:coll:guid:ckit:port1 'N4691-60004 ECal'"
'scpi.Parse "sens:corr:coll:guid:ckit:port2 'N4691-60004 ECal'" ' Non-factory
characterizations are specified as follows: 'scpi.Parse
"sens:corr:coll:guid:ckit:port2 'N4691-60004 User 1 ECal'" ' When two or more
ECal modules with the same model number are connected ' also specify the
serial number as follows: 'scpi.Parse "sens:corr:coll:guid:ckit:port2
'N4691-60004 ECal 01234'" ' When Disk Memory ECal user characterizations are
used, ' specify both the User char and the serial number as follows:
'scpi.Parse "sens:corr:coll:guid:ckit:port2 'N4691-60004 MyDskChar ECal
01234'" ' ' By default, VMC requires the measurement of a Calibration Mixer. '
To determine the conversion loss of the calmixer, the cal wizard ' will add a
step to perform a 1 port cal at the output of the mixer. ' The following
commands opt to perform the mixer ' characterization using a cal kit.
scpi.Parse "SENS:CORR:COLL:GUID:VMC:MIX:CHAR:CAL:OPT CKIT" ' Define the DUT
connectors for the output of the characterization mixer ' Use (logical) Port
3. If it is already used by the DUT, ' then specify port 4. scpi.Parse
"sens:corr:coll:guid:conn:port3 'APC 3.5 male'" ' Specify the mechanical cal
kit for port 3 scpi.Parse "sens:corr:coll:guid:ckit:port3 '85033D/E'" ' To
avoid performing the 1-port cal, provide the cal wizard with a ' mixer
characterization file. Uncomment the following line to ' specify the
characterization file. This S2P file will be read. 'scpi.Parse
"SENS:CORR:COLL:GUID:VMC:MIX:CHAR:CAL:OPT FILE,'c:\users\public\network
analyzer\documents/MyMixer.s2p'" ' ECal orientation ' By default, auto
orientation of the ecal module is performed ' Uncomment the following lines to
manually orient the ecal 'scpi.Parse "SENS:CORR:PREF:ECAL:ORI OFF" ' for
2-port portion, ecal port A connected to VNA port 1 'scpi.Parse
"SENS:CORR:PREF:ECAL:PMAP ECAL2 ="A1,B2" 'for mixer char, ecal port A
connected to cal mixer output 'scpi.Parse
"SENS:CORR:COLL:GUID:VMC:MIXer:ECAL:PORTmap 1,"A1" ' the main calibration loop
' a description for the connection instructions is read ' and then the
standard is acquired dim steps, strPrompt scpi.Parse
"sens:corr:coll:guid:init" steps=scpi.Parse ("sens:corr:coll:guid:steps?")
wscript.echo "Number of Steps = " \+ cstr(steps) if (steps > 0) then '
otherwise an error condition occurred for i = 1 to steps strPrompt =
scpi.Parse ("sens:corr:coll:guid:desc? " \+ CStr(i)) MsgBox strPrompt,
vbOKOnly, step scpi.Parse ("sens:corr:coll:guid:acq STAN" \+ CStr(i)) next
scpi.Parse "sens:corr:coll:guid:save" MsgBox ("Cal is done!") end if  
---  
  
* * *

* * *

