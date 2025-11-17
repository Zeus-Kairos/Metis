# Create and Cal a GCX Measurement

* * *

This VBScript example creates and calibrates a GCX measurement and performs
Compression analysis.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as GCX.vbs. [Learn how to setup and run the
macro](../Using_Macros.htm).

[See Gain Compression
Object](../COM_Reference/Objects/GainCompression_Object.htm) and [Converter
Object](../COM_Reference/Objects/Converter_Object.htm)

option explicit dim CompLevel, Tolerance, StartFreq, StopFreq, LOFreq,
NumFreqs, Scale, LinearPower dim AcqMode, BackOff, StartPower, StopPower,
NumPowers, EnableInterp, CompAlg dim DwellTime, IFBandwidth, ShowIterations,
host, app, parser CompLevel = 1 ' 1 dB compression level Tolerance = 0.05 '
SMART Sweep tolerance StartFreq = 2.5E9 StopFreq = 2.6E9 LOFreq = 1.7E9
NumFreqs = 21 Scale = 0.1 LinearPower = -10 BackOff = 10 ' Not used for
Deviation from linear gain StartPower = -20 StopPower = 8 NumPowers = 60 ' Not
used for SMART Sweep DwellTime = 0.0005 ' Allow some time for DUT bias/thermal
effects IFBandwidth = 1000 ' Reasonable trace noise at -20 dBm EnableInterp =
False ' Disable interpolation AcqMode = 0 ' Smart Sweep CompAlg = 0 '
Deviation from linear gain ShowIterations = False ' Configure SMART to not
show iteration results dim objargs set objargs = wscript.Arguments if
(objArgs.Count = 1) then host = objargs(0)
'\---------------------------------------------------------- ' Create and
Configuration GCX Channel:
'\---------------------------------------------------------- set app =
CreateObject("Agilentpna835x.application") call SetupGCAX( parser,_
StartFreq,_ StopFreq,_ LOFreq,_ NumFreqs,_ EnableInterp,_ Scale,_ CompLevel,_
LinearPower,_ AcqMode,_ BackOff,_ StartPower,_ StopPower,_ NumPowers,_
CompAlg,_ DwellTime,_ IFBAndwidth,_ ShowIterations ) call CalGCAX( parser )
'\---------------------------------------------------------- ' GCAX Setup
'\---------------------------------------------------------- sub SetupGCAX(
parser, StartFreq, StopFreq, LOFreq, NumFreqs, EnableInterp, Scale, CompLevel,
LinearPower,_ AcqMode, BackOff, StartPower, StopPower, NumPowers, CompAlg,
DwellTime, IFBAndwidth,_ ShowIterations ) dim chan, gca app.reset
app.CreateCustomMeasurementEx 1, "Gain Compression Converters", "SC21", 1 set
chan = app.channels(1) dim converter set converter = chan.Converter()
chan.hold 1 app.CreateCustomMeasurementEx 1, "Gain Compression Converters",
"CompIn21", 1 app.CreateCustomMeasurementEx 1, "Gain Compression Converters",
"DeltaGain21", 1 app.nawindows(1).traces(3).YScale = Scale
app.nawindows(1).traces(3).ReferenceValue = -CompLevel set gca =
chan.CustomChannelConfiguration gca.InputLinearPowerLevel = LinearPower
gca.AcquisitionMode = AcqMode gca.CompressionLevel = CompLevel
gca.CompressionBackoff = BackOff gca.CompressionDeltaX = BackOff
gca.CompressionDeltaY = BackOff - CompLevel gca.CompressionAlgorithm = CompAlg
gca.NumberOfPowerPoints = NumPowers gca.CompressionInterpolation =
EnableInterp gca.SmartSweepSettlingTime = DwellTime
gca.SmartSweepShowIterations = ShowIterations chan.IFBandwidth = IFBandwidth
chan.DwellTime = DwellTime chan.StartPower = StartPower chan.StopPower =
StopPower chan.TestPortPower(1) = LinearPower chan.StartFrequency = StartFreq
chan.StopFrequency = StopFreq chan.NumberOfPoints = NumFreqs 'set converter
properties converter.InputRangeMode = 0 ' swept converter.LORangeMode(1) = 1
'fixed converter.OutputRangeMode = 0 'swept converter.InputStartFrequency =
StartFreq converter.InputStopFrequency = StopFreq
converter.LOFixedFrequency(1) = LOFreq converter.LOName(1) = "Port 3"
converter.LOPower(1) = -10 converter.Calculate 2 'calculateOutput chan.Single
1 end sub '\---------------------------------------------------------- ' GCAX
Calibration '\---------------------------------------------------------- sub
CalGCAX( parser ) Dim CalMgr Set CalMgr = app.GetCalManager Dim SMC Set SMC =
CalMgr.CreateCustomCal("SMC") SMC.Initialize 1, 1 SMC.Do2PortEcal = 1 'specify
0 for mechanical cal, 1 for ecal 'use Factory Characterization
SMC.ECALCharacterization(1) = 0 SMC.OmitIsolation = 1 SMC.AutoOrient = 1 ' 1-
forward, 2-reverse, or Both SMC.CalibrationPort = "1" Dim steps steps =
SMC.GenerateSteps Dim i For i = 1 To steps MsgBox SMC.GetStepDescription(i)
SMC.AcquireStep i Next Dim calset calset = SMC.GenerateErrorTerms Msgbox("SMC
Cal Complete!") end sub  
---  
  
* * *

* * *

