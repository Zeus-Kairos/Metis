# Perform a Guided 1-Port Cal on Port 2

* * *

This VBScript program does the following:

  1. Clear measurements from the VNA

  2. Create a new S22 measurement

  3. Set an instrument state

  4. Select the connector types

  5. Select a cal kit

  6. Initiate a Guided calibration

  7. Display a prompt to connect each standard

  8. Save the calibration to a newly created cal set

Note: This example illustrates an important step when calibrating a reflection
measurement in the reverse direction. You MUST create a reverse (S22)
measurement and have it be the active (selected) measurement on the channel
that is being calibrated. This is not necessary for any calibrating any other
measurement parameter.

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do NOT need a GPIB connection to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as Guided.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm)

Dim App  
Set App = CreateObject("AgilentPNA835x.Application")  
App.Preset  
  
Dim step  
Dim Parser  
Dim prompt  
Dim txtDat  
Dim Chan  
  
Rem Clear old measurements  
App.Reset  
  
Rem Create a new Measurement  
Set Parser = App.SCPIStringParser  
Parser.Parse "DISPlay:WINDow1:STATE ON"  
Parser.Parse "CALCulate:PARameter:DEFine:EXT 'MyMeas',S22"  
Parser.Parse "DISPlay:WINDow1:TRACe1:FEED 'MyMeas'"  
  
Rem Initialize state  
Set Chan = App.ActiveChannel  
Chan.StartFrequency = 200e6  
Chan.StopFrequency = 1.5e9  
Chan.IFBandwidth = 1000  
step = 3  
  
Rem Begin a guided calibration  
Parser.Parse "SENS:CORR:COLL:GUID:CONN:PORT1 'Not used'"  
Parser.Parse "SENS:CORR:COLL:GUID:CONN:PORT2 'Type N (50) male'"  
Parser.Parse "SENS:CORR:COLL:GUID:CKIT:PORT1 ''"  
Parser.Parse "SENS:CORR:COLL:GUID:CKIT:PORT2 '85054D'"  
Parser.Parse "SENS:CORR:COLL:GUID:INIT"  
  
Rem Query the number of steps  
txtDat = Parser.Parse("SENS:CORR:COLL:GUID:STEP?")  
  
Rem Display the number of steps  
MsgBox("Number of steps is " \+ txtDat)  
  
Rem Set the loop counter limit  
step = txtDat  
  
Rem Measure the standards  
For i = 1 To step  
If i= 1 Then  
prompt = Parser.Parse("sens:corr:coll:guid:desc? 1")  
MsgBox(prompt)  
Parser.Parse ("sens:corr:coll:guid:acq STAN1")  
ElseIf i = 2 then  
prompt = Parser.Parse("sens:corr:coll:guid:desc? 2")  
MsgBox(prompt)  
Parser.Parse ("sens:corr:coll:guid:acq STAN2")  
ElseIf i = 3 then  
prompt = Parser.Parse("sens:corr:coll:guid:desc? 3")  
MsgBox(prompt)  
Parser.Parse ("sens:corr:coll:guid:acq STAN3")  
End If  
Next  
  
Rem All standards have been measured. Save the result  
Parser.Parse "SENS:CORR:COLL:GUID:SAVE"  
MsgBox("The calibration has been completed")  

