# CALCulate:MEASure:DISTortion Commands

Calculate and display amplitude modulation or phase modulation per trace. This
feature is supported on all standard channels and on all memory traces in a
standard channel.

CALCulate:MEASure:DISTortion BACKoff: | COMPression | [:STATe] MODE SLOPe: | APERture | [:STATe]  
---  
  
Click a keyword to view the command details.

See Also

  * [Calibrating with SCPI](../../Learning_about_GPIB/Calibrating_the_Analyzer_Using_SCPI.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## CALCulate<cnum>:MEASure<mnum>:DISTortion:BACKoff:COMPression <num>

Applicable Models: All (Read-Write) Sets the compression level used in
determining the back off calculation.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<num> | Compression level.  
Examples | CALC1:MEAS2:DIST:BACK:COMP 1 dB calculate2:measure2:distortion:backoff:compression 1 dB  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:DISTortion:BACKoff:COMPression?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1 dB  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:DISTortion:BACKoff[:STATe] <bool>

Applicable Models: All (Read-Write) Enables/disables compression level back
off function specified using the
CALCulate:MEASure:DISTortion:BACKoff:COMPression command. When enabled, the
x-axis changes to display the back off from the compression point.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<bool> | Compression level back off state. Choose from: 0 \- Compression level back off state OFF 1 \- Compression level back off state ON  
Examples | CALC:MEAS2:CORR ON calculate:measure2:correction:state off  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:DISTortion:BACKoff[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

CALCulate<cnum>:MEASure<mnum>:DISTortion:MODE <char>

Applicable Models: All (Read-Write) Displays phase or amplitude distortion.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<char> | Choose from:

  * OFF
  * AMPM - Displays phase distortion (in degrees).
  * AMAM - Displays amplitude distortion (in dB).

  
Examples | CALC:MEAS:DIST:MODE AMAM  
calculate2:measure1:distortion:mode amam  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:DISTortion:MODE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:DISTortion:SLOPe:APERture <num>

Applicable Models: All (Read-Write) Sets the aperture value over which the
phase or gain slope will be calculated.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<num> | Aperture value.  
Examples | CALC1:MEAS2:DIST:SLOP:APER 1 dB calculate2:measure2:distortion:slope:aperture 1 dB  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:DISTortion:SLOPe:APERture?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1 dB  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:DISTortion:SLOPe[:STATe] <bool>

Applicable Models: All (Read-Write) Enables/disables phase slope (AMPM) or
gain slope (AMAM) over the slope aperture to be displayed.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<bool> | Compression level back off state. Choose from: 0 \- Phase or gain slope over aperture state OFF 1 \- Phase or gain slope over aperture state ON  
Examples | CALC:MEAS2:DIST:SLOP ON calculate:measure2:distortion:slope:state off  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:DISTortion:SLOPe[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

