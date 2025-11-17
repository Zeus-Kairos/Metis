# Perform a Guided Cal with Sliding Load

* * *

This example sets the sliding load behavior, then performs a Guided
Calibration that uses a sliding load.

A measurement must first be set up with desired frequency range, power, and so
forth, ready to be calibrated.

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do not need to control the VNA via GPIB to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file, such as Notepad, and save it
on the VNA hard drive as guided.vbs.

[Learn how to setup and run the macro.](../Using_Macros.md#HowToSetup)

See [Guided Cal commands.](../GP-IB_Command_Finder/Sense/CorrGuided.md)

Set app = CreateObject("AgilentPNA835x.Application") Set scpi =
app.ScpiStringParser ' Specify that any sliding loads should be measured using
the ' remote iterative method rather than launching sliding load dialog.
scpi.Execute "sens:corr:coll:guid:pref:slid iter" scpi.Execute
"sens:corr:coll:guid:conn:port1 ""APC 3.5 female"" " scpi.Execute
"sens:corr:coll:guid:conn:port2 ""APC 3.5 male"" "  85052B cal kit uses
sliding loads scpi.Execute "sens:corr:coll:guid:ckit:port1 ""85052B"" "
scpi.Execute "sens:corr:coll:guid:ckit:port2 ""85052B"" " scpi.Execute
"sens:corr:coll:guid:init" numSteps =
scpi.Execute("sens:corr:coll:guid:steps?") ' Measure the standards For i = 1
To numSteps step = "Step " \+ CStr(i) + " of " \+ CStr(numSteps) strPrompt =
scpi.Execute("sens:corr:coll:guid:desc? " \+ CStr(i)) MsgBox strPrompt,
vbOKOnly, step minIterations = scpi.Execute("sens:corr:coll:guid:iter:min? "
\+ CStr(i)) For j = 1 To minIterations If minIterations > 1 Then MsgBox
Adjust/position the standard for measurement  + CStr(j) +  of  +
CStr(minIterations), vbOKOnly scpi.Execute "sens:corr:coll:guid:acq STAN" \+
CStr(i) Next iterationCount = scpi.Execute("sens:corr:coll:guid:iter:coun? "
\+ CStr(i)) If iterationCount <> minIterations Then MsgBox Unexpected
error!, vbOKOnly, step scpi.Execute "sens:corr:coll:guid:iter:res " \+
CStr(i) End If Next ' Conclude the calibration scpi.Execute
"sens:corr:coll:guid:save"  
---  
  
* * *

