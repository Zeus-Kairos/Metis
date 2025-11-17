# Create Multiple Instances of Calibrate All Channels

* * *

This example sets up multiple instances of CalibrateAllChannels.

Note: **You can assign a single client channel to multiple cal all instances.
However, care should be taken here. If you create user calests, all calsets
will be created but only the last one will be applied. If you are only using a
cal register, only the last cal all will be written to the cal register (only
supports one claibration). The order that the cal alls are created should be
the order in which they are saved
([GenerateErrorTerms](../COM_Reference/Methods/GenerateErrorTerms_Method.md)).
This ensures that the client channel imports the proper ETerms.**

### See Also

[CalibrateAllChannels
Object](../COM_Reference/Objects/CalibrateAllChannels_Object.htm)

[Learn about Cal All](../../S3_Cals/Calibrate_All_Channels.md)

[See other COM Examples](COM_Example_Intro.md)

'Access the CalAllChannels object Dim app Set app =
CreateObject("Agilentpna835x.application","strange") Dim mgr Set mgr =
app.GetCalManager Dim scpi' As ScpiStringParser Set scpi =
app.ScpiStringParser 'Preset PNA app.Preset 'Add extra channels
app.CreateCustomMeasurementEx 2, "Standard","S22",2
app.CreateCustomMeasurementEx 3, "Standard","S33",3
app.CreateCustomMeasurementEx 4, "Standard","S44",4 '********** Setup CalAll
Channel Dim CalAll Set CalAll = mgr.CalibrateAllChannelsEx(1) CalAll.Reset 'do
it again Dim CalAll2 Set CalAll2 = mgr.CalibrateAllChannelsEx(2) 'creates
second ComCalibrateAllChannels CalAll2.Reset CalAll.Channels = Array(1,2)
CalAll2.Channels = Array(3,4) CalAll.UserCalsetPrefix = "MyCalAll"
CalAll2.UserCalsetPrefix = "MyCalAll2" 'CalAll.Reset 'Dim guidedcal 'set
guidedcal = CalAll.GuidedCalibration Dim guidedcal set guidedcal =
CalAll.GuidedCalibration MsgBox "Doing First Guidedcal" ' Specify the DUT
connectors guidedcal.ConnectorType(1) = "APC 3.5 male"
guidedcal.ConnectorType(2) = "APC 3.5 male" guidedcal.ConnectorType(3) = "Not
used" guidedcal.ConnectorType(4) = "Not used" guidedCal.CalKitType(1) =
"85052D" guidedCal.CalKitType(2) = "85052D" Numsteps = guidedcal.GenerateSteps
For i = 1 to Numsteps step = "Step " \+ CStr(i) \+ " of " \+ CStr(Numsteps)
strPrompt = guidedCal.GetStepDescription(i) value = MsgBox(strPrompt,
vbOKOnly, step) guidedCal.AcquireStep i Next guidedCal.GenerateErrorTerms set
guidedcal = CalAll2.GuidedCalibration MsgBox "Doing second Guidedcal" '
Specify the DUT connectors guidedcal.ConnectorType(1) = "APC 3.5 male"
guidedcal.ConnectorType(2) = "Not used" guidedcal.ConnectorType(3) = "APC 3.5
male" guidedcal.ConnectorType(4) = "APC 3.5 male" guidedCal.CalKitType(1) =
"85052D" guidedCal.CalKitType(3) = "85052D" guidedCal.CalKitType(4) = "85052D"
Numsteps = guidedcal.GenerateSteps For i = 1 to Numsteps step = "Step " \+
CStr(i) \+ " of " \+ CStr(Numsteps) strPrompt =
guidedCal.GetStepDescription(i) value = MsgBox(strPrompt, vbOKOnly, step)
guidedCal.AcquireStep i Next guidedCal.GenerateErrorTerms  
---  
  
* * *

