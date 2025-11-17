# Perform Guided TRL Calibration

* * *

This VBScript file performs a 2-Port Guided TRL calibration on 2-port VNA
analyzers. ([See an example of TRL cal on a 4-port
VNA](Perform_Unknown_Thru_or_TRL_Cal.htm).) This program does the following:

  * Clear old measurements from the VNA

  * Create a new S22 measurement

  * Set an instrument state

  * Select the connectors and cal kit

  * Initiate a Guided calibration

  * Display a prompt as each new standard must be connected

  * Save the calibration to a newly created cal set.

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do NOT need a GPIB connection to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as TRL.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm)

Dim App Dim Parser Dim Chan Dim txtDat Dim step Dim parserTxt Dim prompt Set
App = CreateObject("AgilentPNA835x.Application") ' Clear old measurements
App.Reset ' Create a new Measurement Set Parser = App.SCPIStringParser
Parser.Parse "DISPlay:WINDow1:STATE ON" Parser.Parse
"CALCulate:PARameter:DEFine:EXT 'MyMeas',S12" Parser.Parse
"DISPlay:WINDow1:TRACe1:FEED 'MyMeas'" ' Initialize state Set Chan =
App.ActiveChannel Chan.StartFrequency = 18.0e9 Chan.StopFrequency = 20.0e9
Chan.IFBandwidth = 1000 ' Begin a guided calibrations Parser.Parse
"SENS:CORR:COLL:GUID:CONN:PORT1 'APC 3.5 male'" Parser.Parse
"SENS:CORR:COLL:GUID:CONN:PORT2 'APC 3.5 female'" Parser.Parse
"SENS:CORR:COLL:GUID:CKIT:PORT1 '85052C'" Parser.Parse
"SENS:CORR:COLL:GUID:CKIT:PORT2 '85052C'" ' Select TRL cal method.
Parser.Parse "SENS:CORR:COLL:GUID:PATH:CMET 1,2,'TRL'" txtDat =
Parser.Parse("SENS:CORR:COLL:GUID:PATH:CMET? 1,2") MsgBox("Method " \+ txtDat)
Parser.Parse "SENS:CORR:COLL:GUID:INIT" ' Query the number of steps txtDat =
Parser.Parse("SENS:CORR:COLL:GUID:STEP?") ' Display the number of steps
MsgBox("Number of steps is " \+ txtDat) ' Set the loop counter limit step =
CInt(txtDat) ' Measure the standards For i = 1 To step parserTxt =
"sens:corr:coll:guid:desc? " \+ CStr(i) prompt = Parser.Parse(parserTxt)
MsgBox(prompt) parserTxt = "sens:corr:coll:guid:acq STAN" \+ CStr(i)
Parser.Parse (parserTxt) Next ' All standards have been measured. Save the
result Parser.Parse "SENS:CORR:COLL:GUID:SAVE" MsgBox("The TRL calibration has
been completed")  
---  
  
* * *

