# Perform Guided Mechanical Cal using SCPI

* * *

This VBScript program performs a Guided Calibration using Mechanical
standards. While this example is good to use as a starting point for guided
mechanical cal, the [Guided comprehensive cal
example](Perform_Guided_2-Port_Comprehensive_Cal.htm) has some advanced
features that are not in this program.

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do NOT need a GPIB connection to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as Guided.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm)

' Performing a 2-port cal (Ports 1 and 2)

Dim app  
Dim scpi  
  
' Create / Get the VNA application.  
Set app = CreateObject("AgilentPNA835x.Application")  
Set scpi = app.ScpiStringParser  
  
' Specify the DUT connectors  
scpi.Execute "sens:corr:coll:guid:conn:port1 ""APC 3.5 female"" "  
scpi.Execute "sens:corr:coll:guid:conn:port2 ""APC 3.5 male"" "  
  
' Note: If your VNA has more than 2 ports, you would need to uncomment  
' one or both of these next two lines, to explicitly specify this is  
' just a 2-port cal.  
'scpi.Execute "sens:corr:coll:guid:conn:port3 ""Not used"" "  
'scpi.Execute "sens:corr:coll:guid:conn:port4 ""Not used"" "  
MsgBox "Connectors defined for Ports 1 and 2"  
  
' Select the Cal Kit for each port being calibrated.  
scpi.Execute "sens:corr:coll:guid:ckit:port1 ""85052D"" "  
scpi.Execute "sens:corr:coll:guid:ckit:port2 ""85052D"" "  
MsgBox "Cal kits defined for Ports 1 and 2"  
  
' Initiate the calibration and query the number of steps  
scpi.Execute "sens:corr:coll:guid:init"  
numSteps = scpi.Execute("sens:corr:coll:guid:steps?")  
MsgBox "Number of steps is " \+ CStr(numSteps)  
  
' Measure the standards  
'The following series of commands shows that standards  
'can be measured in any order. These steps acquire  
'measurement of standards in reverse order.  
'It is easiest to iterate through standards using  
'a For-Next Loop.  
For i = numSteps To 1  
step = "Step " \+ CStr(i) + " of " \+ CStr(numSteps)  
strPrompt = scpi.Execute("sens:corr:coll:guid:desc? " \+ CStr(i))  
MsgBox strPrompt, vbOKOnly, step  
scpi.Execute "sens:corr:coll:guid:acq STAN" \+ CStr(i)  
Next  
  
' Conclude the calibration  
scpi.Execute "sens:corr:coll:guid:save"  
MsgBox "Cal is done!"

* * *

