# Sense:Sweep:Pulse Commands

* * *

Configures the channel to make pulse measurements using the Integrated Pulse
Application.

SENSe:SWEep:PULSe [CWTime](SweepPulse.md#CWSweepAuto) [DETectmode[:AUTO]](SweepPulse.md#detectmode) [DRIVe[:AUTO]](SweepPulse.md#drive) [IFBW[:AUTO]](SweepPulse.md#ifbw) [IFGain[:AUTO]](SweepPulse.md#IFGain) [MODE](SweepPulse.md#mode) [PRF[:AUTO]](SweepPulse.md#prf) PRIMary: | CLOCk | [FREQuency](SweepPulse.md#MasterFreq) | [PERiod](SweepPulse.md#MasterPeriod) | [WIDTh](SweepPulse.md#MasterWidth) PROFile | STARt | STOP [SHAPe](SweepPulse.md#Shape) | [CAalog?](SweepPulse.md#ShapeCat) [SWGate](SweepPulse.md#swgate) [TIMing[:AUTO]](SweepPulse.md#timing) [WIDeband[:STATe]](SweepPulse.md#wideband)  
---  
  
Click on a keyword to view the command details.

See Also

  * [Example Program](../../GPIB_Example_Programs/SCPI_Example_Programs.md) using these commands.

  * [SENS:PULSe](Pulse.md) commands used to configure the pulse generators.

  * [PNA-X IF Path Block diagram](../../../IFAccess/IF_Path_Configuration.md)

  * [SENS:IF configuration commands](XSensIF.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## SENSe<ch>:SWEep:PULSe:CWTime[:AUTO] <bool>

Applicable Models: VNAs with Pulsed RF Measurement Option (Read-Write) This
command replaces [SENSe:SWEep:PULSe:IFBW[:AUTO]](SweepPulse.md#ifbw).  Sets
and returns the state of automatic CW sweep time (used in Pulse Profile mode).
This setting is labeled Autoselect Profile Sweep Time on the UI.  
---  
Parameters |   
<ch> |  Channel number of the pulse measurement. If unspecified, value is set to 1.  
<bool> |  Choose from: OFF (or O) - The Sweep Time is not changed automatically. ON (or 1) - In Pulse Profile mode, adjusts the default X-axis start time to zero and the stop time to double the Pulse Width. This allows you to see one complete pulse.  
Examples |  SENS:SWE:PULS:CWT 1 sense2:sweep:pulse:cwtime:auto off  
Query Syntax |  SENSe<ch>:SWEep:PULSe:CWTime[:AUTO]?  
Return Type |  Boolean  
[ Default ](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## SENSe<ch>:SWEep:PULSe:DETectmode[:AUTO] <bool>

Applicable Models: VNAs with Pulsed RF Measurement Option (Read-Write) Set
pulse mode automatically or manually (Narrowband or Wideband) for the channel.
This setting is labeled Autoselect Pulse Detection Method on the UI.  
---  
Parameters |   
<ch> |  Channel number of the pulse measurement. If unspecified, value is set to 1.  
<bool> |  Choose from: OFF (or O) - Manually set the pulse mode. Use [SENSe:SWEep:PULSe:WIDE](SweepPulse.md#wideband) to set the pulse mode. ON (or 1) - Automatically set the pulse mode.  
Examples |  SENS:SWE:PULS:DET 1 sense2:sweep:pulse:detectmode:auto off  
Query Syntax |  SENSe<ch>:SWEep:PULSe:DETectmode[:AUTO]?  
Return Type |  Boolean  
[ Default ](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## SENSe<ch>:SWEep:PULSe:DRIVe[:AUTO] <bool>

Applicable Models: VNAs with Pulsed RF Measurement Option (Read-Write) In
Narrowband pulse mode, set the drive for the source modulation automatically
or manually.  
---  
Parameters |   
<ch> |  Channel number of the pulse measurement. If unspecified, value is set to 1.  
<bool> |  Choose from: OFF (or O) - Manually set source modulation. ON (or 1) - Automatically set pulse gen 1 as the modulation source and pulse gen 2 as the gate source for all gates.  
Examples |  SENS:SWE:PULS:DRIV 1 sense2:sweep:pulse:drive:auto off  
Query Syntax |  SENSe<ch>:SWEep:PULSe:DRIVe[:AUTO]?  
Return Type |  Boolean  
[ Default ](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## SENSe<ch>:SWEep:PULSe:IFBW[:AUTO] <bool> - Superseded

Applicable Models: VNAs with Pulsed RF Measurement Option (Except M9485A)
(Read-Write) This command is replaced with
[SENS:SWEep:PULSe:CWTime[:AUTO]](SweepPulse.md#CWSweepAuto).  In Wideband
pulse mode, set the IF bandwidth automatically or manually.  
---  
Parameters |   
<ch> |  Channel number of the pulse measurement. If unspecified, value is set to 1.  
<bool> |  Choose from: OFF (or O) - Manually set the IFBW for the measurement. ON (or 1) - Automatically set the IFBW for the measurement.  
Examples |  SENS:SWE:PULS:IFBW 1 sense2:sweep:pulse:ifbw:auto off  
Query Syntax |  SENSe<ch>:SWEep:PULSe:IFBW[:AUTO]?  
Return Type |  Boolean  
[ Default ](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## SENSe<ch>:SWEep:PULSe:IFGain[:AUTO] <bool>

Applicable Models: VNAs with Pulsed RF Measurement Option (Except M9485A,
M98xxA, P50xxA/B, E5080B, E5081A) (Read-Write) In Narrowband pulse mode, set
the IF Gain automatically or manually. This setting is labeled Autoselect IF
Path Gain and Loss on the UI.  
---  
Parameters |   
<ch> |  Channel number of the pulse measurement. If unspecified, value is set to 1.  
<bool> |  Choose from: OFF (or O) - Manually set the IF Gain for the measurement. ON (or 1) - Automatically set the IF Gain for the measurement.  
Examples |  SENS:SWE:PULS:IFG 1 sense2:sweep:pulse:ifgain:auto off  
Query Syntax |  SENSe<ch>:SWEep:PULSe:IFGain[:AUTO]?  
Return Type |  Boolean  
[ Default ](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## SENSe<ch>:SWEep:PULSe:MODE <char>

Applicable Models: VNAs with Pulsed RF Measurement Option (Read-Write) Sets
and returns the pulse measurement state for the channel.  
---  
Parameters |   
<ch> |  Channel number of the pulse measurement. If unspecified, value is set to 1.  
<char> |  Choose from: OFF - Turn OFF pulse measurements. STD \- Turn ON standard pulse measurements. PROFILE \- Turn ON pulse profile measurements.  
Examples |  SENS:SWE:PULS:MODE PROFILE sense2:sweep:pulse:mode off  
Query Syntax |  SENSe<ch>:SWEep:PULSe:MODE?  
Return Type |  Character  
[ Default ](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SENSe<ch>:SWEep:PULSe:PRF[:AUTO] <bool>

Applicable Models: VNAs with Pulsed RF Measurement Option (Except M9485A,
M980xA, P50xxA) (Read-Write) In Narrowband pulse mode, choose to set the Pulse
Repetition Frequency automatically or manually. This is labeled "Optimize
Pulse Frequency" on the user-interface. To make changes manually, use
[SENS:SWE:PULS:PRIM:FREQ](SweepPulse.md#MasterFreq) or
[SENS:SWE:PULS:PRIM:PER](SweepPulse.md#MasterPeriod).  
---  
Parameters |   
<ch> |  Channel number of the pulse measurement. If unspecified, value is set to 1.  
<bool> |  Choose from: OFF (or O) - Manually set the PRF for the measurement. ON (or 1) - Automatically set the PRF for the measurement.  
Examples |  SENS:SWE:PULS:PRF 1 sense2:sweep:pulse:prf:auto off  
Query Syntax |  SENSe<ch>:SWEep:PULSe:PRF[:AUTO]?  
Return Type |  Boolean  
[ Default ](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## SENSe<ch>:SWEep:PULSe:PRIMary:CLOCk <string>

Applicable Models: VNAs with Pulsed RF Measurement Option (Read-Write) Sets
and returns the Primary Clock setting and is controlled by the internal or
external pulse generator which is the primary pulse clock. Learn more.  Note:
If there is a defined pulse generator in the external devices list, its name
will be displayed in the Pulse Setup dialog Primary Clock control and it will
also be an accepted choice for this command.  
---  
Parameters |   
<ch> |  Channel number of the pulse measurement. If unspecified, value is set to 1.  
<string> |  Primary clock (Internal or External).  
Examples |  SENS:SWE:PULS:PRIM:CLOC "Internal" sense2:sweep:pulse:primary:clock "External"  
Query Syntax |  SENSe<ch>:SWEep:PULSe:PRIMary:CLOCk?  
Return Type |  String  
[ Default ](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## SENSe<ch>:SWEep:PULSe:PRIMary:FREQuency <value>

Applicable Models: VNAs with Pulsed RF Measurement Option (Read-Write) Sets
and returns the primary pulse measurement frequency.  The frequency is
1/period, so this value can also be set using
[SENS:SWE:PULS:PRIM:PERiod](SweepPulse.md#MasterPeriod). Note: On the Pulse
Setup dialog, this command is a 'Basic setting, which is intended to be used
with the 'Auto' selections set to ON.  
---  
Parameters |   
<ch> |  Channel number of the pulse measurement. If unspecified, value is set to 1.  
<value> |  Primary frequency.  
Examples |  SENS:SWE:PULS:PRIM:FREQ 1e9 sense2:sweep:pulse:primary:frequency 1e6  
Query Syntax |  SENSe<ch>:SWEep:PULSe:PRIMary:FREQuency  
Return Type |  Value  
[ Default ](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1 kHz  
  
* * *

## SENSe<ch>:SWEep:PULSe:PRIMary:PERiod <value>

Applicable Models: VNAs with Pulsed RF Measurement Option (Read-Write) Sets
and returns the primary pulse period.  The period is 1/frequency, so this
value can also be set using
[SENS:SWE:PULS:PRIM:FREQ](SweepPulse.md#MasterFreq). Note: On the Pulse Setup
dialog, this command is a 'Basic' setting, which is intended to be used with
the 'Auto' selections set to ON.  
---  
Parameters |   
<ch> |  Channel number of the pulse measurement. If unspecified, value is set to 1.  
<value> |  Primary period in seconds.  
Examples |  SENS:SWE:PULS:PRIM:PER 1e-6 sense2:sweep:pulse:primary:period 1e-3  
Query Syntax |  SENSe<ch>:SWEep:PULSe:PRIMary:PERiod?  
Return Type |  Value  
[ Default ](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1 msec  
  
* * *

## SENSe<ch>:SWEep:PULSe:PRIMary:WIDTh <value>

Applicable Models: VNAs with Pulsed RF Measurement Option (Read-Write) Sets
and returns the primary pulse width.  Note: On the Pulse Setup dialog, this
command is a 'Basic' setting, which is intended to be used with the 'Auto'
selections set to ON.  
---  
Parameters |   
<ch> |  Channel number of the pulse measurement. If unspecified, value is set to 1.  
<value> |  Primary pulse width in seconds..  
Examples |  SENS:SWE:PULS:PRIM:WIDT sense2:sweep:pulse:primary:width  
Query Syntax |  SENSe<ch>:SWEep:PULSe:PRIMary:WIDTh?  
Return Type |  Value  
[ Default ](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  100 microseconds  
  
* * *

## SENSe<ch>:SWEep:PULSe:PROFile:STARt <value>

Applicable Models: VNAs with Pulsed RF Measurement Option (Read-Write) Sets
and returns the start time of the pulse. Pulse profile measurements provide a
time domain (CW frequency) view of the pulse envelope. Profiling is performed
using a measurement technique that "walks" a narrow receiver "snapshot" across
the width of the pulse. This is analogous to using a camera to take many small
snapshots of a wide image, then piecing them together to form a single,
panoramic view.  
---  
Parameters |   
<ch> |  Channel number of the pulse measurement. If unspecified, value is set to 1.  
<value> |  Start time in seconds. Note: The start value cannot be negative.  
Examples |  SENS:SWE:PULS:PROF:STAR 1e-6 sense2:sweep:pulse:profile:start 1e-3  
Query Syntax |  SENSe<ch>:SWEep:PULSe:PROFile:STARt?  
Return Type |  Value  
[ Default ](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0  
  
* * *

## SENSe<ch>:SWEep:PULSe:PROFile:STOP <value>

Applicable Models: VNAs with Pulsed RF Measurement Option (Read-Write) Sets
and returns the stop time of the pulse. Pulse profile measurements provide a
time domain (CW frequency) view of the pulse envelope. Profiling is performed
using a measurement technique that "walks" a narrow receiver "snapshot" across
the width of the pulse. This is analogous to using a camera to take many small
snapshots of a wide image, then piecing them together to form a single,
panoramic view.  
---  
Parameters |   
<ch> |  Channel number of the pulse measurement. If unspecified, value is set to 1.  
<value> |  Stop time in seconds. Note: The stop value cannot be negative.  
Examples |  SENS:SWE:PULS:PROF:STOP 1e-6 sense2:sweep:pulse:profile:stop 1e-3  
Query Syntax |  SENSe<ch>:SWEep:PULSe:PROFile:STOP?  
Return Type |  Value  
[ Default ](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## SENSe<ch>:SWEep:PULSe:SHAPe <char>

Applicable Models: VNAs with Pulsed RF Measurement Option (Read-Write) Sets
and returns the pulse shape type.  
---  
Parameters |   
<ch> |  Channel number of the pulse measurement. If unspecified, value is set to 1.  
<char> |  Choose from: Normal - Normal pulse shape Fast \- Fast rise time with low on/off ratio. This is available only for M980xA and P50xxA/B with S9x025A/B. The M983xA accepts the "FAST" but no change on the shape.  
Examples |  SENS:SWE:PULS:SHAP "FAST" sense2:sweep:pulse:shape "Fast"  
Query Syntax |  SENSe<ch>:SWEep:PULSe:SHAPe?  
Return Type |  Character  
[ Default ](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Normal  
  
* * *

## SENSe<ch>:SWEep:PULSe:SHAPe:CATalog?

Applicable Models: VNAs with Pulsed RF Measurement Option (Read-Write) Returns
the list of available pulse shape type.  
---  
Parameters |   
<ch> |  Channel number of the pulse measurement. If unspecified, value is set to 1.  
Examples |  SENS:SWE:PULS:SHAP:CAT? sense2:sweep:pulse:shape:catalog?  
Query Syntax |  SENSe<ch>:SWEep:PULSe:SHAPe:CATalog?  
Return Type |  Character  
[ Default ](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SENSe<ch>:SWEep:PULSe:SWGate[:STATe] <bool>

Applicable Models: VNAs with Pulsed RF Measurement Option (Except M9485A,
M98xxA, P50xxA/B, E5080B, E5081A) (Read-Write) When set to OFF, the improved
software gating sensitivity is turned OFF and all data outside the measurement
band is zeroed. This setting is used for troubleshooting purposes.  
---  
Parameters |   
<ch> |  Channel number of the pulse measurement. If unspecified, value is set to 1.  
<bool> |  Choose from: OFF (or O) - Turn OFF software gating. ON (or 1) - Turn ON software gating.  
Examples |  SENS:SWE:PULS:SWG 0 sense2:sweep:pulse:swgate:state on  
Query Syntax |  SENSe<ch>:SWEep:PULSe:SWGate[:STATe]?  
Return Type |  Boolean  
[ Default ](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## SENSe<ch>:SWEep:PULSe:TIMing[:AUTO] <bool>

Applicable Models: VNAs with Pulsed RF Measurement Option (Read-Write) In
Narrowband pulse mode, choose to set the delay and width automatically or
manually. This setting is labeled Autoselect Width and Delay on the UI.  
---  
Parameters |   
<ch> |  Channel number of the pulse measurement. If unspecified, value is set to 1.  
<bool> |  Choose from: OFF (or O) - Manually set the delay and width for the measurement. ON (or 1) - Automatically set the delay and width for the measurement.  
Examples |  SENS:SWE:PULS:TIM 1 sense2:sweep:pulse:timing:auto off  
Query Syntax |  SENSe<ch>:SWEep:PULSe:TIMing[:AUTO]?  
Return Type |  Boolean  
[ Default ](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## SENSe<ch>:SWEep:PULSe:WIDeband[:STATe] <bool>

Applicable Models: VNAs with Pulsed RF Measurement Option (Except M9485A,
M98xxA, P50xxA/B, E5080B, E5081A) (Read-Write) Set and read the pulse mode
detection method.  
---  
Parameters |   
<ch> |  Channel number of the pulse measurement. If unspecified, value is set to 1.  
<bool> |  Choose from: OFF (or 0) - Narrowband mode. ON (or 1) - Wideband mode  
Examples |  SENS:SWE:PULS:WID 1 sense2:sweep:pulse:wideband:state off  
Query Syntax |  SENSe<ch>:SWEep:PULSe:WIDeband[:STATe]?  
Return Type |  Boolean  
[ Default ](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Based on pulse width  
  
* * *

