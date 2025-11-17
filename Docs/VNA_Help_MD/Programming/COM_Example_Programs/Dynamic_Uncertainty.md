# Dynamic Uncertainty

* * *

This example does the following in separate subprograms:

  * Setup Uncertainty Manager Workspace

  * Perform a standard 2-port Guided Cal

  * Perform a Cable Characterization

  * Perform a Noise Characterization

  * Perform a 2-Port Uncertainty Cal

  * Make Uncertainty Trace Settings

The cable repeatability and noise characterizations can be performed once, and
then they are good for possibly months.

However, the uncertainty calibrations should be performed just as often as
traditional non-uncertainty measurement calibrations.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file, such as Notepad, and save it
on the VNA hard drive as *.vbs.

#### See Also

[Learn how to setup and run the macro.](../Using_Macros.md#HowToSetup)

[See Dynamic Uncertainty commands](../CalTopic.md#uncertainty)

[Learn about Dynamic Uncertainty (Option
S93015A/B)](../../S3_Cals/Dynamic_Uncertainty.htm)

[See Other Example Programs](COM_Example_Intro.md)

Dim app ' Create / Get the VNA application. Set pna =
CreateObject("AgilentPNA835x.Application") 'Preset the analyzer pna.preset
SetupWorkspace TwoPortGuidedCal PerformCableChar PerformNoiseChar
TwoPortUncertCal MakeTraceSettings MsgBox "The example program has now
completed" '********************************************* ' Setup Uncertainty
Workspace Sub SetupWorkspace Set cables = pna.UncertaintyManager.Cables Dim
strCableCatalog For i = 1 To cables.Count strCableCatalog = strCableCatalog &
cables(i).Name If i < cables.Count Then strCableCatalog = strCableCatalog &
Chr(10) ' Uncomment the following line to reset (clear) repeatability data for
the cable 'cables(i).ResetRepeatability Next MsgBox "Cables:" & Chr(10) &
Chr(10) & strCableCatalog Set ports = pna.UncertaintyManager.Ports Dim
strPortCatalog For i = 1 To ports.Count strPortCatalog = strPortCatalog &
"Port " & ports(i).Number & ": " & ports(i).Cable If i < ports.Count Then
strPortCatalog = strPortCatalog & Chr(10) ' Uncomment the following line to
reset (clear) noise data for the port 'ports(i).ResetNoise Next MsgBox "Port
Cables:" & Chr(10) & Chr(10) & strPortCatalog ' Uncomment the following line
to select the particular cable for all ports 'ports.SelectCableForAllPorts
cables(1).Name ' Uncomment this next line to copy the noise data for Port 1 to
be used for all ports 'ports.CopyNoiseToAllPorts 1 ' Uncomment the following
line to reset (clear) the noise data for all ports
'ports.ResetNoiseForAllPorts ' The next lines toggle uncertainty manager
properties on pna.UncertaintyManager.PortNoiseEnabled = True MsgBox "Noise
enabled for cals = " & pna.UncertaintyManager.PortNoiseEnabled
pna.UncertaintyManager.CableRepeatabilityEnabled = True MsgBox "Cable
repeatability enabled for cals = " &
pna.UncertaintyManager.CableRepeatabilityEnabled
pna.UncertaintyManager.StandardDefinitionsEnabled = True MsgBox "Standards
definition uncertainties enabled for cals = " &
pna.UncertaintyManager.StandardDefinitionsEnabled ' Uncomment the following
line to change the max number of uncertainty points for cals to be 500
'pna.UncertaintyManager.MaximumUncertaintyPoints = 500 MsgBox "Max number of
uncertainty points for cals = " &
pna.UncertaintyManager.MaximumUncertaintyPoints ' Uncomment the following line
to perform a Save of the currently loaded uncertainty workspace ('.ml4') file
'pna.UncertaintyManager.Save ' Uncomment the following line to save the
currently loaded uncertainty workspace to a specific ('.ml4') filename
'pna.UncertaintyManager.Save "myUncertaintyWorkspace.ml4" ' Uncomment the
following line to recall the uncertainty workspace ('.ml4') file that we just
saved 'pna.UncertaintyManager.Recall "myUncertaintyWorkspace.ml4" End Sub
'********************************************* ' Measure the steps of a cable
characterization, ' noise characterization, or a calibration. Sub
MeasureStepsOfCharacterizationOrCal(objCharOrCal, isNoiseCharacterization,
numSteps) For i = 1 To numSteps step = "Step " \+ CStr(i) + " of " \+
CStr(numSteps) ' A "connection adjustment" means the user has to change
something about the connection, ' such as wiggling cable and re-connecting
standard during a repeatability characterization, ' or to move the slide
position of a sliding load if a connection step in a calibration ' were to
involve a sliding load. If isNoiseCharacterization = False Then
numConnectionAdjustmentsPerStep = objCharOrCal.MinimumIterationsForStep(i)
Else ' noise characterization ' in this case, "iterations" are just repetitive
measurements, not re-adjust/re-measure the standard
numConnectionAdjustmentsPerStep = 1 End If For j = 1 To
numConnectionAdjustmentsPerStep strPrompt = objCharOrCal.GetStepDescription(i)
retVal = MsgBox(strPrompt, vbOKCancel, step) If retVal = vbCancel Then
WScript.Quit objCharOrCal.AcquireStep i Next Next
objCharOrCal.GenerateErrorTerms End Sub Function FormatList(tokens) For i = 0
To UBound(tokens) list = list & tokens(i) & Chr(10) Next FormatList = list End
Function '********************************************* ' Performing a NON-
UNCERTAINTY Guided 2-port cal (Ports 1 and 2) Sub TwoPortGuidedCal message =
"A non-uncertainty 2-port calibration will now be performed, " message =
message & "because a calibration is needed for characterizing the cables"
MsgBox message ' Create / Get the VNA application. Set app =
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
calibration and query the number of steps numCalSteps =
guidedCal.GenerateSteps MsgBox "Number of steps is " \+ CStr(numCalSteps) '
Measure the standards MeasureStepsOfCharacterizationOrCal guidedCal, False,
numCalSteps MsgBox "The cal needed for the cable repeatability
characterizations is done" End Sub
'********************************************* ' Perform Cable
Characterization Sub PerformCableChar pna.ActiveMeasurement.ErrorCorrection =
True Set uncchar = pna.UncertaintyManager.Characterizer ' Initiate
repeatability characterizations on Channel 1 for Ports 1 and 2, with 3 '
iterative measurements of each standard (normally users should specify more
than 3 ' iterations per standard but it just makes this example speedier)
numCharSteps = uncchar.InitiateCableCharacterization(1, 1, 3) message = "Now
to characterize the cable currently associated with port 1. " message =
message & "Number of standard steps for characterizing port 1 cable = " &
numCharSteps MsgBox message  ' Get guided cal object for Channel 1 to use for
performing the characterization Set guidedcal = uncchar.GuidedCalibration(1)
MeasureStepsOfCharacterizationOrCal guidedcal, False, numCharSteps MsgBox
"Cable characterization for port 1 is done" numCharSteps =
uncchar.InitiateCableCharacterization(1, 2, 3) message = "Now to characterize
the cable currently associated with port 2. " message = message & "Number of
standard steps for characterizing port 2 cable = " & numCharSteps MsgBox
message  Set guidedcal = uncchar.GuidedCalibration(1)
MeasureStepsOfCharacterizationOrCal guidedcal, False, numCharSteps MsgBox
"Cable characterization for port 2 is done" End Sub
'********************************************* 'Perform Noise Characterization
Sub PerformNoiseChar pna.ActiveMeasurement.ErrorCorrection = True Set uncchar
= pna.UncertaintyManager.Characterizer ' Initiate noise characterization on
Channel 1 for Ports 1 and 2, with 3 iterative ' measurements of each standard
(normally users should specify more than 3 iterations ' per standard but it
just makes this example speedier) numCharSteps =
uncchar.InitiateNoiseCharacterization(1, 1, 2, 3) message = "Now to
characterize the system noise for ports 1 and 2. " message = message & "Number
of connection steps to be made = " & numCharSteps MsgBox message ' Get guided
cal object for Channel 1 to use for performing the characterization Set
guidedcal = uncchar.GuidedCalibration(1) MeasureStepsOfCharacterizationOrCal
guidedcal, True, numCharSteps MsgBox "Noise characterization is done" End Sub
'********************************************* 'Perform 2-port Uncertainty
Calibration (Ports 1 and 2) on Channel 1 Sub TwoPortUncertCal ' Note: normally
to use the Application's ActiveChannel property for this, ' you would have to
ensure your active channel is an S-parameter channel ' before this point, but
as the PerformCableChar and PerformNoiseChar ' subroutines have executed right
before this one, that is already ensured. ' Create / Get the VNA application.
Set calMgr = app.GetCalManager Set guidedCal = calMgr.GuidedCalibration Set
chan = app.ActiveChannel chanNum = chan.ChannelNumber ' Initialize guided cal
to be performed on the active channel. ' The boolean argument of True
indicates to create a new calset ' for storing the new calibration to.
guidedCal.Initialize chanNum, True ' Specify this calibration is to be
performed with uncertainties. guidedCal.UncertaintyEnabled = True ' Query the
list of uncertainty cal kits and ECal module factory characterizations '
applicable for the connector of the cable associated with Port 1. kits =
guidedCal.CompatibleCalKits(1) ' Format the list string with linefeed
characters between each substring kitList = FormatList(kits) ' Select the Cal
Kit or ECal module to use for both ports. ' If the selected kit does not have
a suitable set of standards ' that can mate the connector of the cable
attached to Port 2, ' then the attempt to GenerateSteps should yield an
applicable error message. message = "Now to perform an uncertainty calibration
for ports 1 and 2. " message = message & "Enter your cal kit or ECal module to
use. Choose from this list:" message = message & Chr(10) & Chr(10) & kitList
selectedKit = InputBox(message) If selectedKit = "" Then Exit Sub
guidedCal.CalKitType(1) = selectedKit guidedCal.CalKitType(2) = selectedKit '
Note: If your VNA has more than 2 ports, then should uncomment ' one or both
of these next two lines just in case this channel ' may have had a remote non-
Dolcetto cal performed prior that ' involved port 3 and/or 4.
'guidedCal.CalKitType(3) = "" 'guidedCal.CalKitType(4) = "" ' This next block
of commented-out code shows optional functions when using ECal. ' These
OrientECALModule and ECALPortMapEx properties would need to be set prior ' to
calling GenerateSteps on the guidedCal object.
'\-----------------------------------------------------------------------------------
' Read the information about the factory characterization data ' of ECal
module #1 on the USB bus 'Set calibrator = chan.Calibrator 'Const ECalModule1
= 1 'module1Info = calibrator.GetECALModuleInfoEx(ECalModule1) 'MsgBox
"Description of ECal module #1:" & Chr(10) & Chr(10) & module1Info ' By
default, during calibration the VNA automatically determines the orientation '
of the ECal module (senses which port of the module is connected to which port
of ' the VNA). However, since this setting could have recently been overridden
by ' another user of the instrument, use this next line to ensure the auto
orientation ' setting is enabled. 'calibrator.OrientECALModule = True '
Alternatively, if you are measuring at very low power levels where ' the VNA
fails to sense the module's orientation, you may need to turn off the auto '
orientation and specify how the module is connected (as in these next two
lines ' of code, "A1,B2" would indicate Port A of the module is connected to
Port 1 and ' Port B is connected to Port 2). 'c alibrator.OrientECALModule =
False 'calibrator.ECALPortMapEx(ECalModule1) = "A1,B2"
'\-----------------------------------------------------------------------------------
' End of optional ECal setup ' Initiate the calibration and query the number
of steps numCalSteps = guidedCal.GenerateSteps MsgBox "Number of cal steps is
" \+ CStr(numCalSteps) MeasureStepsOfCharacterizationOrCal guidedCal, False,
numCalSteps MsgBox "Cal is done" End Sub
'********************************************* 'Make Uncertainty Trace
Settings Sub MakeTraceSettings ' Note: normally to use the Application's
ActiveMeasurement property for this, ' you would have to first ensure your
active measurement is an S-parameter channel ' measurement before this point,
and that the channel has an uncertainty cal to be ' able to turn on
uncertainty display, but as the TwoPortUncertCal subroutine has ' executed
right before this one, that is already ensured. Set unc =
pna.ActiveMeasurement.Uncertainty MsgBox "DisplayType = " &
GetUncDispEnumValueName(unc.DisplayType) On Error Resume Next unc.DisplayType
= 4 ' naUncertaintyDisplayShade If Err.Number <> 0 Then MsgBox Err.Description
Err.Clear Else MsgBox "DisplayType = " &
GetUncDispEnumValueName(unc.DisplayType) End If On Error GoTo 0 MsgBox
"CoverageFactor = " & unc.CoverageFactor ' Uncomment the following line to try
setting the CoverageFactor = 3 'unc.CoverageFactor = 3
unc.CableRepeatabilityUncertainty = False MsgBox
"CableRepeatabilityUncertainty = " & unc.CableRepeatabilityUncertainty
unc.CableRepeatabilityUncertainty = True MsgBox "CableRepeatabilityUncertainty
= " & unc.CableRepeatabilityUncertainty unc.MeasurementNoiseUncertainty =
False MsgBox "MeasurementNoiseUncertainty = " &
unc.MeasurementNoiseUncertainty unc.MeasurementNoiseUncertainty = True MsgBox
"MeasurementNoiseUncertainty = " & unc.MeasurementNoiseUncertainty
unc.ErrorTermUncertainty = False MsgBox "unc.ErrorTermUncertainty = " &
unc.ErrorTermUncertainty unc.ErrorTermUncertainty = True MsgBox
"unc.ErrorTermUncertainty = " & unc.ErrorTermUncertainty End Sub Function
GetUncDispEnumValueName(uncDispTypeEnum) Select Case uncDispTypeEnum Case 0
GetUncDispEnumValueName = "naUncertaintyDisplayNone" Case 1
GetUncDispEnumValueName = "naUncertaintyDisplayMaximum" Case 2
GetUncDispEnumValueName = "naUncertaintyDisplayMinimum" Case 3
GetUncDispEnumValueName = "naUncertaintyDisplayBar" Case 4
GetUncDispEnumValueName = "naUncertaintyDisplayShade" Case 5
GetUncDispEnumValueName = "naUncertaintyDisplayEllipse" Case Else
GetUncDispEnumValueName = "Unexpected display type enum value!" End Select End
Function  
---  
  
* * *

