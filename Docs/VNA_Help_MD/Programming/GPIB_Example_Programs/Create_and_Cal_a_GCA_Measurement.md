## Create and Cal a GCA Measurement

* * *

This VBS program does the following:

  * creates and configures GCA to perform a SMART Sweep

  * performs a calibration using an ECal with 3.5 mm Female on Port A and 3.5 mm Male connectors on Port B

This program can be run as a macro in the VNA. To do this, copy the code into
a text editor file such as Notepad and save on the VNA hard drive as GCA.vbs.
[Learn how to setup and run the macro.](../Using_Macros.md#HowToSetup)

[See the Gain Compression commands](../GP-
IB_Command_Finder/Sense/Gain_Compression.htm)

option explicit

dim CompLevel, Tolerance, StartFreq, StopFreq, NumFreqs, Scale, LinearPower

dim AcqMode, BackOff, StartPower, StopPower, NumPowers, EnableInterp, CompAlg

dim DwellTime, IFBandwidth, ShowIterations, host, app, parser

'' GCA Settings/Values

''

'' Acquisition Mode:

'' naSmartSweep = 0

'' naSweepPowerAtEachFreq2D = 1

'' naSweepFreqAtEachPower2D = 2

''

'' Compression Algorithm

'' naCompressionFromLinearGain = 0

'' naCompressionFromMaximumGain = 1

'' naBackoffCompression = 2

'' naXYCompression = 3

''

'' EndOfSweepOperation

'' naDefaultPowerSet = 0

'' naSetToStartPower = 1

'' naSetToStopPower = 2

'' naSetRFOff = 3

''

CompLevel = 1 ' 1 dB compression level

Tolerance = 0.05 ' SMART Sweep tolerance

StartFreq = 1E9

StopFreq = 9E9

NumFreqs = 201

Scale = 0.1

LinearPower = -20

BackOff = 10 ' Not used for Deviation from linear gain

StartPower = -20

StopPower = 8

NumPowers = 60 ' Not used for SMART Sweep

DwellTime = 0.0005 ' Allow some time for DUT bias/thermal effects

IFBandwidth = 1000 ' Reasonable trace noise at -20 dBm

EnableInterp = False ' Disable interpolation

AcqMode = 0 ' Smart Sweep

CompAlg = 0 ' Deviation from linear gain

ShowIterations = False ' Configure SMART to not show iteration results

dim objargs

set objargs = wscript.Arguments

if (objArgs.Count = 1) then host = objargs(0)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'' Create and Configuration GCA Channel:

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

set app = CreateObject("Agilentpna835x.application")

set parser = app.ScpiStringParser

call SetupGCA( parser,_

StartFreq,_

StopFreq,_

NumFreqs,_

EnableInterp,_

Scale,_

CompLevel,_

LinearPower,_

AcqMode,_

BackOff,_

StartPower,_

StopPower,_

NumPowers,_

CompAlg,_

DwellTime,_

IFBAndwidth,_

ShowIterations )

call CalGCA( parser )

call Analysis( parser )

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'' GCA Setup

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

sub SetupGCA( parser, StartFreq, StopFreq, NumFreqs, EnableInterp, Scale,
CompLevel, LinearPower,_

AcqMode, BackOff, StartPower, StopPower, NumPowers, CompAlg, DwellTime,
IFBAndwidth,_

ShowIterations )

parser.Parse "*RST"

parser.Parse "CALC:PAR:DEL:ALL"

parser.Parse "CALC:CUST:DEF ""S21"",""Gain Compression"",""S21"" "

parser.Parse "DISP:WIND:TRAC1:FEED ""S21"" "

parser.Parse "CALC:PAR:SEL ""S21"" "

parser.Parse "CALC:CUST:DEF ""CompIn21"",""Gain Compression"",""CompIn21"" "

parser.Parse "DISP:WIND:TRAC2:FEED ""CompIn21"" "

parser.Parse "CALC:CUST:DEF ""DeltaGain21"",""Gain
Compression"",""DeltaGain21"" "

parser.Parse "DISP:WIND:TRAC3:FEED ""DeltaGain21"" "

parser.Parse "SENS:SWE:MODE HOLD"

parser.Parse "DISP:WIND1:TRAC3:Y:SCAL:PDIV " & Scale

parser.Parse "DISP:WIND1:TRAC3:Y:RLEV " & -CompLevel

select case AcqMode

case 0 ' SMART Sweep

parser.Parse "SENS:GCS:AMOD SMAR"

case 1 ' 2D Power Sweeps

parser.Parse "SENS:GCS:AMOD PFREQ"

case 2 ' 2D Freq Sweeps

parser.Parse "SENS:GCS:AMOD FPOW"

end select

select case CompAlg

case 0 ' Deviation from linear gain

parser.Parse "SENS:GCS:COMP:ALG CFLG"

case 1 ' Deviation from max gain

parser.Parse "SENS:GCS:COMP:ALG CFMG"

case 2 ' Back Off

parser.Parse "SENS:GCS:COMP:ALG BACK"

case 3 ' XY

parser.Parse "SENS:GCS:COMP:ALG XYCOM"

end select

if EnableInterp then

parser.Parse "SENS:GCS:COMP:INT ON"

else

parser.Parse "SENS:GCS:COMP:INT OFF"

end if

if ShowIterations then

parser.Parse "SENS:GCS:SMAR:SIT ON"

else

parser.Parse "SENS:GCS:SMAR:SIT OFF"

end if

parser.Parse "SENS:GCS:COMP:LEV " & CompLevel

parser.Parse "SENS:GCS:COMP:BACK:LEV " & BackOff

parser.Parse "SENS:GCS:COMP:DELT:X " & BackOff

parser.Parse "SENS:GCS:COMP:DELT:Y " & BackOff

parser.Parse "SENS:GCS:SWE:FREQ:POIN " & NumPowers

parser.Parse "SENS:GCS:SMAR:STIM " & DwellTime

parser.Parse "SENS:BAND " & IFBandwidth

parser.Parse "SENS:SWE:DWEL " & DwellTime

parser.Parse "SOUR:POW:STAR " & StartPower

parser.Parse "SOUR:POW:STOP " & StopPower

parser.Parse "SENS:FREQ:STAR " & StartFreq

parser.Parse "SENS:FREQ:STOP " & StopFreq

parser.Parse "SENS:SWE:POIN " & NumFreqs

parser.Parse "SENS:SWE:MODE SING"

dim str

str = parser.Parse("*OPC?")

end sub

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'' GCA Calibration

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

sub CalGCA( parser )

dim CalSteps, I

parser.parse "SENS:CORR:COLL:GUID:CONN:PORT1 'APC 3.5 female'"

parser.parse "SENS:CORR:COLL:GUID:CONN:PORT2 'APC 3.5 male'"

parser.parse "SENS:CORR:COLL:GUID:CKIT:PORT1 'N4691-60004 ECal'"

parser.parse "SENS:CORR:COLL:GUID:CKIT:PORT2 'N4691-60004 ECal'"

parser.parse "SENS:CORR:GCSetup:POW 0"

parser.parse "SENS:CORR:COLL:GUID:INIT"

CalSteps = parser.parse("SENS:CORR:COLL:GUID:STEP?")

for I = 1 to CalSteps

msgBox parser.parse("SENS:CORR:COLL:GUID:DESC? " & I)

parser.parse("SENS:CORR:COLL:GUID:ACQ STAN"&I)

next

parser.parse "SENS:CORR:COLL:GUID:SAVE"

msgBox "Done"

end sub

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'' GCA Analysis

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

sub Analysis( parser )

'select measurement 1

parser.parse "CALC:PAR:MNUM 1"

parser.parse "CALC:GCM:ANAL:ENABLE 1" 'turn on the analysis mode

parser.parse "CALC:GCM:ANAL:CWFR 1e9" 'set the analysis cw frequency

'select measurement 2

parser.parse "CALC:PAR:MNUM 2"

parser.parse "CALC:GCM:ANAL:ENABLE 1"

parser.parse "CALC:GCM:ANAL:CWFR 2e9"

parser.parse "CALC:GCM:ANAL:XAX PSO" 'set the axis to power settings

'select measurement 3

parser.parse "CALC:PAR:MNUM 3"

parser.parse "CALC:GCM:ANAL:ENABLE 1"

parser.parse "CALC:GCM:ANAL:CWFR 3e9"

parser.parse "CALC:GCM:ANAL:ISD 0" ' set the discrete frequency option to
false

end sub

* * *

