# CALCulate:MEASure:TRANsform Commands

Specifies the settings for time domain transform.

CALCulate:MEASure:TRANsform COUPle | PARameters TIME | ALIGnment | CENTer | CLIP | IMPulse | WIDTh | KBESsel | LPFRequency | MARKer | MODE | UNIT | SPAN | STARt | STATe | STEP | RTIMe | STOP | [:TYPE] | WINDow | [:TYPE]  
---  
  
Click a keyword to view the command details.

See Also

  * [Learn about Time Domain](../../../Time/TimeDomain.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## CALCulate<cnum>:MEASure<mnum>:TRANsform:COUPle:PARameters <num>

Applicable Models: All (Read-Write) Specifies the time domain transform
parameters to be coupled. The settings for those parameters will be copied
from the selected measurement to all other measurements on the channel.

  * To turn coupling ON and OFF, use [SENS:COUP:PAR](../Sense/Couple.md#Trans)
  * To specify Gating parameters to couple, use [CALC:MEAS:FILT:COUP:PAR](MeasureFILter.md#CALCulate:MEASure:FILTer:GATE:COUPle:PARameters)

Learn more about [Time Domain Trace
Coupling](../../../Time/TimeDomain.htm#Coupling)  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<num> | (Numeric) Parameters to couple. To specify more than one parameter, add the numbers. 1 \- Transform Stimulus (Start, Stop, Center, and Span TIME settings.) 2 \- Transform State (ON / OFF) 4 \- Transform Window Type (including Kaiser Beta / Impulse Width settings for Kaiser Window) 8 \- Transform Mode (Low Pass Impulse, Low Pass Step, Band Pass) 16 \- Transform Distance Marker Units  
Examples | 'To couple all parameters: CALC:MEAS:TRAN:COUP:PAR 31 'To couple Stimulus and Mode:  
calculate2:measure2:transform:couple:parameters 9  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:TRANsform:COUPle:PARameters?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 29 (All parameters except 2 \- Transform State)  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME:ALIGnment <enum>

Applicable Models: All (Read-Write) Sets the way the PNA computes the DC value
of the frequency-domain measurement. The correct DC value is required for
inverse-FFT accuracy, and if not estimated properly, can cause distortions in
the time-domain measurement in the form of an undesired slope in the waveform.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<enum> | Choose from: LEGacy \- The DC value is extrapolated using three data points. The transform offset is calculated using the delay of the first frequency point. This is the same algorithm used in the HP 8510 network analyzer. NORMalize \- The DC value is extrapolated using three data points. The transform offset is set to zero at t=0 minus six rise-times. This mode requires that a good S-parameter calibration has been performed, which can be verified by observing a flat time-domain response at t=0 when measuring a load located at the physical point corresponding to t=0. Normalize mode is principally used to help stabilize the time-domain trace at time t=0 to 50 ohms, to remove bouncing of the response at t=0. This method is similar to that used with PLTS, and is very useful in determining the time-domain-transform response of transmission lines and printed-circuit-board characteristics.  
Examples | CALC:MEAS:TRAN:TIME:ALIG NORM  
calculate2:measure2:transform:time:alignment?  
Return Type | Enumeration  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | NORMalize  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME:CENTer <num>

Applicable Models: All (Read-Write) Sets the center time for time domain
measurements.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<num> | Center time in seconds; any number between:  
± (number of points-1) / frequency span Note: This command will accept MIN or
MAX instead of a numeric parameter. See [SCPI
Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.htm#min)
for more information.  
Examples | CALC:MEAS:TRAN:TIME:CENT 1e-8  
calculate2:measure2:transform:time:center 15 ps  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME:CENTer?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME:CLIP <bool>

Applicable Models: All (Read-Write) Turns the start/stop time limits ON or
OFF. When ON, limits the start/stop times to avoid aliasing.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<bool> | ON (or 1) - turns start/stop time limits ON.  
OFF (or 0) - turns start/stop time limits OFF.  
Examples | CALC:MEAS:TRAN:TIME:CLIP ON  
calculate2:measure2:transform:time:clip off  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME:CLIP?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## CALCulate<cnum>:MEAsure<mnum>:TRANsform:TIME:IMPulse:WIDTh <num>

Applicable Models: All (Read-Write) Sets the impulse width for the transform
window.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<num> | Impulse width in seconds; Choose any number between:  
.6 / frequency span and 1.39 / frequency span  
Examples | CALC:MEAS:TRAN:TIME:IMP:WIDTh 10  
calculate2:measure2:transform:time:impulse:width 13  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME:IMPulse:WIDTh?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | .98 / Default Span  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME:KBESsel <num>

Applicable Models: All (Read-Write) Sets the parametric window for the Kaiser
Bessel window.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<num> | Window width for Kaiser Bessel in seconds; Choose any number between:  
0.0 and 13.0  
Examples | CALC:MEAS:TRAN:TIME:KBES 10  
calculate2:measure2:transform:time:kbessel 13  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME:KBESsel?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 6  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME:LPFREQuency

Applicable Models: All (Write-only) Sets the start frequencies in LowPass
Mode.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS:TRAN:TIME:LPFR  
calculate2:measure2:transform:time:lpfrequency  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME:MARKer:MODE <char>

Applicable Models: All (Read-Write) Specifies the measurement type in order to
determine the correct marker distance.

  * Select Auto for S-Parameter measurements.
  * Select Reflection or Transmission for arbitrary ratio or unratioed measurements.

This setting affects the display of ALL markers for only the ACTIVE
measurement. Learn more about [Distance
Markers](../../../Time/TimeDomain.htm#Distance).  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<char> | Choose from: AUTO \- If the active measurement is an S-Parameter, automatically chooses reflection or transmission. If non S-Parameter measurements, reflection is chosen. REFLection \- Displays the distance from the source to the receiver divided by two (to compensate for the return trip.) TRANsmission \- Displays the distance from the source to the receiver.  
Examples | CALC:MEAS:TRAN:TIME:MARK:MODE REFL  
calculate2:measure2:transform:time:marker:mode auto  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME:MARKer:MODE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | AUTO  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME:MARKer:UNIT <char>

Applicable Models: All (Read-Write) Specifies the unit of measure for the
display of marker distance values. This settings affects the display of ALL
markers for only the ACTIVE measurement (unless Distance Maker Units are
coupled using CALC:MEAS:TRAN:COUP:PAR. Learn more about [Distance
Markers](../../../Time/TimeDomain.htm#Distance).  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<char> | Choose from: METRs FEET INCHes  
Examples | CALC:MEAS:TRAN:TIME:MARK:UNIT INCH  
calculate2:measure2:transform:time:marker:unit feet  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME:MARKer:UNIT?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | METRs  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME:SPAN <num>

Applicable Models: All (Read-Write) Sets the span time for time domain
measurements.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<num> | Span time in seconds; any number between:  
0 and 2* [(number of points-1) / frequency span] Note: This command will
accept MIN or MAX instead of a numeric parameter. See [SCPI
Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.htm#min)
for more information.  
Examples | CALC:MEAS:TRAN:TIME:SPAN 1e-8  
calculate2:measure2:transform:time:span maximum  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME:SPAN?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 20 ns  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME:STARt <num>

Applicable Models: All (Read-Write) Sets the start time for time domain
measurements.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<num> | Start time in seconds; any number between:  
± (number of points-1) / frequency span Note: This command will accept MIN or
MAX instead of a numeric parameter. See [SCPI
Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.htm#min)
for more information.  
Examples | CALC:MEAS:TRAN:TIME:STAR 1e-8  
calculate2:measure2:transform:time:start minimum  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME:STARt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | -10 ns  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME:STATe <bool>

Applicable Models: All (Read-Write) Turns the time domain transform capability
ON or OFF. Note: [Sweep type](../Sense/Sweep_SCPI.md#ssty) must be set to
Linear Frequency in order to use Time Domain Transform.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<bool> | ON (or 1) - turns time domain ON.  
OFF (or 0) - turns time domain OFF.  
Examples | CALC:MEAS:TRAN:TIME:STAT ON  
calculate2:measure2:transform:time:state off  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME:STATe?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME:STEP:RTIMe <num>

Applicable Models: All (Read-Write) Sets the step rise time for the transform
window.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<num> | Rise time in seconds; Choose any number between:  
.45 / frequency span and 1.48 / frequency span  
Examples | CALC:MEAS:TRAN:TIME:STEP:RTIM 1e-8  
calculate2:measure2:transform:time:step:rtime 15 ps  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME:STEP:RTIMe?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | .99 / Default Span  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME:STOP <num>

Applicable Models: All (Read-Write) Sets the stop time for time domain
measurements.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<num> | Stop time in seconds; any number between:  
± (number of points-1) / frequency span Note: This command will accept MIN or
MAX instead of a numeric parameter. See [SCPI
Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.htm#min)
for more information.  
Examples | CALC:MEAS:TRAN:TIME:STOP 1e-8  
calculate2:measure2:transform:time:stop maximum  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME:STOP?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 10 ns  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME[:TYPE] <char>

Applicable Models: All (Read-Write) Sets the type of time domain measurement.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<char> | Type of measurement. Choose from:  
BPASs \- Set transform mode to band pass. LPSTep \- Set transform mode to low
pass step. LPIMpulse \- Set transform mode to low pass impulse. [Learn about
these settings](../../../Time/TimeDomain.htm#Modes).  
Examples | CALC:MEAS:TRAN:TIME BPAS  
calculate2:measure2:transform:time:type bpas  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME[:TYPE]?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | BPAS  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME:WINDow[:TYPE] <char>

Applicable Models: All (Read-Write) Sets the window type for time domain
transform.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<char> | Window Type. Choose from:  
KAISer \- Set window type to Kaiser. RECTangle \- Set window type to
Rectangle. HAMMing \- Set window type to Hamming. HANN \- Set window type to
Hanning. BOHMan \- Set window type to Bohman. [Learn about these
settings](../../../Time/TimeDomain.htm#WindDiag).  
Examples | CALC:MEAS:TRAN:TIME WIND KAIS  
calculate2:measure2:transform:time:window:type hamming  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:TRANsform:TIME:WINDow[:TYPE]?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | KAISer  
  
* * *

