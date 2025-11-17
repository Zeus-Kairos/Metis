# Create and Cal a Swept IMD Measurement

* * *

This program does the following:

  * Create IMD power and IM3 measurements

  * Set sweep mode to Center Frequency Sweep

  * Calibrate the IMD channel

This program can be run as a macro in the VNA. To do this, copy the code into
a text editor file such as Notepad and save on the VNA hard drive as IMD.vbs.

### See Also

[Learn how to setup and run the macro.](../Using_Macros.md#HowToSetup)

[See the IMD commands.](../GP-IB_Command_Finder/Sense/IMD.md)

[See the IMD Cal commands](../GP-IB_Command_Finder/Sense/Corr_IMD.md)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

option explicit 'declare variables dim SweepMode, StartDeltaFreq,
StopDeltaFreq, NumFreqs, TonePower, CWFreq dim app, hostname, parser '' Sweep
type: '' naIMDToneCWSweep = 0 '' naIMDTonePowerSweep = 1 ''
naIMDToneCenterFreqSweep = 2 '' naIMDDeltaFrequencySweep = 3 ''
naIMDToneSegmentSweep = 4 'init variables SweepMode = 3 ' Sweep DeltaF
StartDeltaFreq = 100e3 StopDeltaFreq = 1e9 NumFreqs = 201 TonePower = -7
CWFreq = 5e9 ' get host name from commandline dim objargs set objargs =
wscript.arguments if(objargs.Count = 1) then hostname = objargs(0) set app =
CreateObject("Agilentpna835x.application", hostname) set parser =
app.ScpiStringParser call SetupIMD call CalIMD
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' ''
Create and Configure IMD channel
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' sub
SetupIMD parser.Parse "*RST" parser.Parse "CALC:PAR:DEL:ALL" parser.Parse
"CALC:CUST:DEF 'PwrMain','Swept IMD', 'PwrMain'" ' create PwrMain measurement
parser.Parse "DISP:WIND:TRAC1:FEED 'PwrMain'" parser.Parse "CALC:PAR:SEL
'PwrMain'" parser.Parse "CALC:CUST:DEF 'IM3', 'Swept IMD', 'IM3'" ' create IM3
measurement parser.Parse "DISP:WIND:TRAC2:FEED 'IM3'" parser.Parse
"SENS:SWE:MODE HOLD" ' set sweep mode select case SweepMode case 0 ' CW sweep
parser.Parse "SENS:IMD:SWE:TYPE CW" case 1 ' Power Sweep parser.Parse
"SENS:IMD:SWE:TYPE POW" case 2 ' sweep Fc parser.Parse "SENS:IMD:SWE:TYPE
FCEN" case 3 ' sweep DeltaF parser.Parse "SENS:IMD:SWE:TYPE DFR" case 4 '
segment sweep parser.Parse "SENS:IMD:SWE:TYPE SEGM" end select parser.Parse
"SENS:IMD:FREQ:FCEN " & CWFreq ' Frequency Center parser.Parse
"SENS:IMD:FREQ:DFR:STAR " & startDeltaFreq ' Delta Frequency Start
parser.Parse "SENS:IMD:FREQ:DFR:STOP " & stopDeltaFreq ' Delta Frequency Stop
parser.Parse "SENS:IMD:TPOW:F1 " & TonePower ' F1 power parser.Parse
"SENS:IMD:TPOW:F2 " & TonePower ' F2 power parser.Parse "SENS:SWE:POIN " &
NumFreqs parser.Parse "SENS:SWE:MODE SING" end sub  sub CalIMD 'Configure IMD
GuidedCal for the connector types and ECal module that will be used '
Substitute appropriate connector type and ECal identification strings here
parser.Parse "SENS:CORR:COLL:GUID:CONN:PORT1 'APC 3.5 female'" parser.Parse
"SENS:CORR:COLL:GUID:CONN:PORT2 'APC 3.5 male'" parser.Parse
"SENS:CORR:COLL:GUID:CKIT:PORT1 'N4693-60001 User 2 ECal 00012'" parser.Parse
"SENS:CORR:COLL:GUID:CKIT:PORT2 'N4693-60001 User 2 ECal 00012'" ' imd custom
settings ' Set the Power Level at the power sensor to be used in calibration
parser.Parse "SENS:CORR:IMD:POW 0" ' Specify the connector type of the power
sensor. If there is an adapter between ' the input port and the power sensor,
specify the connector type here, and set ' the appropriate cal kit type for
the connector so that extra calibration can be ' performed. To skip the
calibration for the adapter, set the connection type to "Ignored" ' i.e.:
SENS:CORR:IMD:SENS:CONN 'Ignored' parser.Parse "SENS:CORR:IMD:SENS:CONN 'APC
3.5 female'" 'set power sensor connector type parser.Parse
"SENS:CORR:IMD:SENS:CKIT 'N4693-60001 User 2 ECal 00012'" ' set power sensor
calkit type ' Set the Max product to calibrate, valid values are 3, 5, 7, and
9 parser.Parse "SENS:CORR:IMD:MPR 3" ' Set the calibration Frequencies, can
choose between calibrate only at center Frequencies (CENT) ' or calibrate at
all frequencies (ALL). parser.Parse "SENS:CORR:IMD:CAL:FREQ ALL" 'Include 2nd
order product in calibration parser.Parse "SENS:CORR:IMD:SORD:INCL 1"
parser.Parse "SENS:CORR:COLL:GUID:INIT" dim CalSteps, I CalSteps =
parser.Parse("SENS:CORR:COLL:GUID:STEP?") for I = 1 to CalSteps msgBox
parser.Parse("SENS:CORR:COLL:GUID:DESC? " & I)
parser.Parse("SENS:CORR:COLL:GUID:ACQ STAN" & I) next parser.Parse
"SENS:CORR:COLL:GUID:SAVE" msgBox "IMD Cal Done" end sub  
---

