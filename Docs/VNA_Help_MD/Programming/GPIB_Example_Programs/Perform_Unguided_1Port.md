# Perform an Unguided 1-Port Cal on Port 2

* * *

This VBScript program does the following:

  1. Clear measurements from the VNA

  2. Create a new S22 measurement

  3. Set an instrument state

  4. Select a cal kit

  5. Initiate an Unguided calibration

  6. Display a prompt to connect each standard

  7. Save the calibration to a newly created cal set

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
the VNA hard drive as Unguided.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm)

Dim App  
Set App = CreateObject("AgilentPNA835x.Application")  
App.Preset  
  
Dim Parser  
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
  
Rem Begin an unguided calibration  
Rem Set the calibration method  
Parser.Parse "SENSe:CORRection:COLLect:METHod REFL3"  
  
Rem Turn off continuous sweep  
Parser.Parse "INITiate:CONTinuous OFF"  
  
Rem Select a cal kit  
Parser.Parse "SENSe:CORRection:COLLect:CKIT:SELect 1"  
  
Rem Measure the standards  
MsgBox("Connect OPEN to port 2. Then press OK")  
Parser.Parse ("sens:corr:coll:acq STAN1")  
  
MsgBox("Connect SHORT to port 2. Then press OK")  
Parser.Parse ("sens:corr:coll:acq STAN2")  
  
MsgBox("Connect LOAD to port 2. Then press OK")  
Parser.Parse ("sens:corr:coll:acq STAN3")  
  
Rem All standards have been measured. Save the result  
Parser.Parse "SENS:CORR:COLL:SAVE"  
  
Rem Turn ON continuous sweep  
Parser.Parse "INITiate:CONTinuous ON"  
MsgBox("The calibration has been completed")  

