# CALCulate:MEASure:FUNCtion Commands

CALCulate:MEASure:FUNCtion DATA? DOMain | USER | [:RANGe] | STARt | STOP EXECute STATistics | [:STATe] | RESistance TYPE  
---  
  
Click a keyword to view the command details.

See Also

  * [Learn about Trace Statistics](../../../S4_Collect/Math_Operations.md#statistics)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## CALCulate<cnum>:MEASure<mnum>:FUNCtion:DATA?

Applicable Models: All (Read-only) Returns the trace statistic data for the
selected statistic type for the specified channel. Select the type of
statistic with CALC:MEAS:FUNC:TYPE.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Return Type | Depends on [FORM:DATA](../Format_SCPI.md#fd)  
Example | 

    CALCulate2:MEASure2:FUNCtion:DATA?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:FUNCtion:DOMain:USER[:RANGe] <range>

Applicable Models: All (Read-Write) Sets the range used to calculate trace
statistics. Each channel has 16 user ranges. The x-axis range is specified
with the CALC:MEAS:FUNC:DOM:USER:START and [STOP](Function.md#stop) commands.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<range> | Range number. Choose from: 0 to 16 0 is Full Span of the current x-axis range 1 to 16 are user-specified ranges  
Examples | CALC:MEAS2:FUNC:DOM:USER 4  
calculate2:measure2:function:domain:user:range 0  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:FUNCtion:DOMain:USER[:RANGe]?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 \- Full Span  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:FUNCtion:DOMain:USER:STARt <range>, <start>

Applicable Models: All (Read-Write) Sets the start of the specified user-
domain range. To apply this range, use CALC:MEAS:FUNC:DOM:USER To set the stop
of the range, use CALC:MEAS:FUNC:DOM:USER:STOP. Note: This command does the
same as
[CALC:MEAS:MARK:FUNC:DOM:USER:STAR](MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:DOMain:USER:STARt)  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<range> | Range number that will receive the start value. Choose an integer between 1 and 16  
<start> | Start value of the specified range. Choose a real number between:  
the analyzer's Minimum and Maximum x-axis value.  
Examples | CALC:MEAS2:FUNC:DOM:USER:STAR 1,1e9  
calculate2:measure2:function:domain:user:start 2,2e9  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:FUNCtion:DOMain:USER:STARt? <range>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | The analyzer's Minimum x-axis value  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:FUNCtion:DOMain:USER:STOP <range>, <stop>

Applicable Models: All (Read-Write) Sets the stop value of the specified user-
domain range. To apply this range, use CALC:MEAS:FUNC:DOM:USER. To set the
start of the range, use
[CALC:MEAS:MARK:FUNC:DOM:USER:STAR](MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:DOMain:USER:STARt)
Note: This command does the same as
[CALC:MEAS:MARK:FUNC:DOM:USER:STOP](MeasureMARKer.md#CALCulate:MEASure:MARKer:FUNCtion:DOMain:USER:STOP)  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<range> | Range number that will receive the stop value. Choose an integer between 1 and 16  
<stop> | Stop value of the specified range. Choose a real number between:  
the analyzer's Minimum and Maximum x-axis value.  
Examples | CALC:MEAS2:FUNC:DOM:USER:STOP 4,5e9  
calculate2:measure2:function:domain:user:stop 3,8e9  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:FUNCtion:DOMain:USER:STOP? <range>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | The analyzer's Maximum x-axis value  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:FUNCtion:EXECute

Applicable Models: All (Write-only) For the active trace of specified channel,
executes the statistical analysis specified by the CALC:MEAS:FUNC:TYPE
command.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:FUNC:EXEC  
calculate2:measure2:function:execute  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:FUNCtion:STATistics[:STATe] <ON|OFF>

Applicable Models: All (Read-Write) Displays and hides the trace statistics
(peak-to-peak, mean, standard deviation) on the screen. The analyzer will
display either measurement statistics or Filter Bandwidth statistics; not
both.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<ON|OFF> | ON - Displays trace statistics OFF - Hides trace statistics  
Examples | CALC:MEAS2:FUNC:STAT ON  
calculate2:measure2:function:statistics:state off  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:FUNCtion:STATistics[:STATe]?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF (0)  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:FUNCtion:STATistics:RESistance[:STATe]
<ON|OFF>

Applicable Models: All (Read-Write) For Smith Chart format, changes trace
statistics (peak-to-peak, mean, standard deviation) units from Log Mag (dB) to
impedance (ohms) on the screen.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<ON|OFF> | ON - Units displayed in ohms OFF - Units displayed in dB  
Examples | CALC:MEAS2:FUNC:STAT:RES ON  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:FUNCtion:STATistics:RESistance[:STATe]?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF (0)  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:FUNCtion:TYPE <char>

Applicable Models: All (Read-Write) Sets statistic TYPE that you can then
query using CALC:MEAS:FUNCtion:DATA?. Note: This command affects only the
selected measurement on the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<char> | Choose from: PTPeak \- the difference between the max and min data points on the trace. STDEV \- standard deviation of all data points on the trace MEAN - mean (average) of all data points on the trace MIN \- lowest data point on the trace MAX \- highest data point on the trace  
Examples | CALC:MEAS2:FUNC:TYPE PTP  
calculate2:measure2:function:type stdev  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:FUNCtion:TYPE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | PTPeak  
  
* * *

