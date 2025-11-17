# Calculate:Transform Commands

* * *

Specifies the settings for time domain transform.

These commands are Superseded by the
[CALCulate:MEASure:TRANsform](MeasureTRANsform.md) commands.

CALCulate:TRANsform COUple: | PARameters TIME: | ALIGnment | CENTer | IMPulse | WIDTh | KBESsel | LPFRequency | MARKer | MODE | UNIT | SPAN | STARt | STATe | STEP | RTIMe | STIMulus | STOP | [:TYPE]  
---  
  
Click on a keyword to view the command details.

See Also

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Learn about Time Domain](../../../Time/TimeDomain.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

Critical Note: CALCulate commands act on the selected measurement. You can
select one measurement for each channel using
[Calc:Par:MNUM](Parameter.md#MnumSel) or
[Calc:Par:Select](Parameter.md#cps).

* * *

## CALCulate<cnum>:TRANsform:COUPle:PARameters <num>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write)
Specifies the time domain transform parameters to be coupled. The settings for
those parameters will be copied from the selected measurement to all other
measurements on the channel.

  * To turn coupling ON and OFF, use [SENS:COUP:PAR](../Sense/Couple.md#Trans)
  * To specify Gating parameters to couple, use [CALC:FILT:COUP:PAR](Filter.md#couple)

Learn more about [Time Domain Trace
Coupling](../../../Time/TimeDomain.htm#Coupling) See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<num> | (Numeric) Parameters to couple. To specify more than one parameter, add the numbers. 1 \- Transform Stimulus (Start, Stop, Center, and Span TIME settings.) 2 \- Transform State (ON / OFF) 4 \- Transform Window (Kaiser Beta / Impulse Width) 8 \- Transform Mode (Low Pass Impulse, Low Pass Step, Band Pass) 16 \- Transform Distance Marker Units  
Examples | 'To couple all parameters: CALC:TRAN:COUP:PAR 31 'To couple Stimulus and Mode:  
calculate2:transform:couple:parameters 9  
Query Syntax | CALCulate<cnum>:TRANsform:COUPle:PARameters?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 29 (All parameters except 2 \- Transform State)  
  
* * *

## CALCulate<cnum>:TRANsform:TIME:CENTer <num>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Sets
the center time for time domain measurements. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<num> | Center time in seconds; any number between:  
± (number of points-1) / frequency span Note: This command will accept MIN or
MAX instead of a numeric parameter. See [SCPI
Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.htm#min)
for more information.  
Examples | CALC:TRAN:TIME:CENT 1e-8  
calculate2:transform:time:center 15 ps  
Query Syntax | CALCulate<cnum>:TRANsform:TIME:CENTer?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:TRANsform:TIME:IMPulse:WIDTh <num>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Sets
the impulse width for the transform window. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<num> | Impulse width in seconds; Choose any number between:  
.6 / frequency span and 1.39 / frequency span  
Examples | CALC:TRAN:TIME:IMP:WIDTh 10  
calculate2:transform:time:impulse:width 13  
Query Syntax | CALCulate<cnum>:TRANsform:TIME:IMPulse:WIDTh?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | .98 / Default Span  
  
* * *

## CALCulate<cnum>:TRANsform:TIME:KBESsel <num>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Sets
the parametric window for the Kaiser Bessel window. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<num> | Window width for Kaiser Bessel in seconds; Choose any number between:  
0.0 and 13.0  
Examples | CALC:TRAN:TIME:KBES 10  
calculate2:transform:time:kbessel 13  
Query Syntax | CALCulate<cnum>:TRANsform:TIME:KBESsel?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 6  
  
* * *

## CALCulate<cnum>:TRANsform:TIME:LPFREQuency

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Write-only) Sets
the start frequencies in LowPass Mode. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:TRAN:TIME:LPFR  
calculate2:transform:time:lpfrequency  
Query Syntax | Not applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:TRANsform:TIME:MARKer:MODE <char>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write)
Specifies the measurement type in order to determine the correct marker
distance.

  * Select Auto for S-Parameter measurements.
  * Select Reflection or Transmission for arbitrary ratio or unratioed measurements.

This setting affects the display of ALL markers for only the ACTIVE
measurement. Learn more about [Distance
Markers](../../../Time/TimeDomain.htm#Distance). See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<char> | Choose from: AUTO If the active measurement is an S-Parameter, automatically chooses reflection or transmission. If non S-Parameter measurements, reflection is chosen. REFLection Displays the distance from the source to the receiver divided by two (to compensate for the return trip.) TRANsmission Displays the distance from the source to the receiver.  
Examples | CALC:TRAN:TIME:MARK:MODE REFL  
calculate2:transform:time:marker:mode auto  
Query Syntax | CALCulate<cnum>:TRANsform:TIME:MARKer:MODE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Auto  
  
* * *

## CALCulate<cnum>:TRANsform:TIME:MARKer:UNIT <char>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write)
Specifies the unit of measure for the display of marker distance values. This
settings affects the display of ALL markers for only the ACTIVE measurement
(unless Distance Maker Units are coupled using
[CALC:TRAN:COUP:PAR](Transform_Calc.md#couple). Learn more about [Distance
Markers](../../../Time/TimeDomain.htm#Distance). See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<char> | Choose from: METRs FEET INCHes  
Examples | CALC:TRAN:TIME:MARK:UNIT INCH  
calculate2:transform:time:marker:unit feet  
Query Syntax | CALCulate<cnum>:TRANsform:TIME:MARKer:UNIT?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | METRs  
  
* * *

## CALCulate<cnum>:TRANsform:TIME:SPAN <num>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Sets
the span time for time domain measurements. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<num> | Span time in seconds; any number between:  
0 and 2* [(number of points-1) / frequency span] Note: This command will
accept MIN or MAX instead of a numeric parameter. See [SCPI
Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.htm#min)
for more information.  
Examples | CALC:TRAN:TIME:SPAN 1e-8  
calculate2:transform:time:span maximum  
Query Syntax | CALCulate<cnum>:TRANsform:TIME:SPAN?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 20 ns  
  
* * *

## CALCulate<cnum>:TRANsform:TIME:STARt <num>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Sets
the start time for time domain measurements. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<num> | Start time in seconds; any number between:  
± (number of points-1) / frequency span Note: This command will accept MIN or
MAX instead of a numeric parameter. See [SCPI
Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.htm#min)
for more information.  
Examples | CALC:TRAN:TIME:STAR 1e-8  
calculate2:transform:time:start minimum  
Query Syntax | CALCulate<cnum>:TRANsform:TIME:STARt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | -10 ns  
  
* * *

## CALCulate<cnum>:TRANsform:TIME:STATe <ON | OFF>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Turns
the time domain transform capability ON or OFF. See Critical Note Note: [Sweep
type](../Sense/Sweep_SCPI.htm#ssty) must be set to Linear Frequency in order
to use Time Domain Transform.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<ON|OFF> | ON (or 1) - turns time domain ON.  
OFF (or 0) - turns time domain OFF.  
Examples | CALC:TRAN:TIME:STAT ON  
calculate2:transform:time:state off  
Query Syntax | CALCulate<cnum>:TRANsform:TIME:STATe?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:TRANsform:TIME:STOP <num>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Sets
the stop time for time domain measurements. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<num> | Stop time in seconds; any number between:  
± (number of points-1) / frequency span Note: This command will accept MIN or
MAX instead of a numeric parameter. See [SCPI
Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.htm#min)
for more information.  
Examples | CALC:TRAN:TIME:STOP 1e-8  
calculate2:transform:time:stop maximum  
Query Syntax | CALCulate<cnum>:TRANsform:TIME:STOP?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 10 ns  
  
* * *

## CALCulate<cnum>:TRANsform:TIME:STEP:RTIMe <num>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Sets
the step rise time for the transform window. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<num> | Rise time in seconds; Choose any number between:  
.45 / frequency span and 1.48 / frequency span  
Examples | CALC:TRAN:TIME:STEP:RTIM 1e-8  
calculate2:transform:time:step:rtime 15 ps  
Query Syntax | CALCulate<cnum>:TRANsform:TIME:STEP:RTIMe?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | .99 / Default Span  
  
* * *

## CALCulate<cnum>:TRANsform:TIME:STIMulus <char>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Sets
the type of simulated stimulus that will be incident on the DUT. See Critical
Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<char> | Choose from:  
STEP - simulates a step DUT stimulus  
IMPulse - simulates a pulse DUT stimulus STEP can ONLY be used when
CALC:TRAN:TIME:TYPE is set to LPASs (Lowpass). (STEP cannot be used with TYPE
= BPASs.) :STIM STEP will set :TYPE to LPASs :TYPE BPASs will set :STIM to
IMPulse  
Examples | CALC:TRAN:TIME:STIM STEP  
calculate2:transform:time:stimulus impulse  
Query Syntax | CALCulate<cnum>:TRANsform:TIME:STIMulus?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | IMPulse  
  
* * *

## CALCulate<cnum>:TRANsform:TIME:ALIGnment <enum>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Selects
the way the PNA computes the DC value of the frequency-domain measurement. The
correct DC value is required for inverse-FFT accuracy, and if not estimated
properly, can cause distortions in the time-domain measurement in the form of
an undesired slope in the waveform. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurements to be listed. If unspecified, <cnum> is set to 1.  
<enum> | Choose from: LEGacy \- The DC value is extrapolated using three data points. The transform offset is calculated using the delay of the first frequency point. This is the same algorithm used in the HP 8510 network analyzer. NORMalize \- The DC value is extrapolated using three data points. The transform offset is set to zero at t=0 minus six rise-times. This mode requires that a good S-parameter calibration has been performed, which can be verified by observing a flat time-domain response at t=0 when measuring a load located at the physical point corresponding to t=0. Setting the time domain trace to zero at a time before t=0 stabilizes the trace for determining impedances after time t=0, resulting in improved behavior compared to Legacy mode. This method is similar to that used with PLTS, and is very useful in determining the time-domain-transform response of transmission lines and printed-circuit-board characteristics.  
Examples | CALC:TRAN:TIME:ALIG NORM  
calculate2:transform:time:alignment?  
Return Type | Enumeration  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | LEGacy  
  
* * *

## CALCulate<cnum>:TRANsform:TIME[:TYPE] <char>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Sets
the type of time domain measurement. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<char> | Type of measurement. Choose from:  
LPASs \- Lowpass; Must also send
[CALC:TRAN:TIME:LPFRequency](Transform_Calc.md#cttl) before calibrating.  
BPASs \- Bandpass; BPASs can only be used when
[CALC:TRAN:TIME:STIM](Transform_Calc.md#cttt) is set to IMPulse. (BPASs
cannot be used with :STIM = STEP) :STIM STEP will set :TYPE to LPASs :TYPE
BPASs will set :STIM to IMPulse  
Examples | CALC:TRAN:TIME LPAS  
calculate2:transform:time:type bpas  
Query Syntax | CALCulate<cnum>:TRANsform:TIME[:TYPE]?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | BPAS

