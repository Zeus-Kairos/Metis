# Calculate:Math Commands

* * *

Controls math operations on the currently selected measurement and memory.

These commands are Superseded by the
[CALCulate:MEASure:MATH](Measure.md#CALCulate:MEASure:MATH:FUNCtion)
commands.

CALCulate:MATH: FUNCtion INTerpolate MEMorize  
---  
  
Click on a keyword to view the command details.

See Also

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Learn about Math Operations](../../../S4_Collect/Math_Operations.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

Critical Note: CALCulate commands act on the selected measurement. You can
select one measurement for each channel using
[Calc:Par:MNUM](Parameter.md#MnumSel) or
[Calc:Par:Select](Parameter.md#cps). [Learn
more](../../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.htm).

* * *

## CALCulate<cnum>:MATH:FUNCtion <char>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Sets
math operations on the currently selected measurement and the trace stored in
memory. (There MUST be a trace stored in Memory. See [CALC:MATH
MEM](Math_Calc.htm#cmm)) See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<char> | The math operation to be applied. Choose from the following:  
| NORMal | Trace data only  
---|---|---  
| ADD | Data + Memory  
| SUBTract | Data - Memory  
| MULTiply | Data * Memory  
| DIVide | Data / Memory  
Examples | CALC:MATH:FUNC NORM  
calculate2:math:function subtract  
---|---  
Query Syntax | CALCulate<cnum>:MATH:FUNCtion?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | NORMal  
  
* * *

## CALCulate<cnum>:MATH:INTerpolate <bool>

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Sets and reads the
state of the memory data interpolation. [Learn
more](../../../S4_Collect/Math_Operations.htm#MemoryTraceInterpolation). See
Critical Note  
---  
Parameters |   
<ch> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <ch> is set to 1.  
<bool> | Choose from: 0 - OFF \- Turn memory data interpolation OFF. 1 - ON \- Turn memory data interpolation ON.  
Examples | CALC2:MATH:INT 1  
Query Syntax | CALCulate<ch>:MATH:INTerpolate?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:MATH:MEMorize

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Write-only) Puts
the currently selected measurement trace into memory. (Data-> Memory). See
Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:MATH:MEM  
calculate2:math:memorize  
Query Syntax | Not applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

