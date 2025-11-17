# Cal All Independent Calibration Channels

The following program creates an Independent Calibration Channels which is a
comma-separated channel list. Any selected channels will perform their own
SmartCal instead of importing the calibration from the SmartCal performed on
the special Cal All channel (typically Channel 200).

This VBScript (*.vbs) program can be run as a macro in the PNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the PNA hard drive as BalancedCOM.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

dim host: host = "localhost" dim pna: set pna =
createobject("Agilentpna835x.application",host) wscript.echo pna.idstring
pna.preset Set scpi = pna.ScpiStringParser Dim mgr Set mgr = pna.GetCalManager
Dim CalAll Set CalAll = mgr.CalibrateAllChannels CalAll.Reset 'Perform
calibration on Channel 2 SMC: CalAll.Channels = Array(1)
CalAll.PropertyValue("Include Power Calibration") = "true"
CalAll.PropertyValue("Independent Calibration Channels") = "1"
CalAll.PowerLevel(1) = -5 Dim guidedcal set guidedcal =
calAll.GuidedCalibration ' Specify the DUT connectors
guidedcal.ConnectorType(1) = "APC 3.5 male" guidedcal.ConnectorType(2) = "APC
3.5 female" guidedcal.ConnectorType(3) = "Not used" guidedcal.ConnectorType(4)
= "Not used" guidedCal.CalKitType(1) = "85052D" guidedCal.CalKitType(2) =
"85052D" Numsteps = guidedcal.GenerateSteps wscript.echo "Numsteps: " \+
cstr(Numsteps) For i = 1 to Numsteps step = "Step " \+ CStr(i) \+ " of " \+
CStr(Numsteps) strPrompt = guidedCal.GetStepDescription(i) value =
MsgBox(strPrompt, vbOKOnly, step) guidedCal.AcquireStep i Next
guidedCal.GenerateErrorTerms  
---

