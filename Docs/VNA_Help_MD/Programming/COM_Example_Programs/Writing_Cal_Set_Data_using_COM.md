# Writing Cal Set Data using COM

* * *

This example creates a Cal Set and then writes data to the Cal Set.

Learn more about [Reading and Writing Calibration data using
COM.](../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)

Learn more about [Cal Sets.](../../S3_Cals/Cal_Sets.md)

See example: [Reading Calset Data](COM_Reading_CalSet_Examples.md)

[See Other COM Example Programs](COM_Example_Intro.md)

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save on
the VNA hard drive as CalSetsWrite.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

dim pna  
dim v  
Set pna=CreateObject("AgilentPNA835x.Application")  
InitPhonyData  
PutPhonyData  
' This sub creates phony data  
Sub InitPhonyData()  
Dim i  
Dim numpts  
wscript.echo "init phony"  
numpts = pna.ActiveChannel.NumberOfPoints  
ReDim v(numpts - 1, 1)  
For i = 0 To numpts - 1  
v(i, 0) = i  
v(i, 1) = 0  
Next  
End Sub  
  
' This sub creates a Cal Set, then writes the phony data to it  
Sub PutPhonyData()  
Dim cmgr  
Dim cset  
wscript.echo "putphony"  
Set cmgr = pna.GetCalManager  
Set cset = cmgr.CreateCalSet(1)  
cset.OpenCalSet naCalType_OnePort, 1  
const directivity = 0  
const sourcematch=1  
const reflectiontracking =2  
cset.putErrorTerm directivity,1, 1, v  
cset.putErrorTerm sourcematch,1, 1, v  
cset.putErrorTerm reflectiontracking ,1, 1, v  
cset.CloseCalSet  
cset.Description = "Phony One Port"  
cset.save  
End Sub  

