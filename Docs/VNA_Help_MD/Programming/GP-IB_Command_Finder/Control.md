# Control Commands

* * *

Specifies the settings to remotely control the rear panel connectors, an
external test set, Calpod modules, and ECal Module state.

CONTrol [AUXiliary - More Commands](ControlAux.md) [CALPod:COMMand](Control.md#Calpod) CHANnel:INTerface:CONTrol | [CONFig:RECall](Control.md#InterfaceRecall) | [[STATe]](Control.md#InterfaceState) ECAL:MODule | PATH | [COUNt?](Control.md#ECalPathCount) | [STATe](Control.md#EcalPathState) | PORT | [CATalog](Control.md#ECalModPortCat) | STATe | [CATalog](Control.md#EcalModPortStatCal) | [[:SELect]](Control.md#EcalModPortStateSel) | [STATe](Control.md#ECALState) [EXTernal:TESTset - More Commands](ControlExt.md) [HANDler - More Commands](ControlHandler.md) [NOISe:SOURce[:STATe]](Control.md#NoiseSourceState) PHASe | COUNt? | MODule | DATA | STORe | MODel? | SERial? | SETup [SIGNal:](Control.md#signal) | TRIGger | [ATBA](Control.md#atba) | [OUTP](Control.md#outp) | AIO | PIN | [COUNt?](Control.md#AppCount) | [FUNCtion](Control.md#AppFunc) | [CATalog?](Control.md#AppFuncCat) | [INPut:LEVel?](Control.md#AppInpLev) | CHANnel |FUNCtion | CATalog | KDMI | MAIN | [COUNt?](Control.md#KdmiMainCoun) | [CHANnl:FUNCion](Control.md#KdmiMainChanFunc) | [FUNCtion](Control.md#KdmiMainFunc) | [CATalog?](Control.md#KdmiMainFuncCat) | [INPut:LEVel?](Control.md#KdimMainInpLev) | LOGic | SUB | [COUNt?](Control.md#KdmiSubCoun) | [CHANnl:FUNCion](Control.md#KdmiSubChanFunc) | [FUNCtion](Control.md#KdmiSubFunc) | [CATalog?](Control.md#KdmiSubFuncCat) | [INPut:LEVel?](Control.md#KdimSubInpLev) | LOGic | PXI | RTRigger | [:STATe] | ROUTe | TRIGger | OUTPut | [:STATe] | ROUTe | STReamline | RTRigger | [:STATe] | ROUTe | TRIGger | OUTPut | [:STATe] | ROUTe  
---  
  
Click on a keyword to view the command details.

Blue command is superseded.

See Also

  * [Example Programs](../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

  * See a pinout and detailed description of the rear panel connectors:

  1.      * [Material Handler IO connector](../HandlerIO_Connector.md)

* * *

## CONTrol:CALPod:COMMand <string>

Applicable Models: N522xB, N523xB, N524xB, M937xA, E5080A/B, E5081A, P937xA,
P50xxA/B, M980xA, M983xA (Write-Read) Sends commands that control a Calpod
module. Reads query versions Calpod commands.  See [ALL Calpod
commands](Calpod.htm). [Learn more about Calpod.](../../S3_Cals/CalPod.md)  
---  
Parameters |   
<string> |  Calpod command. See [ALL Calpod commands](Calpod.md) that can be used in this string.  
Write Example |  CONT:CALP:COMM 'CALP:INIT:ACT' 'Enclose all strings in SINGLE quotes (NOT double quotes)  
Query Syntax |  CONTrol:CALPod:COMMand? <string> Relevant only for query strings.  
Read Example |  CONT:CALP:COMM? '*OPC?' 'returns 0 if the calpod software is currently processing an operation 'returns 1 if operations are complete  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CONTrol:CHANnel:INTerface:CONTrol:CONFig:RECall[:STATe] <string>

Applicable Models: N522xB, N523xB, N524xB, E5080A (Write-only) Recalls an
Interface Control configuration file. [Learn more about Interface
Control.](../../System/Interface_Control.htm)  
---  
Parameters |   
<string> |  File name and extension (.xml) of the configuration file to recall. Files are typically stored in the default folder "D:\". To recall from a different folder, specify the full path name.  
Examples |  CONT:CHAN:INT:CONT:CONF:REC 'MyConfigFile.xml' control:channel:interface:control:config:recall:state 'D:\MyFile.xml'  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CONTrol:CHANnel:INTerface:CONTrol[:STATe] <bool>

Applicable Models: N522xB, N523xB, N524xB, E5080A/B, E5081A (Read-Write)
Enables and disables ALL Interface Control settings. To send data, the
individual interfaces must also be enabled. [Learn more about Interface
Control.](../../System/Interface_Control.htm)  
---  
Parameters |   
<bool> |  Boolean OFF (0) \- Interface Control is disabled;NO control data is sent. ON (1) \- Interface Control is enabled.  
Examples |  CONT:CHAN:INT:CONT 1 control:channel:interface:control:state 0  
Query Syntax |  CONTrol:CHANnel:INTerface:CONTrol[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF (0)  
  
* * *

## CONTrol:ECAL:MODule<num>:PATH:COUNt? <name> Superseded

Applicable Models: All This command is replaced with
CONTrol:ECAL:MODule:PORT:CATalog? (Read-only) Returns the number of unique
states that exist for the specified path name on the selected ECal module.
This command performs exactly the same function as
[SENS:CORR:CKIT:ECAL:PATH:COUNt?](Sense/CorrCKIT_SCPI.md#ECalPathCount) Use
the [CONT:ECAL:MOD:PATH:STAT](Control.md#EcalPathState) command to set the
module into one of those states.  Use
[SENS:CORR:CKIT:ECAL:PATH:DATA?](Sense/CorrCKIT_SCPI.md#EcalPathData) to read
the data for a state.  
---  
Parameters |   
[num] |  Optional argument. USB number of the ECal module. If unspecified (only one ECal module is connected to the USB), <num> is set to 1. If two or more modules are connected, use [SENS:CORR:CKIT:ECAL:LIST?](Sense/CorrCKIT_SCPI.md#List) to determine how many, and [SENS:CORR:CKIT:ECAL:INF?](Sense/CorrCKIT_SCPI.md#ECALInf) to verify their identities.  
<name> |  Name of the path for which to read number of states. Choose from: Reflection paths

  * A
  * B
  * C (4-port modules)
  * D (4-port modules)

Transmission paths

  * AB
  * AC (4-port modules)
  * AD (4-port modules)
  * BC (4-port modules)
  * BD (4-port modules)
  * CD (4-port modules)

Note: For each transmission path, the first of the available states is the
through state, the second is the confidence (attenuator) state.  
Examples |  CONT:ECAL:MOD:PATH:COUNt? A control:ecal:module2:path:count? cd [See example program](../GPIB_Example_Programs/Set_ECal_States.md)  
Return Type |  Integer  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CONTrol:ECAL:MODule<num>:PATH:STATe <path>, <stateNum> Superseded

Applicable Models: All This command is replaced with
[CONTrol:ECAL:MODule:PORT:STATe[:SELect]](Control.md#EcalModPortStateSel)
(Write-only) Sets the internal state of the selected ECAL module. This command
supersedes [CONT:ECAL:MOD:STAT](Control.md#ECALState).

  * Use [CONT:ECAL:MOD:PATH:COUN?](Control.md#ECalPathCount) to read the number of unique states that exist for the specified path name on the module.
  * Use [SENS:CORR:CKIT:ECAL:PATH:DATA?](Sense/CorrCKIT_SCPI.md#EcalPathData) to read the data for a state (from the module memory) corresponding to the stimulus values of a channel.

  
---  
Parameters |   
[num] |  Optional argument. USB number of the ECal module. If unspecified (only one ECal module is connected to the USB), <num> is set to 1. If two or more modules are connected, use [SENS:CORR:CKIT:ECAL:LIST?](Sense/CorrCKIT_SCPI.md#List) to determine how many, and [SENS:CORR:CKIT:ECAL:INF?](Sense/CorrCKIT_SCPI.md#ECALInf) to verify their identities.  
<path> |  Path name for which to set a state.  Note: The impedance paths are not independent. For example, changing the impedance presented on path A will cause a change to the impedance on path B. Choose from: Reflection paths

  * A
  * B
  * C (4-port modules)
  * D (4-port modules)

Transmission paths

  * AB
  * AC (4-port modules)
  * AD (4-port modules)
  * BC (4-port modules)
  * BD (4-port modules)
  * CD (4-port modules)

  
<stateNum> |  Number of the state to set. Refer to the following table to associate the <stateNum> with a state in your ECal module. In addition, [CONT:ECAL:MOD:PATH:COUNt?](Control.md#ECalPathCount) returns the number of states in the specified ECal module. |  <stateNum> |  N4432x and  
N4433x States |  N4431x States |  N469x and N755x States** |  8509x States  
---|---|---|---|---  
One-Port Reflection States  
1 |  Open |  Open |  Impedance 1 |  Open  
2 |  Short |  Short |  Impedance 2 |  Short  
3 |  Impedance 1 |  Impedance 1 |  Impedance 3 |  Impedance 1  
4 |  Impedance 2 |  Impedance 2 |  Impedance 4 |  Impedance 2  
5 |  |  |  Impedance 5 |   
6 |  |  |  Impedance 6 |   
7 |  |  |  Impedance 7 |   
Two-Port Transmission States  
1 |  Thru |  Thru |  Thru |  Thru  
2 |  Confidence |  Confidence |  Confidence |  Confidence  
  
** The following modules have only FOUR Impedance states (1, 2, 3, 4): N4690B
,N4691B ,N4692A ,N4696B, N7550A - N7556A.  
  
Examples |  CONT:ECAL:MOD:PATH:STATe A,5 control:ecal:module2:state BC,1 [See example program](../GPIB_Example_Programs/Set_ECal_States.md)  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CONTrol:ECAL:MODule<num>:PORT:CATalog?

Applicable Models: All (Read-only) Returns the list of port labels on the
selected ECal module.  
---  
Parameters |   
[num] |  Optional argument. USB number of the ECal module. If unspecified (only one ECal module is connected to the USB), <num> is set to 1. If two or more modules are connected, use [SENS:CORR:CKIT:ECAL:LIST?](Sense/CorrCKIT_SCPI.md#List) to determine how many, and [SENS:CORR:CKIT:ECAL:INF?](Sense/CorrCKIT_SCPI.md#ECALInf) to verify their identities.  
Examples |  CONT:ECAL:MOD2:PORT:CAT? > A,B,C,D // 4-port ECal > 1-A,1-B,1-C,1-D,1-E,1-F,2-A,2-B, ,6-E,6-F // 6-module of N756xA (36-port ECal)  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CONTrol:ECAL:MODule<num>:PORT:STATe:CATalog? <type>,<port>

Applicable Models: All (Read-only) Returns  a list of state or port labels for
ECal. The returned values is used for CONTrol:ECAL:MODule:PORT:STATe[:SELect]  
---  
Parameters |   
[num] |  Optional argument. USB number of the ECal module. If unspecified (only one ECal module is connected to the USB), <num> is set to 1. If two or more modules are connected, use [SENS:CORR:CKIT:ECAL:LIST?](Sense/CorrCKIT_SCPI.md#List) to determine how many, and [SENS:CORR:CKIT:ECAL:INF?](Sense/CorrCKIT_SCPI.md#ECALInf) to verify their identities.  
<type> |  Choose from:

  * REFL :Reflection
  * TRAN :Transmission
  * CONF: Confidence

  
<port> |  Port label. Candidates are response of the [CONT:ECAL:MOD:PORT:CAT?](Control.md#ECalModPortCat) command. Response: Depends on the <type> value.

  * If <type> is REFL, This command returns one port state number. (Ex. 1=Open, 2=Short, etc.)
  * If <type> is TRAN or CONF,This command returns candidate port labels that are possible to connect to.

  
Examples |  CONT:ECAL:MOD2:PORT:STAT:CAT? REFL,A > 1,2,3,4 // 4-state ECal module > 1,2,3,4,5,6,7 // 7-state ECal module CONT:ECAL:MOD2:PORT:STAT:CAT? TRAN,A > B,C,D // Port A can be connected to B, C or D CONT:ECAL:MOD128:PORT:STAT:CAT? TRAN,2-A > 1-F,2-B,2-F // N756xA example  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CONTrol:ECAL:MODule<num>:PORT:STATe[:SELect] <type>,<port>,<stateOrPort>

Applicable Models: All (Write-only) Sets the internal state of the ECal
module.  
---  
Parameters |   
[num] |  Optional argument. USB number of the ECal module. If unspecified (only one ECal module is connected to the USB), <num> is set to 1. If two or more modules are connected, use [SENS:CORR:CKIT:ECAL:LIST?](Sense/CorrCKIT_SCPI.md#List) to determine how many, and [SENS:CORR:CKIT:ECAL:INF?](Sense/CorrCKIT_SCPI.md#ECALInf) to verify their identities.  
<type> |  Choose from:

  * REFL :Reflection
  * TRAN :Transmission
  * CONF: Confidence

  
<port> |  Port label. Candidates are response of the [CONT:ECAL:MOD:PORT:CAT?](Control.md#ECalModPortCat) command. Response: Depends on the <type> value.

  * If <type> is REFL, This command returns one port state number. (Ex. 1=Open, 2=Short, etc.)
  * If <type> is TRAN or CONF,This command returns candidate port labels that are possible to connect to.

  
<stateOrPort> |  State or port label. The [CONT:ECAL:MOD:PORT:STAT:CAT?](Control.md#EcalModPortStatCal) command returns possible parameter.  
Examples |  CONT:ECAL:MOD2:PORT:STAT:SEL REFL,A,2 CONT:ECAL:MOD128:PORT:STAT:SEL REFL,1-C,6 CONT:ECAL:MOD2:PORT:STAT:SEL TRAN,A,C CONT:ECAL:MOD128:PORT:STAT:SEL TRAN,2-A,1-F  
Return Type |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CONTrol:ECAL:MODule<num>:STATe <value> Superseded

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA This command is
replaced with [CONT:ECAL:MOD:PATH:STATe.](Control.md#EcalPathState) (Write-
only) Sets the internal state of the selected ECAL module.  
---  
Parameters |   
[num] |  Optional argument. USB number of the ECal module. If unspecified (only one ECal module is connected to the USB), <num> is set to 1. If two or more modules are connected, use [SENS:CORR:COLL:CKIT:INF?](Sense/CorrCollCKIT.md#Inf) to verify their identity.  
<value> |  Integer code for switching the module. The following are codes for Keysight ECal modules. |  8509x Modules  
---  
State |  Port A |  Port B  
Open |  0 |  0  
Short |  43 |  43  
Load |  33 |  33  
Mismatch |  4 |  16  
Thru |  84  
Confidence |  20  
  
N469xA/B and N755x Modules (See also, N469xD Modules)  
---  
State |  Port A |  Port B  
Open |  36 |  33  
Short |  39 |  45  
Load |  37 |  37  
Mismatch  
(Offset short) |  53 |  53  
Impedance 5  
(Offset open) |  5 |  5  
Impedance 6  
(Offset short) |  21 |  21  
Impedance 7  
(Offset short) |  38 |  41  
Thru |  42  
Confidence |  40  
N469xD Modules (See also, N469xA/B and N755x Modules)  
---  
State |  Port A |  Port B  
Open |  9 |  3  
Short |  15 |  27  
Load |  11 |  11  
Mismatch  
(Offset short) |  43 |  43  
Impedance 5  
(Offset open) |  10 |  10  
Impedance 6  
(Offset short) |  42 |  42  
Impedance 7  
(Offset short) |  13 |  19  
Thru |  21  
Confidence |  17  
  
N4431A Modules  
---  
State |  Port A |  Port B |  Port C |  Port D  
Open |  -1398 |  -1384 |  -2774 |  -2654  
Short |  -1350 |  -1381 |  -2582 |  -2642  
Load |  26985 |  -26986 |  -26986 |  26985  
Mismatch |  -26986 |  26985 |  26985 |  -26986  
Path |  Thru |  Confidence  
---|---|---  
AB Path |  -2590 |  -598  
AC Path |  -4011 |  85  
AD Path |  -2517 |  16042  
BC Path |  -1650 |  -598  
BD Path |  -4011 |  85  
CD Path |  -1352 |  16042  
  
N4432A and N4433A Modules  
---  
State |  Port A |  Port B |  Port C |  Port D  
Open |  -6971 |  -11835 |  -14895 |  -14876  
Short |  -14395 |  -12859 |  -14899 |  -14905  
Load |  -14907 |  -14907 |  -14907 |  -14907  
Offset Short |  -9787 |  -6459 |  -14874 |  -14887  
Path |  Thru |  Confidence  
---|---|---  
AB Path |  13765 |  30069  
AC Path |  -10519 |  -2327  
AD Path |  -10538 |  -2346  
BC Path |  -5655 |  -1559  
BD Path |  -5674 |  -1578  
CD Path |  -15051 |  30069  
Examples |  CONT:ECAL:MOD:STAT 36  
control:ecal:module2:state 38  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CONTrol:MULTiplexer<id>:OUTPut:<grp>[:DATA] <num>

Applicable Models: E5080A/B, E5081A

(Read-Write) Sets or returns the output port data for specified group with id
of the E5092A multiport test set. Notes: This command is available only for
E5092A multiport test set.  
---  
Parameters |   
<id> |  Id of the multiport test set either 1 or 2. If unspecified, Id is assumed to be 1.  
<grp> |  A | B | C | D  
<num> |  An integer specifying the decimal value of the control line. Values are obtained by adding weights from the following table that correspond to individual lines. The output port data range is between 0 to 255 (0=All line are turns OFF and 255 all lines are turn ON). |  Line |  Weight  
---|---  
1 |  1  
2 |  2  
3 |  4  
4 |  8  
5 |  16  
6 |  32  
7 |  64  
8 |  128  
Examples |  CONT:MULT1:OUTP:B 8  
Query Syntax |  CONTrol:MULTiplexer<id>:OUTPut:<grp>[:DATa]?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0  
  
* * *

## CONTrol:MULTiplexer<id>:OUTPut:<grp>VOLTage[:DATA] <volt>

Applicable Models: E5080A/B, E5081A

(Read-Write) Sets or returns the output voltage for specified group with id of
the E5092A multiport test set. Notes: This command is available only for
E5092A multiport test set.  
---  
Parameters |   
<id> |  Id of the multiport test set either 1 or 2. If unspecified, Id is assumed to be 1.  
<grp> |  A | B | C | D  
<volt> |  Output voltage range for <grp> is between 0 to 5.2V and resolution is 10mV.  
Examples |  CONT:MULT1:OUTP:B:VOLT 4.2  
Query Syntax |  CONTrol:MULTiplexer<id>:OUTPut:<grp>:VOLtage[:DATa]?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0 V  
  
## CONTrol:NOISe:SOURce[:STATe] <bool>

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Set and read the noise
source [(28V)](../../Rear_Panel/XRtour.md#28) ON and OFF.  
---  
Parameters |   
<bool> |  Boolean OFF (0) \- Noise Source OFF ON (1) \- Noise Source ON  
Examples |  CONT:NOIS:SOUR 1 control:noise:source:state 0  
Query Syntax |  CONTrol:NOISe:SOURce[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  For VNA models with a [Noise Figure option](../../Applications/Noise_Figure.md#OptionsExplained) (028/029/H29), the 28V line is ON at application start and after a preset. The ON/OFF state is also available from a VNA softkey menu. For VNA models WITHOUT a Noise Figure option (028/029/H29), the 28V line is OFF at application start and its state is not affected by a preset. The ON/OFF state is NOT available from a VNA softkey menu.  
  
* * *

## CONTrol:PHASe:COUNt?

Applicable Models: All (Read only) Reads the number of phase reference modules
connected.  
---  
Parameters |  None  
Examples |  CONT:PHAS:COUN? control:phase:count?  
Return Type |  Numeric value  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## CONTrol:PHASe:MODule[x]:DATA:STORe <path>

Applicable Models:  All (Write-only) Reads the calibration data from the phase
reference of the specified module (x), and writes the data to the Path  
---  
Parameters |   
<path> |  (String) Directory path to stored data.  
Examples |  CONT:PHAS:MOD1:DATA:STOR "D:MyPhaseRefCalData.csv" control:phase:module1:data:store "D:MyPhaseRefCalData.csv"  
Return Type |  N/A  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## CONTrol:PHASe:MODule[x]:MODel?

Applicable Models:  All (Read only) Reads the model number of the specified
module (x).  
---  
Parameters |  None  
Examples |  CONT:PHAS:MOD1:MOD? control:phase:module1:model?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## CONTrol:PHASe:MODule[x]:SERial?

Applicable Models:  All (Read only) Reads the serial number of the specified
module (x).  
---  
Parameters |   
Examples |  CONT:PHAS:MOD1:SER? control:phase:module1:serial?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## CONTrol:PHASe:MODule[x]:SETup <divideNumber>

Applicable Models: All

(Write-only) Turns on the phase reference, and sets the divide number.  
---  
Parameters |   
<divideNumber> |  Divide number can be 1, 2, 4, 8, 16.  
Examples |  CONT:PHAS:MOD1:SET 2 control:phase:module1:setup 2  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## CONTrol:SIGNal <conn>,<char>

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Configures external
triggering in the VNA.  Note: To configure external triggering in the current
VNA models, use the [Trigger](Trigger_SCPI.md) commands.

  * To control BNC1 and BNC2 with this command, then you MUST have [TRIG:PREF:AIGLobal = ON](Trigger_SCPI.md#PrefGlobal). [Learn more](../../S1_Settings/External_Triggering.md#Output)
  * [Trigger:Sequence:Source](Trigger_SCPI.md#tss) is automatically set to External when CONTrol:SIGNal is sent.
  * Edge triggering is only available on some Microwave VNA models. 
  * For more information, see [External Triggering](../../S1_Settings/External_Triggering.md#Edge) in the VNA.

  
---  
Parameters |   
<conn> |  Rear Panel connector to send or receive trigger signals. Choose from: BNC1 Trigger IN from rear-panel Trigger IN BNC connector Note: Only one of the input connectors is active at a time. When a command is sent to one, the VNA automatically makes the other INACTIVE. BNC2 Trigger OUT to rear-panel Trigger OUT BNC connector. MATHtrigger \- Trigger IN from rear-panel [Material Handler connector Pin 18](../HandlerIO_Connector.md) RDY \- Ready for trigger OUT.

  * PNA-X: [Meas Trig RDY](../../Rear_Panel/XRtour.md#ExternalTrig)
  * PNA-L: [Handler I/O p21](../HandlerIO_Connector.md#ReadyForTrigger) ([Some models](../HandlerIO_Connector.md#PinAssignments))

  
<char> |  INACTIVE - Disables the specified connector <conn>. Choose from ONLY the following when <conn> is set to BNC1 or AUXT or MATHtrigger:

  * TIENEGATIVE \- (Trigger In Edge Negative) - Triggers the VNA when receiving a negative going signal
  * TIEPOSITIVE \- (Trigger In Edge Positive) - Triggers the VNA when receiving a positive going signal
  * TILLOW \- (Trigger In Level Low) - Triggers the VNA when receiving a low level signal
  * TILHIGH \- (Trigger In Level High) - Triggers the VNA when receiving a High-level signal

Choose from ONLY the following when <conn> is set to BNC2: Use
CONTrol:SIGNal:TRIGger:OUTP to enable the BNC2 output. The following
selections send a positive or negative pulse before or after each trigger
acquisition. This normally occurs each sweep unless a channel is in [point
trigger](../../S1_Settings/Trigger.htm#state_point) mode.

  * TOPPAFTER \- (Trigger Out Pulse Positive After) - Sends a POSITIVE going TTL pulse at the END of each trigger acquisition.
  * TOPPBEFORE \- (Trigger Out Pulse Positive Before) - Sends a POSITIVE going TTL pulse at the START of each trigger acquisition.
  * TOPNAFTER \- (Trigger Out Pulse Negative After) - Sends a NEGATIVE going TTL pulse at the END of each trigger acquisition.
  * TOPNBEFORE \- (Trigger Out Pulse Negative Before) - Sends a NEGATIVE going TTL pulse at the START of each trigger acquisition.

Choose from ONLY the following when <conn> is set to RDY:

  * LOW Outputs a TTL low when the VNA is ready for trigger. (Default setting)
  * HIGH Outputs a TTL high when the VNA is ready for trigger.

  
Examples |  CONT:SIGN BNC1,TIENEGATIVE  
control:signal bnc2,toppbefore CONT:SIGN RDY,LOW  
Query Syntax |  CONTrol:SIGNal? <conn> In addition to the arguments listed above, the following is also a possible returned value: NAVAILABLE \- This feature is not available on this VNA  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  At Preset: BNC1 = INACTIVE  
BNC2 = INACTIVE  
AUXT = TILHIGH When Output is enabled: BNC1 = INACTIVE  
BNC2 = TOPPAFTER  
AUXT = TILHIGH  
  
* * *

## CONTrol:SIGNal:TRIGger:ATBA <bool>

Applicable Models: N522xB, N523xB, N524xB. M980xA, P50xxA/B, P93xxB, E5080B,
E5081A (Read-Write) Accept Trigger Before Armed Determines what happens to an
EDGE trigger signal if it occurs before the VNA is ready to be triggered.
(LEVEL trigger signals are always ignored.) For more information, see
[External triggering.](../../S1_Settings/External_Triggering.md)  
---  
Parameters |   
<bool> |  Boolean OFF (0) - A trigger signal is ignored if it occurs before the VNA is ready to be triggered. ON (1) - A trigger signal is remembered and then used when the VNA becomes armed (ready to be triggered). The VNA remembers only one trigger signal.  
Examples |  CONT:SIGN:TRIG:ATBA 0  
control:signal:trigger:atba ON  
Query Syntax |  CONTrol:SIGNal:TRIGger:ATBA?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## CONTrol:SIGNal:TRIGger:OUTP <bool>

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Output Enabled The VNA
can be enabled to send trigger signals out the rear-panel TRIGGER OUT BNC
connector. Use CONTrol:SIGNal to configure for output triggers.  Note: To
configure external triggering in the current VNA models, use the
[Trigger](Trigger_SCPI.md) commands. For more information, see [External
triggering.](../../S1_Settings/External_Triggering.htm#ExternalDiag)  
---  
Parameters |   
<bool> |  Boolean OFF (0) - VNA does NOT output trigger signals. ON (1) - VNA DOES output trigger signals.  
Examples |  CONT:SIGN:TRIG:OUTP 1 control:signal:trigger:outp OFF  
Query Syntax |  CONTrol:SIGNal:TRIGger:OUTP?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## CONTrol:SIGNal:AIO:PIN:COUNt?

Applicable Models: E5080B, E5081A (Read only) Read the total number of pin on
the application I/O. In case for the E5080B, always 15. For more information,
see application I/O.  
---  
Parameters |  None  
Examples |  CONT:SIGN:AIO:PIN:COUN? control:signal:aio:pin:count?  
Query Syntax |  CONTrol:SIGNal:AIO:PIN:COUNt?  
Return Type |  Numeric value  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  15  
  
* * *

## CONTrol:SIGNal:AIO:PIN<pin>:FUNCtion <func>

Applicable Models: E5080B, E5081A (Write-Read) Set and Read the function for
the specified port in the application I/O interface. The assigned settings are
not saved in a state file, but the setting is stored when changing function
and recall them at the next firmware start up.  
---  
Parameters |   
<pin> |  Pin Number.  
<func> |  function name |  Function name |  Description |  Type |  Assignable pot number |  Default Assignment  
---|---|---|---|---  
PULSE_OUT1 |  1st pulse output |  Output |  10 |  10  
PULSE_OUT2 |  2nd pulse output |  Output |  11 |  11  
PULSE_OUT3 |  3rd pulse output |  Output |  12 |  12  
PULSE_OUT4 |  4th pulse output |  Output |  13 |  13  
RF_PULSE_MOD_IN |  RF pulse modulation |  Input |  8 |  8  
PULSE_SYNC_IN |  Pulse generator synchronization trigger input |  INPUT |  7 |  7  
AUX TRIG IN |  AUX trigger input |  INPUT |  7 |  N/A  
INPUT |  Arbitrary input (CONT:SIGN:APPL:INP:LEV? to query the level on the assigned port) |  Input |  1 to 5, 10 to 13 |  N/A  
LOW |  Set the Low (Output Low level) at the assigned port. |  Output |  1 to 5, 10 to 13 |  1 to 5  
HIGH |  Set the High (Output High level) at the assigned port |  Output |  1 to 5, 10 to 13 |  N/A  
NF_SOURCEx (x=1,2,...) *1 |  Noise Figure source switch control for port x |  Output |  1 to 5, 10 to 13 |  N/A  
NF_RECEIVERx (x=1,2,...) *1 |  Noise Figure receiver switch control for port x |  Output |  1 to 5, 10 to 13 |  N/A  
DCV_ON |  +12V power output enable |  Output |  14 |  N/A  
DCV_OFF |  +12V power output disable |  Output |  14 |  14  
CHANNEL_CTRL |  Function is controlled per channel by :CONTrol:SIGNal:AIO:PIN<pin>:CHANnel<ch>:FUNCtion |  |  1 to 5, 10 to 13 |  N/A  
  
*1) For Noise Figure switch control, the signal is asserted no matter which pins are used in the NF channel if the port index(x) is not specified.  
  
Examples |  CONT:SIGN:AIO:PIN:FUNC "LOW" control:signal:aio5:pin:function "NF_SOURCE15"  
Query Syntax |  CONTrol:SIGNal:AIO:PIN:FUNC?  
Return Type |  <sting>  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  See the table in <func>  
  
* * *

## CONTrol:SIGNal:AIO:PIN<pin>:FUNCtion:CATalog?

Applicable Models: E5080B, E5081A (Read Only) Read the list of the available
function for the specified pin in the application I/O. Example,
"RF_PULSE_MOD_IN" is returned for the pin 8.  
---  
Parameters |   
<pin> |  Pin Number.  
Examples |  CONT:SIGN:AIO:PIN3:FUNC:CAT? control:signal:aio:pin3:function:catalog?  
Query Syntax |  CONTrol:SIGNal:AIO:PIN:FUNC:CAT?  
Return Type |  <sting>, available function list with Comma separated chars  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  See the table in <func> of CONTrol:SIGNal:APPLication:FUNC?  
  
* * *

## :CONTrol:SIGNal:AIO:PIN<pin>:CHANnel<ch>:FUNCtion <func>

Applicable Models: E5080B, E5081A (Write-Read) Set and read the function for
the selected pin on the Application I/O connector. It is set on channel basis
and reflected only when CHANNEL_CTRL is selected in
[:CONTrol:SIGNal:AIO:PIN<pin>:FUNCtion <func>](Control.md#AppFunc) for the
specified pin. The setting is saved in the state file and subject to preset.
Function can be selected from Output signals  
---  
Parameters |   
<pin> |  Pin Number 1-5, 10-13  
<ch> |  Channel number  
Examples |  :CONT:SIGN:AIO:PIN3:CHAN1:FUNC? :CONT:SIGN:AIO:PIN3:CHAN1:FUNC HIGH  
Query Syntax |  CONTrol:SIGNal:AIO:PIN:CHAN:FUNC?  
Return Type |  <char>  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  HIGH  
  
* * *

## :CONTrol:SIGNal:AIO:PIN<pin>:CHANnel<ch>:FUNCtion:CATalog

Applicable Models: E5080B, E5081A (Read Only) Read the catalog of the
functions assignable to the pin on the Application I/O connector.  
---  
Parameters |   
<pin> |  Pin Number 1-5, 10-13  
Examples |  :CONT:SIGN:AIO:PIN5:CHAN1:FUNC:CAT? control:signal:aio:pin5:channel:function:catalog?  
Query Syntax |  CONTrol:SIGNal:AIO:PIN:CHAN:FUNC:CAT?  
Return Type |  Comma separated chars  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  NA  
  
* * *

## CONTrol:SIGNal:AIO:PIN<pin>:INPut:LEVel?

Applicable Models:  E5080B, E5081A (Read only) Read the level of the specified
INPUT pin of the application I/O. This command reads the level immediately
after its execution. It is not necessary to assign the pin as INPUT by
command. When the specified pin number is 6 to 9 or 14, "Specified Application
IO port is not input port." error is returned.  
---  
Parameters |   
<pin> |  Pin Number. (E5080B: 1 to 5, 10 to 13)  
Examples |  CONT:SIGN:AIO:PIN:INP2:LEV? control:signal:aio:pin:input1:level?  
Query Syntax |  CONTrol:SIGNal:AIO:PIN:INPut:LEVel?  
Return Type |  Char ("HIGH" or "LOW")  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## CONTrol:SIGNal:KDMI:MAIN:COUNt?

Applicable Models: M980xA, M983xA,P50xxA/B, P93xxB (Read only) Read the number
of ports in the main control port of the I/O connector interface. In case for
the M980xA/P50xxA, always 6.  For more information, see I/O Connector
Interface (M980xA/P50xxA)  
---  
Parameters |  None  
Examples |  CONT:SIGN:KDMI:MAIN:COUN? control:signal:kdmi:main:count?  
Query Syntax |  CONTrol:SIGNal:KDMI:MAIN:COUNt?  
Return Type |  Numeric value  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  6.  
  
* * *

## CONTrol:SIGNal:KDMI:MAIN<port>:CHANnel<ch>:FUNCtion <func>

Applicable Models: M980xA, M983xA,P50xxA/B, P93xxB (Write-Read) Set and Read
the function for the specified port and channel in the main of the I/O adapter
interface. To use this, set
[CONTrol:SIGNal:KDMI:MAIN:FUNCion](Control.md#KdmiMainFunc) at CHANNEL_CTRL.
The setting is saved in the state file and subject to preset. Function can be
selected from Output signal.  
---  
Parameters |   
<port> |  Port Number. The number of total ports is returned by [CONTrol:SIGNal:KDMI:MAIN:COUNt?.](Control.md#KdmiMainCoun)  
<func> |  function name |  Function name |  Description |  Type |  Assignable pot number  
---|---|---|---  
PULSE_OUT1 |  1st pulse output |  Output |  1  
PULSE_OUT2 |  2nd pulse output |  Output |  2  
PULSE_OUT3 |  3rd pulse output |  Output |  3  
PULSE_OUT4 |  4th pulse output |  Output |  4  
LOW |  Set the Low (Output Low level) at the assigned port. |  Output |  1, 2, 3 or 4  
HIGH |  Set the High (Output High level) at the assigned port |  Output |  1, 2, 3 or 4  
NF_SOURCEx (x=1,2,...) *1 |  Noise Figure source switch control for port x |  Ouptpu |  1, 2, 3 or 4  
NF_RECEIVERx (x=1,2,...) *1 |  Noise Figure receiver switch control for port x |  Output |  1, 2, 3 or 4  
NF_LOy (y=1,2, ) |  Noise Figure LO switch control for module y |  Output |  1, 2, 3 or 4  
  
*1) For Noise Figure switch control, the signal is asserted no matter which ports are used in the NF channel if the port/module index(x) is not specified.  
  
Examples |  CONTrol:SIGNal:KDMI:MAIN1:FUNCion "CHANNEL_CTRL" CONT:SIGN:KDMI:MAIN1:CHAN1:FUNC "LOW" CONTrol:SIGNal:KDMI:main2:FUNCion "CHANNEL_CTRL" control:signal:kdmi:main2:channel2:function "NF_LO1"  
Query Syntax |  CONTrol:SIGNal:KDMI:MAIN:CHAN:FUNC?  
Return Type |  <sting>  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  HIGH  
  
* * *

## CONTrol:SIGNal:KDMI:MAIN<port>:FUNCtion <func>

Applicable Models: M980xA, M983xA,P50xxA/B, P93xxB (Write-Read) Set and Read
the function for the specified port in the main c of the I/O adapter
interface. The assigned settings are preserved for each system configuration
even after preset, firmware restart and power on/off. The
[CONTrol:SIGNal:KDMI:MAIN:CHANnel:FUNCion](Control.md#KdmiMainChanFunc)
allows you to set the function independently for each channel.  For more
information, see I/O Connector Interface  
---  
Parameters |   
<port> |  Port Number. The number of total ports is returned by [CONTrol:SIGNal:KDMI:MAIN:COUNt?.](Control.md#KdmiMainCoun)  
<func> |  function name |  Function name |  Description |  Type |  Assignable pot number  
---|---|---|---  
PULSE_OUT1 |  1st pulse output |  Output |  1  
PULSE_OUT2 |  2nd pulse output |  Output |  2  
PULSE_OUT3 |  3rd pulse output |  Output |  3  
PULSE_OUT4 |  4th pulse output |  Output |  4  
RF_PULSE_MOD_IN |  RF pulse modulation |  Input |  5 (Factory default)  
INPUT |  Arbitrary input ([CONTl:SIGN:KDMI:MAIN:INP:LEV?](Control.md#KdimMainInpLev) to query the level on the assigned port) |  Input |  3 (Factory default), 4 (Factory default), 6 (Factory default)  
LOW |  Set the Low (Output Low level) at the assigned port. |  Output |  1, 2, 3 or 4  
HIGH |  Set the High (Output High level) at the assigned port |  Output |  1 (Factory default), 2 (Factory default) , 3 or 4  
CHANNEL_CTRL |  Function is controlled per channel. Define the function by :CONTrol:SIGNal:KDMI:MAIN:CHANnel:FUNCtion |  N/A |  1, 2, 3 or 4  
NF_SOURCEx (x=1,2,...) *1 |  Noise Figure source switch control for port x |  Ouptpu |  1, 2, 3 or 4  
NF_RECEIVERx (x=1,2,...) *1 |  Noise Figure receiver switch control for port x |  Output |  1, 2, 3 or 4  
NF_LOy (y=1,2, ) |  Noise Figure LO switch control for module y |  Output |  1, 2, 3 or 4  
  
*1) For Noise Figure switch control, the signal is asserted no matter which ports are used in the NF channel if the port/module index(x) is not specified.  
  
Examples |  CONT:SIGN:KDMI:MAIN1:FUNC "LOW" control:signal:kdmi:main2:function "NF_LO1"  
Query Syntax |  CONTrol:SIGNal:KDMI:MAIN:FUNC?  
Return Type |  <sting>  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  See the table in <func>  
  
* * *

## CONTrol:SIGNal:KDMI:MAIN<port>:FUNCtion:CATalog?

Applicable Models: M980xA, M983xA,P50xxA/B, P93xxB (Read Only) Read the list
of the available function for the specified port in the main control of the
I/O adapter interface. Example, "RF_PULSE_MOD_IN, INPUT1" is returned for the
port 5.  For more information, see I/O Connector Interface  
---  
Parameters |   
<port> |  Port Number. The number of total ports is returned by [CONTrol:SIGNal:KDMI:MAIN:COUNt?](Control.md#KdmiMainCoun).  
Examples |  CONT:SIGN:KDMI:MAIN:FUNC:CAT? control:signal:kdmi:main:function:catalog?  
Query Syntax |  CONTrol:SIGNal:KDMI:MAIN:FUNC:CAT?  
Return Type |  <sting>, available function list with Comma separated chars  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  See the table in <func> of [CONTrol:SIGNal:KDMI:MAIN:FUNC?](Control.md#KdmiMainFunc)  
  
* * *

## CONTrol:SIGNal:KDMI:MAIN<port>:INPut:LEVel?

Applicable Models: M980xA, M983xA, P50xxA/B, P93xxB (Read only) Read the level
of the specified INPUT port of the I/O adapter main side. This command reads
the level immediately after its execution. It is not necessary to assign the
port as INPUT by CONTrol:SIGNal:KDMI:MAIN:FUNCion command. When the specified
port is not input port, "Specified KDMI port is not input port" error is
returned.  For more information, see I/O Connector Interface  
---  
Parameters |   
<port> |  Port Number (3 to 6)  
Examples |  CONT:SIGN:KDMI:MAIN3:INP:LEV? control:signal:kdmi:main3:input:level?  
Query Syntax |  CONTrol:SIGNal:KDMI:MAIN:INPut:LEVel?  
Return Type |  Char ("HIGH" or "LOW")  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## CONTrol:SIGNal:KDMI:SUB:COUNt?

Applicable Models: M980xA, M983xA,P50xxA/B, P93xxB (Read only) Read the number
of ports in the sub control of the I/O adapter interface. In case for the
M980xA/P50xxA, always 6.  For more information, see I/O Connector Interface  
---  
Parameters |  None  
Examples |  CONT:SIGN:KDMI:SUB:COUN? control:signal:kdmi:sub:count?  
Query Syntax |  CONTrol:SIGNal:KDMI:SUB:COUNt?  
Return Type |  Numeric value  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  6  
  
* * *

## CONTrol:SIGNal:KDMI:SUB<port>:CHANnel<ch>:FUNCtion <func>

Applicable Models: M980xA, M983xA,P50xxA/B, P93xxB (Write-Read) Set and Read
the function for the specified port and specified channel in the sub control
port of the I/O adapter interface. To use this, set
[CONTrol:SIGNal:KDMI:SUB:FUNCion](Control.md#KdmiSubFunc) at CHANNEL_CTRL.
The setting is saved in th state file and subject to preset. Function can be
selected from Output signal.  
---  
Parameters |   
<port> |  Port Number. The number of total ports is returned by [CONTrol:SIGNal:KDMI:SUB:COUNt?](Control.md#KdmiSubCoun).  
<ch> |  Channel Number.  
<func> |  function name |  Function name |  Description |  Type |  Assignable pot number  
---|---|---|---  
READY_FOR_TRIGGER |  Ready for trigger |  Output |  3  
TRIGGER_OUT |  AUX trigger |  Output |  4  
INDEX |  index |  Output |  5  
SWEEP_END |  Sweep end |  Output |  6  
LOW |  Set the Low at the assigned port |  Output |  3, 4, 5 or 6  
HIGH |  Set the High at the assigned port |  Output |  3, 4, 5 or 6  
NF_RECEIVERx (x=1,2,...) *1 |  Noise Figure receiver switch control for port x |  Output |  3, 4, 5 or 6  
NF_LOy (y=1,2, ) |  Noise Figure LO switch control for module y |  Output |  3, 4, 5 or 6  
  
*1) For Noise Figure switch control, the signal is asserted no matter which ports are used in the NF channel if the port/module index(x) is not specified.  
  
Examples |  CONT:SIGN:KDMI:SUB3:FUNC "CHANNEL_CTRL" CONT:SIGN:KDMI:SUB3:CHAN3:FUNC "LOW" CONTrol:SIGNal:KDMI:SUB2:FUNCion "CHANNEL_CTRL" control:signal:kdmi:sub2:chan2:function "INPUT4"  
Query Syntax |  CONTrol:SIGNal:KDMI:SUB:FUNCion?  
Return Type |  <sting>  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  HIGH  
  
* * *

## CONTrol:SIGNal:KDMI:SUB<port>:FUNCtion <func>

Applicable Models: M980xA, M983xA,P50xxA/B, P93xxB (Write-Read) Set and Read
the function for the specified port in the sub control port of the I/O adapter
interface. The assigned settings are preserved for each system configuration
even after preset, firmware restart and power on/off. The
CONTrol:SIGNal:KDMI:SUB:CHANnel:FUNCion allows you to set the function
independently for each channel.  For more information, see I/O Connector
Interface  
---  
Parameters |   
<port> |  Port Number. The number of total ports is returned by [CONTrol:SIGNal:KDMI:SUB:COUNt?](Control.md#KdmiSubCoun).  
<func> |  function name |  Function name |  Description |  Type |  Assignable pot number  
---|---|---|---  
TRIGGER_IN |  External trigger |  Input |  1 (Factory default)  
PULSE_SYNC_IN |  Pulse synchronization |  Input |  2 (Factory default)  
AUX_TRIG_IN |  AUX trigger input |  Input |  2  
READY_FOR_TRIGGER |  Ready for trigger |  Output |  3  
TRIGGER_OUT |  AUX trigger |  Output |  4  
INDEX |  index |  Output |  5  
SWEEP_END |  Sweep end |  Output |  6  
INPUT |  Arbitrary input ([CONTl:SIGN:KDMI:SUB:INP:LEV?](Control.md#KdimSubInpLev) to query the level on the assigned port) |  Input |  3 (Factory default), 4 (Factory default)  
LOW |  Set the Low at the assigned port |  Output |  3, 4, 5 or 6  
HIGH |  Set the High at the assigned port |  Output |  3, 4, 5 (Factory default) or 6 (Factory default)  
CHANNEL_CTRL |  Function is controlled per channel. Define the function by :CONTrol:SIGNal:KDMI:SUB:CHANnel:FUNCtion |  N/A |  3, 4, 5 or 6  
NF_RECEIVERx (x=1,2,...) *1 |  Noise Figure receiver switch control for port x |  Output |  3, 4, 5 or 6  
NF_LOy (y=1,2, ) |  Noise Figure LO switch control for module y |  Output |  3, 4, 5 or 6  
  
*1) For Noise Figure switch control, the signal is asserted no matter which ports are used in the NF channel if the port/module index(x) is not specified.  
  
Examples |  CONT:SIGN:KDMI:SUB3:FUNC "LOW" control:signal:kdmi:sub2:function "INPUT4"  
Query Syntax |  CONTrol:SIGNal:KDMI:SUB:FUNCion?  
Return Type |  <sting>  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  See the table in <func>  
  
* * *

## CONTrol:SIGNal:KDMI:SUB<port>:FUNCtion:CATalog?

Applicable Models: M980xA, M983xA,P50xxA/B, P93xxB (Read Only) Read the list
of the available function for the specified port in the sub control port of
the I/O adapter interface. Example, "TRIGGER_IN, INPUT3" is returned for the
port 1.  For more information, see I/O Connector Interface  
---  
Parameters |   
<port> |  Port Number. The number of total ports is returned by [CONTrol:SIGNal:KDMI:SUB:COUNt?.](Control.md#KdmiSubCoun)  
Examples |  CONT:SIGN:KDMI:SUB:FUNC:CAT? control:signal:kdmi:sub:function:catalog?  
Query Syntax |  CONTrol:SIGNal:KDMI:SUB:FUNC:CAT?  
Return Type |  <sting>, available function list with Comma separated chars  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  See the table in <func> of [CONTrol:SIGNal:KDMI:SUB:FUNC?](Control.md#KdmiSubFunc)  
  
* * *

## CONTrol:SIGNal:KDMI:SUB<port>:INPut:LEVel?

Applicable Models: M980xA, M983xA, P50xxA/B, P93xxB (Read only) Read the level
of the specified INPUT port of the I/O adapter sub side. This command reads
the level immediately after its execution. It is not necessary to assign the
port as INPUT by [CONTrol:SIGNal:KDMI:SUB:FUNCtion](Control.md#KdmiSubFunc)
command. The When the specified port is not input port, "Specified KDMI port
is not input port" error is returned.  For more information, see I/O Connector
Interface  
---  
Parameters |   
<num> |  Port Number (1 to 4)  
Examples |  CONT:SIGN:KDMI:SUB3:INP:LEV? control:signal:kdmi:sub3:input:level?  
Query Syntax |  CONTrol:SIGNal:KDMI:MAIN:INPut:LEVel?  
Return Type |  Char ("HIGH" or "LOW")  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## CONTrol:SIGNal:PXI:RTRigger[:STATe] <bool>

Applicable Models: M980xA, M983xA (Write-Read) Turns ON / OFF Ready for
Trigger output from Backplane Trigger Lines.  
---  
Parameters |   
<bool> |  Choose from:

  * ON (or 1) - VNA DOES output ready for trigger signal from Backplane Trigger line
  * OFF (or 0)  VNA does NOT output ready for trigger signal from Backplane Trigger line.

  
Examples |  CONT:SIGN:PXI:RTR 1 control:signal:pxi:rtrigger:stat off  
Query Syntax |  CONTrol:SIGNal:PXI:RTRigger[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0 (Preset will not reset the setting.)  
  
* * *

## CONTrol:SIGNal:PXI:RTRigger:ROUTe <char>

Applicable Models: M980xA, M983xA (Write-Read) Specifies the Backplane Trigger
Line to use for the trigger OUT ready line.  
---  
Parameters |   
<char> |  Choose from: TRIG0  Backplane Trigger Lines (PXI TRIG0) TRIG1  Backplane Trigger Lines (PXI TRIG1) TRIG2  Backplane Trigger Lines (PXI TRIG2) TRIG3  Backplane Trigger Lines (PXI TRIG3) TRIG4  Backplane Trigger Lines (PXI TRIG4) TRIG5  Backplane Trigger Lines (PXI TRIG5) TRIG6  Backplane Trigger Lines (PXI TRIG6) TRIG7  Backplane Trigger Lines (PXI TRIG7)  
Examples |  CONT:SIGN:PXI:RTR:ROUT TRIG0 control:signal:pxi:rtrigger:route trig0  
Query Syntax |  CONTrol:SIGNal:PXI:RTRigger:ROUTe?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  TRIG1  
  
* * *

## CONTrol:SIGNal:PXI:TRIGger:OUTPut[:STATe] <bool>

Applicable Models: M980xA, M983xA (Write-Read) Turns ON / OFF the trigger
output from PXI Backplane line when CONTrol:SIGNal:TRIGger:OUTP[:STATe] is
ON.  
---  
Parameters |   
<bool> |  ON (or 1) - VNA DOES output trigger signals from PXI Backplane when CONTrol:SIGNal:TRIGger:OUTP[:STATe] is ON. OFF (or 0)  VNA does NOT output trigger signals from PXI Backplane.  
Examples |  CONT:SIGN:PXI:TRIG:OUTP 1 control:signal:pxi:trigger:output:stat off  
Query Syntax |  CONTrol:SIGNal:PXI:TRIGger:OUTPut[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## CONTrol:SIGNal:PXI:TRIGger:OUTPut:ROUTe <char>

Applicable Models: M980xA, M983xA (Write-Read) Specifies the Backplane Trigger
Line to use for the trigger output line.  
---  
Parameters |   
<char> |  Choose from: TRIG0  Backplane Trigger Lines (PXI TRIG0) TRIG1  Backplane Trigger Lines (PXI TRIG1) TRIG2  Backplane Trigger Lines (PXI TRIG2) TRIG3  Backplane Trigger Lines (PXI TRIG3) TRIG4  Backplane Trigger Lines (PXI TRIG4) TRIG5  Backplane Trigger Lines (PXI TRIG5) TRIG6  Backplane Trigger Lines (PXI TRIG6) TRIG7  Backplane Trigger Lines (PXI TRIG7)  
Examples |  CONT:SIGN:PXI:TRIG:OUTP:ROUT TRIG0 control:signal:pxi:trigger:output:route trig0  
Query Syntax |  CONTrol:SIGNal:PXI:TRIGger:OUTPut:ROUTe?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  TRIG2  
  
* * *

## CONTrol:SIGNal:STReamline:RTRigger[:STATe] <bool>

Applicable Models: P50xxA/B, P93xxB (Write-Read) Turns ON / OFF Ready for
Trigger output from Streamline Rear SMB.  
---  
Parameters |   
<bool> |  Choose from:

  * **ON** (or 1) - VNA DOES output ready for trigger signal from Streamline Rear SMB
  * **O FF** (or 0)  VNA does NOT output ready for trigger signal from Streamline Rear SMB

  
Examples |  CONT:SIGN:STR:RTR 1 control:signal:streamline:rtrigger:stat off  
Query Syntax |  CONTrol:SIGNal:STReamline:RTRigger[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0 (Preset will not reset the setting.)  
  
* * *

## CONTrol:SIGNal:STReamline:RTRigger:ROUTe <char>

Applicable Models: P50xxA/B, P93xxB (Write-Read) Specifies the Backplane
Trigger Line to use for the trigger OUT ready line.  
---  
Parameters |   
<char> |  Choose from: NONE  Streamline Rear SMB Not connected (NONE) REAR1  Streamline Rear SMB (TRIG1) REAR2  Streamline Rear SMB (TRIG2)  
Examples |  CONT:SIGN:STR:RTR:ROUT TRIG1 control:signal:streamline:rtrigger:route trig1  
Query Syntax |  CONTrol:SIGNal:STReamline:RTRigger:ROUTe?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## CONTrol:SIGNal:STReamline:TRIGger:OUTPut[:STATe] <bool>

Applicable Models: P50xxA/B, P93xxB  (Write-Read) Turns ON / OFF the trigger
output from Streamline Rear SMB when CONTrol:SIGNal:TRIGger:OUTP[:STATe] is
ON.  
---  
Parameters |   
<bool> |  ON (or 1) - VNA DOES output trigger signals from Streamline Rear SMB when  CONTrol:SIGNal:TRIGger:OUTP[:STATe] is ON. OFF (or 0)  VNA does NOT output trigger signals from Streamline Rear SMB.  
Examples |  CONT:SIGN:STR:TRIG:OUTP 1 control:signal:streamline:trigger:output:stat off  
Query Syntax |  CONTrol:SIGNal:STReamline:TRIGger:OUTPut[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## CONTrol:SIGNal:STReamline:TRIGger:OUTPut:ROUTe <char>

Applicable Models: P50xxA/B, P93xxB (Write-Read) Specifies the Streamline Rear
SMB to use for the trigger output line.  
---  
Parameters |   
<char> |  Choose from: NONE  Streamline Rear SMB Not connected (NONE) REAR1  Streamline Rear SMB (REAR TRIG1) REAR2  Streamline Rear SMB (REAR TRIG2)  
Examples |  CONT:SIGN:STR:TRIG:OUTP:ROUT REAR1 control:signal:streamline:trigger:output:route rear1  
Query Syntax |  CONTrol:SIGNal:STReamline:TRIGger:OUTPut:ROUTe?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  REAR2  
  
* * *

