# Create and Cal a Swept IMD Measurement

* * *

This VBScript example creates IMD power and IM3 measurements, sets sweep mode
to Center Frequency Sweep, and performs an IMD cal.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as IMD.vbs.

You can see the VB Script program on the VNA that produces an IM spectrum
channel from the Marker function at C:\Program Files(x86)\Keysight\Network
Analyzer\Applications\IMD\IMD.VBS.

[Learn how to setup and run the macro](../Using_Macros.md).

[See SweptIMD Object.](../COM_Reference/Objects/SweptIMD_Object.md)

option explicit 'declare variables dim SweepMode, StartDeltaFreq,
StopDeltaFreq, NumFreqs, TonePower, CWFreq dim app, hostname '' Sweep type: ''
naIMDToneCWSweep = 0 '' naIMDTonePowerSweep = 1 '' naIMDToneCenterFreqSweep =
2 '' naIMDDeltaFrequencySweep = 3 '' naIMDToneSegmentSweep = 4 'init variables
SweepMode = 3 ' Sweep DeltaF StartDeltaFreq = 100e3 StopDeltaFreq = 1e9
NumFreqs = 201 TonePower = -7 CWFreq = 5e9 ' get host name from commandline
dim objargs set objargs = wscript.arguments if(objargs.Count = 1) then
hostname = objargs(0) set app = CreateObject("Agilentpna835x.application",
hostname) call SetupIMD call CalIMD
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' ''
Create and Configure IMD channel
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' sub
SetupIMD dim chan, imd app.reset ' Create IMD measurements
app.CreateCustomMeasurementEx 1, "Swept IMD", "PwrMain", 1
app.CreateCustomMeasurementEx 1, "Swept IMD", "IM3", 1 set chan =
app.channels(1) chan.hold 1 set imd = chan.CustomChannelConfiguration
imd.SweepType = SweepMode imd.FrequencyCenter = CWFreq imd.DeltaFrequencyStart
= StartDeltaFreq imd.DeltaFrequencyStop = StopDeltaFreq imd.TonePower(0) =
TonePower 'F1 power imd.TonePower(1) = TonePower 'F2 power chan.NumberOfPoints
= NumFreqs chan.single 1 end sub  sub CalIMD dim chan, CalMgr, IMDCal,
IMDCustomCal, CalSteps, I, CalSet set chan = app.ActiveChannel set CalMgr =
app.GetCalManager set IMDCal = CalMgr.CreateCustomCalEx(1) 'Configure IMD
GuidedCal for the connector types and ECal module that will be used '
Substitute appropriate connector type and ECal identification strings here
IMDCal.Initialize 1, true 'channel number is 1 IMDCal.ConnectorType(1) = "APC
3.5 female" IMDCal.ConnectorType(2) = "APC 3.5 male" IMDCal.CalKitType(1) =
"N4693-60001 User 2 ECal 00012" IMDCal.CalKitType(2) = "N4693-60001 User 2
ECal 00012" ' IMD Custom settings set IMDCustomCal =
IMDCal.CustomCalConfiguration ' Set the Power Level at the power sensor to be
used in calibration IMDCustomCal.PowerLevel = 0 ' Specify the connector type
of the power sensor. If there is an adapter between ' the input port and the
power sensor, specify the connector type here, and set ' the appropriate cal
kit type for the connector so that extra calibration can be ' performed. To
skip the calibration for the adapter, set PowerSensorConnectorType to
"Ignored" ' i.e.: IMDCustomCal.PowerSensorConnectorType = "Ignored"
IMDCustomCal.PowerSensorConnectorTYpe = "APC 3.5 female"
IMDCustomCal.PowerSensorCalKitType = "N4693-60001 User 2 ECal 00012" ' Set the
Max product to calibrate, valid values are 3, 5, 7, and 9
IMDCustomCal.MaxProduct = 3 ' Set the calibration Frequencies, can choose
between calibrate only at center Frequencies (0) ' or calibrate at all
frequencies (1). IMDCustomCal.CalibrationFrequencies = 1 'Include 2nd order
product in calibration IMDCustomCal.Include2ndOrderProduct = true CalSteps =
IMDCal.GenerateSteps for I = 1 to CalSteps msgBox IMDCal.GetStepDescription(I)
IMDCal.AcquireStep(I) next CalSet = IMDCal.GenerateErrorTerms msgBox "IMD Cal
Done" end sub  
---  
  
* * *

  

