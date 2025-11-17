# Perform a Guided 2-Port or 4-Port Cal using SCPI

* * *

This example performs a Guided 2-Port or 4-port Calibration using ONE set of
calibration standards or an ECAL module.

A measurement must first be set up with desired frequency range, power, and so
forth, ready to be calibrated.

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do NOT need a GPIB connection to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file, such as Notepad, and save it
on the VNA hard drive as *.vbs.

[Learn how to setup and run the macro.](../Using_Macros.md#HowToSetup)

[See Guided Cal SCPI commands](../GP-IB_Command_Finder/Sense/CorrGuided.md)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

Dim app  
Dim scpi  
' Create / Get the VNA application.  
Set app = CreateObject("AgilentPNA835x.Application")  
Set scpi = app.ScpiStringParser  
  
' To perform 2-port cal, Uncomment TwoPortGuidedCal()  
' Then comment FourPortGuidedCal()  
  
'Do 2-port Cal  
'TwoPortGuidedCal()  
  
'Do 4-port Cal  
FourPortGuidedCal  
  
Sub TwoPortGuidedCal()  
' Select the connectors  
scpi.Execute("sens:corr:coll:guid:conn:port1 ""APC 3.5 female"" ")  
scpi.Execute("sens:corr:coll:guid:conn:port2 ""APC 3.5 male"" ")  
scpi.Execute("sens:corr:coll:guid:conn:port3 ""Not used"" ")  
scpi.Execute("sens:corr:coll:guid:conn:port4 ""Not used"" ")  
MsgBox("Connectors defined for Ports 1 and 2") ' Select the Cal Kit for each
port being calibrated. scpi.Execute("sens:corr:coll:guid:ckit:port1 ""85052D""
") scpi.Execute("sens:corr:coll:guid:ckit:port2 ""85052D"" ") ' To use an ECal
module instead, comment out the above two lines ' and uncomment the
appropriate lines below: ' Your ECal module must already be connected ' via
USB to the VNA. 'scpi.Parse "sens:corr:coll:guid:ckit:port1 'N4691-60004
ECal'" 'scpi.Parse "sens:corr:coll:guid:ckit:port2 'N4691-60004 ECal'" ' Non-
factory characterizations are specified as follows: 'scpi.Parse
"sens:corr:coll:guid:ckit:port2 'N4691-60004 User 1 ECal'" ' When two or more
ECal modules with the same model number are connected ' also specify the
serial number as follows: 'scpi.Parse "sens:corr:coll:guid:ckit:port2
'N4691-60004 ECal 01234'" ' When Disk Memory ECal user characterizations are
used, ' specify both the User char and the serial number as follows:
'scpi.Parse "sens:corr:coll:guid:ckit:port2 'N4691-60004 MyDskChar ECal
01234'" ' MsgBox("Cal kits defined for Ports 1 and 2") ' Initiate the
calibration and query the number of steps  
numSteps = GenerateSteps()  
' Measure the standards, compute and apply the cal  
MeasureAndComplete(numSteps)  
End Sub  
  
Sub FourPortGuidedCal()  
' Select the connectors  
scpi.Execute("sens:corr:coll:guid:conn:port1 ""APC 3.5 female"" ")  
scpi.Execute("sens:corr:coll:guid:conn:port2 ""APC 3.5 female"" ")  
scpi.Execute("sens:corr:coll:guid:conn:port3 ""APC 3.5 female"" ")  
scpi.Execute("sens:corr:coll:guid:conn:port4 ""APC 3.5 female"" ")  
MsgBox("Connectors defined for Ports 1 to 4")  
' Select the Cal Kit for each port being calibrated.  
scpi.Execute("sens:corr:coll:guid:ckit:port1 ""85052D"" ")  
scpi.Execute("sens:corr:coll:guid:ckit:port2 ""85052D"" ")  
scpi.Execute("sens:corr:coll:guid:ckit:port3 ""85052D"" ")  
scpi.Execute("sens:corr:coll:guid:ckit:port4 ""85052D"" ")  
' To use an ECal module instead, comment out the above four lines  
' and uncomment these four lines and use the part number printed  
' on your module (which in our case was N4431-60003), followed  
' by the word 'ECal'. Your ECal module must already be connected  
' via USB to the VNA. ' see above for ECal options
'scpi.Execute("sens:corr:coll:guid:ckit:port1 ""N4431-60003 ECal"" ")  
'scpi.Execute("sens:corr:coll:guid:ckit:port2 ""N4431-60003 ECal"" ")  
'scpi.Execute("sens:corr:coll:guid:ckit:port3 ""N4431-60003 ECal"" ")  
'scpi.Execute("sens:corr:coll:guid:ckit:port4 ""N4431-60003 ECal"" ")  
MsgBox("Cal kits defined for Ports 1 to 4") ' Initiate the calibration and
query the number of steps  
numSteps = GenerateSteps()  
' If your selected cal kit is not a 4-port ECal module which can  
' mate to all 4 ports at once, then you may want to choose which  
' thru connections to measure for the cal. You must measure at  
' least 3 different thru paths for a 4-port cal (for greatest  
' accuracy you can choose to measure a thru connection for all 6  
' pairings of the 4 ports). If you omit this command, the default  
' is to measure from port 1 to port 2, port 1 to port 3, and  
' port 1 to port 4. For this example we select to measure  
' from port 1 to port 2, port 2 to port 3, and port 2 to port 4.  
scpi.Execute("sens:corr:coll:guid:thru:ports 1,2,2,3,2,4")  
' Re-generate the connection steps to account for the thru changes  
numSteps = GenerateSteps()  
' Measure the standards, compute and apply the cal  
MeasureAndComplete(numSteps)  
End Sub  
  
Function GenerateSteps()  
' Initiate the calibration and query the number of steps  
scpi.Execute("sens:corr:coll:guid:init")  
GenerateSteps = scpi.Execute("sens:corr:coll:guid:steps?")  
End Function  
  
Sub MeasureAndComplete(numSteps)  
MsgBox("Number of steps is " \+ CStr(numSteps))  
' Measure the standards  
For i = 1 To numSteps  
step = "Step " \+ CStr(i) + " of " \+ CStr(numSteps)  
strPrompt = scpi.Execute("sens:corr:coll:guid:desc? " \+ CStr(i))  
MsgBox strPrompt, vbOKOnly, step  
' Note: if you have set up a slow sweep speed (for example, if  
' youre using a narrow IF bandwidth) or youre using ECal, and  
' while a cal step is being measured you wish to have your program  
' perform other operations (like checking for the click event of a  
' Cancel button) and youre NOT using the COM ScpiStringParser,  
' you can use the optional ASYNchronous argument with the ACQuire  
' command as shown in this commented-out line below. The SCPI  
' parser then will return immediately while the cal step measurement  
' proceeds (i.e., the parser will NOT block-and-wait for the  
' measurement step to finish, so you can send additional commands  
' in the meantime). So you can do *ESR? or *STB? queries to  
' monitor the status register bytes to see when the OPC bit gets set,  
' which indicates the cal measurement step has finished. This OPC  
' detection works for all of the VNAs SCPI parsers except the COM  
' ScpiStringParser.  
' sens:corr:coll:guid:acq STAN + CStr(i) + ,ASYN;*OPC  
scpi.Execute("sens:corr:coll:guid:acq STAN" \+ CStr(i))  
Next  
' Conclude the calibration  
scpi.Execute("sens:corr:coll:guid:save")  
MsgBox ("Cal is done!")  
End Sub  
  
---  
  
* * *

* * *

