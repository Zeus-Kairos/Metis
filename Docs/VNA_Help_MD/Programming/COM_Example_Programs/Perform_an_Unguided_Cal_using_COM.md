# Perform an Unguided Cal using COM

* * *

This example uses the
[ICalibrator](../COM_Reference/Objects/Calibrator_Object.md) interface to do
the following:

  * perform a two port calibration

  * retrieve the error term data

  * retrieve the standard data (cal acquisition data)

Learn more about [Reading and Writing Calibration data using
COM.](../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)

[See Other COM Example Programs](COM_Example_Intro.md)

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save on
the VNA hard drive as Calibrate.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

dim pna  
' To run from an external PC, substitute your VNA Name and use the following
command.  
' set pna = CreateObject("AgilentPNA835x.Application", "VNA Name")  
set pna = CreateObject("AgilentPNA835x.Application")  
dim calibrator  
set calibrator=pna.activechannel.calibrator  
  
wscript.echo "setcalinfo for two port cal"  
calibrator.setcalinfo 5,1, 2  
  
' only have one set of standards  
calibrator.Simultaneous2PortAcquisition = false  
  
'first acquire forward reflection standards, then reverse  
dim p  
for p = 1 to 2  
  
if (p = 1) then  
calibrator.AcquisitionDirection = 0  
else  
calibrator.AcquisitionDirection = 1  
end if  
  
wscript.echo "connect open to port ", p  
calibrator.acquirecalstandard 1  
  
wscript.echo "connect short to port ", p  
calibrator.acquirecalstandard 2  
  
wscript.echo "connect load to port ", p  
calibrator.acquirecalstandard 3  
  
next  
  
wscript.echo "connect a thru1"  
calibrator.acquirecalstandard 4  
  
'Optional - perform isolation  
wscript.echo "connect loads to both ports"  
calibrator.acquirecalstandard 5  
  
wscript.echo "calculating"  
calibrator.CalculateErrorCoefficients  
  
'Calibration complete  
' Now read error terms and standard data  
  
dim termName  
termName= Array("Directivity","SourceMatch","ReflectionTracking")  
dim vardata  
  
' iterate over error terms  
dim t  
for t = 0 to 2 ' per error term  
for p = 1 to 2 ' per port  
wscript.echo "Requesting ",termName(t),p,p  
vardata = calibrator.GetErrorTerm( t, p, p)  
next  
next  
  
' now get the path terms: iterator each one request  
termName = Array("Isolation", "LoadMatch", "TransmissionTracking")  
for t = 0 to 2  
  
wscript.echo "Requesting Forward term",termName(t),1,2  
vardata = calibrator.GetErrorTerm( t, 1,2)  
wscript.echo "Requesting Reverse Term",termName(t),2,1  
vardata = calibrator.GetErrorTerm( t, 2,1)  
next  
  
dim stdname  
stdname= Array("","Open","Short","Load","Thru","Isolation")  
  
' iterate over the port standards  
for t = 1 to 3  
for p = 1 to 2  
' request the standard term for each port of interest  
wscript.echo "Requesting",stdname(t),p,p  
  
vardata = calibrator.GetStandard( t, p, p)  
next  
next  
  
' now get the path standards: iterator each one request  
for t = 4 to 5  
  
wscript.echo "Requesting Forward",stdname(t),1,2  
vardata = calibrator.GetStandard( t, 1,2)  
  
wscript.echo "Requesting Reverse",stdname(t),2,1  
vardata = calibrator.GetStandard( t, 2,1)  
  
next  

