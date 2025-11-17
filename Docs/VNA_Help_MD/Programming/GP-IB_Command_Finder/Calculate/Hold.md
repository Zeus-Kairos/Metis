# CALC:HOLD Commands

* * *

Controls the Trace Hold settings.

These commands are Superseded by the
[CALCulate:MEASure:HOLD](Measure.md#CALCulate:MEASure:HOLD:CLEar) commands.

CALCulate:HOLD [TYPE](Hold.md#type) [CLEar](Hold.md#clear)  
---  
  
Click on a keyword to view the command details.

See Also

  * [Learn about Trace Hold](../../../S0_Start/Traces_Channels_and_Windows.md#Trace_Hold)

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

Critical Note: CALCulate commands act on the selected measurement. You can
select one measurement for each channel using
[Calc:Par:MNUM](Parameter.md#MnumSel) or
[Calc:Par:Select](Parameter.md#cps). [Learn
more](../../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.htm).

* * *

## CALCulate<cnum>:HOLD:TYPE <char>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Sets
the type of trace hold to perform. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<char> | Trace Hold type. Choose from: OFF \- Disables the Trace Hold feature. MINimum \- Sets Trace Hold to store the lowest measured data points. MAXimum \- Sets Trace Hold to store the highest measured data points.  
Examples | CALC:HOLD:TYPE MAX calculate2:hold:type minimum  
Query Syntax | CALCulate<ch>:HOLD:TYPE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:HOLD:CLEar

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Write-only) Resets
the currently-stored data points to the live data trace and restarts the
currently-selected Trace Hold type. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:HOLD:CLE calculate2:hold:clear  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

