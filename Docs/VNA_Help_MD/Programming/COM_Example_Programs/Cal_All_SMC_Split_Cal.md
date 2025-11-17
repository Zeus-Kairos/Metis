# Cal All SMC Split Cal

* * *

The following program creates a Split Cal which applies to SMC and GCX
channels only. If selected, these channels will perform their own
calibrations, performing two 1-port calibrations (no thru).

This VBScript (*.vbs) program can be run as a macro in the PNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the PNA hard drive as BalancedCOM.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

dim host: host = "localhost" dim pna: set pna =
createobject("Agilentpna835x.application",host) wscript.echo pna.idstring
pna.preset pna.CreateCustomMeasurementEx 2, "Scalar Mixer/Converter", "SC12",
1 Set scpi = pna.ScpiStringParser Dim mgr Set mgr = pna.GetCalManager Dim
CalAll Set CalAll = mgr.CalibrateAllChannels CalAll.Reset 'Perform calibration
on Channel 2 SMC: CalAll.Channels = Array(2) CalAll.PropertyValue("Include
Power Calibration") = "true" CalAll.PropertyValue("Split Cal") = "true"
CalAll.PowerLevel(1) = -5 Dim guidedcal set guidedcal =
calAll.GuidedCalibration ' Specify the DUT connectors
guidedcal.ConnectorType(1) = "APC 3.5 male" guidedcal.ConnectorType(2) = "APC
3.5 female" guidedcal.ConnectorType(3) = "Not used" guidedcal.ConnectorType(4)
= "Not used" guidedCal.CalKitType(1) = "85052D" guidedCal.CalKitType(2) =
"85052D" Numsteps = guidedcal.GenerateSteps wscript.echo "Numsteps: " \+
cstr(Numsteps) 'Note that this performs two one-port calibrations 'So the
power sensor will be prompted to connect on P1 and P2 For i = 1 to Numsteps
step = "Step " \+ CStr(i) \+ " of " \+ CStr(Numsteps) strPrompt =
guidedCal.GetStepDescription(i) value = MsgBox(strPrompt, vbOKOnly, step)
guidedCal.AcquireStep i Next guidedCal.GenerateErrorTerms  
---

