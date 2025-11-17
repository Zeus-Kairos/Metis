# Set ECal States

* * *

This example cycles through the state settings on the first ECal module it
finds on the USB bus.

The state settings include all of the ECal states on Port A, Port B and the AB
thru path. The first state on a port-pair path such as AB is the thru state
that is used during calibrations. The second state on that path is the
"confidence state" which is the equivalent of an attenuator that is used by
the ECal Confidence Check feature.

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do NOT need a GPIB connection to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file, such as Notepad, and save it
on the VNA hard drive as *.vbs.

[Learn how to setup and run the macro.](../Using_Macros.md#HowToSetup)

[See ECal State commands](../GP-IB_Command_Finder/Control.md#EcalPathState)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

Option Explicit Dim app Set app = CreateObject("AgilentPNA835x.Application")
Dim scpi Set scpi = app.ScpiStringParser Dim moduleIndexList ' These are
1-based indices as opposed to 0-based, ' so if this query returns 0 it
indicates there appear ' to be no ECal modules connected. moduleIndexList =
Split( scpi.Parse("SENS:CORR:CKIT:ECAL:LIST?"), ",") If
CInt(moduleIndexList(0)) = 0 Then MsgBox "No ECal module was found"
WScript.Quit(0) End If SetStates("A") SetStates("B") SetStates("AB") MsgBox
"Done" Sub SetStates(path) Dim pathNumStates pathNumStates = CInt(
scpi.Parse("CONT:ECAL:MOD1:PATH:COUN? " \+ path) ) Dim stateNum For stateNum =
1 To pathNumStates Dim stateNumStr stateNumStr = CStr(stateNum) Dim pathDescr
If Len(path) = 1 Then pathDescr = "port " \+ path Else pathDescr = "path " \+
path End If Dim isOK isOK = MsgBox("Click OK to switch to state number " \+
stateNumStr + " of " \+ pathDescr, vbOKCancel) If isOK = vbCancel Then
WScript.Quit(0) scpi.Parse "CONT:ECAL:MOD1:PATH:STAT " \+ path + "," \+
stateNumStr Next End Sub  
---  
  
* * *

* * *

