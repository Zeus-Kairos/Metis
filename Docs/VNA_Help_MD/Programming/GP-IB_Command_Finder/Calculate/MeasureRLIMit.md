# CALCulate:MEASure:RLIMit Commands

These commands are for setting up ripple tests.

CALCulate:MEASure:RLIMit DATA DISPlay | LINE | STATe | SELect | TYPe FAIL REPort | DATA STATe  
---  
  
Click a keyword to view the command details.

See Also

  * [Learn about Ripple tests](../../../Tutorials/Pass-Band_Measurements.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## CALCulate<cnum>:MEASure<mnum>:RLIMit:DATA <data>

Applicable Models: All (Read-Write) Sets or returns the ripple limit table for
the active trace of selected channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optinal).  
<mnum> | Measurement number for each measurement.   
<data> | Indicates the array data (for ripple line) of 1 + Num (number of limit lines)* 4\. Where n is an integer between 1 and Num.

  * Data(0) :The number of limit lines you want to set. Specify an integer ranging 0 to 12. When the number of limit lines is set to 0 (clears the limit table), the variable Data is only required with Data(0).
  * Data(nx4-3) :The type of the n-th line.

Specify an integer 0 to 1 as follows. 0: OFF 1: ON

  * Data(nx4-2) :The value on the horizontal axis (frequency/power/time) of the start point of the n-th line.
  * Data(nx4-1) :The value on the horizontal axis (frequency/power/time) of the end point of the n-th line.
  * Data(nx4) :The ripple line value (dB) of the n-th line.

The index of the array starts from 0.  
Examples | CALC:MEAS:RLIM:DATA  
calculate2:measure2:rlimit:data  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:RLIMit:DATA?  
Return Type | Variant type Array  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:RLIMit:DISPlay:LINE:STATe <bool>

Applicable Models: All (Read-Write) Turns ON/OFF the ripple limit line
display, for the active trace of selected channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optinal).  
<mnum> | Measurement number for each measurement.   
<bool> | ON or 1 \- Turns limit testing ON.  
OFF or 0 \- Turns limit testing OFF.  
Examples | CALC:MEAS:RLIM:DISP:LINE:STAT ON  
calculate2:measure2:rlimit:display:line:state off  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:RLIMit:DISPLay:LINE:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:RLIMit:DISPlay:SELect <band>

Applicable Models: All (Read-Write) Sets or gets the ripple limit band for
ripple value display for selected channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optinal).  
<mnum> | Measurement number for each measurement.   
<band> |  1 to 12  
Examples | CALC:MEAS:RLIM:DISP:RIPP:SEL calculate2:measure2:rlimit:display:ripple:select  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:RLIMit:DISPlay:SELect?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:RLIMit:DISPlay:TYPE <typ>

Applicable Models: All (Read-Write) Sets/gets the display type of ripple value
for the active trace of selected channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optinal).  
<mnum> | Measurement number for each measurement.   
<typ> | Select from the following:

  * "OFF": Specifies the display OFF.
  * "ABSolute": Specifies the absolute value for display type.
  * "MARgin": Specifies the margin for display type.

  
Examples | CALC:MEAS:RLIM:DISP:TYPE  
calculate2:measure2:rlimit:display:type  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:RLIMit:DISPLay:TYPE?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:RLIMit:FAIL

Applicable Models: All (Read-only) Read the ripple test result for the active
trace.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optinal).  
<mnum> | Measurement number for each measurement.   
<bool> | Boolean

  * 0 is returned when Pass
  * 1 is returned when Fail

  
Examples | CALC:MEAS:RLIM:FAIL?  
calculate2:measure2:rlimit:FAIL?  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:RLIMit:FAIL?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:RLIMit:REPort:DATA

Applicable Models: All (Read-only) Reads the ripple value of the ripple test
for the active trace.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optinal).  
<mnum> | Measurement number for each measurement.   
<data> | {numeric 1} ... {numeric NOP×3+1}<newline><^END> NOP is the number of measurement points.

  * {numeric 1}: Number of ripple limit line
  * {numeric n×3-1} : Number of ripple limit bands.
  * {numeric n×3} : Ripple value.
  * {numeric n×3+1} : Ripple test result (1: Fail, 0: Pass)

  
Examples | CALC:MEAS:RLIM:REP:DATA? calculate2:measure2:rlimit:report:data?  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:RLIMit:REPort:DATA?  
Return Type | Variant  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:RLIMit:STATe <bool>

Applicable Models: All (Read-Write) Turns ON/OFF the ripple test function for
the active trace of selected channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optinal).  
<mnum> | Measurement number for each measurement.   
<bool> | ON (or 1) - turns limit testing ON.  
OFF (or 0) - turns limit testing OFF.  
Examples | CALC:MEAS:RLIM:STAT ON  
calculate2:measure2:rlimit:state off  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:RLIMit:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

