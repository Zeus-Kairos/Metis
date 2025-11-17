# Create and Cal an NFX Measurement

* * *

This program does the following:

  * Setup a Noise Figure SC21 Measurement

  * Calibrate Noise Figure channel

  * Optional - Configure for an Embedded LO

To run this program, make the following edits, highlighted in yellow:

  * Set hostname to your VNA computer name

  * Set tunerECal and pullECal to your ECal model and info

  * Set ENR to correct file name and location

  * Set connector types for ECal, power sensor, and noise source

This program can be run as a macro in the VNA. To do this, copy the code into
a text editor file such as Notepad and save on the VNA hard drive as NFX.vbs.
[Learn how to setup and run the macro.](../Using_Macros.md#HowToSetup)

### See SCPI commands

[Calc:Custom command](../GP-IB_Command_Finder/Calculate/Custom.md)

[Noise Figure commands](../GP-IB_Command_Finder/Sense/Noise.md)

[Mixer commands](../GP-IB_Command_Finder/Sense/MIXerSCPI.md)

[Embedded LO commands](../GP-IB_Command_Finder/Sense/MixrEmbedLO.md)

[Guided Cal commands](../GP-IB_Command_Finder/Sense/CorrGuided.md)

[Noise Cal commands](../GP-
IB_Command_Finder/Sense/Sense_Correction.htm#NoiseENRDeemb)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

option explicit dim app dim hostname dim parser hostname = "MyPNA" set app =
CreateObject("Agilentpna835x.application", hostname) set parser =
app.ScpiStringParser ' ecal and noise tunner dim tunerEcal dim sParamECal
tunerECal = "N4691-60003 ECal 00591" sParamECal = "N4693-60001 User 2 ECal
00012" ' ENR file dim ENRFile ENRFile = "C:\Program
Files(x86)\Keysight\Network Analyzer\Noise\346C_44420601.enr" call SetupNFX
'optional if not doing embedded LO 'call SetupEmbeddedLO call CalNFX sub
SetupNFX 'Create NF and SC21 traces parser.Parse "*RST" parser.Parse
"CALC:PAR:DEL:ALL" parser.Parse "CALC:CUST:DEF 'NF', 'Noise Figure
Converters', 'NF' " parser.Parse "DISP:WIND:TRAC1:FEED 'NF'" parser.Parse
"CALC:CUST:DEF 'SC21', 'Noise Figure Converters', 'SC21' " parser.Parse
"DISP:WIND:TRAC2:FEED 'SC21' " parser.Parse "SENS:SWE:MODE SING" 'set channel
properties ' set sweep type to linear sweep parser.Parse "SENS:SWE:TYPE LIN" '
set number of points parser.Parse "SENS:SWE:POIN 101" ' set IFbandwidth
parser.Parse "SENS:BWID 1e3" 'set nfx properties ' turn averaging on
parser.Parse "SENS:NOIS:AVER:STAT ON" ' noise averaging factor parser.Parse
"SENS:NOIS:AVER 40" ' noise tuner ecal module parser.Parse "SENS:NOIS:TUN:ID
'" & tunerECal & "' " ' noise tuner input parser.Parse "SENS:NOIS:TUN:INP 'B'
" ' noise tuner output parser.Parse "SENS:NOIS:TUN:OUTP 'A' " ' noise
bandwidth parser.Parse "SENS:NOIS:BWID 8e6" ' low gain of noise receiver
parser.Parse "SENS:NOIS:GAIN 0" ' sweep single parser.Parse "SENS:SWE:MODE
SING" ' Mixer settings parser.Parse "SENS:MIX:INPut:FREQ:MODE SWEPt"
parser.Parse "SENS:MIX:INPut:FREQ:STAR 3.6e9" parser.Parse
"SENS:MIX:INPut:FREQ:STOP 3.9e9" parser.Parse "SENS:MIX:LO:FREQ:MODE FIXED"
parser.Parse "SENS:MIX:LO:FREQ:FIX 1e9" parser.Parse "SENS:MIX:LO:POW 10"
parser.Parse "SENS:MIX:OUTP:FREQ:SID LOW" parser.Parse "SENS:MIX:CALC Output"
parser.Parse "SENS:MIX:APPLY" 'First apply the settings, then set LO Name
parser.Parse "SENS:MIX:LO:NAME 'Port 3'" parser.Parse "SENS:MIX:APPLY"
parser.Parse "SENS:MIX:SAVE "C:\Program Files(x86)\Keysight\Network
Analyzer\Documents\Mixer\MyMixer.mxrx"" ' sweep single parser.Parse
"SENS:SWE:MODE SING" end sub sub CalNFX ' dut connector parser.Parse
"SENS:CORR:COLL:GUID:CONN:PORT1 'APC 3.5 female'" parser.Parse
"SENS:CORR:COLL:GUID:CONN:PORT2 'APC 3.5 female'" ' port calkits parser.Parse
"SENS:CORR:COLL:GUID:CKIT:PORT1 '" & sParamECal & "' " parser.Parse
"SENS:CORR:COLL:GUID:CKIT:PORT2 '" & sParamECal & "' " ' power sensor
connector parser.Parse "SENS:CORR:COLL:GUID:PSEN1:CONN 'APC 3.5 female'" '
power sensor adapter calkit parser.Parse "SENS:CORR:COLL:GUID:PSEN1:CKIT '" &
sParamECal & "' " ' disable LO power cal parser.Parse
"SENS:CORR:COLL:NOIS:LO:PCAL 0" ' power calibration power level parser.Parse
"SENS:CORR:COLL:GUID:PSEN1:POW:LEV -20" ' noise source connector parser.Parse
"SENS:NOIS:SOUR:CONN 'APC 3.5 male'" ' noise source adapter cal calkit
parser.Parse "SENS:NOIS:SOUR:CKIT '" & sParamECal & "' " ' cal method
parser.Parse "SENS:NOIS:CAL:METH 'Vector'" ' ENR file parser.Parse
"SENS:NOIS:ENR:FIL '" & ENRFile & "' " ' set force both adapter cals de-embed
to false parser.Parse "SENS:CORR:COLL:NOIS:ENR:ADAP:DEEM 0" parser.Parse
"SENS:CORR:COLL:NOIS:PSEN:ADAP:DEEM 0" ' initialize guided cal parser.Parse
"SENS:CORR:COLL:GUID:INIT" ' step through calsteps dim steps steps =
parser.Parse("SENS:CORR:COLL:GUID:STEP?") dim i, str for i = 1 to steps str =
parser.Parse("SENS:CORR:COLL:GUID:DESC? " & i) msgbox str parser.Parse
"SENS:CORR:COLL:GUID:ACQ STAN" & i next parser.Parse "SENS:CORR:COLL:GUID:SAVE
0" parser.Parse "SENS:SWE:MODE CONT" end sub sub SetupEmbeddedLO ' embedded LO
properties ' normalize point parser.Parse "SENS:MIX:ELO:NORM:POIN 101" ' set
tuning mode to broadband and precise parser.Parse "SENS:MIX:ELO:TUN:MODE BRO"
' tuning ifbw parser.Parse "SENS:MIX:ELO:TUN:IFBW 3e4" ' max tuning iterations
parser.Parse "SENS:MIX:ELO:TUN:ITER 5" ' tuning tolerance parser.Parse
"SENS:MIX:ELO:TUN:TOL 1" ' tuning interval parser.Parse "SENS:MIX:ELO:TUN:INT
1" ' turn on ELO parser.Parse "SENS:MIX:ELO:STAT 1" ' sweep single
parser.Parse "SENS:SWE:MODE SING" end sub  
---  
  
* * *

