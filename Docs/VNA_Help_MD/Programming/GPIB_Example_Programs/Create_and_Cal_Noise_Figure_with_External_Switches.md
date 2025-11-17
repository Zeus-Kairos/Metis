# Create and Cal Noise Figure with External Switches

This example program creates a Noise Figure that uses external switches, then
calibrates the measurement.

This VBScript program can be run as a macro in the VNA. To do this, copy the
code into a text editor file such as Notepad and save on the VNA hard drive as
NF.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

[See the Noise figure commands.](../GP-IB_Command_Finder/Sense/Noise.md)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

' This section gets the VNA application ' starts the scpi parser, and presets
the VNA windowNum = 1 channelNum = 1 set
pna=CreateObject("AgilentPNA835x.Application") set scpi = pna.ScpiStringParser
' Create noise figure measurement scpi.Parse "SYST:FPR" scpi.Parse "DISP:WIND
ON" 'Put only 1 trace S11 before the cal, because the switch needs to start in
the S-parameter position: scpi.Parse "CALC:CUST:DEF 'MyMeas', 'Noise Figure
Cold Source', 'S11'" scpi.Parse "DISPlay:WINDow1:TRACe1:FEED 'MyMeas'"
scpi.Parse "CALC:PAR:SEL 'MyMeas'" pullEcal = "85052D" 'pullEcal = "N4691D
ECal MY59410340" ' configure channel ConfigureChannel ConfigureNoiseSettings '
perform calibration SetupCalAttributes_Insertable FinishCalibration ' \-----
Support subroutines ------ ' Configure noise channel sub ConfigureChannel
scpi.Parse "SENS:FREQ:START 1GHz" scpi.Parse "SENS:FREQ:STOP 2.5GHz"
scpi.Parse "SENS:SWEEP:POINTS 21" scpi.Parse "SENS:BWID 1.0E3" scpi.Parse
"SENS:SWE:DWEL:SDEL .2" 'increase the power for the Ecal during calibration
scpi.Parse "SOUR:POW -15" end sub ' Configure noise-specific channel settings
sub ConfigureNoiseSettings scpi.Parse "SENS:NOIS:REC NORM" 'Use std PNA
receiver scpi.Parse "SENS:NOIS:AVER:STAT ON" ' turn averaging ON scpi.Parse
"SENS:NOIS:AVER 100" ' noise averaging  scpi.Parse "SENS:NOIS:BWID 1.2MHz" '
noise bandwidth scpi.Parse "SENS:NOIS:TEMP:AMB 301" ' ambient temperature, in
Kelvin 'The two next SCPI commands are here to assign pin to drive external
switches scpi.Parse "CONTrol:CHANnel:INTerface:CONTrol:STATE 1" scpi.Parse
"SENSe:NOISe:CONTrol:HANDler:PIN22:FUNCtion 'NF_SOURCE'" scpi.Parse
"SENSe:NOISe:CONTrol:HANDler:PIN23:FUNCtion 'NF_SOURCE_INVERTED'" end sub sub
SetupCalAttributes_Insertable scpi.Parse "SENS:CORR:COLL:GUID:CONN:PORT1 'APC
3.5 female'" scpi.Parse "SENS:CORR:COLL:GUID:CONN:PORT2 'APC 3.5 female'"
scpi.Parse "SENS:CORR:COLL:GUID:CKIT:PORT1 '" & pullEcal & "'" ' port 1 calkit
scpi.Parse "SENS:CORR:COLL:GUID:CKIT:PORT2 '" & pullEcal & "'" ' port 2 calkit
scpi.Parse "SENS:NOISE:CAL:METHOD 'Scalar'" 'Only power Meter can be use here
as we are using STD receiver scpi.Parse "SENS:NOISE:CAL:RMEThod 'PowerMeter'"
scpi.Parse "SENS:CORR:COLL:GUID:INIT" end sub sub FinishCalibration ' Build
the connection list and acquire the calibration steps =
scpi.Parse("SENS:CORR:COLL:GUID:STEPS?") for i = 1 to steps str =
scpi.Parse("SENS:CORR:COLL:GUID:DESC? " & i) msgbox str scpi.Parse
"SENS:CORR:COLL:GUID:ACQ STAN" & i next scpi.Parse "SENS:CORR:COLL:GUID:SAVE
0" scpi.Parse "SOUR:POW -30" wscript.echo "Calibration complete" end sub  
---

