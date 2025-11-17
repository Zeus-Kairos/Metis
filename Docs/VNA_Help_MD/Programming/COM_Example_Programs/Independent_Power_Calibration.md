# Independent Power Calibration

* * *

The following program creates an independent power calibration over a
specified frequency span when performing a Cal All.

This VBScript (*.vbs) program can be run as a macro in the PNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the PNA hard drive as BalancedCOM.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

dim host: host = "K-N5222B-10034"  
dim pna: set pna = createobject("Agilentpna835x.application",host)  
wscript.echo pna.idstring  
pna.preset  
pna.CreateCustomMeasurementEx 2, "Gain Compression", "S21", 1  
  
Dim mgr  
Set mgr = pna.GetCalManager  
Dim CalAll  
  
Set CalAll = mgr.CalibrateAllChannels  
  
CalAll.Reset  
CalAll.Channels = Array(1,2)  
CalAll.PropertyValue("Include Power Calibration") = "true"  
CalAll.PropertyValue("Enable Extra Power Cals") = "Port 2,Port 3"  
  
'Add power calibrations on port 3:  
CalAll.IndependentPowerCalibration(3).AddPowerCalRange  
CalAll.IndependentPowerCalibration(3).PowerCalRange(1).StartFrequency = 3e9  
CalAll.IndependentPowerCalibration(3).PowerCalRange(1).StopFrequency = 4e9  
CalAll.IndependentPowerCalibration(3).PowerCalRange(1).NumberOfPoints = 21  
CalAll.IndependentPowerCalibration(3).AddPowerCalRange  
CalAll.IndependentPowerCalibration(3).PowerCalRange(2).StartFrequency = 20e9  
CalAll.IndependentPowerCalibration(3).PowerCalRange(2).StopFrequency = 21e9  
CalAll.IndependentPowerCalibration(3).PowerCalRange(2).NumberOfPoints = 7  
CalAll.IndependentPowerCalibration(2).AddPowerCalRange  
CalAll.IndependentPowerCalibration(2).PowerCalRange(1).StartFrequency = 3e9  
CalAll.IndependentPowerCalibration(2).PowerCalRange(1).StopFrequency = 4e9  
CalAll.IndependentPowerCalibration(2).PowerCalRange(1).NumberOfPoints = 21  
  
dim calPorts  
calPorts = CalAll.IndependentPowerCalibration.ValidPorts  
PrintVector calPorts, "Cal Ports"  
  
src3rangecount = CalAll.IndependentPowerCalibration(3).RangeCount  
wscript.echo "src3rangecount: " \+ cstr(src3rangecount)  
src2rangecount = CalAll.IndependentPowerCalibration(2).RangeCount  
wscript.echo "src2rangecount: " \+ cstr(src2rangecount)  
  
CalAll.IndependentPowerCalibration(2).Reset  
src2rangecount = CalAll.IndependentPowerCalibration(2).RangeCount  
wscript.echo "src2rangecount: " \+ cstr(src2rangecount)  
  
start = CalAll.IndependentPowerCalibration(3).PowerCalRange(1).StartFrequency  
stopf = CalAll.IndependentPowerCalibration(3).PowerCalRange(1).StopFrequency  
points = CalAll.IndependentPowerCalibration(3).PowerCalRange(1).NumberOfPoints  
  
wscript.echo "start,stop,points: " \+ cstr(start) +"," \+ cstr(stopf) + "," \+
cstr(points)  
  
CalAll.PowerLevel(1) = -5  
  
Dim guidedcal  
set guidedcal = calAll.GuidedCalibration  
' Specify the DUT connectors  
guidedcal.ConnectorType(1) = "APC 3.5 male"  
guidedcal.ConnectorType(2) = "APC 3.5 female"  
guidedcal.ConnectorType(3) = "Not used"  
guidedcal.ConnectorType(4) = "Not used"  
  
guidedCal.CalKitType(1) = "N4691-61004 ECal 13442"  
guidedCal.CalKitType(2) = "N4691-61004 ECal 13442"  
  
Numsteps = guidedcal.GenerateSteps  
wscript.echo "Numsteps: " \+ cstr(Numsteps)  
  
For i = 1 to Numsteps  
step = "Step " \+ CStr(i) + " of " \+ CStr(Numsteps)  
strPrompt = guidedCal.GetStepDescription(i)  
value = MsgBox(strPrompt, vbOKOnly, step)  
guidedCal.AcquireStep i  
Next  
  
guidedCal.GenerateErrorTerms  
  
sub PrintVector (vec, msg)  
dim i, str  
if (IsArray(vec)) then  
for i = lbound(vec) to ubound(vec)  
str = str + cstr(vec(i)) + " "  
next  
else  
str = "vector is EMPTY"  
end if  
wscript.echo msg +": " \+ str  
end sub

