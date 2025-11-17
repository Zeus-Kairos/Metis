# Perform a Guided QSOLT Cal

* * *

This example performs a Guided QSOLT calibration on a 4-port VNA.

Because the DUT port 1 is female and the other ports are male, a 'Zero Thru'
can be used between port 1 and the other ports. If this were NOT the case, a
"Defined Thru" would be needed in the listed Cal Kits for those ports. [Learn
more about Thru methods](../../S3_Cals/Calibration_THRU_Methods.htm).

Although no standards are used for ports 2, 3, and 4, a Cal Kit must be
defined for these ports.

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do not need to control the VNA via GPIB to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file, such as Notepad, and save it
on the VNA hard drive as qsolt.vbs.

### See Also

[Learn more about QSOLT.](../../S3_Cals/Select_Cal.md#QSOLT)

[Learn how to setup and run the macro.](../Using_Macros.md#HowToSetup)

See [Guided Cal commands.](../GP-IB_Command_Finder/Sense/CorrGuided.md)

Set app = CreateObject("AgilentPNA835x.Application") Set scpi =
app.ScpiStringParser scpi.Execute "Calc1:Par:Mnum 1" scpi.Execute
"Sens1:CORR:COLL:GUID:CONN:PORT1:SEL 'APC 3.5 female'" scpi.Execute
"Sens1:CORR:COLL:GUID:CONN:PORT2:SEL 'APC 3.5 male'" scpi.Execute
"Sens1:CORR:COLL:GUID:CONN:PORT3:SEL 'APC 3.5 male'" scpi.Execute
"Sens1:CORR:COLL:GUID:CONN:PORT4:SEL 'APC 3.5 male'" scpi.Execute
"Sens1:CORR:COLL:GUID:CKIT:PORT1:SEL '85052B'" scpi.Execute
"Sens1:CORR:COLL:GUID:CKIT:PORT2:SEL '85052B'" scpi.Execute
"Sens1:CORR:COLL:GUID:CKIT:PORT3:SEL '85052B'" scpi.Execute
"Sens1:CORR:COLL:GUID:CKIT:PORT4:SEL '85052B'" scpi.Execute
"Sens1:CORR:COLL:GUID:THRU:PORT 1,2,1,3,1,4" scpi.Execute
"Sens1:CORR:COLL:GUID:PATH:TMET 1,2,'Zero Thru'" scpi.Execute
"Sens1:CORR:COLL:GUID:PATH:TMET 1,3,'Zero Thru'" scpi.Execute
"Sens1:CORR:COLL:GUID:PATH:TMET 1,4,'Zero Thru'" scpi.Execute
"Sens1:CORR:COLL:GUID:PATH:CMET 1,2,'QSOLT1'" scpi.Execute
"SENS1:CORR:COLL:GUID:PATH:CMET 1,3,'QSOLT1'" scpi.Execute
"SENS1:CORR:COLL:GUID:PATH:CMET 1,4,'QSOLT1'" ' Initiate the calibration and
query the number of steps scpi.Execute "sens1:corr:coll:guid:init" numSteps =
scpi.Execute("sens:corr:coll:guid:steps?") MsgBox "Number of steps is " \+
CStr(numSteps) ' Measure the standards For i = 1 To numSteps step = "Step " \+
CStr(i) + " of " \+ CStr(numSteps) strPrompt =
scpi.Execute("sens:corr:coll:guid:desc? " \+ CStr(i)) MsgBox strPrompt,
vbOKOnly, step scpi.Execute "sens:corr:coll:guid:acq STAN" \+ CStr(i) Next '
Conclude the calibration scpi.Execute "SENS1:CORR:COLL:GUID:SAVE"  
---  
  
* * *

