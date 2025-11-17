# Sense:Sweep Commands

* * *

Specifies the sweep functions of the analyzer.

SENSe:SWEep: [BLOCked](Sweep_SCPI.md#BLOCked_) [DWELl](Sweep_SCPI.md#ssd) | [AUTO](Sweep_SCPI.md#ssda) | [SDELay](Sweep_SCPI.md#SweepDelay) [GENeration](Sweep_SCPI.md#ssg) | [POINtsweep](Sweep_SCPI.md#GenPoint) GROups | [COUNt](Sweep_SCPI.md#ssgc) LFEXtension:STATe [MODE](Sweep_SCPI.md#ssm) [POINts](Sweep_SCPI.md#ssp) [PULSe More commands](SweepPulse.md) SLOCal | MAXimum | STATe [SPEed](Sweep_SCPI.md#SweepSpeed) [SRCPort](Sweep_SCPI.md#sss) [STEP](Sweep_SCPI.md#Step) TIME | [AUTO](Sweep_SCPI.md#ssta) | STARt? | [:STOP] TRIGger | [DELAY](Sweep_SCPI.md#Delay) | [MODE](Sweep_SCPI.md#Mode) | [POINt](Sweep_SCPI.md#sstp) [TYPE](Sweep_SCPI.md#ssty) | [FACW](Sweep_SCPI.md#swpTypeFASTCW)  
---  
  
Click on a keyword to view the command details.

See Also

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * Example [Triggering the VNA using SCPI](../../GPIB_Example_Programs/Triggering_the_PNA_using_SCPI.md)

  * [Learn about Sweeping](../../../S1_Settings/Sweep.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## SENSe<cnum>:SWEep:BLOCked?

Applicable Models: N522xB, N523xB, N524xB, M937xA, M9485A, P937xA (Read-only)
Reads whether the specified channel is currently 'blocked' from sweeping.
Learn more about the [Mechanical
Devices](../../../System/Mechanical_Devices.htm) dialog.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
Examples | SENS:SWE:BLOC? sense2:sweep:blocked?  
Return Type | Boolean 0 - No, the channel is NOT blocked. 1 - Yes, the channel is blocked.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | N/A  
  
* * *

## SENSe<cnum>:SWEep:DWELl <num>

Applicable Models: All (Read-Write) Sets the dwell time between each sweep
point.

  * Dwell time is ONLY available with SENSe:SWEep:GENeration set to STEPped; It is Not available in ANALOG.
  * Sending dwell = 0 is the same as setting SENS:SWE:DWEL:AUTO ON. Sending a dwell time > 0 sets SENS:SWE:DWEL:AUTO OFF.

  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<num> | Dwell time in seconds. This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
Examples | SENS:SWE:DWEL .1  
sense2:sweep:dwell min  
Query Syntax | SENSe<cnum>:SWEep:DWELl?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 - (Note: dwell time set to 0 is the same as dwell:auto ON)  
  
* * *

## SENSe<cnum>:SWEep:DWELl:AUTO <ON | OFF>

Applicable Models: All (Read-Write) Specifies whether or not to automatically
calculate and set the minimum possible dwell time. Setting Auto ON has the
same effect as setting dwell time to 0.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<ON | OFF> | ON (or 1) - turns dwell ON.  
OFF (or 0) - turns dwell OFF.  
Examples | SENS:SWE:DWEL:AUTO ON  
sense2:sweep:dwell:auto off  
Query Syntax | SENSe<cnum>:SWEep:DWELl:AUTO?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## SENSe<cnum>:SWEep:DWELl:SDELay <num>

Applicable Models: All (Read-Write) Specifies the time to wait just before
acquisition begins for each sweep. This delay is in addition to [Dwell
Time](Sweep_SCPI.htm#ssd) and the following two External Trigger delays if
enabled.

  * [Trig:Delay](../Trigger_SCPI.md#delay) (global scope)
  * [Sens:Swe:Trig:Delay](Sweep_SCPI.md#Delay) (channel scope)

  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<num> | Sweep delay in seconds. This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
Examples | SENS:SWE:DWEL:SDEL .1  
sense2:sweep:dwell:sdelay .5  
Query Syntax | SENSe<cnum>:SWEep:DWELl:SDELay?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## SENSe<cnum>:SWEep:GENeration <char>

Applicable Models: All (Read-Write) Sets sweep as Stepped or Analog.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<char> | Choose from: STEPped \- source frequency is CONSTANT during measurement of eah displayed point. More accurate than ANALog. Dwell time can be set in this mode. ANALog \- source frequency is continuously RAMPING during measurement of each displayed point. Faster than STEPped. Sweep time (not dwell time) can be set in this mode.  
Examples | SENS:SWE:GEN STEP  
sense2:sweep:generation analog  
Query Syntax | SENSe<cnum>:SWEep:GENeration?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Analog  
  
* * *

## SENSe<cnum>:SWEep:GENeration:POINtsweep <bool>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Turns
ON and OFF point sweep mode. When enabled, the VNA measures both the forward
and reverse parameters at each frequency point before stepping to the next
frequency. [Learn more.](../../../S1_Settings/Sweep.md#SweepSetupDiag)  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<char> | Choose from: ON or (1) - Enable point sweep mode. OFF or (0) - Disable point sweep mode.  
Examples | SENS:SWE:GEN:POIN 1 sense2:sweep:generation:pointsweep off  
Query Syntax | SENSe<cnum>:SWEep:GENeration:POINtsweep?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SENSe<cnum>:SWEep:GROups:COUNt <num>

Applicable Models: All (Read-Write) Sets the trigger count (groups) for the
specified channel. Set trigger mode to group after setting this count.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<num> | Count (groups) number. Choose any number between:  
1 and 2e6 (1 is the same as single trigger)  
Examples | SENS:SWE:GRO:COUN 10  
sense2:sweep:groups:count 50  
Query Syntax | SENSe<cnum>:SWEep:GROups:COUNt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## SENSe<cnum>:SWEep:LFEXtension:STATe <bool>

Applicable Models: N5222B, N5227B, N5242B, N5247B, N5290A, N5291A (Read-Write)
Turns ON or OFF low frequency extension for extending the range down to 1 kHz
start frequency.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<bool> | Choose from: ON or 1 - Turns ON low frequency extension. OFF or 0 - Turns OFF low frequency extension.  
Examples | SENS:SWE:LFEX:STAT ON  
sense2:sweep:lfextension:state off  
Query Syntax | SENSe<cnum>:SWEep:LFEXtension:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF or 0  
  
* * *

## SENSe<cnum>:SWEep:MODE <char>

Applicable Models: All (Read-Write) Sets the number of trigger signals the
specified channel will ACCEPT. See [Triggering the VNA Using
SCPI.](../../GPIB_Example_Programs/Triggering_the_PNA_using_SCPI.htm)  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<char> | Trigger mode. Choose from: HOLD \- channel will not trigger CONTinuous \- channel triggers indefinitely GROups \- channel accepts the number of triggers specified with the last [SENS:SWE:GRO:COUN](Sweep_SCPI.md#ssgc) <num>. This is one of the VNA overlapped commands. [Learn more.](../../Learning_about_GPIB/Understanding_Command_Synchronization.md) SINGle \- channel accepts ONE trigger, then goes to HOLD. Note: To perform simple, single-triggering, use SINGle which requires that [TRIG:SOURce](../Trigger_SCPI.md#tss) remain in the default (internal) setting.  
Examples | SENS:SWE:MODE CONT  
sense2:sweep:mode hold  
Query Syntax | SENSe<cnum>:SWEep:MODE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | CONTinuous  
  
* * *

## SENSe<cnum>:SWEep:POINts <num>

Applicable Models: All (Read-Write) Sets the number of data points for the
measurement.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<num> | Choose any number between 1 and the [VNA maximum number of points.](../../../S1_Settings/DPoints.md#PointsDiag) This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information.  
Examples | SENS:SWE:POIN 51  
sense2:sweep:points max  
Query Syntax | SENSe<cnum>:SWEep:POINts?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 201  
  
* * *

## SENSe<cnum>:SWEep:SLOCal:MAXimum <num>

Applicable Models: N522xB, N523xB, N524xB, E5080A/B, M9485A, M98xxA, P50xxA/B,
P93xxB (Read-Write) Sets the Shift LO maximum frequency for the selected
channel.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<num> | Range of shift LO maximum frequency is 1.5E8 to Maximum frequency.  
Examples | SENS:SWE:SCLOC:MAX 1.5E8  
sense2:sweep:slocal:maximum 1.5E8  
Query Syntax | SENSe<cnum>:SWEep:SLOCal:MAXimum?  
Return Type | Numeric / Double precision floating point  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Maximum frequency  
  
* * *

## SENSe<cnum>:SWEep:SLOCal:STATe <bool>

Applicable Models: N522xB, N523xB, N524xB, E5080A/B, M9485A, M98xxA, P50xxA/B,
P93xxB  (Read-Write) Turns ON or OFF the Shift LO mode for the selected
channel.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<bool> | Select shoft LO mode from either of the following: ON or 1 - Turns ON the Shift LO mode. OFF or 0 - Turns OFF the Shift LO mode.  
Examples | SENS:SWE:SLOC:STAT ON  
sense2:sweep:slocal:state off  
Query Syntax | SENSe<cnum>:SWEep:SLOCal:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF or 0  
  
* * *

## SENSe<cnum>:SWEep:SRCPort <1 | 2> Superseded

Applicable Models: All but M9485A This command is superseded. The
[Calc:Par:Def:Ext](../Calculate/Parameter.md#DefineExtend) and
[Calc:Par:Mod:Ext](../Calculate/Parameter.md#ModExtend) can now optionally
include the source port. (Read-Write) Sets the source port when making non
S-parameter measurements. Has no effect on S-parameter measurements.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<1 | 2> | 1 \- Source power comes out Port 1 2 \- Source power comes out Port 2  
Examples | SENS:SWE:SRCP 1  
sense2:sweep:srcport 2  
Query Syntax | SENSe<cnum>:SWEep:SRCPort?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## SENSe<cnum>:SWEep:SPEed <char>

Applicable Models: All (Read-Write) Sets and returns the state of Fast Sweep
mode. [Learn more about Fast
Sweep.](../../../S1_Settings/Sweep.htm#SweepSetupDiag)  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<char> | Fast Sweep mode. Choose from: FAST \- turns Fast Sweep Mode ON NORMal \- turns Fast Sweep Mode OFF (Normal Mode).  
Examples | SENS:SWE:SPE NORM  
sense2:sweep:speed fast  
Query Syntax | SENSe<cnum>:SWEep:SPEed?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | NORMal  
  
* * *

## SENSe<cnum>:SWEep:STEP <num>

Applicable Models: All (Read-Write) Sets the frequency step size across the
selected frequency range. This effectively sets the number of data points.
Available ONLY when [Sweep Type](Sweep_SCPI.md#ssty) = Linear.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<num> | Frequency step size in Hz. Select any value up to the frequency range of the analyzer.  
Examples | SENS:SWE:STEP 1e6  
sense2:sweep:step 1000000  
Query Syntax | SENSe<cnum>:SWEep:STEP?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | NA  
  
* * *

## SENSe<cnum>:SWEep:SRCPort:EXTended

(Read-Write) This command is a helper command for
[CALC:MEAS:DEF](../Calculate/Measure.md#CALCulate:MEASure:DEFine). The user
would set the srcport with this command and then request a non S-parameter
measurem,ent from
[CALC:MEAS:DEF](../Calculate/Measure.md#CALCulate:MEASure:DEFine), such as
"A".  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
|  
Examples | SENS:SWE:SRCP:EXT sense2:sweep:srcport:extended  
Query Syntax | SENSe<cnum>:SWEep:SRCPort:EXTended?  
Return Type |   
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<cnum>:SWEep:TIME:AUTO <ON | OFF>

Applicable Models: All (Read-Write) Turns the automatic sweep time function ON
or OFF.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<ON | OFF> | ON (or 1) - turns the automatic sweep time ON. OFF (or 0) \- turns the automatic sweep time OFF.  
Examples | SENS:SWE:TIME:AUTO  
sense2:sweep:time:auto off  
Query Syntax | SENSe<cnum>:SWEep:TIME:AUTO?  
Return Type | Boolean (1 = ON, 0 = OFF)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## SENSe<cnum>:SWEep:TIME:STARt?

Applicable Models: All (Read-only) Returns the time the first point of a Time
Sweep is measured.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
Examples | SENS:SWE:TIME:STAR?  
sense2:sweep:time:start?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<cnum>:SWEep:TIME[:STOP] <num>

Applicable Models: All (Read-Write) Sets the time the analyzer takes to
complete one sweep. If sweep time accuracy is critical, use ONLY the values
that are attained using the up and down arrows next to the sweep time entry
box. [See Sweep Time.](../../../S1_Settings/Sweep.md#sweepTimeDiag)  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<num> | Sweep time in seconds. To select the fastest sweep speed, either send MIN as an argument to this command, or send SENS:SWE:TIME:AUTO 1. This command will accept MIN or MAX instead of a numeric parameter. See [SCPI Syntax](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min) for more information. The MAX value will change based on point count, IFBW, and dwell time.  
Examples | SENS:SWE:TIME 1ms  
sense2:sweep:time .001  
Query Syntax | SENSe<cnum>:SWEep:TIME[:STOP]?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | NA  
  
* * *

## SENSe<cnum>:SWEep:TRIGger:DELay <num>

Applicable Models: All (Read-Write) Sets and reads the trigger delay for all
measurements in the specified CHANNEL. This delay is only applied while
[TRIG:SOURce EXTernal](../Trigger_SCPI.md#tss) and [TRIG:SCOP
CURRent](../Trigger_SCPI.htm#tssc) . After an external trigger is applied, the
start of the sweep is delayed for the specified delay value plus any inherent
latency. To apply a trigger delay for all channels (Global), use
[TRIG:DEL](../Trigger_SCPI.md#delay)  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<num> | Trigger delay value in seconds. Range is from 0 to 3 seconds  
Examples | SENS:SWE:TRIG:DELay .003  
sense2:sweep:trigger:delay 1  
Query Syntax | SENSe<cnum>:SWEep:TRIGger:DELay?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## SENSe<cnum>:SWEep:TRIGger:MODE <char>

Applicable Models: All (Read-Write) Sets and reads the trigger mode for the
specified channel. This determines what EACH signal will trigger. [Learn
more.](../../../S1_Settings/Trigger.htm#TriggerMode) Note: Setting Point and
Sweep mode forces [Trigger:SCOPe](../Trigger_SCPI.md#tssc) = CURRent  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<char> | Trigger mode. choose from:

  * CHANnel \- Each trigger signal causes ALL traces in that channel to be swept.
  * SWEep \- Each Manual or External trigger signal causes ALL traces that share a source port to be swept.
  * POINt -\- Each Manual or External trigger signal causes one data point to be measured.
  * TRACe \- Allowed ONLY when [SENS:SWE:GEN:POIN](Sweep_SCPI.md#GenPoint) is enabled. Each trigger signal causes two identical measurements to be triggered separately - one trigger signal is required for each measurement. Other trigger mode settings cause two identical parameters to be measured simultaneously.
  * SEGment \- Each trigger signal causes one Segment of a Segment Sweep to be measured.

  
Examples | SENS:SWE:TRIG:MODE SWE  
sense2:sweep:trigger:mode point  
Query Syntax | SENSe<cnum>:SWEep:TRIGger:MODE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Channel  
  
* * *

## SENSe<cnum>:SWEep:TRIGger:POINt <ON | OFF> Superseded

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA This command is
replaced with [SENS:SWE:TRIG:MODE POINT](Sweep_SCPI.md#Mode) (Read-Write)
Specifies whether the specified channel will measure one point for each
trigger or all of the measurements in the channel. Setting any channel to
POINt mode will automatically set the
[TRIGger:SCOPe](../Trigger_SCPI.md#tssc) = CURRent.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<ON | OFF> | ON (or 1) - Channel measures one data point per trigger. OFF (or 0) \- All measurements in the channel made per trigger.  
Examples | SENS:SWE:TRIG:POIN ON  
sense2:sweep:trigger:point off  
Query Syntax | SENSe<cnum>:SWEep:TRIGger:POINt?  
Return Type | Boolean (1 = Point, 0 = Measurement)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 - Measurement  
  
* * *

## SENSe<cnum>:SWEep:TYPE <char>

Applicable Models: All (Read-Write) Sets the type of analyzer sweep mode.
First set sweep type, then set sweep parameters such as frequency or power
settings. Note: For SweptIMD channels, use [SENS:IMD:SWE:TYPE
SEGMent](IMD.htm#SweepType) See Also: [FCA Segment Sweep
commands](MixerSegment.htm)  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<char> | Choose from: LINear | LOGarithmic | POWer | CW | SEGMent | PHASe Note: SWEep TYPE cannot be set to SEGMent if there are no segments turned ON. A segment is automatically turned ON when the analyzer is started.  
Examples | SENS:SWE:TYPE LIN sense2:sweep:type segment  
Query Syntax | SENSe<cnum>:SWEep:TYPE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | LINear  
  
* * *

## SENSe<cnum>:SWEep:TYPE:FACW <num>

Applicable Models: N522xB, N524xB, M937xA, P937xA (Read-Write) Enables Fast CW
sweep and sets the number of data points for the channel. [Sweep
Type](Sweep_SCPI.htm#ssty) must already be set to CW and FIFO must already be
enabled.

### See Also

[FIFO commands](../SystFIFO.md) [Example
program](../../GPIB_Example_Programs/Setup_FastCW_and_FIFO.htm) [N5264B
Measurement Receiver](../../../IFAccess/N5264A.htm)  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<num> | Number of data points to measure in Fast CW mode. This setting overwrites the standard number of points setting for the channel. The minimum value is 1. The maximum value is 232 \- 1 = 2,147,483,647. The "-1" indicates infinite point count (i.e., go forever). Any other value will produce invalid results. If the data acquisition rate exceeds 400,000 points per second, the upper limit on the number of points is 11e6. The following are conditions that can cause the higher data rate:

  * IFBW's >= 1 MHz and internally triggered.
  * fastCW sweeps that are externally triggered at a rate faster than 400,000 points per second.

Set to 0 to disable Fast CW.  
Examples | SENS:SWE:TYPE:FACW 1e6  
sense2:sweep:type facw 1e3  
Query Syntax | SENSe<cnum>:SWEep:TYPE:FACW?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 \- Disabled  
  
* * *

