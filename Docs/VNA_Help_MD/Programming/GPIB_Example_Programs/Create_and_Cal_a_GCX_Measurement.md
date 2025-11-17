# Create and Cal a GCX Measurement

* * *

This VBS program does the following:

  * creates and configures GCX

  * performs a calibration using an ECal with 3.5 mm Female on Port A and 3.5 mm Male connectors on Port B

To run this example without modification you need the following:

  * An ECal module that covers the frequency range of the measurement. You may need to change the ECal model number in the program.

  * A power meter must be available to the VNA. This can be accomplished either by attaching the meter to the VNA via a GPIB cable, or by using SCPI over LAN.

By removing the comments ( ' ) at the start of the BLUE code, it can also do
the following:

  * Use ECal characterizations

  * Specify Mechanical Cal Kits

  * Perform manual ECal orientation.

  * Specify the thru measurement method.

  * Omit the isolation part of the 2-port cal.

  * Perform an LO Power Cal.

  * Set LO power level on External Source (MUST be pre-configured either remotely or [using the GUI](../../System/Configure_an_External_Source.md). [See example program](Configure_an_External_Source.md).)

The SCPI commands in this example are sent over a COM interface using the
SCPIStringParser object. You do NOT need a GPIB connection to run this
example. However, some modification is necessary to make the program run on a
traditional GPIB Interface. For example, during the power meter portion of
this calibration, scpi.Parse will not process a command until the power meter
routine has completed. Traditional GPIB would require a serial polling
technique to ensure the routine has completed before proceeding.

This program can be run as a macro in the VNA. To do this, copy the code into
a text editor file such as Notepad and save on the VNA hard drive as GCX.vbs.
[Learn how to setup and run the macro.](../Using_Macros.md#HowToSetup)

See the [Gain Compression](../GP-IB_Command_Finder/Sense/Gain_Compression.md)
and [Mixer](../GP-IB_Command_Finder/Sense/MIXerSCPI.md) Commands  
  
See other [SCPI example programs](SCPI_Example_Programs.md)

option explicit dim CompLevel, Tolerance, StartFreq, StopFreq, LOFreq,
NumFreqs, Scale, LinearPower dim AcqMode, BackOff, StartPower, StopPower,
NumPowers, EnableInterp, CompAlg dim DwellTime, IFBandwidth, ShowIterations,
host, app, parser, i CompLevel = 1 ' 1 dB compression level Tolerance = 0.05 '
SMART Sweep tolerance NumFreqs = 21 Scale = 0.1 LinearPower = -10 BackOff = 10
' Not used for Deviation from linear gain StartPower = -20 StopPower = 8
NumPowers = 60 ' Not used for SMART Sweep DwellTime = 0.0005 ' Allow some time
for DUT bias/thermal effects IFBandwidth = 1000 ' Reasonable trace noise at
-20 dBm EnableInterp = False ' Disable interpolation AcqMode = 0 ' Smart Sweep
CompAlg = 0 ' Deviation from linear gain ShowIterations = False ' Configure
SMART to not show iteration results dim objargs set objargs =
wscript.Arguments if (objArgs.Count = 1) then host = objargs(0)
''''''''''''''''''''''''''''''''''''''''''''''''''' '' Create and
Configuration GCX Channel: '''''''''''''''''''''''''''''''''''''''''''''''''''
set app = CreateObject("Agilentpna835x.application") set parser =
app.ScpiStringParser ''''''''''''''''''''''''''''''''''''''''''''''''''' ''
GCX Setup ''''''''''''''''''''''''''''''''''''''''''''''''''' parser.Parse
"*RST" parser.Parse "CALC:PAR:DEL:ALL" parser.Parse "CALC:CUST:DEF
""SC21"",""Gain Compression Converters"",""SC21"" " parser.Parse
"DISP:WIND:TRAC1:FEED ""SC21"" " parser.Parse "CALC:PAR:SEL ""SC21"" "
parser.Parse "CALC:CUST:DEF ""CompIn21"",""Gain Compression
Converters"",""CompIn21"" " parser.Parse "DISP:WIND:TRAC2:FEED ""CompIn21"" "
parser.Parse "CALC:CUST:DEF ""DeltaGain21"",""Gain Compression
Converters"",""DeltaGain21"" " parser.Parse "DISP:WIND:TRAC3:FEED
""DeltaGain21"" " parser.Parse "SENS:SWE:MODE HOLD" parser.Parse
"DISP:WIND1:TRAC3:Y:SCAL:PDIV " & Scale parser.Parse "DISP:WIND1:TRAC3:Y:RLEV
" & -CompLevel select case AcqMode case 0 ' SMART Sweep parser.Parse
"SENS:GCS:AMOD SMAR" case 1 ' 2D Power Sweeps parser.Parse "SENS:GCS:AMOD
PFREQ" case 2 ' 2D Freq Sweeps parser.Parse "SENS:GCS:AMOD FPOW" end select
select case CompAlg case 0 ' Deviation from linear gain parser.Parse
"SENS:GCS:COMP:ALG CFLG" case 1 ' Deviation from max gain parser.Parse
"SENS:GCS:COMP:ALG CFMG" case 2 ' Back Off parser.Parse "SENS:GCS:COMP:ALG
BACK" case 3 ' XY parser.Parse "SENS:GCS:COMP:ALG XYCOM" end select if
EnableInterp then parser.Parse "SENS:GCS:COMP:INT ON" else parser.Parse
"SENS:GCS:COMP:INT OFF" end if if ShowIterations then parser.Parse
"SENS:GCS:SMAR:SIT ON" else parser.Parse "SENS:GCS:SMAR:SIT OFF" end if
parser.Parse "SENS:GCS:COMP:LEV " & CompLevel parser.Parse
"SENS:GCS:COMP:BACK:LEV " & BackOff parser.Parse "SENS:GCS:COMP:DELT:X " &
BackOff parser.Parse "SENS:GCS:COMP:DELT:Y " & BackOff parser.Parse
"SENS:GCS:SWE:FREQ:POIN " & NumPowers parser.Parse "SENS:GCS:SMAR:STIM " &
DwellTime parser.Parse "SENS:BAND " & IFBandwidth parser.Parse "SENS:SWE:DWEL
" & DwellTime parser.Parse "SOUR:POW:STAR " & StartPower parser.Parse
"SOUR:POW:STOP " & StopPower parser.Parse "SOUR:POW " & LinearPower
parser.Parse "SENS:SWE:POIN " & NumFreqs ' Mixer settings parser.Parse
"SENS:MIX:INPut:FREQ:MODE SWEPt" parser.Parse "SENS:MIX:INPut:FREQ:STAR 3.6e9"
parser.Parse "SENS:MIX:INPut:FREQ:STOP 3.9e9" parser.Parse
"SENS:MIX:LO:FREQ:MODE FIXED" parser.Parse "SENS:MIX:LO:FREQ:FIX 1e9"
parser.Parse "SENS:MIX:LO:POW 10" parser.Parse "SENS:MIX:OUTP:FREQ:SID LOW"
parser.Parse "SENS:MIX:CALC Output" parser.Parse "SENS:MIX:APPLY" 'First apply
the settings, then set LO Name parser.Parse "SENS:MIX:LO:NAME 'Port 3'"
parser.Parse "SENS:MIX:APPLY" parser.Parse "SENS:MIX:SAVE "C:\Program
Files(x86)\Keysight\Network Analyzer\Documents\Mixer\MyMixer.mxrx"" ' sweep
single parser.Parse "SENS:SWE:MODE SING" dim str str =parser.Parse("*OPC?")
''''''''''''''''''''''''''''''''''''''''''''''''''' '' GCX Calibration
''''''''''''''''''''''''''''''''''''''''''''''''''' '\--------------Perform A
GCX Cal using SMC commands---------------------- 'Specify the connector types
and the cal kits for each of the ports. parser.Parse
"SENS:CORR:COLL:GUID:CONN:PORT1:SEL ""APC 3.5 male""" parser.Parse
"SENS:CORR:COLL:GUID:CONN:PORT2:SEL ""APC 3.5 female""" parser.Parse
"SENS:CORR:COLL:GUID:CKIT:PORT1:SEL ""N4691-60004 ECal""" parser.Parse
"SENS:CORR:COLL:GUID:CKIT:PORT2:SEL ""N4691-60004 ECal""" ' Non-factory
characterizations are specified as follows: 'parser.Parse
"sens:corr:coll:guid:ckit:port2 'N4691-60004 User 1 ECal'" ' When two or more
ECal modules with the same model number are connected ' also specify the
serial number as follows: 'parser.Parse "sens:corr:coll:guid:ckit:port2
'N4691-60004 ECal 01234'" ' When Disk Memory ECal user characterizations are
used, ' specify both the User char and the serial number as follows:
'parser.Parse "sens:corr:coll:guid:ckit:port2 'N4691-60004 MyDskChar ECal
01234'" ' Uncomment the following lines to manually orient ' the ecal port A
connected to VNA port 1 'parser.Parse "SENS:CORR:PREF:ECAL:ORI OFF"
'parser.Parse "SENS:CORR:PREF:ECAL:PMAP ECAL2 ="A1,B2" ' Specify Mechanical
cal kits 'parser.Parse "sens:corr:coll:guid:ckit:port1 '85033D/E'"
'parser.Parse "sens:corr:coll:guid:ckit:port2 '85033D/E'" 'Optional settings
'Specify the thru measurement method. 'Always send an INIT command before the
THRU command. 'parser.Parse "SENS:CORR:COLL:GUID:INIT" 'parser.Parse
"SENS:CORR:COLL:GUID:PATH:TMET 1,2,""UNDEFINED THRU""" 'Omit the isolation
part of the 2-port cal (default behavior). 'parser.Parse
"SENS:CORR:COLL:GUID:ISOL NONE" ' 'Perform LO Power Cal 'parser.Parse
"SENS:CORR:COLL:GUID:SMC:LO1:PCAL 1" **' Set the LO power level for the cal on
an external PSG source.** **' scpi.Parse "SENS:CORR:COLL:GUID:PSEN1:POW:LEV
10,PSG** **'** 'Initialize a Guided calibration. parser.Parse
"SENS:CORR:COLL:GUID:INIT" 'Tell the wizard to generate and report the number
of steps in this cal. Dim steps Dim desc 'Determine the number of steps
required to complete the calibration. steps =parser.Parse
("SENS:CORR:COLL:GUID:STEP?") For i = 1 To steps 'Display the prompt for each
step desc =parser.Parse ("SENS:CORR:COLL:GUID:DESC? " & CStr(i)) MsgBox (desc)
'Perform the measurement for each step parser.Parse "SENS:CORR:COLL:GUID:ACQ
STAN" & CStr(i) Next 'Finish the cal and save the calset parser.Parse
("SENS:CORR:COLL:GUID:SAVE ON") Msgbox ("GCX cal saved to CH1_CALREG")  
---  
  
* * *

