# Perform a Guided Calibration using COM

* * *

This example uses the
[GuidedCalibration](../COM_Reference/Objects/GuidedCalibration_Object.md)
interface to perform either a 2-port or 4-port calibration.

Learn more about [Reading and Writing Calibration data using
COM.](../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)

[See Other COM Example Programs](COM_Example_Intro.md)

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save on
the VNA hard drive as Calibrate.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

Set pna = CreateObject("AgilentPNA835x.Application")  
Set calMgr = pna.GetCalManager  
Set guidedCal = calMgr.GuidedCalibration  
Set chan = pna.ActiveChannel  
chanNum = chan.ChannelNumber  
' Initialize guided cal to be performed on the active channel.  
' The boolean argument of True indicates to store the cal only  
' in the channel's calibration register. If instead you wish  
' to create a new calset that the new cal will get stored to,  
' comment out this next line and uncomment the three lines below it.  
guidedCal.Initialize chanNum, True  
'Set calset = calMgr.CreateCalSet(chanNum)  
'chan.SelectCalSet calset.GetGUID, True  
'guidedCal.Initialize chanNum, False  
  
' To perform 2-port cal, Uncomment the following  
' Then comment the 4-port cal  
  
' Do 2-port cal  
' TwoPortGuidedCal  
  
' Do 4-port cal  
FourPortGuidedCal  
  
  
Sub TwoPortGuidedCal()  
' Select the connectors  
guidedCal.ConnectorType(1) = "APC 3.5 female"  
guidedCal.ConnectorType(2) = "APC 3.5 male"  
For i = 3 To pna.NumberOfPorts  
guidedCal.ConnectorType(i) = "Not used"  
Next  
value = MsgBox("Connectors defined for Ports 1 and 2")  
' Select the Cal Kit for each port being calibrated.  
guidedCal.CalKitType(1) = "85052D"  
guidedCal.CalKitType(2) = "85052D" ' To use an ECal module instead, comment
out the above two lines ' and uncomment the appropriate lines below: ' Your
ECal module must already be connected ' via USB to the VNA.
'guidedCal.CalKitType(1) = "N4691-60004 ECal" 'guidedCal.CalKitType(2) =
"N4691-60004 ECal" ' Non-factory characterizations are specified as follows:
'guidedCal.CalKitType(1) = "N4691-60004 User 1 ECal" ' When two or more ECal
modules with the same model number are connected ' also specify the serial
number as follows: 'guidedCal.CalKitType(1) = "N4691-60004 ECal 01234" ' When
Disk Memory ECal user characterizations are used, ' specify both the User char
and the serial number as follows: 'guidedCal.CalKitType(1) = "N4691-60004
MyDskChar ECal 01234" MsgBox("Cal kits defined for Ports 1 and 2") ' Initiate
the calibration and query the number of steps  
numSteps = guidedCal.GenerateSteps  
' Measure the standards, compute and apply the cal  
MeasureAndComplete(numSteps)  
End Sub  
  
Sub FourPortGuidedCal()  
' Select the connectors  
guidedCal.ConnectorType(1) = "APC 3.5 female"  
guidedCal.ConnectorType(2) = "APC 3.5 female"  
guidedCal.ConnectorType(3) = "APC 3.5 female"  
guidedCal.ConnectorType(4) = "APC 3.5 female"  
' If a VNA which has more than 4 ports  
For i = 5 To pna.NumberOfPorts  
guidedCal.ConnectorType(i) = "Not used"  
Next  
value = MsgBox("Connectors defined for Ports 1 to 4")  
' Select the Cal Kit for each port being calibrated.  
guidedCal.CalKitType(1) = "85052D"  
guidedCal.CalKitType(2) = "85052D"  
guidedCal.CalKitType(3) = "85052D"  
guidedCal.CalKitType(4) = "85052D"  
' To use an ECal module instead, comment out the above four lines  
' and uncomment the following four lines.  
' Replace N4691-60003 with your own ECAL model followed by 'ECal'.  
' Your ECal module must already be connected to a VNA USB port.  
' See above for ECal options 'guidedCal.CalKitType(1) = "N4431-60003 ECal"  
'guidedCal.CalKitType(2) = "N4431-60003 ECal"  
'guidedCal.CalKitType(3) = "N4431-60003 ECal"  
'guidedCal.CalKitType(4) = "N4431-60003 ECal"  
value = MsgBox("Cal kits defined for Ports 1 to 4")  
' Initiate the calibration  
guidedCal.GenerateSteps  
' If your selected cal kit is not a 4-port ECal module which can  
' mate to all 4 ports at once, then you may want to choose which  
' thru connections to measure for the cal. You must measure at  
' least 3 different thru paths for a 4-port cal (for greatest  
' accuracy you can choose to measure a thru connection for all 6  
' pairings of the 4 ports). If you omit this command, the default  
' is to measure from port 1 to port 2, port 1 to port 3, and  
' port 1 to port 4. For this example we select to measure  
' from port 1 to port 2, port 2 to port 3, and port 2 to port 4.  
portList = Array(1,2,2,3,2,4)  
guidedCal.ThruPortList = portList  
' Re-generate the connection steps to account for the thru changes  
numSteps = guidedCal.GenerateSteps  
' Measure the standards, compute and apply the cal  
MeasureAndComplete(numSteps)  
End Sub  
  
Sub MeasureAndComplete(ByVal numSteps)  
value = MsgBox("Number of steps is " \+ CStr(numSteps))  
  
' Measure the standards  
'The following series of commands shows that standards  
'can be measured in any order. These steps acquire  
'measurement of standards in reverse order.  
'It is easiest to iterate through standards using  
'a For-Next Loop.  
For i = NumSteps To 1  
step = "Step " \+ CStr(i) + " of " \+ CStr(numSteps)  
strPrompt = guidedCal.GetStepDescription(i)  
value = MsgBox(strPrompt, vbOKOnly, step)  
guidedCal.AcquireStep i  
Next  
  
' Conclude the calibration  
guidedCal.GenerateErrorTerms  
MsgBox ("Cal is done!")  
End Sub  
  
---  
  
* * *

