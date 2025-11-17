# Trigger Commands

* * *

Controls External Triggering.

TRIGger: AUXiliary | [COUNt](Trigger_SCPI.md#auxCount) CHANnel:AUXiliary | [DELay](Trigger_SCPI.md#AuxDelay) | [DURation](Trigger_SCPI.md#AuxDuration) | [[ENABle](Trigger_SCPI.md#auxEnable)] | [HANDshake](Trigger_SCPI.md#AuxHandshake) | INPut | [DELay](Trigger_SCPI.md#AuxInpDelay) | [HANDshake](Trigger_SCPI.md#AuxInpHandshake) | [POLarity](Trigger_SCPI.md#auxInpPolarity) | ROUTe | [TYPE](Trigger_SCPI.md#auxInpType) | [INTerval](Trigger_SCPI.md#auxInterval) | [IPOLarity](Trigger_SCPI.md#auxIpolarity) | [OPOLarity](Trigger_SCPI.md#auxOpolarity) | OUTPUT | [Delay](Trigger_SCPI.md#AuxOutpDelay) | [DURation](Trigger_SCPI.md#AuxOutpDuration) | [INTerval](Trigger_SCPI.md#auxOutpInterval) | [POLarity](Trigger_SCPI.md#auxOutpPolarity) | [POSition](Trigger_SCPI.md#auxOutpPosition) | [POSition](Trigger_SCPI.md#auxPosition) | [TYPE](Trigger_SCPI.md#auxType) [DELay](Trigger_SCPI.md#delay) PREFerence | [AIGLobal](Trigger_SCPI.md#PrefGlobal) [READy](Trigger_SCPI.md#ReadyPolarity) | [POLarity](Trigger_SCPI.md#ReadyPolarity) | [SOURce:MANual:ENABle](Trigger_SCPI.md#ReadSourManEnable) [SEQuence] | [LEVel](Trigger_SCPI.md#tssl) | ROUTE | [INPut](Trigger_SCPI.md#input) | [READy](Trigger_SCPI.md#Ready) | [SCOPe](Trigger_SCPI.md#tssc) | [SOURce](Trigger_SCPI.md#tss) | [SLOPe](Trigger_SCPI.md#slope) | [TYPE](Trigger_SCPI.md#type) STATus | READy?  
---  
  
Click on a keyword to view the command details.

Blue commands are superseded.

See Also

  * Example program [Triggering the VNA](../GPIB_Example_Programs/Triggering_the_PNA_using_SCPI.md)

  * [See other SCPI Triggering commands](../XStimulusTopic.md#Trigger)

  * [Learn about External / Aux Triggering](../../S1_Settings/External_Triggering.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## TRIGger:AUXiliary:COUNt?

Applicable Models: All (Read-only) Returns the number of AUX trigger input /
output connector pairs in the instrument.  
---  
Parameters |   
Examples | TRIG:AUX:COUN? trigger:auxiliary:count?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## TRIGger:CHANnel<ch>:AUXiliary<n>:DELay <num> Superseded

Applicable Models: N522xB, N523xB, N524xB, M937xA This command is replaced
with [TRIG:CHAN:AUX:INP:DEL](Trigger_SCPI.md#AuxInpDelay). (Read-Write)
Specifies the delay that should be applied by the VNA after the Aux trigger
input is received and before the acquisition is made.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | AUX Trigger connector used to send or receive signals. Choose from 1 [(AUX TRIG 1)](../../Rear_Panel/XRtour.md#ExternalTrig) or 2 [(AUX TRIG 2)](../../Rear_Panel/XRtour.md#ExternalTrig) If unspecified, value is set to 1.  
<num> | Delay value in seconds. Choose a value between 0 and 3.0 seconds.  
Examples | TRIG:CHAN:AUX:DEL .5 trigger:channel2:aux2:delay 1.5  
Query Syntax | TRIGger:CHANnel<ch>:AUXiliary<n>:DELay?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## TRIGger:CHANnel<ch>:AUXiliary<n>:DURation <num> Superseded

Applicable Models: N522xB, N523xB, N524xB, E5080A, M937xA, M9485A This command
is replaced with [TRIG:CHAN:AUX:OUTP:DUR](Trigger_SCPI.md#AuxOutpDuration).
(Read-Write) Specifies the width of the output pulse, which is the time that
the Aux trigger output will be asserted.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | AUX Trigger connector used to send or receive signals. Choose from 1 [(AUX TRIG 1)](../../Rear_Panel/XRtour.md#ExternalTrig) or 2 [(AUX TRIG 2)](../../Rear_Panel/XRtour.md#ExternalTrig) If unspecified, value is set to 1.  
<num> | Duration value in seconds. Choose a value between 1us (1E-6) and 1  
Examples | TRIG:CHAN:AUX:DUR .1 trigger:channel2:aux2:duration .01  
Query Syntax | TRIGger:CHANnel<ch>:AUXiliary<n>:DURation?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1E-6  
  
* * *

## TRIGger:CHANnel<ch>:AUXiliary<n>[:ENABle] <bool>

Applicable Models: All except M937xA and P937xA (Read-Write) Turns ON / OFF
the trigger output.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | AUX Trigger connector used to send or receive signals. Choose from 1 [(AUX TRIG 1)](../../Rear_Panel/XRtour.md#ExternalTrig) or 2 [(AUX TRIG 2)](../../Rear_Panel/XRtour.md#ExternalTrig) If unspecified, value is set to 1.  
<bool> | ON (or 1) - turns trigger output ON. OFF (or 0) - turns trigger output OFF.  
Examples | TRIG:CHAN:AUX 1 trigger:channel2:aux2:enable off  
Query Syntax | TRIGger:CHANnel<ch>:AUXiliary<n>:[ENABle]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## TRIGger:CHANnel<ch>:AUXiliary<n>:HANDshake <bool> Superseded

Applicable Models: N522xB, N523xB, N524xB This command is replaced with
[TRIG:CHAN:AUX:INP:HAND](Trigger_SCPI.md#AuxInpHandshake). (Read-Write) Turns
handshake ON / OFF. To enable handshake, the main trigger enable must also be
set using [TRIG:CHAN:AUX:ENAB](Trigger_SCPI.md#auxEnable). When ON, VNA waits
indefinitely for the input line to be asserted before continuing with the
acquisition. When OFF, the VNA acquires data without waiting.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | AUX Trigger connector used to send or receive signals. Choose from 1 [(AUX TRIG 1)](../../Rear_Panel/XRtour.md#ExternalTrig) or 2 [(AUX TRIG 2)](../../Rear_Panel/XRtour.md#ExternalTrig) If unspecified, value is set to 1.  
<bool> | ON (or 1) - turns handshaking ON. OFF (or 0) - turns handshaking OFF.  
Examples | TRIG:CHAN:AUX:HAND 1 trigger:channel2:aux2:handshake off  
Query Syntax | TRIGger:CHANnel<ch>:AUXiliary<n>:HANDshake?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## TRIGger:CHANnel<ch>:AUXiliary<n>:INPput:DELay <num>

Applicable Models: All except M937xA and P937xA (Read-Write) Specifies the
delay that should be applied by the VNA after the Aux trigger input is
received and before the acquisition is made.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | AUX Trigger connector used to send or receive signals. Choose from 1 (AUX TRIG 1) or 2 (AUX TRIG 2) If unspecified, value is set to 1.  
<num> | Delay value in seconds. Choose a value between 0 and 3.0 seconds.  
Examples | TRIG:CHAN:AUX:INP:DEL .5 trigger:channel2:aux:input:delay 1.5  
Query Syntax | TRIGger:CHANnel<ch>:AUXiliary<n>:INPut:DELay?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## TRIGger:CHANnel<ch>:AUXiliary<n>:INPut:HANDshake <bool>

Applicable Models: All except M937xA and P937xA (Read-Write) Turns handshake
ON / OFF. To enable handshake, the main trigger enable must also be set using
[TRIG:CHAN:AUX:ENAB](Trigger_SCPI.md#auxEnable). When ON, VNA waits
indefinitely for the input line to be asserted before continuing with the
acquisition. When OFF, the VNA acquires data without waiting.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | AUX Trigger connector used to send or receive signals. Choose from 1 (AUX TRIG 1) or 2 (AUX TRIG 2) If unspecified, value is set to 1.  
<bool> | ON (or 1) - turns handshaking ON. OFF (or 0) - turns handshaking OFF.  
Examples | TRIG:CHAN:AUX:INP:HAND 1 trigger:channel2:aux:input:handshake off  
Query Syntax | TRIGger:CHANnel<ch>:AUXiliary<n>:INPut:HANDshake?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## TRIGger:CHANnel<ch>:AUXiliary<n>:INPut:POLarity <char>

Applicable Models: All except M937xA and P937xA (Read-Write) Specifies the
polarity of the trigger IN signal to which the VNA will respond.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | AUX Trigger connector used to send or receive signals. Choose from 1 (AUX TRIG 1) or 2 (AUX TRIG 2) If unspecified, value is set to 1.  
<char> | Choose from:

  * POSitive VNA responds to leading edge or HIGH level
  * NEGative VNA responds to trailing edge or LOW level.

Set Edge or Level triggering using
[TRIG:CHAN:AUX:TYPE](Trigger_SCPI.md#auxType)  
Examples | TRIG:CHAN:AUX:INP:POL POS trigger:channel2:aux2:input:polarity negative  
Query Syntax | TRIGger:CHANnel<ch>:AUXiliary<n>:INPut:POLarity?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | NEGative  
  
* * *

## TRIGger:CHANnel<ch>:AUXiliary<n>:INPut:ROUTe <char>

Applicable Models: All except M937xA and P937xA (Read-Write) Specifies the
auxiliary trigger input source.  
---  
Parameters |   
<char> | Choose from: MAIN \- Meas Trig In BNC (PNA,ENA) PXI/USB VNA CTRL_S  KDMI Ctrl-S  **TRIG0**  Backplane Trigger Lines (PXI TRIG0) **TRIG1**  Backplane Trigger Lines (PXI TRIG1) **TRIG2**  Backplane Trigger Lines (PXI TRIG2) **TRIG3**  Backplane Trigger Lines (PXI TRIG3) **TRIG4**  Backplane Trigger Lines (PXI TRIG4) **TRIG5**  Backplane Trigger Lines (PXI TRIG5) **TRIG6**  Backplane Trigger Lines (PXI TRIG6) **TRIG7**  Backplane Trigger Lines (PXI TRIG7) (The P50xxA/B, P93xxB, P94xxB support the following parameters for streamline Rear Trig 1/2 SMB port.) NONE  Streamline Rear SMB Not connected (NONE) REAR1  Streamline Rear SMB (TRIG1) REAR2  Streamline Rear SMB (TRIG2)  
Examples | TRIG:CHAN:AUX:INP:ROUT MAIN trigger:channel:auxiliary:input:route main  
Query Syntax | TRIGger:CHANnel<ch>:AUXiliary<n>:INPut:ROUTe?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | MAIN  
  
* * *

## TRIGger:CHANnel<ch>:AUXiliary<n>:INPut:TYPE <char>

Appplicable Models: N522xB, N523xB, N524xB (Read-Write) Specifies the type of
Aux input detection that the VNA will employ.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | AUX Trigger connector used to send or receive signals. Choose from 1 (AUX TRIG 1) or 2 (AUX TRIG 2) If unspecified, value is set to 1.  
<char> | Choose from: EDGE VNA responds to the leading edge of a signal LEVel VNA responds to the level (HIGH or LOW) of a signal  
Examples | TRIG:CHAN:AUX:INP:TYPE EDGE trigger:channel2:aux:input:type level  
Query Syntax | TRIGger:CHANnel<ch>:AUXiliary<n>:INPut:TYPE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | EDGE  
  
* * *

## TRIGger:CHANnel<ch>:AUXiliary<n>:INTerval <char> Superseded

Applicable Models: N522xB, N523xB, N524xB, M937xA, E5080A/B, M9485A, M98xxA,
P50xxA This command is replaced with
[TRIG:CHAN:AUX::OUTP:INT](Trigger_SCPI.md#auxOutpInterval). (Read-Write)
Specifies how often a trigger output signal is sent.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | AUX Trigger connector used to send or receive signals. Choose from 1 [(AUX TRIG 1)](../../Rear_Panel/XRtour.md#ExternalTrig) or 2 [(AUX TRIG 2)](../../Rear_Panel/XRtour.md#ExternalTrig) If unspecified, value is set to 1.  
<char> | Choose from:

  * POINt Trigger signal is sent every data point. (effectively the same as [Point sweep](../../S1_Settings/Trigger.md#state_point))
  * SWEep Trigger signal is sent once every sweep.

  
Examples | TRIG:CHAN:AUX:INT POI trigger:channel2:aux2:interval sweep  
Query Syntax | TRIGger:CHANnel<ch>:AUXiliary<n>:INTerval?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | SWEep  
  
* * *

## TRIGger:CHANnel<ch>:AUXiliary<n>:IPOLarity <char> Superseded

Applicable Models: N522xB, N523xB, N524xB This command is replaced with
TRIG:CHAN:AUX::INP:POL. (Read-Write) Specifies the polarity of the trigger IN
signal to which the VNA will respond.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | AUX Trigger connector used to send or receive signals. Choose from 1 [(AUX TRIG 1)](../../Rear_Panel/XRtour.md#ExternalTrig) or 2 [(AUX TRIG 2)](../../Rear_Panel/XRtour.md#ExternalTrig) If unspecified, value is set to 1.  
<char> | Choose from:

  * POSitive VNA responds to leading edge or HIGH level
  * NEGative VNA responds to trailing edge or LOW level.

Set Edge or Level triggering using
[TRIG:CHAN:AUX:TYPE](Trigger_SCPI.md#auxType)  
Examples | TRIG:CHAN:AUX:IPOL POS trigger:channel2:aux2:ipolarity negative  
Query Syntax | TRIGger:CHANnel<ch>:AUXiliary<n>:IPOLarity?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | NEGative  
  
* * *

## TRIGger:CHANnel<ch>:AUXiliary<n>:OPOLarity <char> Superseded

Applicable Models: N522xB, N523xB, N524xB, M937xA, E5080A/B, M9485A, M98xxA,
P50xxA This command is replaced with
[TRIG:CHAN:AUX::OUTP:POL](Trigger_SCPI.md#auxOutpPolarity). (Read-Write)
Specifies the polarity of the Aux Output signal being supplied by the VNA.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | AUX Trigger connector used to send or receive signals. Choose from 1 [(AUX TRIG 1)](../../Rear_Panel/XRtour.md#ExternalTrig) or 2 [(AUX TRIG 2)](../../Rear_Panel/XRtour.md#ExternalTrig) If unspecified, value is set to 1.  
<char> | Choose from:

  * POSitive VNA sends positive going pulse.
  * NEGative VNA sends negative going pulse.

  
Examples | TRIG:CHAN:AUX:OPOL NEG trigger:channel2:aux2:opolarity positive  
Query Syntax | TRIGger:CHANnel<ch>:AUXiliary<n>:OPOLarity?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | NEGative  
  
* * *

## TRIGger:CHANnel<ch>:AUXiliary<n>:OUTPut:DELay <num>

Applicable Models: All except M937xA and P937xA (Read-Write) Specifies the
delay that should be applied by the VNA after the Aux trigger output is output
and before the acquisition is made.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | AUX Trigger connector used to send or receive signals. Choose from 1 (AUX TRIG 1) or 2 (AUX TRIG 2) If unspecified, value is set to 1.  
<num> | Delay value in seconds. Choose a value between 0 and 1 seconds.  
Examples | TRIG:CHAN:AUX:OUTP:DEL .5 trigger:channel2:aux:putput:delay 1.5  
Query Syntax | TRIGger:CHANnel<ch>:AUXiliary<n>OUTPut::DELay?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## TRIGger:CHANnel<ch>:AUXiliary<n>:OUTPut:DURation <num>

Applicable Models: All except M937xA and P937xA (Read-Write) Specifies the
width of the output pulse, which is the time that the Aux trigger output will
be asserted.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | AUX Trigger connector used to send or receive signals. Choose from 1 (AUX TRIG 1) or 2 (AUX TRIG 2) If unspecified, value is set to 1.  
<num> | Duration value in seconds. Choose a value between 1us (1E-6) and 1  
Examples | TRIG:CHAN:AUX:OUTP:DUR .1 trigger:channel2:aux:output:duration .01  
Query Syntax | TRIGger:CHANnel<ch>:AUXiliary<n>:OUTPut:DURation?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1E-6  
  
* * *

## TRIGger:CHANnel<ch>:AUXiliary<n>:OUTPut:INTerval <char>

Applicable Models: All except M937xA and P937xA (Read-Write) Specifies how
often a trigger output signal is sent.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | AUX Trigger connector used to send or receive signals. Choose from 1 (AUX TRIG 1) or 2 (AUX TRIG 2)   
<char> | Choose from:

  * POINt Trigger signal is sent every data point. (effectively the same as [Point sweep](../../S1_Settings/Trigger.md#state_point))
  * SWEep Trigger signal is sent once every sweep.

  
Examples | TRIG:CHAN:AUX:OUTP:INT POI trigger:channel2:aux:output:interval sweep  
Query Syntax | TRIGger:CHANnel<ch>:AUXiliary<n>:OUTPut:INTerval?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | SWEep  
  
* * *

## TRIGger:CHANnel<ch>:AUXiliary<n>:OUTPut:POLarity <char>

Applicable Models: All except M937xA and P937xA (Read-Write) Specifies the
polarity of the Aux Output signal being supplied by the VNA.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | AUX Trigger connector used to send or receive signals. Choose from 1 (AUX TRIG 1) or 2 (AUX TRIG 2)  If unspecified, value is set to 1.  
<char> | Choose from:

  * POSitive VNA sends positive going pulse.
  * NEGative VNA sends negative going pulse.

  
Examples | TRIG:CHAN:AUX:OUTP:POL NEG trigger:channel2:aux:output:polarity positive  
Query Syntax | TRIGger:CHANnel<ch>:AUXiliary<n>:OUTPut:POLarity?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | NEGative  
  
* * *

## TRIGger:CHANnel<ch>:AUXiliary<n>:OUTPut:POSition <char>

Appplicable Models: All except M937xA and P937xA (Read-Write) Specifies
whether the aux trigger out signal is sent BEFore or AFTer the acquisition.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | AUX Trigger connector used to send or receive signals. Choose from 1 (AUX TRIG 1) or 2 (AUX TRIG 2) If unspecified, value is set to 1.  
<char> | Choose from:

  * BEFore Use if the external device needs to be triggered before the data is acquired, such as a power meter.
  * AFTer Use if the external device needs to be triggered just after data has been acquired, such as an external source. This could be more efficient since it allows the external device to get ready for the next acquisition at the same time as the VNA.

  
Examples | TRIG:CHAN:AUX:OUTP:POS BEF trigger:channel2:aux:output:position after  
Query Syntax | TRIGger:CHANnel<ch>:AUXiliary<n>:OUTPut:POSition?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | AFTer  
  
* * *

## TRIGger:CHANnel<ch>:AUXiliary<n>:POSition <char> Superseded

Appplicable Models: N522xB, N523xB, N524xB, M937xA, E5080A/B, M9485A, M98xxA,
P50xxA This command is replaced with
[TRIG:CHAN:AUX::OUTP:POS](Trigger_SCPI.md#auxOutpPosition). (Read-Write)
Specifies whether the aux trigger out signal is sent BEFore or AFTer the
acquisition.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | AUX Trigger connector used to send or receive signals. Choose from 1 [(AUX TRIG 1)](../../Rear_Panel/XRtour.md#ExternalTrig) or 2 [(AUX TRIG 2)](../../Rear_Panel/XRtour.md#ExternalTrig) If unspecified, value is set to 1.  
<char> | Choose from:

  * BEFore Use if the external device needs to be triggered before the data is acquired, such as a power meter.
  * AFTer Use if the external device needs to be triggered just after data has been acquired, such as an external source. This could be more efficient since it allows the external device to get ready for the next acquisition at the same time as the VNA.

  
Examples | TRIG:CHAN:AUX:POS BEF trigger:channel2:aux2:position after  
Query Syntax | TRIGger:CHANnel<ch>:AUXiliary<n>:POSition?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | AFTer  
  
* * *

## TRIGger:CHANnel<ch>:AUXiliary<n>:TYPE <char> Superseded

Appplicable Models: N522xB, N523xB, N524xB This command is replaced with
[TRIG:CHAN:AUX::INP:TYPE](Trigger_SCPI.md#auxInpType). (Read-Write) Specifies
the type of Aux input detection that the VNA will employ.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | AUX Trigger connector used to send or receive signals. Choose from 1 [(AUX TRIG 1)](../../Rear_Panel/XRtour.md#ExternalTrig) or 2 [(AUX TRIG 2)](../../Rear_Panel/XRtour.md#ExternalTrig) If unspecified, value is set to 1.  
<char> | Choose from: EDGE VNA responds to the leading edge of a signal LEVel VNA responds to the level (HIGH or LOW) of a signal  
Examples | TRIG:CHAN:AUX:TYPE EDGE trigger:channel2:aux2:type level  
Query Syntax | TRIGger:CHANnel<ch>:AUXiliary<n>:TYPE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | EDGE  
  
* * *

## TRIGger:DELay <num>

Applicable Models: All (Read-Write) Sets and reads the trigger delay for ALL
channels (globally). This delay is only applied while
[TRIG:SOURce](Trigger_SCPI.md#tss) = EXTernal and
[TRIG:SCOP](Trigger_SCPI.md#tssc) = ALL After an external trigger is applied,
the start of the sweep is held off for an amount of time equal to the delay
setting plus any inherent latency. To apply a trigger delay for the specified
channel ONLY, use [SENS:SWE:TRIG:DELay](Sense/Sweep_SCPI.md#Delay)  
---  
Parameters |   
<num> | Delay value in seconds. Choose from 0 to 3.  
Examples | TRIG:DEL .0003 Sets the trigger delay to 300 microseconds. The sweep will not start until approximately 300 microseconds after an external trigger is applied.  
Query Syntax | TRIGger:DELay?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## TRIGger:PREFerence:AIGLobal <bool>

Applicable Models: N522xB, N523xB, N524xB, E5080A, M937xA, M9485A, P937xA,
M983xA (Read-Write) Sets the Trigger OUT behavior to either Global or Channel.
[Learn more about this
setting.](../../S1_Settings/External_Triggering.htm#Output) This command will
cause the VNA to Preset. This setting remains until changed again using this
command, or until the hard drive is changed or reformatted. To send this
command using the VNA GUI, open the [GPIB Command Processor
Console](../Learning_about_GPIB/How_to_Configure_for_GPIB_SCPI_and_SICL.htm#console),
then type either of the following examples at the command prompt. Then type
the Query Syntax and press enter to be sure the VNA took the command.  
---  
Parameters |   
<bool> | Choose from:

  * ON (or 1) - Trigger properties apply to ALL channels (Global).
  *     * Allows use of [CONT:SIGNal](Control.md#signal) command to configure the external trigger properties.
    * "Per Point" trigger property is not settable. Use the channel's [Point trigger](Sense/Sweep_SCPI.md#Mode) setting.
  * OFF (or 0) - External Trigger properties apply to each channel independently.
  *     * Must use [TRIG:CHAN:AUX](Trigger_SCPI.md) commands to configure the external trigger properties. [CONT:SIGNal](Control.md#signal) will NOT work.
    * "Per Point" trigger output property is set using the channel's [Point trigger](Sense/Sweep_SCPI.md#Mode) setting AND [TRIG:CHAN:AUX:INTerval](Trigger_SCPI.md#auxInterval).

  
Examples | TRIG:PREF:AIGL 1 trigger:preference:aiglobal 0  
Query Syntax | TRIGger:PREFerence:AIGLobal?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## TRIGger:READy:POLarity <char>

Applicable Models: All (Read-Write) Specifies the polarity of Ready for
Trigger output. All existing Ready for Trigger outputs are configured
simultaneously with this command.  
---  
Parameters |   
<char> | LOW \- Outputs a TTL low when the VNA is ready for trigger. HIGH \- Outputs a TTL high when the VNA is ready for trigger.  
Examples | TRIG:READ:POL HIGH trigger:ready:polarity low  
Query Syntax | TRIGger:READy:POLarity?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Low  
  
* * *

## TRIGger:READy:SOURce:MANual:ENABle <bool>

Applicable Models: M980xA, P50xxA/B, E5080B, M983xA (Read-Write) Sets the mode
of Ready for Trigger output. This allows you to have a same operation with
M937xA and P937xA. This setting is not saved/recalled in the status file.  
---  
Parameters |   
<bool> | Choose from:

  * ON (or 1) - Outputs ready for trigger when trigger source is external or manual. Same operation with M937xA and P937xA.
  * OFF (or 0) - Outputs ready for trigger when trigger source is external.

  
Examples | TRIG:READ:SOUR:MAN:ENAB 1 trigger:ready:source:manual:enable 0  
Query Syntax | TRIGger:READy:SOURce:MANual:ENABle?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 (Preset will not reset the setting.)  
  
* * *

## TRIGger[:SEQuence]:LEVel <char> \- Superseded

This command is replaced with [CONTrol:SIGNal](Control.md#signal) (Read-
Write) Triggers either on a High or Low level trigger signal. This setting
only has an effect when [TRIG:SOURce EXTernal](Trigger_SCPI.md#tss) is
selected.  
---  
Parameters |   
<char> | Choose from:

  * HIGH - analyzer triggers on TTL High
  * LOW - analyzer triggers on TTL Low

  
Examples | TRIG:LEV HIGH  
trigger:sequence:level low  
Query Syntax | TRIGger[:SEQuence]:LEVel?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | HIGH  
  
* * *

## TRIGger[:SEQuence]:ROUTE:INPut <char>

Applicable Models: All (Read-Write) Specifies the connector to use for the
external trigger input.  
---  
Parameters |   
<char> | Choose from: MAIN \- Meas Trig In BNC (PNA, ENA) MATH \- handler I/O Pin 18  PULSE3 \- Internal routing of pulse 3 output to the MEAS TRIG IN PXI/USB VNA SMB  Meas Trig In SMB (M937xA only) CTRL_S  KDMI Ctrl-S (Except M937xA) (The PXI VNA supports the following parameters for backplane trigger.) DSTARB  Backplane Trigger Lines (PXIe DSTARB) (M937xA only) **STAR**  Backplane Trigger Lines (PXI STAR) (M937xA only) **TRIG0**  Backplane Trigger Lines (PXI TRIG0) **TRIG1**  Backplane Trigger Lines (PXI TRIG1) **TRIG2**  Backplane Trigger Lines (PXI TRIG2) **TRIG3**  Backplane Trigger Lines (PXI TRIG3) **TRIG4**  Backplane Trigger Lines (PXI TRIG4) **TRIG5**  Backplane Trigger Lines (PXI TRIG5) **TRIG6**  Backplane Trigger Lines (PXI TRIG6) **TRIG7**  Backplane Trigger Lines (PXI TRIG7) (The P50xxA/B, P93xxB and P94xxB support the following parameters for streamline Rear Trig 1/2 SMB port.) NONE  Streamline Rear SMB Not connected (NONE) REAR1  Streamline Rear SMB (TRIG1) REAR2  Streamline Rear SMB (TRIG2)  
Examples | TRIG:ROUTE:INP MAIN trigger:sequence:route:input main  
Query Syntax | TRIGger[:SEQuence]:ROUTE:INPut?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | MAIN  
  
* * *

## TRIGger[:SEQuence]:ROUTE:READy <char>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA, M980xA, M983xA,
P50xxA/B (Read-Write) Specifies the connector to use for the trigger OUT ready
line.  
---  
Parameters |   
<char> | Choose from: MATH \- [handler pin 21](../HandlerIO_Connector.md#ReadyForTrigger)  
Examples | TRIG:ROUTE:READ MATH trigger:sequence:route:ready math  
Query Syntax | TRIGger[:SEQuence]:ROUTE:READy?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | MAIN  
  
* * *

## TRIGger[:SEQuence]:SCOPe <char>

Applicable Models: All (Read-Write) Specifies whether a trigger signal is sent
to all channels or only the current channel. See [Triggering the VNA using
SCPI](../GPIB_Example_Programs/Triggering_the_PNA_using_SCPI.htm).  
---  
Parameters |   
<char> | Choose from:

  * ALL - trigger signal is sent to all channels. Also sets [SENS:SWEep:TRIG:POINt OFF](Sense/Sweep_SCPI.md#sstp) on ALL channels.
  * CURRent - trigger signal is sent to only one channel at a time. With each trigger signal, the channel is incremented to the next triggerable channel.
  * ACTive \- trigger signal is sent to active channel only.

  
Examples | TRIG:SCOP ALL  
trigger:sequence:scope current  
Query Syntax | TRIGger[:SEQuence]:SCOPe?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ALL  
  
* * *

## TRIGger[:SEQuence]:SLOPe <char>

Applicable Models: All (Read-Write) Specifies the polarity expected by the
external trigger input circuitry. Also specify
[TRIG:TYPE](Trigger_SCPI.md#type) (Level |Edge). See [Triggering the VNA
using SCPI](../GPIB_Example_Programs/Triggering_the_PNA_using_SCPI.htm).  
---  
Parameters |   
<char> | Choose from:

  * POSitive (rising Edge) or High Level
  * NEGative (falling Edge) or Low Level

  
Examples | TRIG:SLOP NEG  
trigger:sequence:slope positive  
Query Syntax | TRIGger[:SEQuence]:SLOPe?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | POSitive  
  
* * *

## TRIGger[:SEQuence]:SOURce <char>

Applicable Models: All (Read-Write) Sets the source of the sweep trigger
signal. This command is a super-set of
[INITiate:CONTinuous](Initiate.md#cont) which can NOT set the source to
External. See [Triggering the VNA using
SCPI](../GPIB_Example_Programs/Triggering_the_PNA_using_SCPI.htm).  
---  
Parameters |   
<char> | Choose from:

  * EXTernal - external (rear panel) source.
  * IMMediate \- internal source sends continuous trigger signals
  * MANual \- sends one trigger signal when manually triggered from the front panel or [INIT:IMM](Initiate.md#immed) is sent.

  
Examples | TRIG:SOUR EXT  
trigger:sequence:source immediate  
Query Syntax | TRIGger[:SEQuence]:SOURce?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | IMMediate  
  
* * *

## TRIGger[:SEQuence]:TYPE <char>

Applicable Models: All (Read-Write) Specifies the type of EXTERNAL trigger
input detection used to listen for signals on the Meas Trig IN connectors.
Edge triggers are most commonly used.  
---  
Parameters |   
<char> | Choose from: EDGE VNA responds to the rising and falling edge of a signal. LEVel VNA responds to a level (HIGH or LOW). Use [TRIG:SLOPe](Trigger_SCPI.md#slope) to specify Rising or falling - High or Low.  
Examples | TRIG:TYPE EDGE trigger:sequence:type level  
Query Syntax | TRIGger[:SEQuence]:TYPE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | LEVel  
  
* * *

## TRIGger:STATus:READy? <char>

Applicable Models: All (Read-only) Checks if the VNA is ready for a hardware
trigger. This command is not intended to be used in a dynamic triggering
situation where the ready status is constantly changing. Instead, the expected
use is a more static situation where you are expecting the VNA to transition
from not ready to ready, and then wait for a trigger. The VNA is polled until
it becomes ready and then an operation that triggers the VNA is performed.
Note: This command is only supported on the PNA-L, PNA, and PNA-X with DSP5
installed. Any other model will return an error.  
---  
Parameters |   
<char> | ANY \- Check if the VNA is ready for any of the following hardware triggers. MEAS - Check if the VNA is ready for an External trigger from the Meas Trig In BNC, Handler IO Pin 18, or Pulse 3 line. AUX1 \- Check if the VNA is ready for a trigger from the AUX TRIG 1 IN on the rear panel. (PNA, ENA) AUX2 - Check if the VNA is ready for a trigger from the AUX TRIG 2 IN on the rear panel. (PNA, ENA) MANual - Check if the VNA is ready for manual trigger.  
Examples | TRIG:STAT:READ? MEAS trigger:status:ready? aux1  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ANY  
  
* * *

