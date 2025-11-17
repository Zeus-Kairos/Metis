# Perform Global Delta Match Cal

* * *

The following program performs a [Global Delta Match
Calibration.](../../S3_Cals/Delta_Match_Calibration.htm#Global) This may be
required when performing an Unknown Thru Cal or TRL Cal on PNA-L models. [See
example of Unknown Thru or TRL Cal.](Perform_Unknown_Thru_or_TRL_Cal.htm)

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as Delta.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

Sub PerformGlobalDeltaMatchCal()  
Set pna = CreateObject("AgilentPNA835x.Application")  
Set scpi = pna.ScpiStringParser  
  
' Initiate a Global Delta Match calibration, choosing connector and cal kit  
scpi.Parse "SENS:CORR:COLL:GUID:DMAT 'APC 3.5 female', '85033D/E'"  
  
' Query the number of calibration steps  
retStr = scpi.Parse("SENS:CORR:COLL:GUID:STEP?")  
numSteps = CInt(retStr)  
  
' Measure the cal standards  
For i = 1 To numSteps  
prompt = scpi.Parse("SENS:CORR:COLL:GUID:DESC? " & CStr(i))  
retVal = MsgBox(prompt, vbOKCancel)  
If retVal = vbCancel Then Exit Sub  
retStr = scpi.Parse("SENS:CORR:COLL:GUID:ACQ STAN" & CStr(i) & ";*OPC?")  
Next  
  
' Compute the error coefficients and save the cal to Global Delta Match CalSet  
scpi.Parse "SENS:CORR:COLL:GUID:SAVE"  
MsgBox "Cal is done!"  
End Sub

