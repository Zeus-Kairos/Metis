# SYSTem:PREFerences Commands

* * *

Sets and reads the VNA Preferences settings.

SYSTem:PREFerences | [DEFault](System_Preferences.md#PrefDefault) | ITEM | ASMRamp | CALibration | SAFE | [:STATe] | CORRectrion | PARallel | PROCess | CSET | COMPact | DIALog | SHOW | LICense | [EEXTrapolate](System_Preferences.md#EcalExtrap) | [EDEV: DPOLicy](System_Preferences.md#PrefEdevDpol) | [FCAL](System_Preferences.md#ItemFcal) | FIXTure | CIRCuit | DEFAults | GDELay | LEGacy | [TWOPoint](System_Preferences.md#groupDelay) | KEYS | MARKer:BANDwidth:SEARch | MARKer:SINGle | [MCControl](System_Preferences.md#markerCouplControl) | [MCMethod](System_Preferences.md#markerCoupleMethod) | [MCPreset](System_Preferences.md#MarkerCouplPreset) | MINTerpolate | [MRU](System_Preferences.md#mru) | OFFSet | [RCV](System_Preferences.md#prefRCV) | [SRC](System_Preferences.md#prefSRC) | [OPTimize:MEMory](System_Preferences.md#ItemOptMem) | PRESet:CONFirm [ | PRESet:POWer:STATe](System_Preferences.md#PowerState) | [PSRTrace](System_Preferences.md#pwrSwpRetrace) | QSTart | RECeivers | [CERRor](System_Preferences.md#RecError) | [OVERload:POWer](System_Preferences.md#overloadOFF) | [REDLimits](System_Preferences.md#Redlimits) | [REFMarker](System_Preferences.md#REFMarker) | REMote | AUTO | [:STATe] | [RETRace:POWer](System_Preferences.md#freqRetrace) | ROSCillator | RECall | [RTOF](System_Preferences.md#rtof) | SOFTkeys:NAVigation | [SWITch:DEF](System_Preferences.md#Switch) | USOLt SOURce | GLOBal | FREQuency | MODulation | FILE? | LOAD | [:STATe] | OUTPut | [:STATe] | POFF | IGNore | [:STATe] | POWer | [:STATe]  
---  
  
Click on a keyword to view the command details.

See Also

  * [SENS:CORRection:PREFerences](Sense/Sense_Correction.md)

  * [Learn about VNA Preferences](../../System/Preferences.md)

  * [Example Programs](../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## SYSTem:PREFerences:ITEM:ASMRamp <bool>

Applicable Models: N522xB, N523xB, N524xB, E5080A/B, M983xA (Read-Write) Set
and return whether ramp sweep is used whenever possible when sweep mode is in
Auto.  
---  
Parameters |   
<bool> |  Choose from: ON (1) Enable ramp sweep. OFF (0) Disable ramp sweep.  
Examples |  SYST:PREF:ITEM:ASMR 1  
system:preferences:item:asmramp OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:ASMRamp?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SYSTem:PREFerences:ITEM:CALibration:SAFE[:STATe] <bool>

Applicable Models: All (Read-Write) Set and reads whether to turn off RF Power
after calibration or not.  
---  
Parameters |   
<bool> |  Choose from: ON (1) Enable to turn off RF power after calibration.  OFF (0) Disable the turn off RF power after calibration.   
Examples |  SYST:PREF:ITEM:CAL:SAFE:STAT ON  
system:preferences:item:calibration:safe:state ON  
Query Syntax |  SYSTem:PREFerences:ITEM:CALibration:SAFE:STATe?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SYSTem:PREFerences:DEFault

Applicable Models: All (Write-only) Resets the VNA preferences to their
default settings. Some default settings vary depending on the VNA Model.
[Learn more about VNA Preferences.](../../System/Preferences.md#Preferences)  
---  
Examples |  SYST:PREF:DEF  
system:preferences:default  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:PREFerences:ITEM:CORRection:PARallel:PROCess <bool>

Applicable Models: All (Read-Write) Enable or disable parallel processing in
the CPU which provides higher calculation speeds.  
---  
Parameters |   
<bool> |  Choose from: OFF (0) Disable parallel processing. ON (1) Enable parallel processing.  
Examples |  SYST:PREF:ITEM:CORR:PAR:PROC 1  
system:preferences:item:correctrion:parallel:process OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:CORRection:PARallel:PROCess?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON or 1  
  
* * *

## SYSTem:PREFerences:ITEM:EDEV:DPOLicy <bool>

Applicable Models: All (Read-Write) Set and return whether External Devices
remain activated or are de-activated when the VNA is Preset or when a
Instrument State is recalled.  This setting remains until changed again using
this command, or until the hard drive is changed or reformatted.  
---  
Parameters |   
<bool> |  Choose from: OFF (0) External devices remain active when the VNA is Preset or when a Instrument State is recalled. ON (1) External devices are de-activated ([SYST:CONF:EDEV:STAT](SystConfigExternalDevice.md#State) to OFF) when the VNA is Preset or when a Instrument State is recalled.  
Examples |  SYST:PREF:ITEM:EDEV:DPOL 1  
system:preferences:item:edev:dpolicy OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:EDEV:DPOLicy?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON or 1  
  
* * *

## SYSTem:PREFerences:ITEM:CSET:COMPact <bool>

Applicable Models: All (Read-Write) Enables/disables the creation of compact
calsets.  
---  
Parameters |   
<bool> |  Choose from: ON (1) Enable creation of compact calsets. OFF (0) Disable creation of compact calsets.  
Examples |  SYST:PREF:ITEM:CSET:COMP 1 system:preferences:item:cset:compact OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:CSET:COMPact?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## SYSTem:PREFerences:ITEM:DIALog:SHOW:LICense <bool>

Applicable Models: All (Read-Write) Enables/disables showing the licensed
features dialog on startup.  
---  
Parameters |   
<bool> |  Choose from: ON (1) Enable showing licensed features on startup. OFF (0) Disable showing licensed features on startup.  
Examples |  SYST:PREF:ITEM:DIAL:SHOW:LIC 1  
system:preferences:item:dialog:show:license OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:DIALog:SHOW:LICense?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SYSTem:PREFerences:ITEM:EEXTrapolate <bool>

Applicable Models: All (Read-Write) Sets whether a Swept IMD or IMDx
calibration can exceed the stop frequency limit of an ECal module. [Learn
more](../../Applications/Swept_IMD.htm#ECalExtrap).  
---  
Parameters |   
<bool> |  Choose from: ON (1) Allow extrapolation. OFF (0) Do NOT allow extrapolation.  
Examples |  SYST:PREF:ITEM:EEXT 1 system:preferences:item:eextrapolate OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:EEXTrapolate?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SYSTem:PREFerences:ITEM:FCAL <bool>

Applicable Models: M980xA, P50xxA/B, P93xxB, E5080B, E5081A (Read-Write) Set
and return whether factory calibration is enabled after preset  
---  
Parameters |   
<bool> |  Choose from: ON (1) Enable factory calibration after preset OFF (0) Disable factory calibration after preset  
Examples |  SYST:PREF:ITEM:FCAL 0 system:preferences:item:fcal OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:FCAL?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## SYSTem:PREFerences:ITEM:FIXTure:CIRCuit:DEFAults <char>

Applicable Models: All (Read-Write) Sets the Series-C and Shunt-L components
to legacy or theoretical behavior when set to zero.  Note: This command is
only applicable in Firmware versions A.14.00.00 and later.  
---  
Parameters |   
<char> |  Choose from: THEoretical- When "R" or "L" is set to 0, the component is defined as "Short"; when "C" or "G" is set to 0, the component is defined as "Open". LEGacy - Legacy operation provided as a user-convenience for backward compatibility. When either of the two components of Series-C, "C", and "G", is set to 0, the component is defined as "Open"; when both components are set to 0, they are defined as "Short". When either of the two components of Shunt-L, "L", and "R", is set to 0, the component is defined as "Short"; when both components are set to 0, they are defined as "Open".  
Examples |  SYST:PREF:ITEM:FIXT:CIRC:DEFA THE  
system:preferences:item:fixture:circuit:defaults legacy  
Query Syntax |  SYSTem:PREFerences:ITEM:FIXTure:CIRCuit:DEFAults?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  THEoretical  
  
* * *

## SYSTem:PREFerences:ITEM:GDELay:LEGacy <bool>

Applicable Models: All (Read-Write) Sets the group delay aperture to use the
legacy computation method. [Learn more about group delay
aperture.](../../Tutorials/Group_Delay6_5.htm#aperture)  
---  
Parameters |   
<bool> |  Choose from: ON (1) Use legacy computation method. OFF (0) Do not use legacy computation method.  
Examples |  SYST:PREF:ITEM:GDEL:LEG 1  
system:preferences:item:gdelay:legacy OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:GDELay:LEGacy?  
Return Type |  Boolean  
|  OFF  
  
## SYSTem:PREFerences:ITEM:GDELay:TWOPoint <bool>

Applicable Models: All (Read-Write) Sets the default group delay aperture
setting. [Learn more about group delay
aperture.](../../Tutorials/Group_Delay6_5.htm#aperture)  
---  
Parameters |   
<bool> |  Choose from: ON (1) Sets default group delay aperture to 2 points. OFF (0) Sets default group delay aperture to 11 points.  
Examples |  SYST:PREF:ITEM:GDELay:TWOPoint 1  
system:preferences:item:gdelay:twopoint OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:GDELay:TWOPoint?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SYSTem:PREFerences:ITEM:KEYS <bool>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA, M983xA (Read-Write)
Set and return whether the keys are displayed or not.  
---  
Parameters |   
<bool> |  Choose from: ON (1)  Turn keys on. OFF (0)  Turn keys off.  
Examples |  SYST:PREF:ITEM:KEYS 1 system:preferences:item:keys OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:KEYS?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF (0)  
  
* * *

## SYSTem:PREFerences:ITEM:MARKer:BANDwidth:SEARch <char>

Applicable Models: All (Read-Write) Sets the bandwidth search preference to
start a bandwidth or notch search in either peak or marker mode.  
---  
Parameters |   
<char> |  Choose from: MARKer - **BW/Notch marker search reference is set to current marker position after Preset.** . PEAK - **BW/Notch marker search reference is set to peak after Preset.**  
Examples |  SYST:PREF:ITEM:MARK:BAND:SEAR MARK  
system:preferences:item:marker:bandwidth:search PEAK  
Query Syntax |  SYSTem:PREFerences:ITEM:MARKer:BANDwidth:SEARch?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  MARK (E5080A/B), PEAK (Others)  
  
* * *

## SYSTem:PREFerences:ITEM:MARKer:SINGle <bool>

Applicable Models:All (Read-Write) Set and return whether to use one marker
for marker search.  Enabled behavior:

  * Only one marker is used for bandwidth, notch, PNOP, and PSAT marker searches. The points of interest are marked with a notational UI element, i.e. a small triangle.
  * Bandwidth, notch, PNOP, and PSAT marker searches are always tracking. Tracking cannot be disabled.
  * One basic search and one advanced search may be set per marker.
  * The advanced search is enabled until the user disables the search or a multi-peak or multi-target search is executed.

Disabled behavior:

  * Bandwidth, notch, PSAT, and PNOP marker searches use multiple markers.
  * One advanced marker search is allowed per trace.
  * A marker may only perform a basic search or be part of an advanced search. Not both.
  * If an advanced marker search is enabled on a trace and then the user performs a basic search, the advanced search is automatically disabled.
  * Advanced searches may enable or disable tracking. Only one search may be tracked.

  
---  
Parameters |   
<bool> |  Choose from: ON (1) Enable single marker search. OFF (0) Disable single marker search.  
Examples |  SYST:PREF:ITEM:MARK:SING 1  
system:preferences:item:marker:single OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:MARKer:SINGle?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## SYSTem:PREFerences:ITEM:MCControl <bool>

Applicable Models: All (Read-Write) Set and return whether the Coupled Markers
setting controls the ON|OFF state of markers that are coupled. [Learn more
about Coupled Markers](../../S4_Collect/Markers.htm#Coupled_Markers). Refer
also to [CALC:MEAS:MARK:COUP:STATe
ON](Calculate/MeasureMARKer.htm#CALCulate:MEASure:MARKer:COUPling:STATe).  
---  
Parameters |   
<bool> |  Choose from: ON (1)  With Coupled Markers ON, when a marker is turned on, the same-numbered marker on all coupled traces will also be turned on. Likewise, turning off a marker will turn it off on all coupled traces. OFF (0)  Turning a marker on or off will have no effect on the markers on other traces.  
Examples |  SYST:PREF:ITEM:MCC 1 system:preferences:item:mccontrol OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:MCControl?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF (0)  
  
* * *

## SYSTem:PREFerences:ITEM:MCMethod <bool>

Applicable Models: All (Read-Write) Set and return whether Coupled Markers is
set to Channel or All after Preset. [Learn more about Coupled
Markers](../../S4_Collect/Markers.htm#Coupled_Markers). Refer also to
[CALC:MEAS:MARK:COUP:STATe
ON](Calculate/MeasureMARKer.htm#CALCulate:MEASure:MARKer:COUPling:STATe) and
SYST:PREF:ITEM:MCPR ON.  
---  
Parameters |   
<bool> |  Choose from: ON (1)  Marker Coupling Method is set to Channel after Preset. OFF (0)  Marker Coupling Method is set to ALL after Preset.  
Examples |  SYST:PREF:ITEM:MCM 1 system:preferences:item:mcmethod OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:MCMethod?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF (0)  
  
* * *

## SYSTem:PREFerences:ITEM:MCPRest <bool>

Applicable Models: All (Read-Write) Set and return whether Coupled Markers is
set to ON or OFF after Preset. [Learn more about Coupled
Markers](../../S4_Collect/Markers.htm#Coupled_Markers).  
---  
Parameters |   
<bool> |  Choose from: OFF (0)  Coupled Markers is OFF after Preset. ON (1)  Coupled Markers is ON after Preset.  
Examples |  SYST:PREF:ITEM:MCPR 1 system:preferences:item:mcpreset OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:MCPReset?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF (0)  
  
* * *

## SYSTem:PREFerences:ITEM:MINTerpolate <bool>

Applicable Models: N522xB, N523xB, N524xB, M983xA (Read-Write) Sets and reads
the state of the memory data interpolation default preference. The PNA will
return to the default interpolation state after a Preset, creating a new
trace, or closing the PNA application. [Learn
more](../../S4_Collect/Math_Operations.htm#MemoryTraceInterpolation).  
---  
Parameters |   
<bool> |  Choose from: 0 - OFF \- Set memory interpolation to OFF as the default. 1 - ON \- Set memory interpolation to ON as the default.  
Examples |  SYST:PREF:ITEM:MINT 1  
Query Syntax |  SYSTem:PREFerences:ITEM:MINTerpolate?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0  
  
* * *

## SYSTem:PREFerences:ITEM:MRU <bool>

Applicable Models: All (Read-Write) Set and return whether to list files for
recall on softkeys by most-recently used or alphabetically.  
---  
Parameters |   
<bool> |  Choose from: ON (1)  Recall softkeys show most recently-used files. OFF (0)  Recall softkeys show alphabetically-ordered files.  
Examples |  SYST:PREF:ITEM:MRU 1 system:preferences:item:mru OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:MRU?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF (0)  
  
* * *

## SYSTem:PREFerences:ITEM:OFFSet:RCV <bool>

Applicable Models: All (Read-Write) Set and return whether to offset the test
port receivers by the amount of receiver attenuation. [Learn
more.](../../S1_Settings/Power_Level.htm#Receiver_Atten) To send this command
using the VNA front panel, open the [GPIB Command Processor
Console](../Learning_about_GPIB/How_to_Configure_for_GPIB_SCPI_and_SICL.htm#console),
then type either of the following examples at the command prompt. Then type
the Query Syntax and press enter to be sure the VNA took the command. This
setting remains until changed again using this command, or until the hard
drive is changed or reformatted.  
---  
Parameters |   
<bool> |  Choose from: ON (1) Offset the test port receivers OFF (0) Do NOT offset the test port receivers  
Examples |  SYST:PREF:ITEM:OFFS:RCV 1  
system:preferences:item:offset:rcv OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:OFFSet:RCV?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  PNA-L and E836xB: OFF (does NOT offset the display). PNA-X: ON (offsets the display).  
  
* * *

## SYSTem:PREFerences:ITEM:OFFSet:SRC <bool>

Applicable Models: All (Read-Write) Set and return whether to offset the
reference receiver by the amount of source attenuation. [Learn
more.](../../S1_Settings/Power_Level.htm#Source_Atten) To send this command
using the VNA front panel, open the [GPIB Command Processor
Console](../Learning_about_GPIB/How_to_Configure_for_GPIB_SCPI_and_SICL.htm#console),
then type either of the following examples at the command prompt. Then type
the Query Syntax and press enter to be sure the VNA took the command. This
setting remains until changed again using this command, or until the hard
drive is changed or reformatted.  
---  
Parameters |   
<bool> |  Choose from: ON (1) Offset the reference receivers. OFF (0) Do NOT Offset the reference receivers.  
Examples |  SYST:PREF:ITEM:OFFS:SRC 1  
system:preferences:item:offset:src OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:OFFSet:SRC?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  All models: ON (offset the display).  
  
* * *

## SYSTem:PREFerences:ITEM:OPTimize:MEMory <bool>

Applicable Models: M9485A (Read-Write) Set and return the memory optimization
function status. This extends the maximum number of channel. However, this
causes slow measurement.  
---  
Parameters |   
<bool> |  Choose from: ON (1) Memory optimization on (more channesl, but slower speed) OFF (0) Memory optimization off  
Examples |  SYST:PREF:ITEM:OPT:MEM 1  
system:preferences:item:optimize:memory OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:OPTimize:MEMory?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SYSTem:PREFerences:ITEM:PRESet:CONFirm <bool>

Applicable Models: All (Read-Write) Set and return preset confirmation. If
preset confirmation is OFF, pressing the green PRESET key presets the
instrument and opens the Preset softkey menu. If preset confirmation is ON,
pressing the green PRESET causes the Preset menu to appear.  
---  
Parameters |   
<bool> |  Choose from: ON (1) Enable preset confirmation. OFF (0) Disable preset confirmation.  
Examples |  SYST:PREF:ITEM:PRES:CONF 1  
system:preferences:item:preset:confirm OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:PRESet:CONFirm?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## SYSTem:PREFerences:ITEM:PRESet:POWer[:STATe] <char>

Applicable Models: All (Read-Write) Set and return the Preset Power ON/OFF
state. [Learn more.](../../S1_Settings/Power_Level.md#PowerStatePreset) This
setting remains until changed again using this command, or until the hard
drive is changed or reformatted.  
---  
Parameters |   
<char> |  Choose from: ON - Instrument Preset always turns RF power ON. AUTO - When the current power setting is OFF, leave power OFF after Preset. When the current power setting is ON, turn power ON after Preset.  
Examples |  SYST:PREF:ITEM:PRES:POW ON  
system:preferences:item:preset:power:state auto  
Query Syntax |  SYSTem:PREFerences:ITEM:PRESet:POWer[:STATe]?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## SYSTem:PREFerences:ITEM:PSRTrace <char>

Applicable Models: All (Read-Write) At the end of a power sweep, while waiting
to trigger the next sweep, maintain source power at either the start power
level or at the stop power level.  To send this command using the VNA front
panel, open the [GPIB Command Processor
Console](../Learning_about_GPIB/How_to_Configure_for_GPIB_SCPI_and_SICL.htm#console),
then type either of the following examples at the command prompt. Then type
the Query Syntax and press enter to be sure the VNA took the command. This
setting remains until changed again using this command, or until the hard
drive is changed or reformatted.  
---  
Parameters |   
<char> |  Choose from: STARt - Maintain source power at the start power level. STOP - Maintain source power at the stop power level.  
Examples |  SYST:PREF:ITEM:PSRT STOP  
system:preferences:item:psrtrace start  
Query Syntax |  SYSTem:PREFerences:ITEM:PSRTrace?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  STARt  
  
* * *

## SYSTem:PREFerences:ITEM:QSTart <bool>

Applicable Models: All (Read-Write) This command controls the on/off state of
the preference, "On PRESET show Quick Start dialog".  
---  
Parameters |   
<bool> |  Choose from: ON (1) Display the Quick Start dialog on PRESET. OFF (0) Do not display the Quick Start dialog on PRESET.  
Examples |  SYST:PREF:ITEM:QST 1  
system:preferences:item:qstart OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:QST?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SYSTem:PREFerences:ITEM:RECeivers:CERRor[:STATe] <bool>

Applicable Models: All (Read-Write) Set and return whether to display receiver
overload warnings. [Learn more.](../../System/Preferences.md#RcvrOverload)  
---  
Parameters |   
<bool> |  Choose from: ON (1) Display overload warnings, OFF (0) Do NOT display overload warnings.  
Examples |  SYST:PREF:ITEM:REC:CERR 1 system:preferences:item:receivers:cerror:state OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:RECeivers:CERRor[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## SYSTem:PREFerences:ITEM:RECeivers:OVERload:POWer[:STATe] <bool>

Applicable Models: All (Read-Write) Set and return whether to turn source
power OFF when a receiver is overloaded. [Learn
more.](../../System/Preferences.htm#RcvrOverload)  
---  
Parameters |   
<bool> |  Choose from: ON (1) Turn OFF source power to ALL ports when a receiver is overloaded. OFF (0) Power remains ON when a receiver is overloaded.  
Examples |  SYST:PREF:ITEM:REC:OVER:POW 1 system:preferences:item:receivers:overload:power:state OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:RECeivers:OVERload:POWer[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF (0)  
  
* * *

## SYSTem:PREFerences:ITEM:REDLimits <bool>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA, M983xA (Read-Write)
Set and return whether to draw limits lines in Red or the trace color.  
---  
Parameters |   
<bool> |  Choose from: ON (1) All Limit lines are drawn in Red. OFF (0) Limit lines are drawn the same color as the trace.  
Examples |  SYST:PREF:ITEM:REDL 1 system:preferences:item:redlimits OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:REDLimits?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SYSTem:PREFerences:ITEM:REFMarker <bool>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA, M983xA (Read-Write)
Set and return whether to treat marker 10 as a reference marker. If set to ON
(1) for legacy behavior, marker 10 is the reference marker. If set to OFF (0),
marker 16 is the reference marker and marker 10 becomes a normal marker.
[Learn more.](../../S4_Collect/Markers.md#Number_of_Markers)  
---  
Parameters |   
<bool> |  Choose from: ON (1) Marker 10 is always a reference marker (Pre A.10.40 behavior). OFF (0) Marker 10 is just another marker and marker 16 becomes the reference marker. See [Reference Marker commands](../XResponseTopic.md#Reference_Markers)  
Examples |  SYST:PREF:ITEM:REFM 1 system:preferences:item:refmarker OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:REFMarker?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SYSTem:PREFerences:ITEM:REMote:AUTO[:STATe] <bool>

Applicable Models: All (Read-Write) Enables/disables changing from local to
remote status when a SCPI command is received.  
---  
Parameters |   
<bool> |  Choose from: OFF (0)  Turn OFF local/remote behavior. ON (1)  Turn ON local/remote behavior.  
Examples |  SYST:PREF:ITEM:REM:AUTO 0  
system:preferences:item:remote:auto:state OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:REMote:AUTO[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## SYSTem:PREFerences:ITEM:RETRace:POWer <char>

Applicable Models: N522xB, N523xB, N524xB, E5080B, E5081A (Read-Write) For
single-band frequency or segment sweeps ONLY, specify whether to turn RF power
ON or OFF during a retrace. [Learn more about RF power during sweep
retrace.](../../S1_Settings/Power_Level.htm#PowerONOFF) To send this command
using the VNA front panel, open the [GPIB Command Processor
Console](../Learning_about_GPIB/How_to_Configure_for_GPIB_SCPI_and_SICL.htm),
then type either of the following examples at the command prompt. Then type
the Query Syntax and press enter to be sure the VNA took the command. This
setting remains until changed using this command, or until the hard drive is
changed or reformatted.  
---  
Parameters |   
<char> |  Choose from: AUTO: Power is left ON during retrace of single-band frequency or segment sweeps ONLY. OFF: Power is turned OFF during retrace of single-band frequency or segment sweeps ONLY.  
Examples |  SYST:PREF:ITEM:RETR:POW OFF system:preferences:item:retrace:power auto  
Query Syntax |  SYSTem:PREFerences:ITEM:RETRace:POWer?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  AUTO  
  
* * *

## SYSTem:PREFerences:ITEM:ROSCillator:RECall <bool>

Applicable Models: All (Read-Write) Enables/disables External Reference
settings being affected by Recall/Preset.  
---  
Parameters |   
<bool> |  Choose from: OFF (0)  External Reference settings will be maintained until changed. ON (1)  External Reference settings will be affected by Recall/Preset.  
Examples |  SYST:PREF:ITEM:ROSC:REC 0  
system:preferences:item:roscillator:recall OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:ROSCillator:RECall?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## SYSTem:PREFerences:ITEM:RTOF <bool>

Applicable Models: All (Read-Write) Set and return whether to display limit
line failures as red trace segments or red data points (dots). [Learn
more.](../../S4_Collect/Use_Limits_to_Test_Devices.htm#dots)  
---  
Parameters |   
<bool> |  Choose from: ON (1) Display failures as red trace segments. (Red Trace On Fail). OFF (0) Display failures as red data points (dots).  
Examples |  SYST:PREF:ITEM:RTOF 1  
system:preferences:item:rtof OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:RTOF?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SYSTem:PREFerences:ITEM:SOFTkeys:NAVigation <bool>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA, M983xA (Read-Write)
This command controls the on/off state of the preference, "Use keyboard to
navigate softkeys".  
---  
Parameters |   
<bool> |  Choose from: ON (1) Enable softkey navigation with keyboard. OFF (0) Disable softkey navigation with keyboard.  
Examples |  SYST:PREF:ITEM:SOFT:NAV 1  
system:preferences:item:softkeys:navigation OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:SOFTkeys:NAVigation?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SYSTem:PREFerences:ITEM:SWITch:DEF <string>, <int>

Applicable Models: All (Read-Write) Sets the default setting for the Noise
Tuner switch. This is the setting that occurs when a new channel is created.
[Learn more.](../../Applications/Noise_Figure.md#blockDiag) This command will
return an error on VNA models with a built-in Noise tuner. To send this
command using the VNA front panel, open the [GPIB Command Processor
Console](../Learning_about_GPIB/How_to_Configure_for_GPIB_SCPI_and_SICL.htm),
then type either of the following examples at the command prompt. Then type
the Query Syntax and press enter to be sure the VNA took the command. This
setting remains until changed using this command, or until the hard drive is
changed or reformatted.  
---  
Parameters |   
<string> |  Name of the switch to set. Choose from:

  * "Port1NoiseTuner"

  
<int> |  Value to set. Choose from: 0 Sets the default (preset) to INTERNAL 1 Sets the default (preset) to EXTERNAL  
Examples |  SYST:PREF:ITEM:SWIT:DEF "Port1NoiseTuner" 1 'Write system:preferences:item:switch:def? "Port1NoiseTuner" 'Read  
Query Syntax |  SYSTem:PREFerences:ITEM:SWITch:DEF? <switch>  
Return Type |  Integer  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1 (External)  
  
* * *

## SYSTem:PREFerences:ITEM:USOLt <bool>

Applicable Models: All (Read-Write) This command controls the on/off state of
the preference, "Use Unknown thru math for SOLT methods".  
---  
Parameters |   
<bool> |  Choose from: ON (1) Error terms are computed using the unknown thru method. OFF (0)Error terms are computed using the definition of the defined thru.  
Examples |  SYST:PREF:ITEM:USOL 1  
system:preferences:item:usolt OFF  
Query Syntax |  SYSTem:PREFerences:ITEM:USOLt?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SYSTem:PREFerences:SOURce<port>:GLOBal:FREQuency <num>

Applicable Models: All (Read-Write) Set and return the frequency of the
specified global source. [Learn more](../../S1_Settings/Global_Source.md).  
---  
Parameters |   
<port> |  Source port number of the VNA.  
<num> |  Global source frequency. Choose any number between the minimum and maximum frequency limits of the analyzer. Units are Hz.  
Examples |  SYST:PREF:SOUR:GLOB:FREQ 1E9 system:preferences:source2:global:frequency 1 GHz  
Query Syntax |  SYSTem:PREFerences:SOURce<port>:GLOBal:FREQuency?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:PREFerences:SOURce<port>:GLOBal:MODulation:FILE?

Applicable Models: All (Read only) Returns the filename of the currently
loaded internal source modulation file. [Learn
more](../../S1_Settings/Internal_Source_Modulation.htm).  
---  
Parameters |  None  
<port> |  Source port number of the VNA.  
Examples |  SYST:PREF:SOUR1:GLOB:MOD:FILE?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:PREFerences:SOURce<port>:GLOBal:MODulation:LOAD <filename>

Applicable Models: All (Write-only) Loads the internal source modulation file.
[Learn more](../../S1_Settings/Internal_Source_Modulation.md).  
---  
Parameters |   
<port> |  Source port number of the VNA.  
<filename> |  Modulation file name.  
Examples |  SYST:PREF:SOUR1:GLOB:MOD:LOAD "c:\temp\mymodfile.mdx"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:PREFerences:SOURce<port>:GLOBal:MODulation[:STATe] <bool>

Applicable Models: All (Read-Write) Set and return the state of the specified
internal source modulation port. [Learn
more](../../S1_Settings/Global_Source.htm).  
---  
Parameters |   
<port> |  Source port number of the VNA.  
<bool> |  Choose from: OFF (0)  Turn modulation state for specified port OFF. ON (1)  Turn modulation state for specified port ON.  
Examples |  SYST:PREF:SOUR1:GLOB:MOD 1  
system:preferences:source1:global:modulation:state OFF  
Query Syntax |  SYSTem:PREFerences:SOURce<port>:GLOBal:MODulation[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SYSTem:PREFerences:SOURce<port>:GLOBal:OUTPut[:STATe] <bool>

Applicable Models: All (Read-Write) Set and return the output state of the
specified global source. [Learn more](../../S1_Settings/Global_Source.md).  
---  
Parameters |   
<port> |  Source port number of the VNA.  
<bool> |  Choose from: OFF (0)  Turn global source output OFF. ON (1)  Turn global source output ON.  
Examples |  SYST:PREF:SOUR2:GLOB:OUTP 1  
system:preferences:source3:global:output:state OFF  
Query Syntax |  SYSTem:PREFerences:SOURce<port>:GLOBal:OUTPut[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SYSTem:PREFerences:SOURce<port>:GLOBal:POFF:IGNore[:STATe] <bool>

Applicable Models: All (Read-Write) Set and return the global sources that
ignore the power off setting. [Learn
more](../../S1_Settings/Global_Source.htm).  
---  
Parameters |   
<port> |  Source port number of the VNA.  
<bool> |  Choose from: OFF (0)  Do not ignore power off settings for specified global sources. ON (1)  Ignore power off settings for specified global sources.  
Examples |  SYST:PREF:SOUR2:GLOB:POFF:IGN 1  
system:preferences:source3:global:poff:ignore:state OFF  
Query Syntax |  SYSTem:PREFerences:SOURce<port>:GLOBal:POFF:IGNore[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SYSTem:PREFerences:SOURce<port>:GLOBal:POWer <num>

Applicable Models: All (Read-Write) Set and return the power of the specified
global source. [Learn more](../../S1_Settings/Global_Source.md).  
---  
Parameters |   
<port> |  Source port number of the VNA.  
<num> |  Global source frequency. Choose any number between the minimum and maximum frequency limits of the analyzer. Units are Hz.  
Examples |  SYST:PREF:SOUR3:GLOB:POW -5 system:preferences:source2:global:power -5  
Query Syntax |  SYSTem:PREFerences:SOURce<port>:GLOBal:POWer?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:PREFerences:SOURce<port>:GLOBal[:STATe] <bool>

Applicable Models: All (Read-Write) Set and return the global state of the
specified global source. [Learn more](../../S1_Settings/Global_Source.md).  
---  
Parameters |   
<port> |  Source port number of the VNA.  
<bool> |  Choose from: OFF (0)  Turn global state of the specified source OFF. ON (1)  Turn global state of the specified source ON.  
Examples |  SYST:PREF:SOUR2:GLOB 1  
system:preferences:source3:global:state OFF  
Query Syntax |  SYSTem:PREFerences:SOURce<port>:GLOBal[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

