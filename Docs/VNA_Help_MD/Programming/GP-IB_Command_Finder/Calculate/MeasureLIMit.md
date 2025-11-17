# CALCulate:MEASure:LIMit Commands

Controls the limit segments used for pass / fail testing.

CALCulate:MEASure:LIMit DATA | DELete DISPlay | [:STATe] FAIL? REPort | ALL? | [:DATA]? | POINts? SEGMent | AMPLitude | STARt | STOP | COUNt? | STIMulus | STARt | STOP | TYPE SOUNd | [:STATe] [:STATe]  
---  
  
Click a keyword to view the command details.

See Also

  * [Learn about Limit Lines](../../../S4_Collect/Use_Limits_to_Test_Devices.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## CALCulate<cnum>:MEASure<mnum>:LIMit:DATA <block>

Applicable Models: All (Read-Write) Sets data for limit segments.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<block> | Data for all limit segments. The following is the data format for 1 segment:  
Type,BegStim, EndStim, BegResp,EndResp | Type | Type of limit segment. Choose from  
0 - Off  
1 - Max  
2 - Min  
---|---  
BegStim | Start of X-axis value (freq, power, time)  
EndStim | End of X-axis value  
BegResp | Y-axis value that corresponds with Start of X-axis value  
EndResp | Y-axis value that corresponds with End of X-axis value  
Examples | The following writes three max limit segments for a bandpass filter. CALC:MEAS2:LIM:DATA 1,3e5,4e9,-60,0,1,4e9,7.5e9,0,0,1,7.5e9,9e9,0,-30  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:LIMit:DATA?  
Return Type | Depends on [FORM:DATA](../Format_SCPI.md#fd)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Maximum limit = 100  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:LIMit:DATA:DELete

Applicable Models: All (Write-only) Deletes all limit line data for the
selected measurement on the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC2:MEAS2:LIM:DATA:DEL  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:LIMit:DISPlay[:STATe] <ON | OFF>

Applicable Models: All (Read-Write) Turns the display of limit segments ON or
OFF (if the data trace is turned ON).  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<ON | OFF> | ON (or 1) - turns the display of limit segments ON.  
OFF (or 0) - turns the display of limit segments OFF.  
Examples | CALC:MEAS2:LIM:DISP:STAT ON  
calculate2:limit:display:state off  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:LIMit:DISPlay[:STATe]?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:LIMit:FAIL?

Applicable Models: All (Read-only) Returns the Pass / Fail status of the limit
line test. Returns 1 (Fail) if any data point fails for any limit segment.
Limit display (CALC:LIM:DISP) does NOT have to be ON.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2LIM:FAIL?  
Return Type | Boolean

  * 0 is returned when Pass
  * 1 is returned when Fail

  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:LIMit:REPort:ALL? <block>

Applicable Models: All (Read-only) Returns the test results (stimulus value,
limit test result, upper limit value and lower limit value of all measurement
points), for the selected trace. This command returns a point by point
description of the limit table and pass/fail test result.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<block> | Depends on [FORM:DATA](../Format_SCPI.md#fd) If the number of the measurement points is N, <Block> = <first stimulus>,<test result>,<upper limit>,<lower limit>, , <Nth stimulus>,<test result>,<upper limit>,<lower limit> Where <test result>= -1: No limit, 0:Fail, 1:Pass  
Examples | The following example returns three points: CALC:MEAS2:LIM:REP:ALL? +1.00000000000E+009, 'bucket 1 XAxis value +1.00000000000E+000, 'result (1 == Pass) -4.90000009537E+000, 'upper limit -5.05000019073E+000, 'lower limit +3.00000000000E+009, 'bucket 2 XAxis value +1.00000000000E+000, -4.84999990463E+000, -5.19999980927E+000, +5.00000000000E+009, 'bucket 3 Xaxis value -1.00000000000E+000, +0.00000000000E+000, +0.00000000000E+000  
Return Type | Variant  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Depend on the preset status  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:LIMit:REPort[:DATA]? <block>

Applicable Models: All (Read-only) Returns the stimulus values (frequency,
power level or time) at all the measurement points that failed the limit test,
for the selected trace. If there are no failures, a large number is returned
(**+9.91000000000E+037).**  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<block> | Depends on [FORM:DATA](../Format_SCPI.md#fd) If the number of the measurement points that failed the limit test is N, <block>=<First failed stimulus>, ..., <Nth failed stimulus>.  
Examples | The following example assumes that there are no failures: CALC:MEAS2:LIM:REP:DATA? **+9.91000000000E+037**  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 9.91E37 (no failures)  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:LIMit:REPort:POINts?

Applicable Models: All (Read-only) Reads the number of the measurement points
that failed the limit test, for the active trace of selected channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS:LIM:REP:POIN?  
Query Syntax | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:LIMit:SEGMent<snum>:AMPLitude:STARt <num>

Applicable Models: All (Read-Write) Sets the start (beginning) of the Y-axis
amplitude (response) value.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<snum> | Segment number; if unspecified, value is set to 1.  
<num> | Choose any number between: -500 and 500 Display value is limited to the Maximum and Minimum displayed Y-axis values.  
Examples | CALC:MEAS2LIM:SEGM1:AMPL:STAR 10  
calculate2:measure2:limit:segment2:amplitude:start 10  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:LIMit:SEGMent<snum>AMPLitude:STARt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:LIMit:SEGMent<snum>:AMPLitude:STOP <num>

Applicable Models: All (Read-Write) Sets the stop (end) of the Y-axis
amplitude (response) value.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<snum> | Segment number; if unspecified, value is set to 1.  
<num> | Choose any number between: -500 and 500 Display value is limited to the Maximum and Minimum displayed Y-axis values.  
Examples | CALC:MEAS:LIM:SEGM1:AMPL:STOP 10  
calculate2:measure2:limit:segment2:amplitude:stop 10  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:LIMit:SEGMent<snum>AMPLitude:STOP?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate:MEASure<mnum>:LIMit:SEGMent:COUNt?

Applicable Models: All (Read-only) Returns the number of segments used in a
limit test. All segments are counted, whether they are on or not.  
---  
Parameters | Not Applicable  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:LIM:SEGM:COUN?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:LIMit:SEGMent<snum>:STIMulus:STARt <num>

Applicable Models: All (Read-Write) Sets the start (beginning) of the X-axis
stimulus value.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<snum> | Segment number; if unspecified, value is set to 1.  
<num> | Choose any number within the X-axis span of the analyzer.  
Examples | CALC:MEAS:LIM:SEGM1:STIM:STAR 10  
calculate2:measure:limit:segment2:stimulus:start 10  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:LIMit:SEGMent<snum>STIMulus:STARt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:LIMit:SEGMent<snum>:STIMulus:STOP <num>

Applicable Models: All (Read-Write) Sets the stop (end) of the X-axis stimulus
value.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<snum> | Segment number; if unspecified, value is set to 1.  
<num> | Choose any number within the X-axis span of the analyzer.  
Examples | CALC:MEAS2:LIM:SEGM1:AMPL:STOP 10  
calculate2:measure2:limit:segment2:stimulus:stop 10  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:LIMit:SEGMent<snum>STIMulus:STOP?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:LIMit:SEGMent<snum>:TYPE <char>

Applicable Models: All (Read-Write) Sets the type of limit segment.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<snum> | Segment number. Choose any number between:  
1 and 100  
If unspecified, value is set to 1.  
<char> | Choose from:  
LMAX \- a MAX limit segment. Any response data exceeding the MAX value will
fail. LMIN \- a MIN limit segment. Any response data below the MIN value will
fail. OFF \- the limit segment (display and testing) is turned OFF.  
Examples | CALC:MEAS2:LIM:SEGM:TYPE LMIN  
calculate2:measure2:limit:segment3:type lmax  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:LIMit:SEGMent<snum>:TYPE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:LIMit:SOUNd[:STATe] <ON | OFF>

Applicable Models: All (Read-Write) Turns limit testing fail sound ON or OFF.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<ON | OFF> | ON (or 1) - turns sound ON.  
OFF (or 0) - turns sound OFF.  
Examples | CALC:MEAS2:LIM:SOUN ON  
calculate2:measure2:limit:sound:state off  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:LIMit:SOUNd[:STATe]?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:LIMit[:STATe] <ON | OFF>

Applicable Models: All (Read-Write) Turns limit segment testing ON or OFF.

  * Use CALCulate:MEASure:LIMit:DISPlay to turn ON and OFF the display of limit segments.
  * If using [Global Pass/Fail](../ControlHandler.md#status) status, trigger the VNA AFTER turning Limit testing ON.

  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<ON | OFF> | ON (or 1) - turns limit testing ON.  
OFF (or 0) - turns limit testing OFF.  
Examples | CALC:MEAS:LIM:STAT ON  
calculate2:measure:limit:state off  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:LIMit:STATe?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

