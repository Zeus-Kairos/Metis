# SYSTem Commands

* * *

Controls and queries settings that affect the VNA system.

SYSTem: [ABORt:THReshold](System.md#abort) ACTive | [CHANnel](System.md#ActiveChannel) | MARKer | MCLass | MEASurement | NUMBer? | PORT | SOURce? | TEST? | SHEet? | TRACe? | WINDow BEEPer | COMPlete:IMMediate | STATe | [VOLume](System.md#beepVol) | WARNing:IMMediate [CAL:ALL More commands](SystCalAll.md) [CAL:PHASe More commands](SystCalPhase.md) [CAPability More commands](SystCapability.md) CHANnels | [CATalog?](System.md#ChanCat) | [COUPle[:STATe]](System.md#chanCouple) | COUPle:GROup | COUPle:PARallel[:ENABle] | COUPle:PARallel:STATe? | [GCSetup More commands](SystChanGCS.md) | [NOISe:PARallel[:ENABle]](System.md#NOISePARallelENABle) | [NOISe:PARallel:GROup](System.md#NOISePARallelGROup) | [NOISe:PARallel:GROup:LIST](System.md#NOISePARallelGROupLIST) | [NOISe:PARallel:STATe?](System.md#NOISePARallelSTATe) | [DELete](System.md#ChanDelete) | [HOLD](System.md#hold) | [RESume](System.md#resume) | SINGle | [SINGle:COMBine](System.md#PXIChanCombine) [CLOCk[:STATe]](System.md#clock) [COMMunicate More commands](SystCommunicate.md) [CONFigure](System.md#config) | BIT? | [DIRectory](System.md#ConfDir) | [MWAVe More commands](SystConfig_mmWave.md) | REVision | [CPU?](System.md#confCPU) | [DSP?](System.md#confDSP) | [DSPFpga?](System.md#confDSPF) | PNA | SYNThesizer:VERSion? [CONFiguration:EDEVice More commands](SystConfigExternalDevice.md) CORRection | [INTerpolate:LINear More commands](SystCorrIntLinear.md) | [WIZard[:IMMediate]](System.md#wiz) DATA | MEMory | Add | CATalog? | CLOSe | FILE | COMMit | FILE | DELete | INITialize | NAME? | OFFSet? | REPeat | RESet | RESet | SIZE DATE? DISK:REVision? [ERRor?](System.md#error) | [COUNt?](System.md#ercount) | REPort | [SUNLeveled](System.md#unlevel) FCORrection:CHANnel: | COUPler[:STATe] | [RFRange[:STATe]](System.md#SystFcorChanRef) [FIFO More commands](SystFIFO.md) [FPReset](System.md#Fpre) ISPControl | [:STATe] LOCal MACRO:COPY | [CHANnel[:TO]](System.md#COPY_CHANnel) | [SOURce](System.md#copySPC) | CHANnel | STATe MCLass | CATalog? | [PARameter:CATalog?](System.md#mClassParCat) | [VALid:CATalog?](System.md#mclass) MEASure [ | CATalog?](System.md#measCat) | CHANnel? | [NAME?](System.md#MeasName) | NUMBer? | [TRACe?](System.md#MeasTrace) | [WINDow?](System.md#MeasWindow) PERSona | MANufacturer | DEFault | MODel | DEFault POFF POWer: | [LIMit](System.md#powerLimit) | CAL | STATe | [LOCK](System.md#PowerLock) | [STATe](System.md#PowerLimState) [PREFerences More commands](System_Preferences.md) [PRESet](System.md#pre) SECurity | [[LEVel]](System.md#Security) [SERVice More commands](System_Service_SCPI.md) [SET](System.md#Set) SHEets:CATalog? SHORtcut | [ARGuments](System.md#MacroArgue) | [DELete](System.md#MacroDelete) | [EXECute](System.md#MacroExecute) | [PATH](System.md#MacroPath) | [TITLe](System.md#MacroTitle) SIMulator:DUT | [FILE](System.md#SimDutFil) | [NOISe[:STATe]](System.md#SimDutNois) [TDR](TDR_System.md) TIME? [TOUChscreen[:STATe]](System.md#touchscreen) [UNCertainty More commands](SystUncertainty.md) [UPReset](System.md#UPreset) | [FPANel[:STATe]](System.md#UpreFpanel) | [LOAD[:FILE]](System.md#UPresetLoad) | [SAVE[:STATe]](System.md#UpresetSave) WINDows [ | CATalog?](System.md#winCat)  
---  
  
Click on a red keyword to view the command details.

See Also

  * [Referring to Traces Channels Windows and Meas Using SCPI](../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.md)

  * [Learn about VNA Preferences](../../System/Preferences.md)

  * [Example Programs](../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## SYSTem:ABORt:THReshold <value>

Applicable Models: All (Read-Write) When a VNA setting is made while a sweep
is in progress, the sweep is immediately aborted by default. This command
allows you to change that behavior by specifying a time threshold. When a
setting change is made during a sweep and if the total sweep time is less than
the threshold time, then the sweep is allowed to finish instead of immediately
aborting.  In general, VNA setting changes that could cause an aborted sweep
are changes that affect how a measurement is made, such as changes in stimulus
conditions. For example, with a threshold setting of 60 seconds:

  * Sweeps that require 60 seconds or less from start to finish will be allowed to complete if a VNA setting change is made at any time during the sweep.
  * Sweeps that require MORE than 60 seconds from start to finish will be immediately aborted when a VNA setting change is made at any time during the sweep.

Notes:

  * Preset clears this setting.
  * Save state saves this setting.
  * Sweep times are estimated.
  * This setting affects ALL channels.

  
---  
Parameters |   
<value> |  Threshold time in seconds. Set to 0 to immediately abort a sweep when a VNA setting is made.  
Examples |  SYST:ABOR:THR 10 'When a setting is made during a sweep, if that sweep requires less than 10 seconds more to complete, it will be allowed to finish instead of aborting.  
Query Syntax |  SYSTem:ABORt:THReshold?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0 - No threshold time; all sweeps are immediately aborted.  
  
* * *

## SYSTem:ACTive:CHANnel?

Applicable Models: All (Read-only) Returns the number of the active channel.
The active channel is the channel number that contains the active measurement.
The active measurement is the trace that has a highlighted Tr# in the [Trace
Status](../../S1_Settings/Customize_Your_Analyzer_Screen.htm#trace_status)
area.  If there is no active channel, 0 is returned.  
---  
Examples |  SYST:PRES SYST:ACT:CHAN? 'Returns 1  
Return Type |  Integer  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:ACTive:MARKer <mkr>

Applicable Models: All (Read-Write) Sets and reads the active marker  
---  
Parameters |   
<mkr> |  Active marker.  
Examples |  SYST:ACT:MARK 1  
Return Type |  Integer  
Query Syntax |  SYSTem:ACTive:MARKer?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1  
  
* * *

## SYSTem:ACTive:MCLass <string>

Applicable Models: All (Read-Write) Sets and reads the active measurement
class.  
---  
Parameters |   
<string> |  Active measurement class.  
Examples |  SYST:ACT:MCL "Standard"  
Return Type |  String  
Query Syntax |  SYSTem:ACTive:MCLass?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Standard  
  
* * *

## SYSTem:ACTive:MEASurement?

Applicable Models: All (Read-only) Returns the name of the active measurement.
While looking at the VNA display, the active measurement is the trace that has
a highlighted Tr# in the [Trace
Status](../../S1_Settings/Customize_Your_Analyzer_Screen.htm#trace_status)
area. Only displayed measurements can be active.  If there is no active
measurement, " " (empty string) is returned.  
---  
Examples |  SYST:PRES  
SYST:ACT:MEAS? 'Returns "CH1_S11_1"  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:ACTive:MEASurement:NUMBer? <mnum>

Applicable Models: All (Read-only) Returns the active measurement number.  
---  
Parameters |   
<mnum> |  Measurement number for each measurement. There must be a selected measurement on the trace. If unspecified, <mnum> is set to 1.  
Examples |  SYST:PRES  
SYST:ACT:MEAS:NUMB?  
Return Type |  Integer  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1  
  
* * *

## SYSTem:ACTive:PORT:SOURce?

Applicable Models: All (Read-only) Gets the active source port number.  
---  
Parameters |   
Examples |  SYST:ACT:PORT:SOURce?  
Return Type |  Integer  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1  
  
* * *

## SYSTem:ACTive:PORT:TEST?

Applicable Models: All (Read-only) Gets the active test port number.  
---  
Parameters |   
Examples |  SYST:ACT:PORT:TEST?  
Return Type |  Integer  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1  
  
* * *

## SYSTem:ACTive:SHEet?

Applicable Models: All (Read-only) Returns the active sheet number.  
---  
Examples |  SYST:ACT:SHE? 'Returns "1"  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1  
  
* * *

## SYSTem:ACTive:TRACe?

Applicable Models: All (Read-only) Returns the active trace number.  
---  
Examples |  SYST:ACT:TRAC? 'Returns "1"  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1  
  
* * *

## SYSTem:ACTive:WINDow <wnum>

Applicable Models: All (Read-Write) Sets or gets the active window number.  
---  
Parameters |   
<wnum> |  The active window number.  
Examples |  SYST:ACT:WIND 1  
Return Type |  Integer  
Query Syntax |  SYSTem:ACTive:WINDow?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1  
  
* * *

## SYSTem:BEEPer:COMPlete:IMMediate

Applicable Models: All (Write-only) This command generates a beep for the
notification of the completion of an operation.  
---  
Parameters |  None  
Examples |  SYST:BEEP:COMP:IMM  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:BEEPer:STATe <num>

Applicable Models: All (Read-Write) Sets the beeper on or off.  
---  
Parameters |   
<bool> |  ON (1) or OFF (0).  
Examples |  SYST:BEEP:STAT 1  
Query Syntax |  SYSTem:BEEPer:STAT?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1  
  
* * *

## SYSTem:BEEPer:VOLume <num>

Applicable Models: N522xB, N523xB, N524xB, M937xA, M9485A, P937xA (Read-Write)
Sets and reads the volume of the internal speaker.  
---  
Parameters |   
<num> |  Relative volume of the internal speaker. Choose a volume between 0 (off) and 100.  
Examples |  SYST:BEEP:VOL 5 system:beeper:volume  
Query Syntax |  SYSTem:BEEPer:VOLume?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0  
  
* * *

## SYSTem:BEEPer:WARNing:IMMediate

Applicable Models: All (Write-only) This command generates a beep for the
notification of warning/limit test results.  
---  
Parameters |  None  
Examples |  SYST:BEEP:WARN:IMM  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:CHANnels:CATalog?

Applicable Models: All (Read-only) Returns the channel numbers currently in
use.  
---  
Examples |  SYST:CHAN:CAT? system:channels:catalog? 'Returns: "1,2,3"  
Return Type |  String of comma-separated numbers  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:CHANnels:COUPle[:STATe] <bool>

Applicable Models: All (Read-Write) Sets and reads the state of channel
coupling. This causes the VNA to emulate Keysight 8720 channel coupling.  When
set to ON, all existing S-parameter channels receive the stimulus settings of
the active channel. Subsequent changes made to any coupled channel are changed
on all coupled channels. Channels with applications such as SMC, VMC, GCA,
Noise, IMD are not affected. Coupling is primarily aimed at stimulus settings
(such as start, stop, points, power) but also applies to many trigger settings
and to Cal Set pointers.  
---  
Parameters |   
<bool> |  ON (or 1) Channels are coupled OFF (or 0) Channels are NOT coupled  
Examples |  SYST:CHAN:COUP 1 system:channels:couple:state OFF  
Query Syntax |  SYSTem:CHANnels:COUPle[:STATe]?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SYSTem:CHANnels:COUPle:GROup <iarray>

Applicable Models:  All (Read-Write) Sets and reads the group of channels for
the mult-DUT parallel measurement.  
---  
Parameters |   
<array> |  {<number of group>, <start channel No.>, <end channel No.>, ... } The first item means number or groups. Next pairs show start/end channel numbers of the group. 1 pair for 1 group. Example: {0} Global coupling (default setting) {1, 1,4} Couples channel 1-4 {2, 1,3, 5,7} Couples channel 1-3 and 5-7 independently  
Examples |  SYST:CHAN:COUP:GRO 2,1,3,5,7 system:channels:couple:group 1,1,4  
Query Syntax |  SYSTem:CHANnels:COUPle:GROup?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0  
  
* * *

## SYSTem:CHANnels:COUPle:PARallel[:ENABle] <bool>

Applicable Models: M9485A, M980xA, P500xA/B, E5080B, E5081A, M983xA (Read-
Write) Sets and reads the Multi DUT parallel measurement state. SYST:CHAN:COUP
should be also turned on when Multi DUT parallel measurement is performed.  
---  
Parameters |   
<bool> |  ON (or 1) Multi DUT parallel measurement are enabled OFF (or 0) Multi DUT parallel measurement are NOT enabled  
Examples |  SYST:CHAN:COUP:PAR 1 system:channels:couple:parallel OFF  
Query Syntax |  SYSTem:CHANnels:COUPle:PARallel[:ENABle]?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SYSTem:CHANnels:COUPle:PARallel:STATe? <value>

Applicable Models: N522xB, N523xB, N524xB, M937xA, M9485A, P937xA, M983xA
(Read Only) Gets the information if the parallel measurement is executed in
the last sweep, for the targeted channel.  
---  
Parameters |   
<value> |  Channel number  
Examples |  SYST:CHAN:COUP:PAR:STAT? 1 system:channels:couple:parallel:state? 2  
Query Syntax |  SYSTem:CHANnels:COUPle:PARallel:STATe?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:CHANnels:NOISe:PARallel[:ENABle] <bool>

Applicable Models: M9485A (Read-Write) Sets and reads the Noise Figure Dual-
band Parallel Measurement state. SYST:CHAN:COUP should be also turned on when
Noise Figure Dual-band Parallel Measurement is performed. This function is
supported only for M9385A which has options both 028 and 720.  
---  
Parameters |   
<bool> |  ON (or 1) Noise Figure Dual-band parallel measurement are enabled OFF (or 0) Noise Figure Dual-band parallel measurement are NOT enabled  
Examples |  SYST:CHAN:NOIS:PAR 1 system:channels:noise:parallel OFF  
Query Syntax |  SYSTem:CHANnels:NOISe:PARallel[:ENABle]?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SYSTem:CHANnels:NOISe:PARallel:GROup <iarray>

Applicable Models: M9485A (Read-Write) Sets and reads the group of channels
for the Noise Figure Dual-band Parallel Measurement. This function is
supported only for M9385A which has options both 028 and 720.  
---  
Parameters |   
<iarray> |  <num of groups>, <first channel of group #1>, <second channel of group #1>,<first channel of group #2>, <second channel of group #2>, ,<first channel of group #n>, <second channel of group #n> Two consecutive channels can be assigned into one group. Example: {1, 1,2} measures NF channels 1 and 2 in parallel. {2, 3,4, 8,9} measures NF channels 3 and 4, then 8 and 9 in parallel.  
Examples |  SYST:CHAN:NOIS:PAR:GRO 1,1,2 system:channels:noise:parallel:group 1,1,2  
Query Syntax |  SYSTem:CHANnels:NOISe:PARallel:GROup?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0  
  
* * *

## SYSTem:CHANnels:NOISe:PARallel:GROup:LIST <iarray>

Applicable Models: M9485A (Read-Write) Sets and reads the group of channels
for the Noise Figure Dual-band Parallel Measurement. This command allows you
to setup any two channels in one group. This function is supported only for
M9385A which has options both 028 and 720.  
---  
Parameters |   
<iarray> |  <num of groups>,  
<num of channels in group #1>, <channel>, <channel>,...  
<num of channels in group #2>, <channel>, <channel>,... Several channels can
be assigned to one group Example: {1, 2,1,3} measures NF channels 1 and 3 in
parallel.  
{2, 2,1,3, 2,5,7} measures NF channels 1 and 3, then 5 and 7 in parallel.  
Examples |  SYST:CHAN:NOIS:GRO:PAR:LIST 2, 3,1,3, 2,5,7 system:channels:noise:parallel:group:list 2, 2,1,3, 2,5,7  
Query Syntax |  SYSTem:CHANnels:NOISe:PARallel:GROup:LIST?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0  
  
* * *

## SYSTem:CHANnels:NOISe:PARallel:STATe? <value>

Applicable Models: M9485A (Read Only) Gets the information if the parallel
measurement is executed in the last sweep, for the targeted channel. This
function is supported only for M9385A which has options both 028 and 720.  
---  
Parameters |   
<value> |  Channel number  
Examples |  SYST:CHAN:NOIS:PAR:STAT? 1 system:channels:noise:parallel:state? 2  
Query Syntax |  SYSTem:CHANnels:NOISe:PARallel:STATe?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:CHANnels:DELete <value>

Applicable Models: All (Write-only) Deletes the specified channel.  
---  
Parameters |   
<value> |  Channel number to delete  
Examples |  SYST:CHAN:DEL 2  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:CHANnels:HOLD

Applicable Models: All (Write-only) Places all channels in hold mode. To place
a single channel in hold mode, use [SENS:SWE:MODE](Sense/Sweep_SCPI.md#ssm).  
---  
Examples |  SYST:CHAN:HOLD  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:CHANnels:RESume

Applicable Models: All (Write-only) Resumes the trigger mode of all channels
that was in effect before sending SYSTem:CHANnels:HOLD (must be sent before
SYST:CHAN:RESume).  
---  
Examples |  SYST:CHAN:RES  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:CHANnels:SINGle <chanNums>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA, M983xA (Write-only)
Sets up multiple channels for manual trigger and provides a method of
triggering multiple channels using manual trigger. There are several
prerequisites for using this command:

  * Manual trigger mode must be used (INIT:CONT OFF)
  * All channels in HOLD (SENS:SWE:MODE HOLD), not just the channels being triggered
  * No acquisitions currently running (instrument is NOT sweeping - see [ABORt:THReshold](System.md#abort))
  * All specified channels must exist

If the above conditions are not met, then the command will generate an error
which describes what is at fault. If the above conditions are met, then the
trigger count for the specified channels is set to 1. Issuing an *OPC? query
will indicate when the first channel is armed (ready for manual trigger). It
is not necessary to wait for *OPC? before sending INIT:IMM to trigger the
first channel. After the first channel is triggered, *OPC? will indicate when
all armed channels have finished acquiring data. Channels will be sorted by
channel number, and acquire in order from lowest channel number first to
highest channel number last.  
---  
Parameters |   
<chanNums> |  Existing comma separated list of channel numbers.  
Examples |  SYST:CHAN:SING 1,3,4 System:channels:single 1,3,4  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:CHANnels:SINGle:COMBine <chanNums>

Applicable Models: M937xA, P937xA (Write-only) Sets the trigger count on the
list of channels to ONE, and then combines the channels into a single
efficient acquisition. The index line stays high during the entire
acquisition.  
---  
Parameters |   
<chanNums> |  Existing comma separated list of channel numbers to combine.  
Examples |  SYST:CHAN:SING:COMB 1,3,4 System:channels:single:combine 1,3,4  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
## SYSTem:CLOCk[:STATe] <bool>

Applicable Models: All (Read-Write) Sets and reads the clock visibility state
in the VNA status bar.  
---  
Parameters |   
<bool> |  ON (or 1) Clock is visible in the VNA status bar. OFF (or 0) Clock is NOT visible in the VNA status bar.  
Examples |  SYST:CLOC 1 system:clock:state OFF  
Query Syntax |  SYSTem:CLOCk[:STATe]?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## SYSTem:CONFigure <model>,<address>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Write-only)
Restarts as an "N-port" VNA using the specified multiport test set.  [Learn
more about VNA Multiport
capability](../../System/External_Testset_Control.htm). [See other commands to
configure multiport test sets.](Sense/Multiplexer.htm)  
---  
Parameters |   
<model> |  String - Model of the test set with which to restart. Use "Native" to restart without a test set. To see a list of supported test sets, use [SENS:MULT:CAT?](Sense/Multiplexer.md#Catalog)  
<address> |  Numeric - GPIB Address of the test set. Ignored when model = "Native".  
Examples |  SYST:CONF "NATIVE",0 system:configure "N44xx",18  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:CONFigure:BIT?

Applicable Models: All (Read-only) Returns whether VNA FW is 32 bit
application or 64 bit application. Returns the word size (32 or 64).  
---  
Parameters |  None  
Examples |  SYST:CONF:BIT?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:CONFigure:DIRectory? <char>

Applicable Models: All (Read-only) Returns the directory path location for the
specified file type.  
---  
Parameters |  None  
<char> |  Type of file. Choose from: STATe - This is the location for the storage of state files. APPLication - This is the location of the VNA firmware executable files. SUPPort - This is the location of private support files for the VNA firmware. [See these file locations](../../S0_Start/Windows_File_Locations.md).  
Example |  SYST:CONF:DIR? SUPP  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SYSTem:CONFigure:REVision:CPU?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Returns
a number that corresponds to the VNA CPU speed that is visible in the Help,
About Network Analyzer dialog box. [Learn more.](../../S0_Start/HelpAbout.md)
Use the following table to learn the clock speed using the returned value.
Reported CPU version - Clock speed 1.0 \- 266 MHz (PNA), 2.53 GHz dual core
(E5080A) 2.0 \- 500 MHz 3.0 \- 1100 MHz 4.0 \- 1600 MHz 5.0 \- 2000 MHz 6.0 \-
2000 MHz dual core 7.0 \- 2200 MHz dual core 8.0 \- 1600 MHz quad core  
---  
Parameters |  None  
Example |  SYST:CONF:REV:CPU?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SYSTem:CONFigure:REVision:DSP?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Returns
the DSP Revision number that is visible in the Help, About Network Analyzer
dialog box. [Learn more.](../../S0_Start/HelpAbout.md)  
---  
Parameters |  None  
Example |  SYST:CONF:REV:DSP?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SYSTem:CONFigure:REVision:DSPFpga?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Returns
the DSP FPGA Revision number that is visible in the Help, About Network
Analyzer dialog box. [Learn more.](../../S0_Start/HelpAbout.md)  
---  
Parameters |  None  
Example |  SYST:CONF:REV:DSPF?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SYSTem:CONFigure:REVision:PNA:SYNThesizer[0,1,2,3]:VERSion?

Applicable Models: N522xB, N524xB (Read-only) Returns the Synthesizer Revision
number.  Synthesizer Versions 5.0 \- Direct Digital Synthesizer to generate
frequencies from 10 to 250 MHz, one synthesizer per assembly. 6.0 \- Improved
filtering and reliability improvements, one synthesizer per assembly. 7.0 \-
Direct Digital Synthesizer to generate frequencies from 10 MHz to 6 GHz, two
or four synthesizers per assembly. Index Definitions for Synthesizer Versions
0 \- LO synthesizer 1 \- Src1 synthesizer 2 \- Src 2 synthesizer 3 \- Src 3
synthesizer  
---  
Parameters |  None  
Example |  SYST:CONF:REV:PNA:SYNT:VERS? "6.0"  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SYSTem:CORRection:WIZard[:IMMediate] <char>

Applicable Models: All (Write-only) Launches either the Calibration Wizard or
the Version 2 Calibration Kit File Manager dialog box.  Remote operation
returns immediately after the dialog is launched. This is done to avoid
timeout issues with I/O protocols such as VISA. Although it is possible to
send commands to the VNA while the dialog is open, this is not encouraged.
Application programs should wait until the dialog is closed before resuming
remote operations.  
---  
Parameters |   
<char> |  Choose from: MAIN \- Launches the Calibration Wizard which matches the current channel, such as standard S-params, NoiseFigure, GCA, and so forth. CKIT \- Launches the Version 2 Calibration Kit File Manager dialog box. RESP \- Launches the Response Cal Type Selection. BASic \- Launches the Basic Cal dialog. CALL \- Launches the Calibrate All Selected Channels dialog. These display on the VNA screen.  
Examples |  SYST:CORR:WIZ MAIN  
system:correction:wizard:immediate ckit  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  MAIN  
  
* * *

## SYSTem:DATA:MEMory:ADD <string>

Applicable Models: All (Write only) Add a request to copy the contents of the
specified measurement into shared memory. Call this command once for each
measurement definition. Once the shared memory is setup, there is no need to
send more SCPI commands. The shared memory is filled automatically on every
sweep.  Refer also to [Shared Memory Example in
C#](../GPIB_Example_Programs/Shared_Memory_Example_in_C_.htm).  
---  
Parameters |   
<string> |  The following elements separated with colons (:). <Ch>:<MeasNum>:<dataFormat>:<numPoints>:[<repeatCount>] where:

  * <Ch> \- Channel number of the measurement to share memory. Use [SYST:ACTive:CHAN](System.md#ActiveChannel) to return the active channel number. Use [SYST:CHAN:CAT?](System.md#ChanCat) to return the channel numbers in use.
  * <MeasNum> \- Measurement (Tr) number to share memory. Use [CALC<ch>:PAR:MNUM](Calculate/Parameter.md#MnumSel)? just after the trace is created to read the measurement number. See also: [Referring to Traces, Measurements, Channels, and Windows Using SCPI](../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.md).
  * <dataFormat> \- Choose from:
  * SDATA \- Complex measurement data.
  *     * Reads data from Apply Error Terms (access point 1). Returns TWO numbers per data point. Corrected data is returned when correction is ON. Uncorrected data is returned when correction is OFF.
  * FDATA \- Formatted measurement data to or from [Data Access Map](../Data_Access_Map.md) location Display (access point 2).
    * Corrected data is returned when correction is ON.
    * Uncorrected data is returned when correction is OFF.
    * Returns one number per data point for all other formats.
    * Format of the read data is same as the displayed format.
  * CAL \- Access the entire set of calibrated SParameter measurements.
    * Only functional if an SParameter calibration is applied to the channel.
    * Always returns all the SParameters.
    * SParameters are in the following order for a 3 port cal:
      * {S11, S21, S31, S12, S22, S32, S13, S23, S33}

  * <numPoints> \- Number of data points in the measurement trace.
  * [<repeatCount>] - This argument is optional. When specified, the buffer will include multiple sweeps of information into the buffer. Each sweep is stored consecutively into the shared data buffer.

  
Examples |  SYSTem:DATA:MEMory:ADD "2:3:SDATA:201" 'copies the data for channel #2, measurement #3, complex data, 201 points into the shared memory buffer.  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:DATA:MEMory:CATalog?

Applicable Models: All (Read only) Returns a list of all the allocated shared
memory buffers  Refer also to [Shared Memory Example in
C#](../GPIB_Example_Programs/Shared_Memory_Example_in_C_.htm).  
---  
Parameters |  None  
Examples |  SYST:DATA:MEM:CAT?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:DATA:MEMory:CLOSe <memName>

Applicable Models: All (Write-only) Closes the specified memory mapped buffer.
Refer also to [Shared Memory Example in
C#](../GPIB_Example_Programs/Shared_Memory_Example_in_C_.htm).  
---  
Parameters |   
<memName> |  String. Name of the memory mapped buffer.  
Examples |  SYST:DATA:MEM:CLOS "VNA_MemoryMap"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:DATA:MEMory:CLOSe:FILE <fileName>

Applicable Models: All (Write-only) Closes the specified memory file.  Refer
also to [Shared Memory Example in
C#](../GPIB_Example_Programs/Shared_Memory_Example_in_C_.htm).  
---  
Parameters |   
<fileName> |  Memory file name.  
Examples |  SYST:DATA:MEM:CLOS "c:\temp\myfile.dat"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:DATA:MEMory:COMMit <memName>

Applicable Models: All (Write only) Allocates the memory mapped buffer.  Refer
also to [Shared Memory Example in
C#](../GPIB_Example_Programs/Shared_Memory_Example_in_C_.htm).  
---  
Parameters |   
<memName> |  String. Name of the memory mapped buffer. This must be a unique name, and cannot conflict with other shared memory buffer names. Use this command in your program when connecting to the shared memory. See SYSTem:DATA:MEMory:NAME?  
Examples |  SYST:DATA:MEM:COMM "VNA_MemoryMap"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:DATA:MEMory:COMMit:FILE <fileName>

Applicable Models: All (Write only) This command creates the memory buffer and
saves the buffer to a file. This command is an alternative to using the
SYST:DATA:MEM:COMMIT command.  Refer also to [Shared Memory Example in
C#](../GPIB_Example_Programs/Shared_Memory_Example_in_C_.htm).  
---  
Parameters |   
<fileName> |  String. Name of the memory mapped buffer file. This must be a unique name, and cannot conflict with other shared memory buffer file names. Use this command in your program when connecting to the shared memory. See SYSTem:DATA:MEMory:NAME?  
Examples |  SYST:DATA:MEM:COMM:FILE "c:\temp\myfile.dat"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:DATA:MEMory:DELete <memName> \- Obsolete

Applicable Models: All (Write only) Deletes the specified memory mapped
buffer.  
---  
Parameters |   
<memName> |  String. Name of the memory mapped buffer. This is the unique name that is used in the COMMit command.  
Examples |  SYST:DATA:MEM:DEL "VNA_MemoryMap"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:DATA:MEMory:INITialize

Applicable Models: All (Write only) Initializes the shared memory setup
buffers.  Refer also to [Shared Memory Example in
C#](../GPIB_Example_Programs/Shared_Memory_Example_in_C_.htm).  
---  
Parameters |  None  
Examples |  SYST:DATA:MEM:INIT  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:DATA:MEMory:NAME?

Applicable Models: All (Read only) Returns a unique, auto-generated name that
can be used in the COMMIt command. By using this generated name, a client can
be sure not to conflict with any other used shared memory regions.  Refer also
to [Shared Memory Example in
C#](../GPIB_Example_Programs/Shared_Memory_Example_in_C_.htm).  
---  
Parameters |  None  
Examples |  SYST:DATA:MEM:NAME?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:DATA:MEMory:OFFSet?

Applicable Models: All (Read only) The shared memory is a contiguous block of
memory. Each measurement takes up a subset of this contiguous block. This
command returns the offset (in bytes) into the shared memory for the most
recently added parameter. The offset is a number that specifies the starting
index (in bytes) of the data.  This query can be sent after sending
SYST:DATA:MEM:ADD. Refer also to [Shared Memory Example in
C#](../GPIB_Example_Programs/Shared_Memory_Example_in_C_.htm).  
---  
Parameters |  None  
Examples |  SYST:DATA:MEM:OFFS?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:DATA:MEMory:REPeat:RESet

Applicable Models: All (Write only) This command resets the current repeat
index to 0.  Refer also to [Shared Memory Example in
C#](../GPIB_Example_Programs/Shared_Memory_Example_in_C_.htm).  
---  
Parameters |  None  
Examples |  SYST:DATA:MEM:REP:RES  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:DATA:MEMory:RESet

Applicable Models: All (Write only) Deletes all allocated shared memory
buffers.  Refer also to [Shared Memory Example in
C#](../GPIB_Example_Programs/Shared_Memory_Example_in_C_.htm).  
---  
Parameters |  None  
Examples |  SYST:DATA:MEM:RES  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:DATA:MEMory:SIZE?

Applicable Models: All (Read only) Returns the size of the memory mapped
region. Send this immediately after SYST:DATA:MEM:COMMit. The result is the
total size (in bytes) of all the measurements in the shared memory region.
Refer also to [Shared Memory Example in
C#](../GPIB_Example_Programs/Shared_Memory_Example_in_C_.htm).  
---  
Parameters |  None  
Examples |  SYST:DATA:MEM:SIZE?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:DATE?

Applicable Models: All (Read-only) Returns the system date.  
---  
Parameters |  None  
Example |  SYST:DATE?  
Return Type |  Comma separated numbers representing year, month, day.  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SYSTem:DISK:REVision?

Applicable Models: N522xB, N523xB, N524xB, E5080A/B, E5081A (Read-only)
Returns the disk drive version. The format is S.XX.YY.ZZ.  
---  
Parameters |  None  
Example |  SYST:DISK:REV?  
Return Type |  Comma separated numbers representing year, month, day.  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SYSTem:ERRor?

Applicable Models: All (Read-only) Returns the next error in the error queue.
Each time the analyzer detects an error, it places a message in the error
queue. When the SYSTEM:ERROR? query is sent, one message is moved from the
error queue to the output queue so it can be read by the controller. Error
messages are delivered to the output queue in the order they were received.
The error queue is cleared when any of the following conditions occur:

  * When the analyzer is switched ON.
  * When the *CLS command is sent to the analyzer.
  * When all of the errors are read.

If the error queue overflows, the last error is replaced with a "Queue
Overflow" error. The oldest errors remain in the queue and the most recent
error is discarded. [See list of all SCPI
Errors.](../../Support/SCPI_Errors.htm)  
---  
Examples |  SYST:ERR?  
system:error?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:ERRor:COUNt?

Applicable Models: All (Read-only) Returns the number of errors in the error
queue. Use SYST:ERR? to read an error.  [See list of all SCPI
Errors.](../../Support/SCPI_Errors.htm)  
---  
Examples |  SYST:ERR:COUN?  
system:error:count?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:ERRor:REPort:SUNLeveled <bool>

Applicable Models: All (Read-Write) Specifies whether or not to report [Source
Unleveled](../../S1_Settings/Power_Level.htm#Unleveled) errors to the SCPI
system error buffer.  This setting will NOT revert to the default (OFF)
setting on Instrument Preset. Use the
[SYSTem:PREFerences:DEFault](System_Preferences.md#PrefDefault) command to
reset the preferences to their default settings.  
---  
Parameters |   
<bool> |  ON (or 1) Report Source Unleveled Errors. Read errors from the system error buffer using [SYST:ERR?](System.md#error) OFF (or 0) Do NOT report Source Unleveled Errors.  
Examples |  SYST:ERR:REP:SUNL 1 system:error:report:sunleveled ON  
Query Syntax |  SYSTem:ERRor:REPort:UNLeveled?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SYSTem:FCORrection:CHANnel<cnum>:COUPler[:STATe] <char>

Applicable Models: M93xxA/B, P937xA, E5080B, E5081A, M980xA, P50xxA/B, M9485A
(Read-Write) (M937xA/P937xA) Sets and returns the coupler state. This command
is not effective for SMC class. (E5080B, M980xA, P50xxA, M9485A) Turn off the
system calibration.  When you perform a 8/12-term error model calibration
(measuring raw measurement data, calculating error term using external
software and then performing correction with calculated error terms and
measured raw data), the following setup is required for calibration using
external PC: 1\. 8-term error model:

  * E5080A: 
    * SYST:FCOR:CHAN:COUP:STAT OFF
    * (SYST:FCOR:CHAN:RFR:STAT OFF is not required.)
  * M9485A: 
    * SYST:FCOR:CHAN:COUP:STAT OFF
    * SYST:FCOR:CHAN:RFR:STAT OFF
  * M980xA, E5080B, P50xxA/B: 
    * SYST:FCOR:CHAN:COUP:STAT OFF
    * SYST:FCOR:CHAN:RFR:STAT OFF or Fixed Gain setup during the calibration (The receiver gain settings are all FIXED [high or low] and have same state for each source port).

2\. 12-term error model:

  * M9485A, E5080A: No setting is required.
  * M980xA, E5080B, P50xxA/B: 
    * SYST:FCOR:CHAN:RFR:STAT OFF or Fixed Gain setup during the calibration (The receiver gain settings are all FIXED [high or low] and have same state for each source port).

  
---  
Parameters |   
<char> |  Choose from: OFF AUTO   
Examples |  SYST:FCOR:CHAN:COUP AUTO  
system:fcorrection:channel1:coupler OFF  
Query Syntax |  SYSTem:FCORrection:CHANnel<cnum>:COUPler[:STATe]?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  AUTO (for ENA/PXI) OFF (for PNA)  
  
* * *

## SYSTem:FCORrection:CHANnel<cnum>:RFRange[:STATe] <bool>

Applicable Models: M980xA, E5080A/B, E5081A, P50xxA/B, M9485A (M9376A only)
(Read-Write) Enable and disable the RF gain ranging state .When you perform a
8/12-term error model calibration (measuring raw measurement data, calculating
error term using external software  and then performing correction with
calculated error terms and measured raw data), this command allows you to
control the RF ranging state. See SYST:FCOR:CHAN:COUP:STAT.  
---  
Parameters |   
<bool> |  Choose from: OFF - 0 (Fix the RF gain range) ON - 1  
Examples |  SYST:FCOR:CHAN:COUP:RFR 0  
system:fcorrection:channel1:rfrange OFF  
Query Syntax |  SYSTem:FCORrection:CHANnel<cnum>:RFRange[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1  
  
* * *

## SYSTem:FPReset

Applicable Models: All (Write-only) Performs a standard
[Preset](System.md#pre), then deletes the default trace, measurement, and
window. The VNA screen becomes blank.  
---  
Examples |  SYST:FPR  
system:fpreset  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SYSTem:ISPContol[:STATe] <bool>

Applicable Models: E5080A/B, E5081A, M9485A, M980xA, P50xxA/B, P93xxB, M983xA
(Read-Write) Sets and reads the status of the Initial Source Port Control
feature (to switch the stimulus output in the trigger hold state to a test
port).  
---  
Parameters |   
<bool> |  ON (or 1) Source is outputted only when measurement is done .Source is not outputted during hold state. OFF (or 0) Source is always outputted.  
Examples |  SYST:ISPC 1 system:ispcontrol OFF  
Query Syntax |  SYSTem:ISPControl[:STATe]?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON (E5080A), OFF (P50xxA, M980xA, M9485A, E5080B)  
  
* * *

## SYSTem:LOCal

Applicable Models: All (Write-only) Sets the local/remote state to local.  
---  
Examples |  SYST:LOC  
system:local  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SYSTem:MACRo:COPY:CHANnel<cnum>[:TO] <num>

Applicable Models: All (Write-only) Copies ALL settings from <cnum> channel to
<num> channel. Learn more about [copy
channels.](../../S1_Settings/CopyChannels.htm) Use
[SENS:PATH:CONF:COPY](Sense/Path.md#copy) to copy ONLY mechanical switch and
attenuator settings.  
---  
Parameters |   
<cnum> |  Channel number to copy settings from. If unspecified, value is set to 1.  
<num> |  Channel number to copy settings to.  
Examples |  SYST:MACR:COPY:CHAN1 2 system:macro:copy:channel2:to 3  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:MACRo:COPY:CHANnel<fromChannel>:STATe
<toChannel>,<toWindow>,[<copyScope>]

Applicable Models: All

(Write-only) Copies settings only, or settings and measurements, traces,
markers, and limit lines from an existing channel, <fromChannel>, to a new
channel, <toChannel>. Traces can be copied into the Active Window, a user
specified window, or a new (next available) window. .  
---  
Parameters |   
<fromChannel> |  Channel number to copy settings from. If unspecified, value is 1.  
<toChannel> |  0 for next available channel, or N for channel number to copy settings to.  
<toWindow> |  -1 will create a new window, 0 will use the active window, and N will use the specified window N. <toWindow> is ignored when <copyScope> is "stimulus"  
<copyScope> |  must be "stimulus" which copies only settings, or "state" which copies settings, measurements, traces, markers, and limit lines.  
Examples |  SYST:MACR:COPY:CHAN1:STAT 2,0,"stimulus" Copies only settings from channel #1 to channel #2. This is equivalent to SYST:MACR:COPY:CHAN1 2 SYST:MACR:COPY:CHAN1:STAT 2,-1,"state" Copies settings, measurements, traces, etc. from channel #1 to channel #2. Traces are placed into a new window (next available window), and additional windows will be created as necessary so that all traces are copied. SYST:MACR:COPY:CHAN1:STAT 0,-1 Copies settings, measurements, etc. from channel #1 to the next available channel and places traces into the next avaialble new window.  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:MACRo:COPY:CHANnel<fromChan>:SOURce <fromPort>,<toChan>,<toPort>

Applicable Models: All (Write-only) Copies and applies an existing Source
Power Calibration to another channel. Learn more about [source power
calibration](../../S3_Cals/PwrCalibration.htm).  
---  
Parameters |   
<fromChan> |  Channel number of the existing source power correction.  
<fromPort> |  Port number of the existing source power correction.  
<toChan> |  Channel number to which the source power correction will be copied.  
<toPort> |  Port number to which the source power correction will be applied.  
Examples |  SYST:MACR:COPY:CHAN1:SOUR 1,2,1 system:macro:copy:channel2:source 2,1,2  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:MCLass:CATalog?

Applicable Models: All (Read-only) Returns measurement class names available
on the VNA. [Learn more about Measurement
Classes](../../S1_Settings/Measurement_Classes.htm).  
---  
Parameters |  None  
Examples |  SYST:MCLass:CAT? "Standard,Differential I/Q,Gain Compression,Gain Compression Converters,IM Spectrum,IM Spectrum Converters,Modulation Distortion,Modulation Distortion Converters,Noise Figure Cold Source,Noise Figure Converters,Phase Noise,Scalar Mixer/Converter,Spectrum Analyzer,Swept IMD,Swept IMD Converters,Vector Mixer/Converter,TDR"  
Return Type |  String of comma-separated measurement class names. [See the complete list of measurement class names](Calculate/Custom.md#CustDef).  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:MCLass:PARameter:CATalog? <name>

Applicable Models: All (Read-only) Returns ALL parameters that are supported
by the specified measurement class.  
---  
Parameters |   
<name> |  String. Measurement Class name. [See the complete list of measurement class names](Calculate/Custom.md#CustDef).  
Examples |  'Returns all parameters for Gain Compression. SYST:MCL:PAR:CAT? "Gain Compression" Return: "S11,S12,S13,S14,S21,S22,S23,S24,S31,S32,S33,S34,S41,S42,S43,S44,A,B,C,D,R,R1,R2,R3,R4"  
Return Type |  String of comma-separated parameters  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:MCLass:VALid:CATalog?

Applicable Models: All (Read-only) Returns valid measurement class names
available on the VNA. [Learn more about Measurement
Classes](../../S1_Settings/Measurement_Classes.htm).  
---  
Parameters |  None  
Examples |  SYST:MCLass:VALid:CAT? "Standard,Differential I/Q,Gain Compression,Gain Compression Converters,IM Spectrum,IM Spectrum Converters,Modulation Distortion,Modulation Distortion Converters,Noise Figure Cold Source,Noise Figure Converters,Phase Noise,Scalar Mixer/Converter,Spectrum Analyzer,Swept IMD,Swept IMD Converters,Vector Mixer/Converter,TDR"  
Return Type |  String of comma-separated measurement class names. [See the complete list of measurement class names](Calculate/Custom.md#CustDef).  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:MEASure:CATalog? [chan]

Applicable Models: All (Read-only) Returns ALL measurement numbers, or
measurement numbers from a specified channel.  
---  
Parameters |   
[chan] |  Optional. Channel number to catalog. If not specified, all measurement numbers are returned.  
Examples |  'Returns all measurement numbers SYST:MEAS:CAT? 'Returns the measurement numbers on channel 2 system:measurement:catalog? 2  
Return Type |  String of comma-separated numbers For example: "1,2"  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:MEASure<n>:CHANnel?

Applicable Models: All (Read-only) Returns the channel number of the specified
measurement.  
---  
Parameters |   
<n> |  Measurement number for which to return the channel number. If unspecified, value is set to 1.  
Examples |  'Returns the channel number of measurement 2 SYST:MEAS2:CHAN?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:MEASure<n>:NAME?

Applicable Models: All (Read-only) Returns the name of the specified
measurement.  
---  
Parameters |   
<n> |  Measurement number for which to return the measurement name. If unspecified, value is set to 1.  
Examples |  'Returns the name of measurement 2 SYST:MEAS2:NAME?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:MEASure:NUMBer? <measName>

Applicable Models: All (Read-only) Returns the measurement number associated
with the measurement name.  
---  
Parameters |   
<measName> |  Measurement name.  
Examples |  'Returns the measurement number of My_Measurement SYST:MEAS:NUMB? "My_Measurement"  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:MEASure<n>:TRACe?

Applicable Models: All (Read-only) Returns the trace number of the specified
measurement number. Trace numbers restart for each window while measurement
numbers are always unique.  
---  
Parameters |   
<n> |  Measurement number for which to return the trace number. If unspecified, value is set to 1.  
Examples |  'Returns the trace number of measurement 1 SYST:MEAS1:TRAC?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:MEASure<n>:WINDow?

Applicable Models: All (Read-only) Returns the window number of the specified
measurement number.  
---  
Parameters |   
<n> |  Measurement number for which to return the window number. If unspecified, value is set to 1.  
Examples |  'Returns the window number of measurement 2 SYST:MEAS2:WIND?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:PERSona:MANufacturer <string>

Applicable Models: All (Read-Write) This command allows you to modify the
manufacturer name returned by the instruments *IDN query response. This is
intended to be used for Agilent backward identity compatibility. For example,
"Agilent Technologies or Agilent. However, it could be used for other
purposes such as emulation of another vendors instrument.  The change to the
manufacturer string will not take effect until after an instrument reboot. The
manufacturer string does not allow commas in the name. If a comma is detected
an error is returned. Also, if an invalid manufacturer is detected, an error
is returned. The manufacturer string used for Keysight is Keysight
Technologies.  
---  
Parameters |   
<string> |  Name of the manufacturer.  
Examples |  SYST:PERS:MAN "Keysight Technologies"  
Query Syntax |  SYSTem:PERSona:MANufacturer?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:PERSona:MANufacturer:DEFault

Applicable Models: All (Read-Write) Sets and returns the instrument's original
manufacturer identification state following the next instrument reboot.  
---  
Parameters |  None  
Examples |  SYST:PERS:MAN:DEF  
Query Syntax |  SYSTem:PERSona:MANufacturer:DEFault?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:PERSona:MODel <string>

Applicable Models: All (Read-Write) This command allows you to modify the
product model returned by the instruments *IDN query response. This is
intended to be used for model compatibility. If not specified, the default
model of the instrument is used.  The change to the model string will not take
effect until after an instrument reboot. The model string does not allow
commas in the name. If a comma is detected an error is returned. Also, if an
invalid model is detected, an error is returned.  
---  
Parameters |   
<string> |  Product model name.  
Examples |  SYST:PERS:MOD "33220A"  
Query Syntax |  SYSTem:PERSona:MANufacturer?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:PERSona:MODel:DEFault

Applicable Models: All (Read-Write) Sets and returns the instrument's original
product model name following the next instrument reboot.  
---  
Parameters |  None  
Examples |  SYST:PERS:MOD:DEF  
Query Syntax |  SYSTem:PERSona:MODel:DEFault?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:POFF

Applicable Models: All (Write-only) Shuts down the system.  
---  
Parameters |   
<n> |  Shutdown or restart. Choose from: 1 - Restart. 0 - Shutdown .  
Examples |  'Shuts down the system SYST:POFF  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0 (Shutdown)  
  
* * *

## SYSTem:POWer<pnum>:LIMit <value>

Applicable Models: All (Read-Write) (M937xA, P937xA: Read-Only) Sets and
returns the power limit for the specified port. [Learn more about Power
Limit.](../../System/Power_Limit_and_Power_Offset.htm)  
---  
Parameters |   
<pnum> |  Port number. Choose any VNA port.  
<value> |  Power limit in dBm  
Examples |  SYST:POW1:LIM 5 system:power2:limit 0  
Query Syntax |  SYSTem:POWer<pnum>:LIMit?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  100 dBm  
  
* * *

## SYSTem:POWer<pnum>:LIMit:CALibration <value>

Applicable Models: All (Read-Write) Sets and returns the calibration power
limit for the specified port. [Learn more about Power
Limit.](../../System/Power_Limit_and_Power_Offset.htm) The values set by this
command are not applied automatically during the calibration. Users need to
call SYSTem:POWer:LIMit:CALibration:STATe to apply the calibration power limit
during calibration.  
---  
Parameters |   
<pnum> |  Port number. Choose any VNA port.  
<value> |  Cal power limit in dBm  
Examples |  SYST:POW1:LIM:CAL 5 system:power2:limit:calibration 0  
Query Syntax |  SYSTem:POWer<pnum>:LIMit:CALibration?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  100 dBm (Factory default. Preset does nothing)  
**Save/Recall** |  No (but stored in ProgramData)  
  
* * *

## SYSTem:POWer:LIMit:CALibration:STATe <bool>

Applicable Models: All (Read-Write) Sets and returns the calibrating state for
the calibration power limit feature works properly from remote UI. [Learn more
about Power Limit.](../../System/Power_Limit_and_Power_Offset.htm) Calibration
power limit is not automatically applied when calibration is started from
SCPI. Users need to call this command properly to apply the calibration power
limit during calibration. To enable the power limit during calibration
feature, users need to call **SYST:POW:LIM:CAL:STAT ON** before starting
calibration and need to call **SYST:POW:LIM:CAL:STAT OFF** after the
calibration finished.  
---  
Parameters |   
<bool> |  Choose from: ON or 1 - Calibrating OFF or 0 - Is not calibrating  
Examples |  SYST:POW1:LIM:CAL:STAT 1 system:power:limit:calibration:state 0  
Query Syntax |  SYSTem:POWer:LIMit:CALibration:STATe?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0 (OFF)  
**Save/Recall** |  No  
  
* * *

## SYSTem:POWer:LIMit:LOCK <bool>

Applicable Models: All (Read-Write) (M937xA, P937xA: Read-Only) Enables or
disables the ability to change the power limit values through the user
interface. [Learn more about Power
Limit.](../../System/Power_Limit_and_Power_Offset.htm)  
---  
Parameters |   
<bool> |  Power limit lock. Choose from: ON or 1 - Disables the ability to change the power limit values from the user interface. OFF or 0 - Enables the ability to change the power limit values from the user interface.  
Examples |  SYST:POW:LIM:LOCK 1 system:power:limit:lock OFF  
Query Syntax |  SYSTem:POWer:LIMit:LOCK?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SYSTem:POWer<pnum>:LIMit:STATe <bool>

Applicable Models: All (Read-Write) (M937xA, P937xA: Read-Only) Enables or
disables the power limit for the specified port. [Learn more about Power
Limit.](../../System/Power_Limit_and_Power_Offset.htm)  
---  
Parameters |   
<pnum> |  Port number. Choose any VNA port.  
<value> |  Power limit state. Choose from: ON or 1 Enables the power limit for the port<pnum>. OFF or 0 Disables the power limit for the port<pnum>.  
Examples |  SYST:POW1:LIM:STAT ON system:power2:limit:state 0  
Query Syntax |  SYSTem:POWer<pnum>:LIMit:STATe?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SYSTem:PRESet

Applicable Models: All (Write-only) Deletes all traces, measurements, and
windows. In addition, resets the analyzer to factory defined default settings
and creates a S11 measurement named "CH1_S11_1". For a list of default
settings, see [Preset](../../S1_Settings/Preset_the_Analyzer.md).  Regardless
of the state of the User Preset Enable checkbox, the SYST:PRESet command will
always preset the VNA to the factory preset settings, and
[SYST:UPReset](System.md#UPreset) will always perform a User Preset. If the
VNA display is disabled with [DISP:ENAB OFF](Display.md#enable) then
SYST:PRES will NOT enable the display. This command performs the same function
as [*RST](Common_Commands.md#rst) with one exception: Syst:Preset does NOT
reset [Calc:FORMAT](Calculate/Format_Calc.md#format) to ASCII as does *RST.  
---  
Examples |  SYST:PRES  
system:preset  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SYSTem:SECurity[:LEVel] <char>

Applicable Models: All (Read-Write) Sets and returns the display of frequency
information on the VNA screen and printouts.  [Learn more about security
level.](../../System/Frequency_Blanking.htm)  
---  
Parameters |   
<char> |  Choose from: NONE - ALL frequency information is displayed. LOW - NO frequency information is displayed. Frequency information can be redisplayed using the Security Setting dialog box or this command. HIGH - LOW setting plus [GPIB console](../Learning_about_GPIB/How_to_Configure_for_GPIB_SCPI_and_SICL.md#console) is disabled. Frequency information can be redisplayed ONLY by performing a Preset, recalling an instrument state with None or Low security settings, or using this command. EXTRa - HIGH setting plus:

  * [ASCII data saving](../../S5_Output/SaveRecall.md#ASCII) is disabled. Same method to redisplay frequency information as HIGH setting.
  * [Mixer setup files](../../Applications/MixerConverter_Setup.md#AboutMxr) (*.mxr) can NOT be saved.

  
Examples |  SYST:SEC LOW  
system:security:level high  
Query Syntax |  SYSTem:SECurity[:LEVel]?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  None  
  
* * *

## SYSTem:SET <block>

Applicable Models: All (Read-Write) Sends a definite-length binary block
Instrument state and sets the VNA with those settings. This command does the
same as saving a *.sta file to the VNA ([MMEM:STOR STATE](Memory.md#save))
and then [MMEM:TRAN](Memory.md#Transfer) to transfer the file to the
computer.  
---  
Parameters |   
<block> |  The Instrument state file as definite-length arbitrary binary block.   
Examples |  SYST:SET <block>  
Query Syntax |  SYSTem:SET? (This saves the instrument state file to the remote computer.)  
Return Type |  Definite-length arbitrary binary block.  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:SHEets:CATalog?

Applicable Models: All (Read-only) Returns comma separated list of visible
sheets.  
---  
Parameters |   
Examples |  SYST:SHE:CAT? 'Returns: "1,2,3"  
Return Type |  String of comma-separated numbers  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1  
  
* * *

## SYSTem:SHORtcut<n>:ARGuments<string>

Applicable Models: All (Read-Write) Reads and writes the arguments for the
specified macro. On the [Edit Macro Dialog](../Using_Macros.md#Edit), this is
called the "Macro run string parameters".  
---  
Parameters |   
<n> |  Numeric. Number of the macro that is stored in the VNA. To find the number of a macro, either open the [Macro Setup dialog](../Using_Macros.md#Setup) and count the line number of the desired macro, or query the titles of all of the macros for the desired macro title.  
<string> |  Arguments for the specified macro.  
Examples |  SYST:SHOR1:ARG "http://www.keysight.com/pna/help/PNAWebHelp/help.htm"  
Query Syntax |  SYSTem:SHORtcut<n>:ARGuments?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:SHORtcut<n>:DELete

Applicable Models: All (Write-only) Removes the specified macro from the list
of macros in the VNA. Does not delete the macro executable file.  
---  
Parameters |   
<n> |  Numeric. Number of the macro that is stored in the VNA. To find the number of a macro, either open the [Macro Setup dialog](../Using_Macros.md#Setup) and count the line number of the desired macro, or query the titles of all of the macros for the desired macro title.  
Examples |  SYST:SHOR1:DEL  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:SHORtcut<n>:EXECute

Applicable Models: All (Write-only) Executes (runs) the specified Macro
(shortcut) that is stored in the VNA.  Note: If [Enable Remote Drive
Access](../Learning_about_GPIB/How_to_Configure_for_GPIB_SCPI_and_SICL.htm#Security)
is unchecked in the Remote Interface dialog, this command will return an
error.  
---  
Parameters |   
<n> |  Numeric. Number of the macro that is stored in the VNA. To find the number of a macro, either open the [Macro Setup dialog](../Using_Macros.md#Setup) and count the line number of the desired macro, or query the titles of all of the macros for the desired macro title.  
Examples |  SYST:SHOR1:EXEC  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:SHORtcut<n>:PATH <string>

Applicable Models: All (Read-Write) Defines a Macro (shortcut) by linking a
path and file name to the Macro number. To be executed, the executable file
must be put in the VNA at the location indicated by this command.  
---  
Parameters |   
<n> |  Numeric. Number of the macro to be stored in the analyzer. If the index number already exists, the existing macro is replaced with the new macro.  
<string> |  Full path, file name, and extension, of the existing macro "executable" file. To find the number of a macro, either open the [Macro Setup dialog](../Using_Macros.md#Setup) and count the line number of the desired macro, or query the titles of all of the macros for the desired macro title.  
Examples |  SYST:SHOR1:PATH "C:\Program Files(x86)\Keysight\Network Analyzer\Documents\unguideMultiple.vbs"  
Query Syntax |  SYSTem:SHORtcut<n>:PATH?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:SHORtcut<n>:TITLe<string>

Applicable Models: All (Read-Write) Reads and writes the name of the specified
macro.  
---  
Parameters |   
<n> |  Numeric. Number of the macro that is stored in the VNA. To find the number of a macro, either open the [Macro Setup dialog](../Using_Macros.md#Setup) and count the line number of the desired macro, or query the titles of all of the macros for the desired macro title.  
<string> |  The name to be assigned to the macro.  
Examples |  SYST:SHOR1:TITL "Guided 4-Port Cal"  
Query Syntax |  SYSTem:SHORtcut<n>:TITLe?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYStem:SIMulator:DUT:FILE <string>

Applicable Models: Simulator only

(Read-Write) Set/get trace sNp file for dummy DUT. Preset & Save/Recall does
not work for this command  
---  
Parameters |  <string> sNp file to be set to dummy DUT  
Examples |  SYST:SIM:FILE?  
system:simulator:dut:file "C:\temp\sampledut.s2p"  
Return Type |  string  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYStem:SIMulator:DUT:NOISe:STATe <bool>

Applicable Models: Simulator only

(Read-Write) add some noise on simulator measurement. Preset & Save/Recall
does not work for this command  
---  
Parameters |  <bool> Noise state.  
Examples |  SYST:SIM:DUT:NOIS:STAT?  
system:simulator:dut:noise:state?  
Return Type |  bool  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## SYSTem:TIME?

Applicable Models: All (Read-only) Returns the system time.  
---  
Parameters |  None  
Example |  SYST:TIME?  
Return Type |  Comma separated numbers representing hours, minutes, seconds.  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SYSTem:TOUChscreen[:STATe] <bool>

Applicable Models: N522xB, N523xB, N524xB, E5080A/B, E5081A (Read-Write)
Enables and disables the touchscreen.  This setting remains until changed
again from the front-panel or remotely, or until the hard drive is changed or
reformatted.  
---  
Parameters |   
<bool> |  Choose from: ON (1) Enables the touchscreen. OFF (0) Disables the touchscreen.  
Examples |  SYST:TOUC 1  
system:touchscreen:state OFF  
Query Syntax |  SYSTem:TOUChscreen[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON when shipped from factory.  
  
* * *

## SYSTem:UPReset

Applicable Models: All (Write-only) Performs a User Preset. There must be an
active User Preset state file (see [Load](System.md#UPresetLoad) and
[Save](System.md#UpresetSave)) or an error will be returned. [Learn more
about User
Preset.](../../S1_Settings/Preset_the_Analyzer.htm#PresetUserDefined)
Regardless of the state of the User Preset Enable checkbox, the SYST:PRESet
command will always preset the VNA to the factory preset settings, and
[SYST:UPReset](System.md#UPreset) will always perform a User Preset.  
---  
Examples |  SYST:UPReset system:upreset  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:UPReset:FPANel[:STATe] <bool>

Applicable Models: All (Read-Write) 'Checks' and 'clears' the enable box on
the [User Preset dialog
box](../../S1_Settings/Preset_the_Analyzer.htm#UserDiag). This only affects
subsequent Presets from the front panel user interface.  Regardless of the
state of the User Preset Enable checkbox, the [SYST:PRESet](System.md#pre)
command will always preset the VNA to the factory preset settings, and
[SYST:UPReset](System.md#UPreset) will always perform a User Preset.  
---  
Parameters |   
<bool> |  Front Panel User Preset State. Choose from: 0 User Preset OFF 1 User Preset ON  
Examples |  SYST:UPR:FPAN 1 system:upreset:fpanel:state 0  
Query Syntax |  SYSTem:UPREset:FPANel[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0  
  
* * *

## SYSTem:UPReset:LOAD[:FILE] <file>

Applicable Models: Alll (Write-only) Loads an existing instrument state file
(.sta or .cst) to be used for User Preset. Subsequent execution of
[SYSTem:UPReset](System.md#UPreset) will cause the VNA to assume this
instrument state.  Regardless of the state of the User Preset Enable checkbox,
the [SYST:PRESet](System.md#pre) command will always preset the VNA to the
factory preset settings, and [SYST:UPReset](System.md#UPreset) will always
perform a User Preset. [Learn more about User
Preset.](../../S1_Settings/Preset_the_Analyzer.htm#PresetUserDefined)  
---  
Parameters |   
<file> |  String - Name of the file to be loaded. Change the default folder name using [MMEMory:CDIRectory](Memory.md#chgdir).  
Examples |  SYST:UPR:LOAD '1MHzto20GHzUserPreset.cst' system:upreset:load:file 'C:\Documents and Settings\Administrator\My Documents\NewUserPreset.cst'  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:UPReset:SAVE[:STATe]

Applicable Models: All (Write-only) Saves the current instrument settings as
UserPreset.sta. Subsequent execution of [SYSTem:UPReset](System.md#UPreset)
will cause the VNA to assume this instrument state.  Regardless of the state
of the User Preset Enable checkbox, the [SYST:PRESet](System.md#pre) command
will always preset the VNA to the factory preset settings, and
[SYST:UPReset](System.md#UPreset) will always perform a User Preset. [Learn
more about User
Preset.](../../S1_Settings/Preset_the_Analyzer.htm#PresetUserDefined)  
---  
Examples |  SYST:UPR:SAVE system:upreset:save:state  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:WINDows:CATalog?

Applicable Models: All (Read-only) Returns the window numbers that are
currently being used.  
---  
Examples |  SYST:WIND:CAT? system:windows:catalog?  
Return Type |  String of comma-separated numbers. For example: "1,2"  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

