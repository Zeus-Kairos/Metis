# Calc:Limit Commands

* * *

Controls the limit segments used for pass / fail testing.

These commands are Superseded by the
[CALCulate:MEASure:LIMit](MeasureLIMit.md) commands.

CALCulate:LIMit: [DATA](Limit.md#data) | [DELete](Limit.md#delete) DISPlay | [[STATe]](Limit.md#disp) [FAIL?](Limit.md#fail) REPort | ALL? | DATA? | POINts? SEGMent | AMPLitude | [STARt](Limit.md#ampstrt) | [STOP](Limit.md#ampstp) | COUNt? | STIMulus | [STARt](Limit.md#stimstrt) | [STOP](Limit.md#stimstop) | [TYPE](Limit.md#type) SOUNd | [[STATe]](Limit.md#sound) [[STATe]](Limit.md#state)  
---  
  
Click on a keyword to view the command details.

See Also

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Learn about Limit Lines](../../../S4_Collect/Use_Limits_to_Test_Devices.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

Critical Note: CALCulate commands act on the selected measurement. You can
select one measurement for each channel using
[Calc:Par:MNUM](Parameter.md#MnumSel) or
[Calc:Par:Select](Parameter.md#cps). [Learn
more](../../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.htm).

* * *

## CALCulate<cnum>:LIMit:DATA <block>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Sets
data for limit segments. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement for which limit lines are to be set. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
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
Examples | The following writes three max limit segments for a bandpass filter. CALC:LIM:DATA 1,3e5,4e9,-60,0,1,4e9,7.5e9,0,0,1,7.5e9,9e9,0,-30  
Query Syntax | CALCulate<cnum>:LIMit:DATA?  
Return Type | Depends on [FORM:DATA](../Format_SCPI.md#fd)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Maximum limit = 100  
  
* * *

## CALCulate<cnum>:LIMit:DATA:DELete

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Write-only) Deletes
all limit line data for the selected measurement on the specified channel. See
Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC2:LIM:DATA:DEL  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:LIMit:DISPlay[:STATe] <ON | OFF>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Turns
the display of limit segments ON or OFF (if the data trace is turned ON). See
Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<ON | OFF> | ON (or 1) - turns the display of limit segments ON.  
OFF (or 0) - turns the display of limit segments OFF.  
Examples | CALC:LIM:DISP:STAT ON  
calculate2:limit:display:state off  
Query Syntax | CALCulate<cnum>:LIMit:DISPlay[:STATe]?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## CALCulate<cnum>:LIMit:FAIL?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Returns
the Pass / Fail status of the limit line test. Returns 1 (Fail) if any data
point fails for any limit segment. Limit display (CALC:LIM:DISP) does NOT have
to be ON. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:LIM:FAIL?  
Return Type | Boolean

  * 0 is returned when Pass
  * 1 is returned when Fail

  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:LIMit:REPort:ALL? <block>

Applicable Models: N522xB, N523xB, N524xB (Read-only) Returns the test results
(stimulus value, limit test result, upper limit value and lower limit value of
all measurement points), for the selected trace. This command returns a point
by point description of the limit table and pass/fail test result. See
Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<block> | Depends on [FORM:DATA](../Format_SCPI.md#fd) If the number of the measurement points is N, <Block> = <first stimulus>,<test result>,<upper limit>,<lower limit>, , <Nth stimulus>,<test result>,<upper limit>,<lower limit> Where <test result>= -1: No limit, 0:Fail, 1:Pass  
Examples | The following example returns three points: CALC:LIM:REP:ALL? +1.00000000000E+009, 'bucket 1 XAxis value +1.00000000000E+000, 'result (1 == Pass) -4.90000009537E+000, 'upper limit -5.05000019073E+000, 'lower limit +3.00000000000E+009, 'bucket 2 XAxis value +1.00000000000E+000, -4.84999990463E+000, -5.19999980927E+000, +5.00000000000E+009, 'bucket 3 Xaxis value -1.00000000000E+000, +0.00000000000E+000, +0.00000000000E+000  
Return Type | Variant  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Depend on the preset status  
  
* * *

## CALCulate<cnum>:LIMit:REPort[:DATA]? <block>

Applicable Models: N522xB, N523xB, N524xB (Read-only) Returns the stimulus
values (frequency, power level or time) at all the measurement points that
failed the limit test, for the selected trace. If there are no failures, a
large number is returned (**+9.91000000000E+037).** See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<block> | Depends on [FORM:DATA](../Format_SCPI.md#fd) If the number of the measurement points that failed the limit test is N, <block>=<First failed stimulus>, ..., <Nth failed stimulus>.  
Examples | The following example assumes that there are no failures: CALC:LIM:REP:DATA? **+9.91000000000E+037**  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 9.91E37 (no failures)  
  
* * *

## CALCulate<cnum>:LIMit:REPort:POINts?

Applicable Models: N522xB, N523xB, N524xB (Read-only) Reads the number of the
measurement points that failed the limit test, for the active trace of
selected channel. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:LIM:REP:POIN?  
Query Syntax | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:LIMit:SEGMent<snum>:AMPLitude:STARt <num>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Sets
the start (beginning) of the Y-axis amplitude (response) value. See Critical
Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<snum> | Segment number; if unspecified, value is set to 1.  
<num> | Choose any number between: -500 and 500 Display value is limited to the Maximum and Minimum displayed Y-axis values.  
Examples | CALC:LIM:SEGM1:AMPL:STAR 10  
calculate2:limit:segment2:amplitude:start 10  
Query Syntax | CALCulate<cnum>:LIMit:SEGMent<snum>AMPLitude:STARt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:LIMit:SEGMent<snum>:AMPLitude:STOP <num>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Sets
the stop (end) of the Y-axis amplitude (response) value. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<snum> | Segment number; if unspecified, value is set to 1.  
<num> | Choose any number between: -500 and 500 Display value is limited to the Maximum and Minimum displayed Y-axis values.  
Examples | CALC:LIM:SEGM1:AMPL:STOP 10  
calculate2:limit:segment2:amplitude:stop 10  
Query Syntax | CALCulate<cnum>:LIMit:SEGMent<snum>AMPLitude:STOP?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:LIMit:SEGMent:COUNt?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Returns
the number of segments used in a limit test. All segments are counted, whether
they are on or not.  
---  
Parameters | Not Applicable  
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:LIM:SEGM:COUN?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:LIMit:SEGMent<snum>:STIMulus:STARt <num>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Sets
the start (beginning) of the X-axis stimulus value. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<snum> | Segment number; if unspecified, value is set to 1.  
<num> | Choose any number within the X-axis span of the analyzer.  
Examples | CALC:LIM:SEGM1:STIM:STAR 10  
calculate2:limit:segment2:stimulus:start 10  
Query Syntax | CALCulate<cnum>:LIMit:SEGMent<snum>STIMulus:STARt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:LIMit:SEGMent<snum>:STIMulus:STOP <num>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Sets
the stop (end) of the X-axis stimulus value. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<snum> | Segment number; if unspecified, value is set to 1.  
<num> | Choose any number within the X-axis span of the analyzer.  
Examples | CALC:LIM:SEGM1:AMPL:STOP 10  
calculate2:limit:segment2:stimulus:stop 10  
Query Syntax | CALCulate<cnum>:LIMit:SEGMent<snum>STIMulus:STOP?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:LIMit:SEGMent<snum>:TYPE <char>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Sets
the type of limit segment. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<snum> | Segment number. Choose any number between:  
1 and 100  
If unspecified, value is set to 1.  
<char> | Choose from:  
LMAX \- a MAX limit segment. Any response data exceeding the MAX value will
fail. LMIN \- a MIN limit segment. Any response data below the MIN value will
fail. OFF \- the limit segment (display and testing) is turned OFF.  
Examples | CALC:LIM:SEGM:TYPE LMIN  
calculate2:limit:segment3:type lmax  
Query Syntax | CALCulate<cnum>:LIMit:SEGMent<snum>:TYPE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:LIMit:SOUNd[:STATe] <ON | OFF>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Turns
limit testing fail sound ON or OFF. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<ON | OFF> | ON (or 1) - turns sound ON.  
OFF (or 0) - turns sound OFF.  
Examples | CALC:LIM:SOUN ON  
calculate2:limit:sound:state off  
Query Syntax | CALCulate<cnum>:LIMit:SOUNd[:STATe]?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:LIMit[:STATe] <ON | OFF>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Turns
limit segment testing ON or OFF.

  * Use [CALC:LIM:DISP](Limit.md#disp) to turn ON and OFF the display of limit segments.
  * If using [Global Pass/Fail](../ControlHandler.md#status) status, trigger the VNA AFTER turning Limit testing ON.

See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<ON | OFF> | ON (or 1) - turns limit testing ON.  
OFF (or 0) - turns limit testing OFF.  
Examples | CALC:LIM:STAT ON  
calculate2:limit:state off  
Query Syntax | CALCulate<cnum>:LIMit:STATe?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

