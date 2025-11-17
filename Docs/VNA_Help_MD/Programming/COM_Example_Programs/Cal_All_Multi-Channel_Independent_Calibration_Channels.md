# Cal All Multi-Channel Independent Calibration Channels

The following program creates an Independent Calibration Channels calibration
on multiple measurement class channels. Any selected channels will perform
their own SmartCal instead of importing the calibration from the SmartCal
performed on the special Cal All channel (typically Channel 200).

This VBScript (*.vbs) program can be run as a macro in the PNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the PNA hard drive as BalancedCOM.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

dim host: host = "localhost" dim pna: set pna =
createobject("Agilentpna835x.application",host) wscript.echo pna.idstring
pna.preset pna.CreateCustomMeasurementEx 2, "Gain Compression Converters",
"CompS11", 1 pna.CreateCustomMeasurementEx 3, "Scalar Mixer/Converter",
"SC12", 1 pna.CreateCustomMeasurementEx 4, "Spectrum Analyzer", "b1", 1
pna.CreateCustomMeasurementEx 5, "Standard", "S22", 1 Set scpi =
pna.ScpiStringParser Dim mgr Set mgr = pna.GetCalManager Dim CalAll Set CalAll
= mgr.CalibrateAllChannels CalAll.Reset 'Perform calibration on Channel 2 SMC:
CalAll.Channels = Array(1,2,3,4,5) CalAll.PropertyValue("Include Power
Calibration") = "true" CalAll.PropertyValue("Independent Calibration
Channels") = "1,3" CalAll.PowerLevel(1) = -5 Dim guidedcal set guidedcal =
calAll.GuidedCalibration ' Specify the DUT connectors
guidedcal.ConnectorType(1) = "APC 3.5 male" guidedcal.ConnectorType(2) = "APC
3.5 female" guidedcal.ConnectorType(3) = "Not used" guidedcal.ConnectorType(4)
= "Not used" guidedCal.CalKitType(1) = "85052D" guidedCal.CalKitType(2) =
"85052D" Numsteps = guidedcal.GenerateSteps wscript.echo "Numsteps: " \+
cstr(Numsteps) 'Note that this calibration is performing multiple calibrations
'But you will only be prompted once for each connection type For i = 1 to
Numsteps step = "Step " \+ CStr(i) \+ " of " \+ CStr(Numsteps) strPrompt =
guidedCal.GetStepDescription(i) value = MsgBox(strPrompt, vbOKOnly, step)
guidedCal.AcquireStep i Next guidedCal.GenerateErrorTerms  
---

