# Perform a Cal All Channels Calibration

* * *

This example sets up an SMC channel and a standard channel. It then performs a
'Cal All Channels' calibration which calibrates both channels.

Note: The example does NOT modify any path configuration settings.

### See Also

[CalibrateAllChannels
Object](../COM_Reference/Objects/CalibrateAllChannels_Object.htm)

[Converter Object](../COM_Reference/Objects/Converter_Object.md)

[GuidedCalibration
Object](../COM_Reference/Objects/GuidedCalibration_Object.htm)

[Learn about Cal All](../../S3_Cals/Calibrate_All_Channels.md)

[See other COM Examples](COM_Example_Intro.md)

'Access the CalAllChannels object Dim app Set app =
CreateObject("AgilentPNA835x.Application") Dim mgr Set mgr = app.GetCalManager
'Preset VNA app.Preset '********** Setup Channel 1, Window 1 ********** ' Get
a handle to the preset channel 1 set meas1=app.ActiveMeasurement set
chan1=app.ActiveChannel set win1=app.ActiveNAWindow 'Modify stimulus settings
'Set IF Bandwidth to 1kHz chan1.IFBandwidth = 1e3 'Set Center and Span Freq's
to 1 GHz chan1.CenterFrequency = 1e9 chan1.FrequencySpan = 1e9 'Set number of
points to 11 chan1.NumberOfPoints = 11 ' '********** Setup SMC in Channel 2 in
new window********** app.CreateCustomMeasurementEx 2, "Scalar
Mixer/Converter","SC21",2 Set smcChan = app.ActiveChannel
smcChan.NumberOfPoints = 11 smcChan.IFBandwidth = 1e3 ' the rest are Mixer
settings dim mixer set mixer = app.ActiveMeasurement mixer.InputRangeMode = 0
'swept Input mixer.InputStartFrequency = 3.6e9 mixer.InputStopFrequency =
3.9e9 mixer.LORangeMode(1) = 1 'fixed LO mixer.LoFixedFrequency(1) = 1e9
mixer.LOPower(1) = 10 mixer.LOName(1) = "Port 3" mixer.OutputSideband = 1 'Low
side mixer.Calculate 2 'Calc Output mixer.Apply ' '********** Setup CalAll
Channel Dim CalAll Set CalAll = mgr.CalibrateAllChannels 'Reset Cal All
settings CalAll.Reset 'Select the channels to cal 'VMC channels are not
supported by Cal All. CalAll.Channels = Array(1,2) 'Set IFBW CalAll.IFBW = 1e3
'Set power level for port 1 CalAll.PowerLevel(1) = 0 'Set CalSet prefix. The
channel number is appended to 'the User Cal set for each channel. 'If you
dont set this, only Cal Registers will be generated. calAll.UserCalsetPrefix
= "MyCalAll" ' Read unique Cal settings for Cal All channels props =
calAll.PropertyNames msg = "calAll.PropertyNames:" & vbCrLf For i = 0 to
UBound(props) msg = msg & " " & CStr(i) & ". " & props(i) & vbCrLf Next resp =
MsgBox(msg) ' We want "Enable Phase Correction" ' Now find valid settings
propName = "Enable Phase Correction" uniqVal = calAll.PropertyValues
(propName) 'returns 'false,true' make it true. For i = 1 to UBound(uniqVal)
MsgBox "calAll.PropertyValues (" & propName & ") = " & uniqVal(i) Next
calAll.PropertyValue(propName) = "true" ' '********* 'Perform Guided Cal
******* ' Get a handle to the GuidedCal object Dim guidedcal set guidedcal =
calAll.GuidedCalibration ' Specify the DUT connectors
guidedcal.ConnectorType(1) = "APC 3.5 male" guidedcal.ConnectorType(2) = "APC
3.5 male" guidedcal.ConnectorType(3) = "Not used" guidedcal.ConnectorType(4) =
"Not used" MsgBox "Connectors defined for Ports 1 and 2" ' Select the Cal Kit
for each port being calibrated. guidedCal.CalKitType(1) = "85052D"
guidedCal.CalKitType(2) = "85052D" MsgBox "Cal kits defined for Ports 1 and 2"
' Initiate the calibration and query the number of steps Numsteps =
guidedcal.GenerateSteps For i = 1 to Numsteps step = "Step " \+ CStr(i) + " of
" \+ CStr(Numsteps) strPrompt = guidedCal.GetStepDescription(i) value =
MsgBox(strPrompt, vbOKOnly, step) guidedCal.AcquireStep i Next ' Conclude the
calibration guidedCal.GenerateErrorTerms csets = calAll.GeneratedCalSets For i
= 0 to UBound(uniqVal) MsgBox (csets(i)) Next  
---  
  
* * *

* * *

