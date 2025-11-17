# Source Commands

* * *

Controls the power delivered to the DUT and turn pulse on and off with an
external source.

SOURce: [CATalog?](source.md#Cat) [DC - More commands](SourceDC.md) [DPD - More commands](SourceDPD.md) [MODulation - More commands](SourceModulation.md) Multi-Dimensional Sweep - More commands M9810 | [COUNT](source.md#SourM9810Coun) | [MODule<mod>:ATTenuation[:VALue]](source.md#SourM9810ModAtt) | [MODule<mod>:ATTenuation:AUTO](source.md#SourM9810ModAttAuto) [PHASe - More commands](SourcePhase.md) [PORT:NUM?](source.md#PortNum) POWer | [ALC:MODE](source.md#ALCMode) | [CATalog?](source.md#ALCModeCat) | [RECeiver - More commands](SourceRxLeveling.md) | [ATTenuation](source.md#attval) | [AUTO](source.md#attauto) | RECeiver | REFerence | TEST | [CENTer](source.md#cent) | [CORRection \- More commands](SourceCorrection.md) | [COUPle](source.md#cplON) | [DETector](source.md#det) | [[LEVel]](source.md#pwrval) | [[IMMediate][AMPLitude]](source.md#pwrval) | [SLOPe](source.md#slope) | [STATe](source.md#slpON) | [MODE](source.md#Mode) | PORT | [STARt](source.md#PortStart) | [STOP](source.md#PortStop) | [SPAN](source.md#span) | [STARt](source.md#start) | [STOP](source.md#stop) PULSe | MODulator | [:STATe] | EXISts? [TDR - More Commands](TDR_Source.md)  
---  
  
Click on a keyword to view the command details.

See Also

  * [Example Programs](../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Learn about Power Settings](../../S1_Settings/Power_Level.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

  * [Remotely Specifying a Source Port](../Remotely_Specifying_a_Source_Port.md)

* * *

## SOURce<cnum>:CATalog?

Applicable Models: All (Read-only) Returns a list of valid port names that can
be controlled. Some ports only have string names, NOT numbers. All commands
that require a port argument have provisions for specifying either a port
number OR a string name.  See also: [Remotely Specifying a Source
Port](../Remotely_Specifying_a_Source_Port.htm).  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
Examples |  SOUR:CAT?  
source:catalog 'Some PNA-X models return  
"Port 1,Port 2,Port 3,Port 4,Port 1 Src2,Source3"  
Return Type |  Comma-separated list of strings.  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SOURce<cnum>:M9810:COUNt?

Applicable Models: M98xxA (Read-only) Returns the total number of M9810A
vector modulator modules that are connected to the VNA firmware. Only one
M9810A module can be installed, Hence, the return value could be 0 or 1.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
Examples |  SOUR:M9810:COUNT?  
source:m9810:coun?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SOURce<cnum>:M9810:MODule<mod>:ATTenuation[:VALue] <num>

Applicable Models: M98xxA (Read-Write) Sets the M9810A attenuation level for
the selected channel. This command disables the automatic attenuation control
([SOURce:M9810:MODule:ATTenuation:AUTO](source.md#SourM9810ModAttAuto)). The
parameter <mod> should be 1 because only one M9810A can be installed.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<num> |  Attenuation level (dB). The range is from 0 to 60 dB with the step size 10 dB.  
Examples |  SOUR:M9810:MODULE1:ATTENUATION 10  
source:m9810:mod1:att?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0  
  
* * *

## SOURce<cnum>:M9810:MODule<mod>:ATTenuation:AUTO <bool>

Applicable Models: M98xxA (Read-Write) Enable/disable the automatic M9810A
attenuation control. When the attenuation value (using
[SOURce:M9810:MODule:ATTenuation](source.md#SourM9810ModAtt)) is set, this
setting is turned off automatically. The parameter <mod> should be 1 because
only one M9810A can be installed.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<bool> |  ON (or 1) - Enable the automatic attenuator control. OFF (or 0) - Disable the automatic attenuator control.  
Examples |  SOUR:M9810:MODULE1:ATTENUATION:AUTO 1  
source:m9810:mod1:att:auto?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## SOURce<cnum>:PORT:NUM? <string>

Applicable Models: N522xB, N523xB, N524xB (Read-only) Returns a port number
for a named source.  All source ports have string names: "Port 1", " Port 2",
etc. All external sources have customized names. To convert a string name to a
port number use this query.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<string> |  String names.  
Examples |  SOUR:PORT:NUM? "MVG"  
source:port:num "port 1"  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SOURce<cnum>:POWer<port>:ALC[:MODE] <char>, [src]

Applicable Models: N522xB, N523xB, N524xB, M9485A, M983xA (Read-Write) Sets
and returns the ALC mode for the specified channel and port. Use
[SOUR:POW:ALC:MODE:CAT?](source.md#ALCModeCat) to return a list of valid ALC
modes for the VNA.  [Learn more about ALC
mode.](../../S1_Settings/Power_Level.htm#Advanced)  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<char> |  ALC Mode. For the PNA-X choose from:

  * INTernal Standard ALC loop
  * OPENloop No ALC loop

To set Leveling Mode to Receiver Leveling, use the [Receiver Leveling
commands](SourceRxLeveling.htm).  
[src] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples |  SOUR:POW:ALC INT source2:power2:alc:mode openloop source:power:alc:mode openloop,"Port 1 Src2"  
Query Syntax |  SOURce<cnum>:POWer<port>:ALC:MODE? [src]  
Return Type |  Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  INTernal  
  
* * *

## SOURce<cnum>:POWer<port>:ALC[:MODE]:CATalog? [src]

Applicable Models: N522xB, N523xB, N524xB, M9485A, M983xA (Read-only) Returns
a list of valid ALC modes for the specified channel and port number. Use the
returned values to set [SOUR:POW:ALC:MODE](source.md#ALCMode).  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
[src] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples |  SOUR:POW:ALC:CAT? source2:power2:alc:mode:catalog? source:power:alc:mode:catalog? "INTernal,OPENloop,RxLeveling"  
Return Type |  Comma-separated list of strings.  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SOURce<cnum>:POWer<port>:ATTenuation <num>, [src]

Applicable Models: All (Read-Write) Sets the attenuation level for the
selected channel. Sending this command turns automatic attenuation control
(SOUR:POW:ATT:AUTO) to OFF. If the ports are coupled, changing the attenuation
on one port will also change the attenuation on all other ports. To turn port
coupling OFF use [SOURce:POWer:COUPle OFF](source.md#cplON).  Note:
Attenuation cannot be set with Sweep Type set to Power See
[Sens:Power:ATT](Sense/Power.md) to change receiver attenuation.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<num> |  Attenuation value. The range of settable values depends on the VNA model. To determine the valid settings, do one of the following:

  * See [VNA models and options](../../Support/Configurations.md) to see the range and step size for each model / option.
  * Perform a query using MAX, then MIN, as an argument. Example: SOURce:POWer:ATT? Max However, this will not tell you the attenuation step size.

If an invalid attenuation setting is entered, the VNA will select the next
lower valid value. For example, if 19 is entered, then for an E8361A, 10 dB
attenuation will be selected. Note: This command will accept MIN or MAX
instead of a numeric parameter. See [SCPI
Syntax](../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.htm#min)
for more information.  
[src] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples |  SOUR:POW:ATT 10 source2:power2:attenuation maximum source:power:att 20, "Port 1 Src2"  
Query Syntax |  SOURce<cnum>:POWer<port>:ATTenuation? [min/max] [src] [min/max,src]   
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0  
  
* * *

## SOURce<cnum>:POWer<port>:ATTenuation:AUTO <bool>, [src]

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Turns
automatic attenuation control ON or OFF. Setting an attenuation value (using
SOURce:POWer:ATTenuation <num>) sets AUTO OFF.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.To make settings for ports that are not simple numbers, use the [src] argument.  
<bool> |  ON (or 1) - turns coupling ON. The analyzer automatically selects the appropriate attenuation level to meet the specified power level. OFF (or 0) - turns coupling OFF. Attenuation level must be set using SOURce:POWer:ATTenuation <num>.  
[src] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples |  SOUR:POW2:ATT:Auto On source2:power:attentuation:auto off sour:pow:att:auto 1, "Port 1 Src2"  
Query Syntax |  SOURce<cnum>:POWer: ATTenuation:Auto? [src]  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## SOURce<cnum>:POWer<port>:ATTenuation:RECeiver:REFerence <num>

Applicable Models: M9377A, M983xA (Read-Write) Sets the attenuation level for
the specified reference attenuator/port.  Note: (M983xA) This command works
only when the gain coupling is disabled by
[:SENS:SOUR:REC:GAIN:COUP:ALL](Sense/SenseSource.md#RecGainCoupAll).  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Receiver port number of the VNA. If unspecified, value is set to 1.  
<num> |  Attenuation value in dB. M9377A: 0 dB (Low) or 35 dB (High), If a number other than these is entered, the analyzer will select the next lower valid value. For example, if 19dB is entered, then 0dB attenuation will be selected. M983xA: 0 dB to 30 dB with 2 dB step  
Examples |  SOUR:POW2:ATT:REC:REF 0 source:power:attenuation:receiver:reference 35  
Query Syntax |  SOURce<cnum>:POWer<port>:ATTenuation:RECeiver:REFerence?  
Return Type |  Numeric. If querying for the standard port, the return value is 0  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  35 (M9377A), 18 (M983xA)  
  
* * *

## SOURce<cnum>:POWer<port>:ATTenuation:RECeiver:TEST <num>

Applicable Models: N522xB, N523xB, N524xB, M9485A, M98xxA, P50xxA/B with
option S9x090A (Read-Write) Sets the attenuation level for the specified test
attenuator/port.  Note (M980xA, P50xxA/B): This command works only for
Spectrum Analyzer channels. For S-parameter channels, use the Receiver Gain
dialog or [SENSe:SOURce:RECeiver:GAIN:*](Sense/SenseSource.md) commands. Note
(M983xA) :This command works only when gain coupling disabled by
[SENS:SOUR:REC:GAIN:COUP:ALL](Sense/SenseSource.md#RecGainCoupAll).  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Receiver port number of the VNA. If unspecified, value is set to 1.  
<num> |  Attenuation value in dB. [M980xA and P50xxA/B] 0dB (Low) or 35dB (High) / 0dB (Low) or 20dB (High)  If a number other than these is entered, the analyzer will select the next lower valid value. For example, if 19dB is entered, then 0dB attenuation will be selected. [M983xA] 0 to 30 dB with 2 dB step  
Examples |  SOUR:POW2:ATT:REC:TEST 0 source:power:attenuation:receiver:test 35  
Query Syntax |  SOURce<cnum>:POWer<port>:ATTenuation:RECeiver:TEST?  
Return Type |  Numeric. If querying for the standard port, the return value is 0  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  35 for others / 20 for M980xA and P50xxA / 18 for M983xA  
  
* * *

## SOURce<cnum>:POWer<port>:CENTer <num>

Applicable Models: All (Read-Write) Sets the power sweep center power. Must
also set:  
[SENS:SWE:TYPE POWer](Sense/Sweep_SCPI.md#ssty) and [SOURce:POWer:SPAN
<num>](source.htm#span).  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<num> |  Center power. Actual achievable leveled power depends on frequency.  
<port> |  If provided, this argument is ignored by the VNA.  
Examples |  SOUR:POW:CENT -15  
source2:power:center -7  
Query Syntax |  SOURce<cnum>:POWer:CENTer?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0 dBm  
  
* * *

## SOURce<cnum>:POWer<port>:COUPle <ON | OFF>

Applicable Models: All (Read-Write) Turns Port Power Coupling ON or OFF.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<ON | OFF> |  ON (or 1) - turns coupling ON. The same power level is used for all source ports. OFF (or 0) - turns coupling OFF.  Power level can be set individually for each source port.  
Examples |  SOUR:POW:COUP ON  
source2:power:couple off  
Query Syntax |  SOURce<cnum>:POWer:COUPle?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## SOURce<cnum>:POWer:DETector <char> OBSOLETE

(Read-Write) The VNA models with external leveling are now OBSOLETE.  Sets the
source leveling loop as Internal or External.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<char> |  INTernal \- Internal leveling is applied to the source EXTernal \- External leveling is applied to the source through a rear-panel connector. ONLY provided on 3 GHz, 6 GHz, and 9 GHz VNA models.  
Examples |  SOUR:POW:DET INT  
source2:power:detector external  
Query Syntax |  SOURce<cnum>:POWer:DETector?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  INTernal  
  
* * *

## SOURce<cnum>:POWer<port>[:LEVel][:IMMediate][:AMPLitude] <num>, [src]

Applicable Models: All (Read-Write) Sets the RF power output level.  Note:
When the sweep type is "segment sweep", and "independent port power per
segment" is set, then this command is not used.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<num> |  Source power in dBm. Note: The range of settable power values depends on the VNA model and if source attenuators are installed. To determine the range of values, perform a query using MAX, then MIN, as an argument. ([SOUR:POW:ATT:AUTO](source.md#attauto) must be set to ON) Example: SOURce:POWer? Max Actual achievable leveled power depends on frequency.  
[src] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples |  SOUR:POW1 5  
source2:power:level:immediate:amplitude maximum sour:pow 5, "Port 1 Src2"  
Query Syntax |  SOURce<cnum>:POWer[:LEVel][:IMMediate][:AMPLitude]? [src]  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0 dBm  
  
* * *

## SOURce<cnum>:POWer[:LEVel]:SLOPe <num>

Applicable Models: All (Read-Write) Sets the RF power slope value.  Also
enable the slope state using [SOUR:POW:SLOP:STAT ON](source.md#slpON).  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<num> |  Slope value in db/GHz. Choose any value between -2 and 2 (0 is no slope).  
Examples |  SOUR:POW:SLOP .5234434 source2:power:level slope -1.345  
Query Syntax |  SOURce<cnum>:POWer[:LEVel]:SLOPe?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0  
  
* * *

## SOURce<cnum>:POWer[:LEVel]:SLOPe:STATe <ON | OFF>

Applicable Models: All (Read-Write) Turns Power Slope ON or OFF. Set the slope
using [SOUR:POW:SLOP](source.md#slope).  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<ON|OFF> |  ON (or 1) - turns slope ON. OFF (or 0) - turns slope OFF.  
Examples |  SOUR:POW:SLOP: STAT ON  
source2:power:slope:state off  
Query Syntax |  SOURce<cnum>:POWer[:LEVel]:SLOPe:STATe ?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SOURce<cnum>:POWer<port>:MODE <state>, [src]

Applicable Models: All (Read-Write) Sets the state of VNA source for the
specified port.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<state> |  Source state. Choose from:

  * AUTO Source power is turned ON when required for a measurement.
  * ON Source power is always ON regardless of the measurement.
  * OFF Source power is always OFF regardless of the measurement.
  * NOCTL Do not send OFF commands to the external sources. If an external source is in the OFF state, this option is used to stop sending OFF commands to the external source to increase sweep speed.

  
[src] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples |  SOUR:POW:MODE ON source2:power4:mode OFF sour:pow:mode on, "Port 1 Src2"  
Query Syntax |  SOURce<cnum>:POWer<port>:MODE? [src]  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Auto  
  
* * *

## SOURce<cnum>:POWer<port>:PORT:STARt <num>, [src]

Applicable Models: All (Read-Write) Sets and reads the power sweep start power
value for a specific port. This allows uncoupled forward and reverse power
sweep ranges. Must also set [SENS:SWE:TYPE POWer](Sense/Sweep_SCPI.md#ssty)
and [SOUR:POW:COUPle OFF](source.md#cplON).  Note: When the sweep type is
"segment sweep", this command is not used.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<num> |  Start power in dBm. Note: The range of settable power values depends on the VNA model and if source attenuators are installed. To determine the range of values, perform a query using MAX, then MIN, as an argument. ([SOUR:POW:ATT:AUTO](source.md#attauto) must be set to ON) Example: SOURce:POWer:STARt? MIN Actual achievable leveled power depends on frequency.  
[src] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples |  SOUR:POW1:PORT:STAR -15  
source2:power:port:start 5, "bal port 1"  
Query Syntax |  SOURce<cnum>:POWer<port>:PORT:STARt? [src]  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  -10 dBm  
  
* * *

## SOURce<cnum>:POWer<port>:PORT:STOP <num>, [src]

Applicable Models: All (Read-Write) Sets and reads the power sweep stop power
value for a specific port. This allows uncoupled forward and reverse power
sweep ranges. Must also set [SENS:SWE:TYPE POWer](Sense/Sweep_SCPI.md#ssty)
and [SOUR:POW:COUPle OFF](source.md#cplON).  Note: When the sweep type is
"segment sweep", this command is not used.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<num> |  Stop power in dBm. Note: The range of settable power values depends on the VNA model and if source attenuators are installed. To determine the range of values, perform a query using MAX, then MIN, as an argument. ([SOUR:POW:ATT:AUTO](source.md#attauto) must be set to ON) Example: SOURce:POWer:STARt? MIN Actual achievable leveled power depends on frequency.  
[src] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples |  SOUR:POW1:PORT:STOP -15  
source2:power:port:stop 5, "bal port 1"  
Query Syntax |  SOURce<cnum>:POWer<port>:PORT:STOP? [src]  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0 dBm  
  
* * *

## SOURce<cnum>:POWer<port>:SPAN <num>

Applicable Models: All (Read-Write) Sets the power sweep span power. Must also
set:

     [SENS:SWE:TYPE POWer](Sense/Sweep_SCPI.md#ssty) and [SOURce:POWer:CENTer <num>](source.md#cent).  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<num> |  Span power. Actual achievable leveled power depends on frequency.  
<port> |  If provided, this argument is ignored by the VNA.  
Examples |  SOUR:POW:SPAN -15  
source2:power:span -7  
Query Syntax |  SOURce<cnum>:POWer:SPAN?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0 dBm  
  
* * *

## SOURce<cnum>:POWer<port>:STARt <num>

Applicable Models: All (Read-Write) Sets the power sweep start power for ALL
ports being used by the specified channel. Must also set:  [SENS:SWE:TYPE
POWer](Sense/Sweep_SCPI.htm#ssty) and [SOURce:POWer:STOP
<num>](source.htm#stop). Note: **This command is not recommended, however this
command is supported for backwards compatibility. This command will limit the
possible power setting to the available range on Port 1, even if other ports
have a wider power range. It is recommended to use** the
SOURce:POWer:PORT:STARt command instead. To set start power for a specific
port, use [SOUR:POW:PORT:STARt](source.md#PortStart). Note: When the sweep
type is "segment sweep", this command is not used.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<num> |  Start power. Note: The range of settable power values depends on the VNA model and if source attenuators are installed. To determine the range of values, perform a query using MAX, then MIN, as an argument. ([SOUR:POW:ATT:AUTO](source.md#attauto) must be set to ON) Example: SOURce:POWer:STARt? MIN Actual achievable leveled power depends on frequency.  
<port> |  If provided, this argument is ignored by the VNA.  
Examples |  SOUR:POW:STAR -15  
source2:power:start -7  
Query Syntax |  SOURce<cnum>:POWer:STARt?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0 dBm  
  
* * *

## SOURce<cnum>:POWer<port>:STOP <num>

Applicable Models: All (Read-Write) Sets the power sweep stop power for ALL
ports being used by the specified channel.. Must also set: [SENS:SWE:TYPE
POWer](Sense/Sweep_SCPI.htm#ssty) and [SOURce:POWer:START
<num>](source.htm#start).  To set start power for a specific port, use
[SOUR:POW:PORT:STOP](source.md#PortStop). Note: When the sweep type is
"segment sweep", this command is not used.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<num> |  Stop power. Note: The range of settable power values depends on the VNA model and if source attenuators are installed. To determine the range of values, perform a query using MAX, then MIN, as an argument. ([SOUR:POW:ATT:AUTO](source.md#attauto) must be set to ON) Example: SOURce:POWer:STOP? MAX Actual achievable leveled power depends on frequency.  
<port> |  If provided, this argument is ignored by the VNA.  
Examples |  SOUR:POW:STOP -15 source2:power:stop -7  
Query Syntax |  SOURce<cnum>:POWer:STOP?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0 dBm  
  
* * *

## SOURce<cnum>:PULSe<port>:MODulator[:STATe] <ON | OFF>,[src]

Applicable Models: All (Read-Write) Turns pulse on and off with an external
modulation source.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<ON|OFF> |  ON (or 1) - turns pulse ON. OFF (or 0) - turns pulse OFF.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
[src] |  String. (NOT case sensitive). Source port. Optional. Use SOUR:CAT? to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples |  SOUR:PULS:MOD:STAT ON,"MyMxg"  
source2:pulse1:modulator:state off  
Query Syntax |  SOURce<cnum>:PULSe<port>:MODulator[:STATe] ?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SOURce<cnum>:PULSe:MODulator:EXISts? [src]

Applicable Models: All (Read-only) Checks if pulse source exists.  
---  
Parameters |   
Examples |  SOUR:PULS:MOD:EXIS?  
source:pulse:modulator:exists? "MyMxg"  
[src] |  String. (NOT case sensitive). Source port. Optional. Use SOUR:CAT? to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable

