# CALCulate:MEASure:BLIMit Commands

These commands are for setting up bandwidth tests.

CALCulate:MEASure:BLIMit BWIDth | THReshold DISPlay | MARKer | STATe FAIL? MAXimum MINimum REPort | DATA? [:STATe]  
---  
  
Click a keyword to view the command details.

See Also

  * [Calibrating with SCPI](../../Learning_about_GPIB/Calibrating_the_Analyzer_Using_SCPI.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## CALCulate<cnum>:MEASure<mnum>:BLIMit:BWIDth:THReshold <value>

Applicable Models: All (Read-Write) Sets bandwidth threshold value
(attenuation from the peak) of the bandwidth test.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<value> | Bandwidth N dB points  
Examples | CALC:MEAS:BLIM:BWID:THR 5  
calculate2:measure2:blimit:display:bwidth:threshold 5  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:BLIMit:BWIDth:THReshold?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 3  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:BLIMit:DISPlay:MARKer:STATe <bool>

Applicable Models: All (Read-Write) Turns ON/OFF the bandwidth value display
of the bandwidth test, for the active trace of selected channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<bool> | ON or 1 \- Turns limit testing ON.  
OFF or 0 \- Turns limit testing OFF.  
Examples | CALC:MEAS:BLIM:DISP:MARK:STAT ON  
calculate2:measure2:blimit:display:marker:state off  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:BLIMit:DISPLay:BWIDth:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:BLIMit:FAIL?

Applicable Models: All (Read-only) Get the bandwidth limit test results, for
the active trace of selected channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<bool> | Boolean

  * 0 is returned when Pass
  * 1 is returned when Fail

  
Examples | CALC:MEAS:BLIM:FAIL?  
calculate2:measure2:blimit:fail?  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:BLIMit:FAIL?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:BLIMit:MAXimum <max>

Applicable Models: All (Read-Write) Sets/gets the upper limit value of the
bandwidth test, for the selected channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<max> | Maximum bandwidth  
Examples | CALC:MEAS:BLIM:MAX 1E6  
calculate2:measure2:blimit:maximum 1E6  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:BLIMit:MAXimum?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 300000  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:BLIMit:MINimum <min>

Applicable Models: All (Read-Write) Sets or returns the lower limit value of
the bandwidth test, for the selected channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<min> | Minimum bandwidth  
Examples | CALC:MEAS:BLIM:MIN 1E6  
calculate2:measure2:blimit:minimum 1E6  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:BLIMit:MINimum?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 10000  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:BLIMit:REPort:DATA?

Applicable Models: All (Read-only) Read the bandwidth value of the bandwidth
test, for the active trace of selected channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS:BLIM:REP:DATA?  
calculate2:measure2:blimit:report:data?  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:BLIMit:REPort:DATA?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:BLIMit[:STATe]

Applicable Models: All (Read-Write) Turns ON/OFF the bandwidth test function,
for the active trace of selected channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<bool> | ON or 1 \- Turns limit testing ON.  
OFF or 0 \- Turns limit testing OFF.  
Examples | CALC:MEAS:LIM:STAT ON  
calculate2:measure2:limit:state off  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:BLIMit:DIPLay:MARKer:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

