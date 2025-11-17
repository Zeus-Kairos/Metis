# Perform Global Delta Match Cal

* * *

The following program performs a [Global Delta Match
Calibration.](../../S3_Cals/Delta_Match_Calibration.htm#Global) This is
required when performing an Unknown Thru cal or TRL cal on VNAs without a
reference receiver for each test port. [See
example.](Perform_an_Unknown_Thru_or_TRL_Cal.htm)

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as Delta.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

Sub PerformGlobalDeltaMatchCal()  
' Create / Get the VNA application.  
Set app = CreateObject("AgilentPNA835x.Application")  
' Get cal manager object  
Set calMgr = app.GetCalManager  
' Get guided cal object  
Set guidedCal = calMgr.GuidedCalibration  
  
' Initiate a Global Delta Match calibration, choosing connector and cal kit  
numSteps = guidedCal.GenerateGlobalDeltaMatchSequence("APC 3.5 female",
"85033D/E")  
MsgBox "Number of steps is " \+ CStr(numSteps)  
  
' Measure the standards  
For i = 1 To numSteps  
step = "Step " \+ CStr(i) + " of " \+ CStr(numSteps)  
strPrompt = guidedCal.GetStepDescription(i)  
retVal = MsgBox(strPrompt, vbOKCancel, step)  
If retVal = vbCancel Then Exit Sub  
guidedCal.AcquireStep i  
Next  
  
' Conclude the calibration  
guidedCal.GenerateErrorTerms  
MsgBox "Cal is done!"  
  
End Sub

