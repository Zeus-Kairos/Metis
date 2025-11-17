## **Create and Cal a Gain Compression Measurement**

* * *

This VBScript example creates and calibrates a Gain Compression measurement
and performs Compression analysis.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as GCA.vbs. [Learn how to setup and run the
macro](../Using_Macros.htm).

[See Gain Compression
Object.](../COM_Reference/Objects/GainCompression_Object.htm)

option explicit

dim CompLevel, Tolerance, StartFreq, StopFreq, NumFreqs, Scale, LinearPower

dim AcqMode, BackOff, StartPower, StopPower, NumPowers, EnableInterp, CompAlg

dim DwellTime, IFBandwidth, ShowIterations, host, app

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

call SetupGCA( app,_

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

call CalGCA( app )

call Analysis( app )

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'' GCA Setup

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

sub SetupGCA( app, StartFreq, StopFreq, NumFreqs, EnableInterp, Scale,
CompLevel, LinearPower,_

AcqMode, BackOff, StartPower, StopPower, NumPowers, CompAlg, DwellTime,
IFBAndwidth,_

ShowIterations )

dim chan, gca

app.reset

app.CreateCustomMeasurementEx 1, "Gain Compression", "S21", 1

set chan = app.channels(1)

chan.hold 1

app.CreateCustomMeasurementEx 1, "Gain Compression", "CompIn21", 1

app.CreateCustomMeasurementEx 1, "Gain Compression", "DeltaGain21", 1

app.nawindows(1).traces(3).YScale = Scale

app.nawindows(1).traces(3).ReferenceValue = -CompLevel

set gca = chan.CustomChannelConfiguration

gca.InputLinearPowerLevel = LinearPower

gca.AcquisitionMode = AcqMode

gca.CompressionLevel = CompLevel

gca.CompressionBackoff = BackOff

gca.CompressionDeltaX = BackOff

gca.CompressionDeltaY = BackOff \- CompLevel

gca.CompressionAlgorithm = CompAlg

gca.NumberOfPowerPoints = NumPowers

gca.CompressionInterpolation = EnableInterp

gca.SmartSweepSettlingTime = DwellTime

gca.SmartSweepShowIterations = ShowIterations

chan.IFBandwidth = IFBandwidth

chan.DwellTime = DwellTime

chan.StartPower = StartPower

chan.StopPower = StopPower

chan.StartFrequency = StartFreq

chan.StopFrequency = StopFreq

chan.NumberOfPoints = NumFreqs

chan.single 1

end sub

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'' GCA Calibration

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

sub CalGCA( app )

dim chan, CalMgr, GCACal, GCACustomCal, CalSteps, I, CalSet

set chan = app.ActiveChannel

set CalMgr = app.GetCalManager

set GCACal = CalMgr.CreateCustomCalEx(1)

' Configure GCA Guided Cal for the connector types and ECal module that will
be used:

GCACal.Initialize 1, 0

GCACal.ConnectorType(1) = "APC 3.5 female"

GCACal.ConnectorType(2) = "APC 3.5 male"

GCACal.CalKitType(1) = "N4691-60004 ECal"

GCACal.CalKitType(2) = "N4691-60004 ECal"

set GCACustomCal = GCACal.CustomCalConfiguration

GCACustomCal.PowerLevel = 0 ' Set power level for source cal to 0 dBm

CalSteps = GCACal.GenerateSteps

for I = 1 to CalSteps

msgBox GCACal.GetStepDescription(I)

GCACal.AcquireStep(I)

next

CalSet = GCACal.GenerateErrorTerms ' Calculate error terms and apply CalSet to
GCA Channel

chan.CalSet.Save("GCA 2P") ' Save CalSet

msgBox "Done"

end sub

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'' GCA Analysis (PNA Rev A.09.00 or later)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

sub Analysis(app)

Dim meass

Dim ana

Set meass = app.Measurements ' get the measurements

Set ana = meass(1).CustomMeasurementConfiguration 'get the measurement

ana.AnalysisEnable = true ' enable the analysis mode

ana.AnalysisCWFreq = 3e9 ' set the analysis cw frequency to 3GHz

Set ana = meass(2).CustomMeasurementConfiguration

ana.AnalysisEnable = true

ana.AnalysisCWFreq = 4e9

ana.AnalysisXAxis = naPsourceAsXAxis ' set the XAxis as the source power
setting

Set ana = meass(3).CustomMeasurementConfiguration

ana.AnalysisEnable = true

ana.AnalysisIsDiscreteFreq = false ' turn off the discrete frequency option

ana.AnalysisCWFreq = 4.5e9

end sub

* * *

