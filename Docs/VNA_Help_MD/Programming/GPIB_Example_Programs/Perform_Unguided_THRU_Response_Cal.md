# Perform Unguided THRU Response Cal

* * *

This example program performs Thru Response cals in both the forward and
reverse directions. It does this by selecting the appropriate measurement
right before acquiring the standard. The cal infers the direction from the
measurement.

This program also demonstrates the use of the
[SENSe:CORR:PREF:CSET:SAVE](../GP-
IB_Command_Finder/Sense/Sense_Correction.htm#CsetSave) command. The details
are in the comments.

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do NOT need a GPIB connection to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as Unguided.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm)

Dim App Set App = CreateObject("AgilentPNA835x.Application") Dim Parser Set
Parser = App.SCPIStringParser 'Preset and delete measurement Parser.Parse
"SYSTem:FPReset" 'The following commands determine how the cal set is saved.
'Pick one of the following preferences, comment the other 'Save cals to
separate new USER CalSets 'Parser.Parse "SENS:CORR:PREF:CSET:SAVE USER" 'Save
both cals to a single cal register 'Parser.Parse "SENS:CORR:PREF:CSET:SAVE
CALR" 'Save both cals to a single currently selected CalSet or register
Parser.Parse "SENS:CORR:PREF:CSET:SAVE REUSE" ' 'Create a new S21 Measurement
Parser.Parse "CALCulate:PARameter:DEFine:EXT 'MyS21Meas',S21" Parser.Parse
"DISPlay:WINDow1 ON" Parser.Parse "DISPlay:WINDow1:TRACe1:FEED 'MyS21Meas'"
'Create a new S12 Measurement Parser.Parse "CALCulate:PARameter:DEFine:EXT
'MyS12Meas',S12" Parser.Parse "DISPlay:WINDow1:TRACe2:FEED 'MyS12Meas'" 'Turn
off continuous sweep Parser.Parse "INITiate:CONTinuous OFF" 'Begin cals
'Select a cal kit Parser.Parse "SENSe:CORRection:COLLect:CKIT:SELect 1"
'Perform a forward thru response cal 'Select the S21 Meas Parser.Parse
"CALCulate1:PARameter:SELect 'MyS21Meas'" 'Set the calibration method to Thru
Response Parser.Parse "SENSe1:CORRection:COLLect:METHod TRAN1" MsgBox("Connect
Thru between ports Then press OK") Parser.Parse
"SENSe1:CORRection:COLLect:ACQuire STAN4" Parser.Parse
"SENSe1:CORRection:COLLect:SAVE" 'Then perform a reverse thru response cal
'Change measurement to S12 Parser.Parse "CALCulate1:PARameter:SELect
'MyS12Meas'" 'Set the calibration method to Thru Response Parser.Parse
"SENSe1:CORRection:COLLect:METHod TRAN1" 'Ensure the thru connection is still
in place 'Acquire Thru std in reverse direction Parser.Parse
"SENSe1:CORRection:COLLect:ACQuire STAN4" 'All standards have been measured.
Parser.Parse "SENSe1:CORRection:COLLect:SAVE" 'Turn ON continuous sweep
Parser.Parse "INITiate:CONTinuous ON" MsgBox("The calibration has been
completed")  
---

