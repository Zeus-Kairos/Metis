# Show Custom Cal Windows during a Guided Calibration

* * *

This VBScript program shows how to send commands that allow you to view
specific 'custom' windows, and sweep specific channels, during a UI (Cal
Wizard) or remote calibration.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as CalWindow.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#Setup)

These commands are used to show and sweep specific windows and channels:

  * [AllowChannelToSweepDuringCalAcquisition Method](../COM_Reference/Methods/AllowChannelToSweepDuringCalAcquisition_Method.md)

  * [DisplayNAWindowDuringCalAcquisition Method](../COM_Reference/Methods/DisplayNAWindowDuringCalAcquisition_Method.md)

  * [DisplayOnlyCalWindowDuringCalAcquisition Method](../COM_Reference/Methods/DisplayOnlyCalWindowDuringCalAcquisition_Method.md)

  * [SweepOnlyCalChannelDuringCalAcquisition Method](../COM_Reference/Methods/SweepOnlyCalChannelDuringCalAcquisition_Method.md)

The following command sweeps the Cal Windows before remote acquisition:

  * [SetupMeasurementsForStep Method](../COM_Reference/Methods/SetupMeasurementsForStep_Method.md)

[See Other COM Example Programs](COM_Example_Intro.md)

Set pna = CreateObject("AgilentPNA835x.Application") pna.Preset ' get a handle
to the preset channel 1 so that we can later cal it set
meas=pna.ActiveMeasurement ' Creates a new S21 measurement in channel 2 and
New window(2) ' this will be the channel and window to show during cal
pna.CreateSParameterEx 2,2,1,2,2 Set calMgr = pna.GetCalManager Set guidedCal
= calMgr.GuidedCalibration ' show window 2 during cal
calMgr.DisplayNAWindowDuringCalAcquisition 2,True ' sweep channel 2 during
calibration of chan 1 calMgr.AllowChannelToSweepDuringCalAcquisition 1,2,True
' make Channel1 the active channel ' activating the measurement also activates
the channel meas.Activate guidedCal.Initialize 1, True ' Do 2-port cal '
Select the connectors guidedCal.ConnectorType(1) = "APC 3.5 female"
guidedCal.ConnectorType(2) = "APC 3.5 male" ' Select the Cal Kit for each port
being calibrated. guidedCal.CalKitType(1) = "85052D" guidedCal.CalKitType(2) =
"85052D" ' Initiate the calibration and query the number of steps numSteps =
guidedCal.GenerateSteps ' Measure the standards, compute and apply the cal
value = MsgBox("Number of steps is " \+ CStr(numSteps)) ' Measure the
standards For i = 1 to NumSteps step = "Step " \+ CStr(i) + " of " \+
CStr(numSteps) strPrompt = guidedCal.GetStepDescription(i) ' Sweep the Cal
window prior to standard acquisition guidedCal.SetupMeasurementsForStep i '
prompt to connect standard value = MsgBox(strPrompt, vbOKOnly, step) ' measure
standard guidedCal.AcquireStep i Next ' Conclude the calibration
guidedCal.GenerateErrorTerms MsgBox ("Cal is complete!") ' clear the Cal
window and channel flags calMgr.DisplayOnlyCalWindowDuringCalAcquisition
calMgr.SweepOnlyCalChannelDuringCalAcquisition  
---  
  
* * *

