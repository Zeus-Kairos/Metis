## Create a Swept IMDX Measurement

* * *

This program configures several Swept IMDx parameters using power sweep. In
this configuration, tone power is swept from -20 dBm to -5 dBm while the
Input, LO, and Output frequencies are fixed as follows:

  * Input center freq= 2.50 GHz

  * Tone Delta freq = 10 MHz (f1 = 2.495 GHz and f2 = 2.505 GHz).

  * LO freq = 2.00 GHz

  * Output freq = 4.50 GHz

This program also allows you to optionally load a .mxr file to perform mixer
setup.

To run this program without error, an external source named 'PSG' must be
connected to drive the LO.

This program can be run as a macro in the VNA. To do this, copy the code into
a text editor file such as Notepad and save on the VNA hard drive as IMDX.vbs.
[Learn how to setup and run the macro.](../Using_Macros.md#HowToSetup)

[See all Swept IMD commands.](../GP-IB_Command_Finder/Sense/IMD.md)

[See all Mixer Setup commands.](../GP-IB_Command_Finder/Sense/MIXerSCPI.md)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

Dim app Dim scpi Dim err ' 'Create / Get the VNA application. Set app =
CreateObject("AgilentPNA835x.Application") Set scpi = app.ScpiStringParser '
'Preset the system scpi.parse "SYST:FPR" scpi.parse "DISP:WIND1:STAT ON" '
'Create an IMDX measurement in Channel 1 and display it as trace 1 in window 1
scpi.parse "CALC1:CUST:DEF 'ch1IMDX', 'Swept IMD Converters', 'PwrMain'"
scpi.parse "DISP:WIND1:TRAC1:FEED 'ch1IMDX'" ' 'Put the channel in trigger
hold scpi.parse "SENS:SWE:MODE HOLD" scpi.parse "SENS:IMD:SWE:TYPE POW" 'Put
the channel in trigger hold and setup all the mixer parameters scpi.parse
"SENS1:SWE:MODE HOLD" scpi.parse "SENS1:IMD:SWE:TYPE POW" scpi.parse
"SENS1:MIX:INP:FREQ:MODE FIXED" scpi.parse "SENS1:MIX:LO:FREQ:MODE FIXED"
scpi.parse "SENS1:MIX:OUTP:FREQ:MODE FIXED" scpi.parse "SENS1:MIX:INP:FREQ:FIX
2500000000" scpi.parse "SENS1:MIX:LO:FREQ:FIX 2000000000" scpi.parse
"SENS1:MIX:OUTP:FREQ:SID HIGH" scpi.parse "SENS1:MIX:CALC OUTP" scpi.Parse
"SENS:MIX:APPLY" 'First apply the settings, then set LO Name scpi.Parse
"SENS:MIX:LO:NAME 'PSG'" scpi.parse "SENS1:MIX:LO:POW 10" scpi.Parse
"SENS:MIX:APPLY" 'Optionally, put the channel in hold and load an 'existing
.mxr file with all the mixer settings 'scpi.parse "SENS1:SWE:MODE HOLD"
'scpi.parse "SENS1:MIX:LOAD 'c:\users\public\network
analyzer\documents/Mixer/IMD/Ch1.mxr'" ' 'Make additional IMD settings
scpi.parse "SENS1:IMD:TPOW:COUP:STAT ON" scpi.parse "SENS1:IMD:TPOW:F1:STAR
-20" scpi.parse "SENS1:IMD:TPOW:F1:STOP -5" scpi.parse "SENS1:IMD:FREQ:DFR:CW
10000000" scpi.parse "SENS1:SWE:POIN 201" scpi.parse "SENS1:imd:ifbw:main
1000" scpi.parse "SENS1:imd:ifbw:imt 500" scpi.parse "SOUR1:POW2:AMPL -5" '
'Create additional measurements in the channel scpi.parse "CALC1:CUST:DEF
'ch1IMDX2', 'Swept IMD Converters', 'IM3'" scpi.parse "DISP:WIND1:TRAC2:FEED
'ch1IMDX2'" scpi.parse "CALC1:CUST:DEF 'ch1IMDX3', 'Swept IMD Converters',
'OIP3'" scpi.parse "DISP:WIND1:TRAC3:FEED 'ch1IMDX3'" scpi.parse
"CALC1:CUST:DEF 'ch1IMDX4', 'Swept IMD Converters', 'IIP3'" scpi.parse
"DISP:WIND1:TRAC4:FEED 'ch1IMDX4'" scpi.parse "CALC1:CUST:DEF 'ch1IMDX5',
'Swept IMD Converters', 'ToneGain'" scpi.parse "DISP:WIND1:TRAC5:FEED
'ch1IMDX5'" ' 'Take a single sweep to apply all stimulus changes scpi.parse
"*cls;*ese 1" scpi.parse "sens1:swe:mode SING;*OPC?" ' 'Check for errors
err=scpi.parse ("SYST:ERR?") MsgBox(err)  
---  
  
* * *

