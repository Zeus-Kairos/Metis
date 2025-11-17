# Upload a Source Power Cal using COM

* * *

This program can be run in either Visual Basic 6 or as a VBScript program. The
VNA can run *.vbs programs as [macros](../Using_Macros.md).

This program demonstrates:

  * Uploading a source power calibration of Port 2 for Channel 1.

  * Reading the calibration data.

Learn more about [Power Calibrations](../../S3_Cals/PwrCalibration.md)

[See Other COM Example Programs](COM_Example_Intro.md)

To run this program you need:

  * Your PC and VNA both connected to a LAN (for communicating with each other).

To make this program work in VBS, save the following code in a text editor
file such as Notepad and save as *.vbs.

To make this program work in Visual Basic 6:

  1. Create a new project

  2. Click Project, Add New Module, click Open.

  3. Paste the following code into the code window.

  4. Delete the first two lines (comment and Main)

  5. Click Project, Properties. Under Startup Object, select Sub Main

  6. Click Project, References, and select the Keysight PNA Series Type Library.

' Run the Main subroutine  
Main  
Public Sub Main()  
Dim PNA, chan ' VNA COM objects  
Const naCorrectionValues = 0 ' enum NASourcePowerCalBuffer  
Const port = 2 ' VNA port #2 as source port  
Dim stimulus, calvalues  
Dim power, calpower, strResult  
' Instantiate our VNA COM objects  
Set PNA = CreateObject("AgilentPNA835x.Application")  
Set chan = PNA.Channels(1)  
  
' Set the number of sweep points to 2 on Channel 1.  
chan.NumberOfPoints = 2  
  
' Ensure there's currently no source power cal on for this channel and port.  
chan.SourcePowerCorrection(port) = False  
  
' Specify if the cal power level is offset (positive value for a gain,
negative  
' value for a loss) from the VNA port power setting on the channel when  
' no source power cal is active. This is to account for components  
' between the VNA test port and cal reference plane.  
' In this example, let's set up our calibration  
' at the output of an amplifier with 15 dB gain.  
chan.SourcePowerCalPowerOffset(port) = 15  
  
' Send our source power correction data to the VNA. For purpose of simplicity  
' in this example, we'll set up for no correction (0) at our start stimulus
and  
' 0.5 dB at our stop stimulus (recall that our sweep currently has just 2
points).  
calvalues = Array(0, 0.5)  
chan.putSourcePowerCalDataEx naCorrectionValues, port, calvalues  
  
' Set the number of sweep points to 21 on Channel 1.  
chan.NumberOfPoints = 21  
  
' Read the fixed power level for this port on Channel 1.  
power = chan.TestPortPower(port)  
  
' Turn the source power cal on.  
chan.SourcePowerCorrection(port) = True  
  
' Again read the fixed power level for this port on Channel 1  
' (with our calibration turned on, this should now include the 15 dB offset  
' we indicated our power amplifier provides).  
calpower = chan.TestPortPower(port)  
  
' Read the stimulus values from Channel 1.  
stimulus = chan.GetXAxisValues  
  
' Read back the source power correction data, now interpolated for 21 points  
calvalues = chan.getSourcePowerCalDataEx(naCorrectionValues, port)  
  
' Print the data using a message box (here, Chr returns the ASCII characters  
' for Tab (9) and Linefeed (10)).  
strResult = "PNA port power = " & power & Chr(10)  
strResult = strResult & "Power at reference plane = " & calpower & Chr(10) &
hr(10)  
strResult = strResult & "Stimulus" & Chr(9) & Chr(9) & "Cal Value" & Chr(10)  
For i = 0 To UBound(stimulus)  
strResult = strResult & stimulus(i) & Chr(9) & calvalues(i) & Chr(10)  
Next  
MsgBox strResult  
End Sub

