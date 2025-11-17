## Perform a Comprehensive 2-Port Guided Cal

* * *

This example program performs a Guided Calibration on the active channel
between ports 1 and 2. The following calibration features are demonstrated:

  * Guided Power Cal

  * Optional functions when using ECal

  * Select the Thru method

  * Save to a new CalSet

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file, such as Notepad, and save it
on the VNA hard drive as CompGuided.vbs. Learn [How to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

### See Also

[VNA Object Model](../COM_Reference/Objects/The_Analyzer_Object_Model.md)

[CalManager Object](../COM_Reference/Objects/CalManager_Object.md)

[GuidedCalibration
Object](../COM_Reference/Objects/GuidedCalibration_Object.htm)

[Calibrator Object](../COM_Reference/Objects/Calibrator_Object.md)

[See Other COM Example Programs](COM_Example_Intro.md)

' Performing a Guided 2-port cal (Ports 1 and 2) TwoPortGuidedCal Sub
TwoPortGuidedCal ' Create / Get the VNA application. Set app =
CreateObject("AgilentPNA835x.Application") Set calMgr = app.GetCalManager Set
guidedCal = calMgr.GuidedCalibration Set chan = app.ActiveChannel chanNum =
chan.ChannelNumber ' Initialize guided cal to be performed on the active
channel. ' The boolean argument of True indicates to create a new calset ' for
storing the new calibration to. guidedCal.Initialize chanNum, True ' Query the
connectors that the VNA system recognizes conns =
guidedCal.ValidConnectorTypes ' Format the list string with linefeed
characters between each substring connList = FormatList(conns) ' Select the
connector for Port 1 selectedConn1 = InputBox("Enter your DUT connector for
Port 1. Choose from this list:" & _ Chr(10) & Chr(10) & connList) If
selectedConn1 = "" Then Exit Sub guidedCal.ConnectorType(1) = selectedConn1 '
Select the connector for Port 2 selectedConn2 = InputBox("Enter your DUT
connector for Port 2. Again, choose from this list:" & _ Chr(10) & Chr(10) &
connList) If selectedConn2 = "" Then Exit Sub guidedCal.ConnectorType(2) =
selectedConn2 ' Note: If your VNA has more than 2 ports, you would need to
uncomment ' one or both of these next two lines, to explicitly specify this is
' just a 2-port cal. 'guidedCal.ConnectorType(3) = "Not used"
'guidedCal.ConnectorType(4) = "Not used" ' Query the list of acceptable cal
kits and ECal module characterizations for Port 1. kits =
guidedCal.GetCompatibleCalKits(selectedConn1) ' Format the list string with
linefeed characters between each substring kitList = FormatList(kits) ' Select
the Cal Kit or ECal module characterization to use for Port 1. selectedKit =
InputBox("Enter your cal kit or ECal module characterization for Port 1. " & _
"Choose from this list:" & Chr(10) & Chr(10) & kitList) If selectedKit = ""
Then Exit Sub guidedCal.CalKitType(1) = selectedKit ' Query the list of
acceptable cal kits and ECal module characterizations for Port 2. kits =
guidedCal.GetCompatibleCalKits(selectedConn2) ' Format the list string with
linefeed characters between each substring kitList = FormatList(kits) ' Select
the Cal Kit or ECal module characterization to use for Port 2. selectedKit =
InputBox("Enter your cal kit or ECal module characterization for Port 2. " & _
"Choose from this list:" & Chr(10) & Chr(10) & kitList) If selectedKit = ""
Then Exit Sub guidedCal.CalKitType(2) = selectedKit ' This determines whether
the cal will be a "Guided Power Cal" ' or just a traditional S-parameter cal.
message = "On which port number shall power be measured? " message = message &
"For a traditional guided cal without power cal, enter 0" Dim powerPort
powerPort = CInt( InputBox(message) ) If powerPort > 0 Then
guidedCal.PerformPowerCalibration(powerPort) = True Dim retVal retVal =
MsgBox("Is the power sensor's connector type or gender different from the DUT
connector for that port?", vbYesNo) If retVal = vbYes Then message = "Enter
your power sensor's connector. Choose from this list:" message = message &
Chr(10) & Chr(10) & connList ' Select the sensor's connector. selectedConn1 =
InputBox(message) If selectedConn1 = "" Then Exit Sub
guidedCal.PowerSensorConnectorType(powerPort) = selectedConn1 ' Query the list
of acceptable cal kits and ECal module characterizations ' that are applicable
for the sensor's connector. kits =
guidedCal.GetCompatibleCalKits(selectedConn1) ' Format the list string with
linefeed characters between each substring kitList = FormatList(kits) message
= "Enter your cal kit or ECal module characterization to use for de-embed of
the sensor's connector. " message = message & "Choose from this list:" message
= message & Chr(10) & Chr(10) & kitList ' Select the Cal Kit or ECal module
characterization to use for de-embed of the sensor's connector. selectedKit =
InputBox(message) If selectedKit = "" Then Exit Sub
guidedCal.PowerSensorCalkitType(powerPort) = selectedKit Else
guidedCal.PowerSensorConnectorType(powerPort) = "Ignored" End If ' End of
block that considers the sensor's connector ' Ask for the power level to
perform the power cal at ' (if this command is omitted, the default is 0 dBm).
Dim powerLevel powerLevel = InputBox("Enter the power level for the power cal
to be performed at") If powerLevel = "" Then Exit Sub
guidedCal.PowerCalibrationPowerLevel(powerPort) = CDbl(powerLevel) Else
guidedCal.PerformPowerCalibration(1) = False End If ' End of block that
considers if the cal will include power calibration
'\-----------------------------------------------------------------------------------
' This next block of commented-out code shows optional functions when using
ECal. ' These OrientECALModule and ECALPortMapEx properties would need to be
set prior to  ' calling GenerateSteps on the guidedCal object. ' Read the
information about the Keysight factory characterization data ' of ECal module
#1 on the USB bus 'Set calibrator = chan.Calibrator 'Const ECalModule1 = 1
'module1Info = calibrator.GetECALModuleInfoEx(ECalModule1) 'MsgBox
"Description of ECal module #1:" & Chr(10) & Chr(10) & module1Info ' By
default, during calibration the VNA automatically determines the orientation
of ' the ECal module (senses which port of the module is connected to which
port of the VNA). ' However, since this setting could have recently been
overridden by another user of ' the instrument, use this next line to ensure
the auto orientation setting is enabled. 'calibrator.OrientECALModule = True '
Alternatively, if you are measuring at very low power levels where ' the VNA
fails to sense the module's orientation, you may need to turn off the auto '
orientation and specify how the module is connected (as in these next two
lines of code, ' "A1,B2" would indicate Port A of the module is connected to
Port 1 and ' Port B is connected to Port 2). 'calibrator.OrientECALModule =
False 'calibrator.ECALPortMapEx(ECalModule1) = "A1,B2" ' End of optional ECal
setup
'\-----------------------------------------------------------------------------------
' Select the thru method of Default. This instructs the VNA to determine which
thru ' standard measurement technique to use, based upon the selected
connectors and ' calibration kit(s) and what model of VNA this is.
guidedCal.ThruCalMethod = 0 ' 0 = naDefaultCalMethod ' Initiate the
calibration and query the number of steps numSteps = guidedCal.GenerateSteps
MsgBox "Number of steps is " \+ CStr(numSteps) ' Measure the standards For i =
1 To numSteps step = "Step " \+ CStr(i) + " of " \+ CStr(numSteps) strPrompt =
guidedCal.GetStepDescription(i) MsgBox strPrompt, vbOKOnly, step
guidedCal.AcquireStep i Next ' Conclude the calibration
guidedCal.GenerateErrorTerms MsgBox "Cal is done!" End Sub Function
FormatList(tokens) For i = 0 To UBound(tokens) list = list & tokens(i) &
Chr(10) Next FormatList = list End Function  
---  
  
* * *

