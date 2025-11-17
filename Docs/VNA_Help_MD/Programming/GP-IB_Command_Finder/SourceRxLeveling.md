# SOURce:POWer:ALC:MODE:RECeiver Commands

* * *

Controls Receiver Leveling.

SOUR:POW:ALC[:MODE]: [RECeiver:](SourceRxLeveling.md#RecLevMode) ACQuisition: | MODE [FAST](SourceRxLeveling.md#RecFast) [FTYPe](SourceRxLeveling.md#FType) [IFBW](SourceRxLeveling.md#recIFBW) ITERation | ENABle | [VALue](SourceRxLeveling.md#recIteration) [LSPC](SourceRxLeveling.md#LSPC) MODulation | APERture | OFFSet | SPAN | [:STATe] | BANDwidth | NOISe [OFFSet](SourceRxLeveling.md#recOffset) [RATio](SourceRxLeveling.md#ReceiverRatio)? [REFerence](SourceRxLeveling.md#RecRef) [SAFE[:STATe]](SourceRxLeveling.md#recSafeMode) | [MAX](SourceRxLeveling.md#recSafeMax) | [MIN](SourceRxLeveling.md#recSafeMin) | [STEP](SourceRxLeveling.md#recSafeStep) [[:STATe]](SourceRxLeveling.md#RecLevMode) [TOLerance](SourceRxLeveling.md#recToler)  
---  
  
Click on a keyword to view the command details.

See Also

  * [Example Programs](../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Learn about Receiver Leveling](../../S1_Settings/Receiver_Leveling.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

  * [Remotely Specifying a Source Port](../Remotely_Specifying_a_Source_Port.md)

* * *

## SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:ACQuisition:MODE <char>, [src]

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Sets all ports to pre-
sweep or point leveling mode for the specified channel. A channel cannot be
set to both pre-sweep and point leveling. For point leveling, the source power
is adjusted per point until the leveling receiver reports that the power is
within tolerance (or the maximum iteration setting is reached). When the
iteration is done, it moves immediately to the next point. This function is
enabled using the SOURce:POWer:ALC[:MODE]:RECeiver:ITERation:ENABle command.
[Learn more about Receiver Leveling](../../S1_Settings/Receiver_Leveling.md)  
---  
Parameters |   
<ch> | Channel number to be receiver leveled. If unspecified, value is set to 1  
<port> | Source port being used for Receiver Leveling. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<char> | Acquisition mode. Choose from: PRESweep \- Leveling sweeps are performed in the background (not visible) before every measurement sweep to measure and apply source correction data. POINt \- Source power is adjusted per point.  
[src] | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SOUR:POW:ALC:REC:ACQ:MODE PRES source2:power2:alc:mode:receiver:acquisition:mode presweep [See ReceiverLeveling example](../GPIB_Example_Programs/Setup_RxLeveling.md)  
Query Syntax | SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:ACQuisition:MODE? [src]  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | PRESweep  
  
* * *

## SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:FAST <bool>, [src]

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Sets and returns the
state of a separate IFBW setting for leveling sweeps. ON allows a higher
(faster) IFBW than the measurement sweep. It also causes leveling sweeps to be
noisier. [Learn more about Receiver
Leveling](../../S1_Settings/Receiver_Leveling.htm)  
---  
Parameters |   
<ch> | Channel number to be receiver leveled. If unspecified, value is set to 1  
<port> | Source port being used for Receiver Leveling. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<bool> | Separate IFBW setting state. ON or 1 \- Separate IFBW setting. Specify IFBW using SOUR:POW:ALC:MODE:REC:IFBW OFF or 0 \- Same IFBW as the measurement sweep. Specify IFBW using [Sens:BWID](Sense/Sense_Bandwidth.md#res)  
[src] | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SOUR:POW:ALC:REC:FAST 1 source2:power2:alc:mode:receiver:fast off source:power:alc:mode:receiver:fast off,"Port 1 Src2" [See ReceiverLeveling example](../GPIB_Example_Programs/Setup_RxLeveling.md)  
Query Syntax | SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:FAST? [src]  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:FTYPe <char>, [src]

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Sets and returns the
frequency range to use for receiver leveling. On the user interface, this is
the "Receiver frequency is determined by:" setting. [Learn more about Receiver
Leveling](../../S1_Settings/Receiver_Leveling.htm)  
---  
Parameters |   
<ch> | Channel number to be receiver leveled. If unspecified, value is set to 1  
<port> | Source port being used for Receiver Leveling. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<char> | Frequency range. Choose from: AUTO \- always uses the frequency range that is assigned to the measurement receiver. INPut \- Mixer/Converter input frequency range. OUTPut \- Mixer/Converter input frequency range. RECeiver \- FOM Receiver frequency range. SOURce \- FOM Source frequency range  
[src] | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SOUR:POW:ALC:REC:FTYP AUTO source2:power2:alc:mode:receiver:ftype input source:power:alc:mode:receiver:ftype output,"Port 1 Src2" [See ReceiverLeveling example](../GPIB_Example_Programs/Setup_RxLeveling.md)  
Query Syntax | SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:FTYPe? [src]  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | AUTO  
  
* * *

## SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:IFBW <value>, [src]

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Sets and returns the
IFBW to be used for leveling sweeps. Enable separate IFBW for leveling sweeps
using SOUR:POW:ALC:MODE:REC:FAST 1 [Learn more about Receiver
Leveling](../../S1_Settings/Receiver_Leveling.htm)  
---  
Parameters |   
<ch> | Channel number to be receiver leveled. If unspecified, value is set to 1  
<port> | Source port being used for Receiver Leveling..If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<value> | IFBW for leveling sweeps in Hz. The list of valid IF Bandwidths is different depending on the VNA model. [(Click to see the lists.)](../../S2_Opt/Trce_Noise.md#IFDiag) If an invalid number is specified, the analyzer will round up to the closest valid number. This parameter supports MIN and MAX as arguments. [Learn more.](../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min)  
[src] | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SOUR:POW:ALC:REC:IFBW 100E3 source2:power2:alc:mode:receiver:ifbw 100khz source:power:alc:mode:receiver:ifbw 70e3,"Port 1 Src2" [See ReceiverLeveling example](../GPIB_Example_Programs/Setup_RxLeveling.md)  
Query Syntax | SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:IFBW? [src]  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 100 kHz  
  
* * *

## SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:ITERation:ENABle <bool>, [src]

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Enables or disables the
receiver leveling maximum iteration search function set using the
SOURce:POWer:ALC[:MODE]:RECeiver:ACQuisition:MODE. The maximum iterations are
set using the SOURce:POWer:ALC[:MODE]:RECeiver:ITERation:VALue command. [Learn
more about Receiver Leveling](../../S1_Settings/Receiver_Leveling.htm)  
---  
Parameters |   
<ch> | Channel number to be receiver leveled. If unspecified, value is set to 1  
<port> | Source port being used for Receiver Leveling. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<bool> | Safe mode state. ON or 1 \- Enable receiver leveling maximum iteration search. OFF or 0 \- Disable receiver leveling maximum iteration search. The prior value for maximum iterations is retained.  
[src] | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SOUR:POW:ALC:REC:ITER:ENAB 1 source2:power2:alc:mode:receiver:iteration:enable on source:power:alc:mode:receiver:iteration:enable off,"Port 1 Src2" [See ReceiverLeveling example](../GPIB_Example_Programs/Setup_RxLeveling.md)  
Query Syntax | SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:ITERation:ENABle? [src]  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:ITERation:VALue <value>, [src]

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Sets and returns the
maximum iterations to be used in order to achieve the tolerance setting.
[Learn more about Receiver Leveling](../../S1_Settings/Receiver_Leveling.md)  
---  
Parameters |   
<ch> | Channel number to be receiver leveled. If unspecified, value is set to 1  
<port> | Source port being used for Receiver Leveling. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<value> | Max iterations. Choose a value 0 to 50. Note: Entering a value of 0 is allowed and sets the receiver leveling to Prior-Sweep mode. [Learn more](../../S1_Settings/Receiver_Leveling.md#Prior_Sweep_Mode).  
[src] | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SOUR:POW:ALC:REC:ITER:VAL 5 source2:power2:alc:mode:receiver:iteration:value 10 source:power:alc:mode:receiver:iteration:value 7,"Port 1 Src2" [See ReceiverLeveling example](../GPIB_Example_Programs/Setup_RxLeveling.md)  
Query Syntax | SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:ITERation:VALue? [src]  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 10  
  
* * *

## SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:LSPC <bool>, [src]

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Sets and returns the
state of Use Last Result for Source Power Cal. When Leveling Mode is switched
back to Internal, this feature turns Source Power Cal correction ON using the
latest receiver leveling correction data. [Learn more about Receiver
Leveling](../../S1_Settings/Receiver_Leveling.htm)  
---  
Parameters |   
<ch> | Channel number to be receiver leveled. If unspecified, value is set to 1  
<port> | Source port being used for Receiver Leveling. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<bool> | State of Use Last Result for Source Power Cal. ON or 1 \- When Leveling Mode is switched back to Internal, Source Power Cal correction is turned ON using the latest receiver leveling correction data. OFF or 0 \- When Leveling Mode is switched back to Internal, Source Power Cal correction is NOT turned ON.  
[src] | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SOUR:POW:ALC:REC:LSPC 1 source2:power2:alc:mode:receiver:lspc off source:power:alc:mode:receiver:lspc off,"Port 1 Src2" [See ReceiverLeveling example](../GPIB_Example_Programs/Setup_RxLeveling.md)  
Query Syntax | SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:LSPC? [src]  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:MODulation:APERture:OFFSet
<value>, [src]

Applicable Models: N524xB with S93070xB, and/or N522xB, N523xB, N524xB with
S9x09xxA/B, S9x090A/B, M98xxA/P50xxA with 090/190 + S9x090B and/or S95070xA/B
(M98xxA only)  (Read-Write) Sets and returns the offset of the frequency
aperture used to measure the signal power. Since the ideal modulation signal
is known, the total power is calculated from this value. The
SOURce:POWer:ALC:MODE:RECeiver:MODulation:APERture:STATe must be set to ON to
enable this setting. [Learn more about Receiver
Leveling](../../S1_Settings/Receiver_Leveling.htm)  
---  
Parameters |   
<ch> | Channel number to be receiver leveled. If unspecified, value is set to 1  
<port> | Source port being used for Receiver Leveling. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<value> | Receiver leveling aperture offset in Hz.  
[src] | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SOUR:POW:ALC:REC:MOD:APER:OFFS 1E6 source2:power2:alc:mode:receiver:modulation:aperture:offset 1E6,"MXG_Vector"  
Query Syntax | SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:MODulation:APERture:OFFSet? [src]  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:MODulation:APERture:SPAN
<value>, [src]

Applicable Models: N524xB with S93070xB, and/or N522xB, N523xB, N524xB with
S9x09xxA/B, S9x090A/B, M98xxA/P50xxA with 090/190 + S9x090B and/or S95070xA/B
(M98xxA only)  (Read-Write) Sets and returns the span of the frequency
aperture used to measure the signal power. Since the ideal modulation signal
is known, the total power is calculated from this value. The
SOURce:POWer:ALC:MODE:RECeiver:MODulation:APERture:STATe must be set to ON to
enable this setting. [Learn more about Receiver
Leveling](../../S1_Settings/Receiver_Leveling.htm)  
---  
Parameters |   
<ch> | Channel number to be receiver leveled. If unspecified, value is set to 1  
<port> | Source port being used for Receiver Leveling. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<value> | Receiver leveling aperture span in Hz.  
[src] | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SOUR:POW:ALC:REC:MOD:APER:SPAN 10e6 source2:power2:alc:mode:receiver:modulation:aperture:span 10e6,"MXG_Vector"  
Query Syntax | SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:MODulation:APERture:SPAN? [src]  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 10e6  
  
* * *

## SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:MODulation:APERture[:STATe]
<bool>, [src]

Applicable Models: N524xB with S93070xB, and/or N522xB, N523xB, N524xB with
S9x09xxA/B, S9x090A/B, M98xxA/P50xxA with 090/190 + S9x090B and/or S95070xA/B
(M98xxA only)  (Read-Write) Sets and returns the state of the receiver
leveling aperture settings for the specified source for Modulation Distortion
measurements. Enabling the aperture settings will measure the power more
quickly by reducing the span of the measurement. Enter the span and offset of
the frequency aperture used to measure the signal power. Since the ideal
modulation signal is known, the total power is calculated from this value.
[Learn more about Receiver Leveling](../../S1_Settings/Receiver_Leveling.md)  
---  
Parameters |   
<ch> | Channel number to be receiver leveled. If unspecified, value is set to 1  
<port> | Source port being used for Receiver Leveling. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<bool> | State of receiver leveling aperture settings. ON or 1 \- Enable span and offset aperture settings. OFF or 0 \- Disable span and offset aperture settings.  
[src] | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SOUR:POW:ALC:REC:MOD:APER 1 source2:power2:alc:mode:receiver:modulation:aperture:state 1,"MXG_Vector"  
Query Syntax | SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:MODulation:APERture[:STATe]? [src]  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:MODulation:BANDwidth:NOISe
<value>, [src]

Applicable Models:N524xB with S93070xB, and/or N522xB, N523xB, N524xB with
S9x09xxA/B, S9x090A/B, M98xxA/P50xxA with 090/190 + S9x090B and/or S95070xA/B
(M98xxA only)  (Read-Write) Sets and returns the receiver noise bandwidth
value for the specified source for Modulation Distortion measurements. Noise
bandwidth is equal to the Resolution bandwidth divided by the Vector Average
factor. The SOURce:POWer:ALC:MODE:RECeiver:FAST command must be set to ON to
enable this setting. [Learn more about Receiver
Leveling](../../S1_Settings/Receiver_Leveling.htm)  
---  
Parameters |   
<ch> | Channel number to be receiver leveled. If unspecified, value is set to 1  
<port> | Source port being used for Receiver Leveling. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<value> | Noise bandwidth value in Hz.  
[src] | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SOUR:POW:ALC:REC:MOD:BAND:NOIS 1e3 source2:power2:alc:mode:receiver:modulation:bandwidth:noise 1e3,"MXG_Vector"  
Query Syntax | SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:MODulation:BANDwidth:NOISe? [src]  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1000  
  
* * *

## SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:OFFSet <value>, [src]

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Sets and returns the
power level offset value. [Learn more about Receiver
Leveling](../../S1_Settings/Receiver_Leveling.htm)  
---  
Parameters |   
<ch> | Channel number to be receiver leveled. If unspecified, value is set to 1  
<port> | Source port being used for Receiver Leveling. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<value> | Power level offset in dB. Choose a value between +200 and -200.  
[src] | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SOUR:POW:ALC:REC:OFFS 10 source2:power2:alc:mode:receiver:offset 5 source:power:alc:mode:receiver:offset 7,"Port 1 Src2" [See ReceiverLeveling example](../GPIB_Example_Programs/Setup_RxLeveling.md)  
Query Syntax | SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:OFFSet? [src]  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:RATio? [src]

Applicable Models: N522xB, N523xB, N524xB (Read-only) Returns the receiver
ratio to be used with receiver leveling. This receiver ratio parameter is the
same as the one set in [SOUR:PHAS:PARameter](SourcePhase.md#parameter).
[Learn more about Receiver Leveling](../../S1_Settings/Receiver_Leveling.md)  
---  
Parameters |   
<ch> | Channel number to be receiver leveled. If unspecified, value is set to 1  
<port> | Source port being used for Receiver Leveling. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
[src] | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SOUR:POW:ALC:REC:RAT 10 source2:power2:alc:mode:receiver:ratio "a1/a3,3" source:power:alc:mode:receiver:ratio "R1/R3,3","Port 1 Src2" [See ReceiverLeveling example](../GPIB_Example_Programs/Setup_RxLeveling.md)  
Query Syntax | SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:RATio? [src] Returned is two VNA physical receivers that are controlled by different sources and the port that is 'paired' with <port>. The receivers and paired port are separated by a comma.  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | "a1/a3,3"  
  
* * *

## SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:REFerence <rec>, [src]

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Sets and returns the
reference receiver to be used with Receiver Leveling. [Learn more about
Receiver Leveling](../../S1_Settings/Receiver_Leveling.htm)  
---  
Parameters |   
<ch> | Channel number to be receiver leveled. If unspecified, value is set to 1  
<port> | Source port being used for Receiver Leveling. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<rec> | (String) VNA receiver. Choose the VNA physical receiver that works with the source port <port>. For example:<port 1> = "R1"  
[src] | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SOUR:POW:ALC:REC:REF 'r1' source2:power2:alc:mode:receiver:reference 'r2' source:power:alc:mode:receiver:reference "r1","Port 1 Src2" 'Read the last setting back source:power:alc:mode:receiver:reference? "Port 1 Src2" 'Returns: "R1,1" [See ReceiverLeveling example](../GPIB_Example_Programs/Setup_RxLeveling.md)  
Query Syntax | SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:REFerence? [src]  
Return Type | String \- Name of the reference receiver.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:SAFE[:STATe] <bool>, [src]

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Sets and returns the
state of Safe Mode. [Learn more about Receiver
Leveling](../../S1_Settings/Receiver_Leveling.htm)  
---  
Parameters |   
<ch> | Channel number to be receiver leveled. If unspecified, value is set to 1  
<port> | Source port being used for Receiver Leveling. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<bool> | Safe mode state. ON or 1 \- Safe mode ON OFF or 0 \- Safe mode OFF  
[src] | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SOUR:POW:ALC:REC:SAFE 1 source2:power2:alc:mode:receiver:safe on source:power:alc:mode:receiver:safe:state off,"Port 1 Src2" [See ReceiverLeveling example](../GPIB_Example_Programs/Setup_RxLeveling.md)  
Query Syntax | SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:SAFE[:STATe]? [src]  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:SAFE:MAX <value>, [src]

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Sets and returns the
maximum power level for Safe Mode. The MAX/MIN limit is always used regardless
of the safe mode state. In addition, the MAX/MIN limit is for port power and
related to power offset. If the power offset is not set correctly, the MAX/MIN
limit is not correct and it may impact the leveling. Ensure that the power
offset in the channel is the same as power offset during calibration. If the
exact power offset is not known, choose a limit for source and then it will
not be related to power offset. [Learn more about Receiver
Leveling](../../S1_Settings/Receiver_Leveling.htm)  
---  
Parameters |   
<ch> | Channel number to be receiver leveled. If unspecified, value is set to 1  
<port> | Source port being used for Receiver Leveling. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<value> | Maximum power level in dB.  
[src] | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SOUR:POW:ALC:REC:SAFE:MAX 10 source2:power2:alc:mode:receiver:safe:max 20 source:power:alc:mode:receiver:safe:max 15,"Port 1 Src2" [See ReceiverLeveling example](../GPIB_Example_Programs/Setup_RxLeveling.md)  
Query Syntax | SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:SAFE:MAX? [src]  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 30 dB  
  
* * *

## SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:SAFE:MIN <value>, [src]

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Sets and returns the
minimum power level for Safe Mode. The MAX/MIN limit is always used regardless
of the safe mode state. In addition, the MAX/MIN limit is for port power and
related to power offset. If the power offset is not set correctly, the MAX/MIN
limit is not correct and it may impact the leveling. Ensure that the power
offset in the channel is the same as power offset during calibration. If the
exact power offset is not known, choose a limit for source and then it will
not be related to power offset. [Learn more about Receiver
Leveling](../../S1_Settings/Receiver_Leveling.htm)  
---  
Parameters |   
<ch> | Channel number to be receiver leveled. If unspecified, value is set to 1  
<port> | Source port being used for Receiver Leveling. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<value> | Minimum power level in dB.  
[src] | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SOUR:POW:ALC:REC:SAFE:MIN -50 source2:power2:alc:mode:receiver:safe:min -80 source:power:alc:mode:receiver:safe:min -40,"Port 1 Src2" [See ReceiverLeveling example](../GPIB_Example_Programs/Setup_RxLeveling.md)  
Query Syntax | SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:SAFE:MIN? [src]  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | -95 dB  
  
* * *

## SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:SAFE:STEP <value>, [src]

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Sets and returns the
maximum step power level for Safe Mode. [Learn more about Receiver
Leveling](../../S1_Settings/Receiver_Leveling.htm)  
---  
Parameters |   
<ch> | Channel number to be receiver leveled. If unspecified, value is set to 1  
<port> | Source port being used for Receiver Leveling. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<value> | Maximum Step power level in dB.  
[src] | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SOUR:POW:ALC:REC:SAFE:STEP 2 source2:power2:alc:mode:receiver:safe:step 1.5 source:power:alc:mode:receiver:safe:min 2,"Port 1 Src2" [See ReceiverLeveling example](../GPIB_Example_Programs/Setup_RxLeveling.md)  
Query Syntax | SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:SAFE:STEP? [src]  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1 dB  
  
* * *

## SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver[:STATe] <bool>, [src]

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Sets and returns the
state of Receiver Leveling for the specified source port. [Learn more about
Receiver Leveling](../../S1_Settings/Receiver_Leveling.htm)  
---  
Parameters |   
<ch> | Channel number to be receiver leveled. If unspecified, value is set to 1  
<port> | Source port being used for Receiver Leveling. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<bool> | Receiver Leveling state. ON or 1 \- Receiver Leveling ON OFF or 0 \- Receiver Leveling OFF  
[src] | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SOUR:POW:ALC:REC 1 source2:power2:alc:mode:receiver on source:power:alc:mode:receiver:state off,"Port 1 Src2" [See ReceiverLeveling example](../GPIB_Example_Programs/Setup_RxLeveling.md)  
Query Syntax | SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver[:STATe]? [src]  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:TOLerance <value>, [src]

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Sets and returns the
tolerance value for leveling sweeps. [Learn more about Receiver
Leveling](../../S1_Settings/Receiver_Leveling.htm)  
---  
Parameters |   
<ch> | Channel number to be receiver leveled. If unspecified, value is set to 1  
<port> | Source port being used for Receiver Leveling. If unspecified, value is set to 1. To make settings for ports that are not simple numbers, use the [src] argument.  
<value> | Tolerance level in dB.  
[src] | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SOUR:POW:ALC:REC:TOL .01 source2:power2:alc:mode:receiver:tolerance .5 source:power:alc:mode:receiver:tolerance .2,"Port 1 Src2" [See ReceiverLeveling example](../GPIB_Example_Programs/Setup_RxLeveling.md)  
Query Syntax | SOURce<ch>:POWer<port>:ALC[:MODE]:RECeiver:TOLerance? [src]  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | .1 dB  
  
* * *

* * *

