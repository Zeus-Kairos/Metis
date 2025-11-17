# Perform an Unknown Thru or TRL Cal

* * *

The following program performs either a 2-port SOLT Unknown Thru Cal or a
2-port TRL Cal. The 85052C Cal Kit used in this program contains both types of
standards. This program can be run on 2-port or 4-port VNAs. When run on
[select PNA-L models](../../S3_Cals/Delta_Match_Calibration.md), a Delta
Match Cal is required. See [Delta Match Cal example
program](Perform_Global_Delta_Match_Cal.htm).

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as Unknown.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

PerformUnknownThruOrTRLCal  
Sub PerformUnknownThruOrTRLCal()  
' Create / Get the VNA application.  
Set app = CreateObject("AgilentPNA835x.Application")  
' Get the cal manager object  
Set calMgr = app.GetCalManager  
' Get the guided cal object  
Set guidedCal = calMgr.GuidedCalibration  
Set chan = app.ActiveChannel  
chanNum = chan.ChannelNumber  
  
' Initialize guided cal to be performed on the active channel.  
' The boolean argument of True specifies the creation of a new calset  
' for storing the new calibration.  
guidedCal.Initialize chanNum, True  
  
' Specify connectors for Ports 1 and 2  
guidedCal.ConnectorType(1) = "APC 3.5 female"  
guidedCal.ConnectorType(2) = "APC 3.5 male"  
  
' If your VNA has more than 2 ports, uncomment one or both of  
' these next two lines, to explicitly specify this is  
' just a 2-port cal.  
'guidedCal.ConnectorType(3) = "Not used"  
'guidedCal.ConnectorType(4) = "Not used"  
  
' Specify cal kit for Ports 1 and 2  
guidedCal.CalKitType(1) = "85052C"  
guidedCal.CalKitType(2) = "85052C"  
  
' Since the 85052C cal kit contains SOLT standards and also TRL  
' standards, these next lines determine whether the cal becomes  
' unknown thru (SOLT), or TRL.  
' Specify cal and Thru method  
  
guidedCal.PathThruMethod (1,2) = "Undefined Thru"  
  
' To set up the cal as TRL, comment the previous line and uncomment this next
line. The Thru method is set by default.  
guidedCal.PathCalMethod (1,2) = "TRL"  
  
'Always send Initialize after modifying the SmartCal logic  
guidedCal.Initialize chanNum, True  
numSteps = guidedCal.GenerateSteps  
MsgBox "Number of steps is " \+ CStr(numSteps)  
  
' Query the list of ports that need delta match  
portList = guidedCal.PortsNeedingDeltaMatch  
' If portList contains just one element and it's value is 0, then that
indicates  
' none of the ports being calibrated require delta match data.  
' If each testport on the VNA has it's own reference receiver (R channel),  
' then delta match is never needed, so portList will always be just 0.  
lowerBound = LBound(portList)  
If (UBound(portList) <> lowerBound) Or (portList(lowerBound) <> 0) Then  
' Delta match data is required for at least one port.  
' For this example, we assume a Global Delta Match Cal has previously been  
' performed so the Global Delta Match CalSet exists.  
' Supplying an empty string to ApplyDeltaMatchFromCalSet indicates to use  
' the Global Delta Match CalSet.  
guidedCal.ApplyDeltaMatchFromCalSet ""  
End If  
  
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

