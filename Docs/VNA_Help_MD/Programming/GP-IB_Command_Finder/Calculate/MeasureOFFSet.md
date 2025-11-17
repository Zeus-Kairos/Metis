# CALCulate:MEASure:OFFSet Commands

Allows the data trace magnitude and phase to be offset.

CALCulate:MEASure:OFFSet MAGNitude | SLOPe PHASe  
---  
  
Click a keyword to view the command details.

See Also

  * [Learn about Magnitude Offset](../../../S1_Settings/Scale.md#Magnitude)

  * [Learn about Phase Offset](../../../S2_Opt/Phase_Accy.md#PhaseDiag)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## CALCulate<cnum>:MEASure<mnum>:OFFSet:MAGNitude <num>

Applicable Models: All (Read-Write) Offsets the data trace magnitude by the
specified value. To offset the data trace magnitude to a slope value that
changes with frequency, use CALC:MEAS:OFFS:MAGN:SLOP  
---  
Parameters |   
<cnum> | Channel number of the measurement (optinal).  
<mnum> | Measurement number for each measurement.   
<num> | Offset value in dB.  
Examples | CALC:MEAS:OFFS:MAGN 4  
calculate1:measure2:offset:magnitude -2  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:OFFSet:MAGNitude?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:OFFSet:MAGNitude:SLOPe <num>

Applicable Models: All (Read-Write) Offsets the data trace magnitude to a
value that changes linearly with frequency. The offset slope begins at 0 Hz.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optinal).  
<mnum> | Measurement number for each measurement.   
<num> | Offset slope value in dB/ 1GHz.  
Examples | CALC:MEAS:OFFS:MAGN:SLOP 1 'Offset slope set to 1dB/GHz  
calculate1:measure2:offset:magnitude:slope -2 'Offset slope set to -2dB/GHz  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:OFFSet:MAGNitude:SLOPe?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:OFFSet:PHASe <num>[<char>]

Applicable Models: All (Read-Write) Sets the phase offset for the selected
measurement.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optinal).  
<mnum> | Measurement number for each measurement.   
<num> | Offset phase value. Choose any number between:  
-360 and 360  
<char> | Units for phase. OPTIONAL. Choose either:  
DEG \- Degrees (default)  
RAD \- Radians  
Examples | CALC:MEAS:OFFS:PHAS 10  
calculate3:measure2:offset:phase 20rad  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:OFFSet:PHASe?  
Return Type | Numeric, returned value always in degrees  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 degrees  
  
* * *

