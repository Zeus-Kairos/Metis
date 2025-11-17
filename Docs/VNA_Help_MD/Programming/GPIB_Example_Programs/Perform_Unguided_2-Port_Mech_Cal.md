# Perform an Unguided 2-Port Mechanical Cal

* * *

This VBScript program performs an Unguided, Full 2-Port, calibration using ONE
set of mechanical calibration standards.

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do NOT need a GPIB connection to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as Unguided.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm)

Set App = CreateObject("AgilentPNA835x.Application")  
Set Scpi = App.SCPIStringParser  
  
'Initialize state  
Scpi.Execute ("SYSTem:PRESet")  
  
'Select the Preset measurement  
Scpi.Execute ("CALCulate:PARameter:SELect 'CH1_S11_1'")  
  
'Set the calibration method  
Scpi.Execute ("SENSe:CORRection:COLLect:METHod SPARSOLT")  
  
'Select a cal kit  
Scpi.Execute ("SENSe:CORRection:COLLect:CKIT:SELect 1")  
  
'Set one set of standards  
Scpi.Execute ("SENSe:CORRection:TSTandards OFF")  
  
'Set acquisition to FORWARD  
Scpi.Execute ("SENSe:CORRection:SFORward ON")  
  
'Measure the standards in forward direction  
MsgBox "Connect OPEN to Port 1; then press OK"  
Scpi.Execute ("SENSe:CORRection:COLLect:ACQuire stan1")  
  
MsgBox "Connect SHORT to Port 1; then press OK"  
Scpi.Execute ("SENSe:CORRection:COLLect:ACQuire stan2")  
  
MsgBox "Connect LOAD to Port 1; then press OK"  
Scpi.Execute ("SENSe:CORRection:COLLect:ACQuire stan3")  
  
'Set acquisition to REVERSE  
Scpi.Execute ("SENSe:CORRection:SFORward OFF")  
  
'Measure the standards in reverse direction  
MsgBox "Connect OPEN to Port 2; then press OK"  
Scpi.Execute ("SENSe:CORRection:COLLect:ACQuire stan1")  
  
MsgBox "Connect SHORT to Port 2; then press OK"  
Scpi.Execute ("SENSe:CORRection:COLLect:ACQuire stan2")  
  
MsgBox "Connect LOAD to Port 2; then press OK"  
Scpi.Execute ("SENSe:CORRection:COLLect:ACQuire stan3")  
  
'Measure the thru standard  
MsgBox "Connect THRU between Ports 1 and 2; then press OK"  
Scpi.Execute ("SENSe:CORRection:COLLect:ACQuire stan4")  
  
'OPTIONAL Measure Isolation  
MsgBox "Connect LOADS to Port 1 AND Port 2; then press OK"  
Scpi.Execute ("SENSe:CORRection:COLLect:ACQuire stan5")  
  
'All standards have been measured. Save the result  
Scpi.Execute ("SENS:CORR:COLL:SAVE")  
MsgBox "The calibration has been completed"  

