# Perform a Guided Cal with Sliding Load

* * *

This example sets a the sliding load behavior, then performs a Guided Cal
using a sliding load.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save on
the VNA hard drive as Calibrate.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

See the [GuidedCalibration
Object](../COM_Reference/Objects/GuidedCalibration_Object.htm)

[See Other COM Example Programs](COM_Example_Intro.md)

Set app = CreateObject("AgilentPNA835x.Application") Set calMgr =
app.GetCalManager Set guidedCal = calMgr.GuidedCalibration Set chan =
app.ActiveChannel chanNum = chan.ChannelNumber guidedCal.Initialize chanNum,
True ' Specify that any sliding loads should be measured using the ' remote
iterative method rather than launching sliding load dialog. ' 0 =
naShowDialog, 1 = naMeasureSlidePosition
guidedCal.SlidingLoadAcquisitionBehavior = 1 guidedCal.ConnectorType(1) = "APC
3.5 female" guidedCal.ConnectorType(2) = "APC 3.5 male"  85052B cal kit uses
sliding loads guidedCal.CalKitType(1) = "85052B" guidedCal.CalKitType(2) =
"85052B" numSteps = guidedCal.GenerateSteps ' Measure the standards For i = 1
To numSteps step = "Step " \+ CStr(i) + " of " \+ CStr(numSteps) strPrompt =
guidedCal.GetStepDescription(i) MsgBox strPrompt, vbOKOnly, step minIterations
= guidedCal.MinimumIterationsForStep(i) For j = 1 To minIterations If
minIterations > 1 Then MsgBox Adjust/position the standard for measurement 
+ CStr(j) +  of  + CStr(minIterations), vbOKOnly guidedCal.AcquireStep i
Next If guidedCal.IterationCountForStep(i) <> minIterations Then MsgBox
Unexpected error!, vbOKOnly, step guidedCal.ResetStep i End If Next '
Conclude the calibration guidedCal.GenerateErrorTerms  
---  
  
* * *

