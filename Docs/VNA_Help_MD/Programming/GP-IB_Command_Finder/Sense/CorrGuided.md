# Sense:Correction:Collect:Guided Commands

* * *

Performs and applies a SmartCal (Guided) calibration and other error
correction features.

Important Notes:

  * To perform a Guided Calibration, use ONLY [Sens:Corr:Coll:Guided](CorrGuided.md) commands. See the ["Guided" example programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md) for clarification.

  * ALWAYS send ALL measurement setup commands BEFORE initializing a remote calibration.

SENSe:CORRection:COLLect:GUIDed: [ABORt](CorrGuided.md#abort) [ACQuire](CorrGuided.md#gAcquire) ADAPter | [COUNt](CorrGuided.md#adaptCount) | [ZERO](CorrGuided.md#adapterCountZero) | [CREate?](CorrGuided.md#adaptCreate) | [DELay](CorrGuided.md#adaptDelay) | [DESCription](CorrGuided.md#adaptDesc) | [PATHs](CorrGuided.md#adaptPaths) [CHANnel:MODE](CorrGuided.md#ChanMode) CKIT | [CATalog?](CorrGuided.md#ckitCatConn) | PORT | [CATalog?](CorrGuided.md#gKitCat) | [[SELect]](CorrGuided.md#gKit) CONFig | DESC | LOAD | DESC | SAVE CONNector | [CATalog?](CorrGuided.md#gConnCat) | PORT | [[SELect]](CorrGuided.md#gConSelect) DATA | CATalog? [DESCription](CorrGuided.md#gDesc) DISPlay | [SMITh](CorrGuided.md#DispSmit) | WINDow | [AOFF](CorrGuided.md#DispWindAoff) | [[:STATe]](CorrGuided.md#DispWindStat) DMATch | APPLy | [[IMMediate]](CorrGuided.md#DmatchApply) | [PORTs?](CorrGuided.md#DmatchApplyPorts) | [[INITiate]](CorrGuided.md#DmatchInit) ECal | ACQuire | SELect ETERms | COMPute | [LOAD[:CSET]](CorrGuided.md#EtermLoad) [INITiate](CorrGuided.md#gInit) ISOLation | [AVERage](CorrGuided.md#IsoAvg) | [INCRement](CorrGuided.md#IsoAvg) | [PATHs](CorrGuided.md#IsolPaths) ITERations | [COUNt?](CorrGuided.md#IterCount) | [MINimum?](CorrGuided.md#iterMin) | [RESet](CorrGuided.md#IterReset) LIST | COUNt? | STEP | COUNt? | DESCription? | LABel? | PORTs? | STANdard | LABel? | PORTs? | STYPe? | TPORts? | STYPe? | TPORts? [METHod](CorrGuided.md#gMETHod) [PACQuire](CorrGuided.md#previewAcquire) PATH | [CMEThod](CorrGuided.md#PathCmethod) | [TMEThod](CorrGuided.md#PathTMethod) PCAL | APPLy PORTs? PREFerence | [SLIDingload](CorrGuided.md#PrefSliding) [PSENsor - More commands](CorrCollGuidPSens.md) [SAVE](CorrGuided.md#gSave) | [CSET](CorrGuided.md#SaveCSET) [SMC - More commands](CorrCollGuidSMC.md) STATes[:CATalog? [STEPS?](CorrGuided.md#gSteps) SWEep | CHANnel | [AOFF](CorrGuided.md#SweepAoff) |[ [:STATe]](CorrGuided.md#SweepChan) [THRU](CorrGuided.md#pairs) UNCertainty | CHARacterize | [CABLe[:INITiate]](CorrGuided.md#UncertCableINIT) | [NOISe[:INITiate]](CorrGuided.md#UncertNoiseInit) | [[:ENABle]](CorrGuided.md#UncertEnab) [VMC - More commands](CorrCollGuidVMC.md)  
---  
  
Click on a keyword to view the command details.

Blue keywords are superseded commands.

### See Also

  * [ECal Orientation commands](../../CalTopic.md#OptionalGuided)
  * [Examples](../../GPIB_Example_Programs/SCPI_Example_Programs.md) using these commands.

  * [Calibrating the VNA Using SCPI](../../Learning_about_GPIB/Calibrating_the_Analyzer_Using_SCPI.md)

  * [Learn about Measurement Calibration](../../../S3_Cals/Measurement_Calibration.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:ABORt

Applicable Models: All (Write-only) Aborts the acquiring of a guided
calibration that has been [INITialized](CorrGuided.md#gInit) but has not yet
been concluded using the [SAVE](CorrGuided.md#gSave) command. If at least one
Cal standard has already been measured, and the [Calibration
Window](../../../S3_Cals/Calibration_Wizard.htm#CalWindow) is being displayed,
this command also closes the Calibration Window and re-tiles the other
measurement windows.  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
Examples |  SENS:CORR:COLL:GUID:ABOR  
sense2:correction:collect:guided:abort  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe:<ch>CORRection:COLLect:GUIDed[:ACQuire] STAN<n>[,sync]

Applicable Models: All (Write-only) Initiates the measurement of the specified
calibration standard. Executing this command with an unnecessary standard has
no affect. The measured data is stored and used for subsequent calculations of
error correction coefficients. All standards must be measured before a
calibration can be completed. Any measurement can be repeated until the
SENS:CORR:COLL:GUID:SAVE command is executed. Query the user prompt
description using SENS:CORR:COLL:GUID:DESC? Query the required calibration
steps using SENS:CORR:COLL:GUID:STEP?  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
STAN<n> |  Choose from:STAN1, STAN2, etc. through STANn where n is the number of cal standard connection steps for the calibration. Note: You do not necessarily have to invoke these connection steps in sequential order, but you must issue this command for all of the steps to be able to complete the calibration.  
[sync] |  Optional argument. Choose from: SYNChronous \- blocks SCPI commands during standard measurement (default behavior). ASYNchronous \- does NOT block SCPI commands during standard measurement. [Learn more about this argument](../../Learning_about_GPIB/Understanding_Command_Synchronization.md#Synch)  
Examples |  SENS:CORR:COLL:GUID STAN1  
sense2:correction:collect:guided:acquire stan1  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:ADAPter:CREate? <conn1>, <conn2>

Applicable Models: All (Read-only) Specifies the use of a THRU adapter to be
used during the Guided Cal Unknown THRU and Adapter Removal Cal. Returns an
adapter index <n> which is used to refer to the adapter in several related
commands. [See Cal Thru
Methods.](../../../S3_Cals/Calibration_THRU_Methods.htm) While the choice of
which end of the adapter is <conn1> and <conn2> is arbitrary, it is necessary
to remember which will be used on each test port. The settings for this
command remain until Preset, or the command is sent using a different setting,
or until the [ZERO](CorrGuided.md#adapterCountZero) command is sent.  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<conn1> |  Adapter port 1 connector type. Use SENS:CORR:COLL:GUID:CONN:CAT? to return a list of valid connector types.  
<conn2> |  Adapter port 2 connector type.  
Examples |  [See example using this command.](../../GPIB_Example_Programs/Perform_Guided_2-Port_Comprehensive_Cal.md)  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:ADAPter:COUNt?

Applicable Models: All (Read-Only) Returns the number of THRU adapters that
have been created for this calibration using SENS:CORR:COLL:GUID:ADAP:CREate.  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
Examples |  [See example using this command.](../../GPIB_Example_Programs/Perform_Guided_2-Port_Comprehensive_Cal.md)  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe:<ch>CORRection:COLLect:GUIDed:ADAPter:COUNt:ZERO

Applicable Models: All (Write-only) Removes all adapters that have been
defined for calibrations on the specified channel using
[SENS:CORR:COLL:GUID:ADAP:CREate](CorrGuided.md#adaptCreate).  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
Examples |  SENS:CORR:COLL:GUID:ADAP:COUNt:ZERO  
sense2:correction:collect:guided:adapter:count:zero  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:ADAPter<n>:DELay[:VALue] <coax>,
[<wphase>], [<wdelay>]

Applicable Models: All (Write-only) Specifies the adapter delay. and
optionally waveguide delay and optional phase offset (degrees) of adapter <n>.
The settings for this command remain until Preset, or the command is sent
using a different setting, or until the
[ZERO](CorrGuided.md#adapterCountZero) command is sent.  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<n> |  Adapter index number that was returned from SENS:CORR:COLL:GUID:ADAP:CREate?  
<coax> |  Delay value of coax adapter <n> in seconds. If the adapter has no coax connector, enter 0.  
<wphase> |  Waveguide phase offset in degrees. If the adapter has no waveguide connector, do not enter a value.  
<wdelay> |  Waveguide delay in seconds. If the adapter has no waveguide connector, do not enter a value.  
Examples |  [See example using this command.](../../GPIB_Example_Programs/Perform_Guided_2-Port_Comprehensive_Cal.md)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:ADAPter<n>:DESCription <string>

Applicable Models: All (Write-only) Specifies the adapter description for use
as the guided cal connection prompts. The settings for this command remain
until Preset, or the command is sent using a different setting, or until the
[ZERO](CorrGuided.md#adapterCountZero) command is sent.  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<n> |  Adapter index number that was returned from SENS:CORR:COLL:GUID:ADAP:CREate?  
<string> |  Adapter description.  
Examples |  [See example using this command.](../../GPIB_Example_Programs/Perform_Guided_2-Port_Comprehensive_Cal.md)  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:ADAPter<n>:PATHs <port pairs>

Applicable Models: All (Write-only) Specifies the port pairs for which the
adapter will be used for a THRU connection. For example, for a 3-port cal on
channel 1 using ports 1,2,and 3), to use adapter 1 between the ports (1 to 2)
and (1 to 3) the following command is used: SENS1:CORR:COLL:GUID:ADAP1:PATH
1,2,1,3. The adapter must have the same DUT connectors as the ports that are
already specified for these ports. The settings for this command remain until
Preset, or the command is sent using a different setting, or until the
[ZERO](CorrGuided.md#adapterCountZero) command is sent.  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<n> |  Adapter index number that was returned from SENS:CORR:COLL:GUID:ADAP:CREate?  
<port pair> |  Ports for which the adapter will be used. The orientation is not critical, as the VNA will align the connector types as necessary. The minimum number of Thru connections required is the number of ports to calibrated -1.  
Examples |  [See example using this command.](../../GPIB_Example_Programs/Perform_Guided_2-Port_Comprehensive_Cal.md)  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:GUIDed:CHANnel:MODE <bool>

Applicable Models: All (Read-Write) Determines whether or not to honor the
channel <ch> argument in guided calibration SCPI commands.  
---  
Parameters |   
<bool> |  OFF (0)  Honor all <ch> arguments. This means the <ch> channel is calibrated regardless of which channel is currently active. ON (1) Legacy behavior. Behavior is specified by the following table: |  <ch> channel type Std or App |  Active channel type Std or App |  Behavior  
---|---|---  
Std |  Std |  Active chan cal'd  
Std |  App |  "Channel not found" error  
App |  Std |  <ch> chan cal'd  
App |  App |  <ch> chan cal'd  
  
Learn about [Standard vs
Application](../../../S1_Settings/Measurement_Classes.htm#StartDiag) channels.  
  
Examples |  SENS:CORR:COLL:GUID:CHAN:MODE 0 sense:correction:collect:guided:channel:mode ON  
Query Syntax |  SENSe:CORRection:COLLect:GUIDed:CHANnel:MODE?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF - This is the default beginning with A.09.50 ON - Default before A.09.50  
  
* * *

## SENSe:CORRection:COLLect:GUIDed:CKIT:CATalog? <connector>

Applicable Models: All (Read-only) This command replaces
[SENS:CORR:COLL:GUID:CKIT:PORT:CAT?](CorrGuided.md#gKitCat) Returns a comma-
separated list of valid kits that use the specified connector type. This
includes mechanical cal kits, applicable characterizations found within ECal
modules currently connected to the VNA, and all user characterizations stored
in VNA disk memory. For ECal modules, the returned list includes the serial
numbers. [See ECal User Characterization commands.](ECalCharacterize.md) Use
items in the list to select the kit to be used with the
SENS:CORR:COLL:GUID:CKIT:PORT and
[SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:CKIT](CorrCollGuidPSens.md#PsenCKIT)
commands.  
---  
Parameters |   
<conn> |  String. Connector type. Use [SENS:CORR:COLL:GUID:CONN:CAT?](CorrGuided.md#gConnCat) to return a list of valid connector types.  
Examples |  SENSe:CORR:COLL:GUID:CKIT:CAT? "Type N (50) male"  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:GUIDed:CKIT:PORT<pnum>:CATalog? Superseded

Applicable Models: All (Read-only) This command is replaced by
[SENSe:CORR:COLL:GUID:CKIT:CAT?](CorrGuided.md#ckitCatConn). Returns a comma-
separated list of valid kits for the specified VNA port. In addition to
mechanical calibration kits, this will include applicable characterizations
found within ECal modules currently connected to the VNA. Use items in the
list to select the kit to be used with the SENS:CORR:COLL:GUID:CKIT:PORT
command. Note: The serial number is returned for ALL ECal modules that are
connected with the connector type of the specified port. Previously, the
returned list would include the serial numbers to distinguish the ECal modules
only when two or more identical ECal models were connected to the VNA.  
---  
Parameters |   
<pnum> |  Any existing port number. If unspecified, value is set to 1  
Examples |  SENS:CORR:COLL:GUID:CKIT:PORT1:CAT?  
'When "Type N (50) male" is specified for connector type, returns: "85054D,
85032F" 'When two identical ECal modules are connected for the connector type,  
'the return string includes serial numbers "85092-60010 ECal 10675,
85092-60010 ECal 00758"  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:CKIT:PORT<pnum>[:SELect] <kit>

Applicable Models: All (Read-Write) Specifies the calibration kit (mechanical
or ECal) for each port to be used during a guided calibration. An unused port
does NOT need to have a specified Cal Kit.

  1. Specify the connector type for the port with [SENS:CORR:COLL:GUID:CONN:PORT](CorrGuided.md#gConSelect).
  2. Query the valid available kits for the connector on each port with SENS:CORR:COLL:GUID:CKIT:PORT:CAT?
  3. Specify the kit using this command.
  4. Perform a query of this command. If the <kit> parameter was incorrectly entered, an error will be returned.

When using this command to specify the cal kit for the output of a VMC
calibration mixer, specify port 3. If port 3 is already used for the output of
the DUT mixer, then specify port 4. [Learn
more](CorrCollSessVMC.htm#MIX_CHAR_CAL_OPT).  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<pnum> |  Any existing port number. If unspecified, value is set to 1  
<kit> |  Calibration kit to be used for the specified port. Case-sensitive. When using an ECal module, include the characterization name in the <kit> string. Use [SENSe:CORR:COLL:GUID:CKIT:CAT?](CorrGuided.md#ckitCatConn) to read the list of characterizations available in the module and in VNA disk memory. If two or more identical ECal modules are connected to the VNA, the serial number must be included to distinguish the ECal modules.  
Examples |  'Note: All of the following examples specify port 1 only ' Mechanical Cal kit SENS:CORR:COLL:GUID:CKIT:PORT1 '85055A' ' Standard ECal modules SENS:CORR:COLL:GUID:CKIT:PORT1 "N4691-60004 ECal" ' Non-factory ECal characterizations are specified as follows: SENS:CORR:COLL:GUID:CKIT:PORT1 "N4691-60004 User 1 ECal" ' When two or more ECal modules with the same model number are ' connected, also specify the serial number as follows: SENS:CORR:COLL:GUID:CKIT:PORT1 "N4691-60004 ECal 01234" ' When Disk Memory ECal user characterizations are used, ' specify both the User char and the serial number as follows: SENS:CORR:COLL:GUID:CKIT:PORT1 "N4691-60004 MyDskChar ECal 01234"  
Query Syntax |  SENSe:CORRection:COLLect:GUIDed:CKIT:PORT<pnum>[:SELect]?  
Return Type |  String - If the <kit> parameter was incorrectly entered while writing, an error will be returned.  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:CONFig:DESCription?

Applicable Models: All Models (Read-Only) Returns a text description (string)
of the current calibration settings. In order to capture all values, the
settings should have been previously committed using
SENS:CORR:COLL:GUID:INITiate:IMMediate.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
Examples |  SENS:CORR:COLL:GUID:CONF:DESC?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:CONFig:LOAD[:IMMediate] <string>

Applicable Models: All Models (Read-Write) Loads the calibration
configurations from file and commits all settings. If no path name is
provided, the file is loaded from the VNA document folder (D: or Public
Documents/Network Analyzer). After this command, if no settings are modified,
it is not required to send SENS:CORR:COLL:GUID:INITiate:IMMediate.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<string> |  File name for the calibration configuration. Use the full path name, file name, and .CFD suffix, enclosed in quotes.  
Examples |  SENS:CORR:COLL:GUID:CONF:LOAD "C:\Users\Public\Documents\Network Analyzer\myconfig.cfd"  
Query Syntax |  SENS<ch>:CORRection:COLLect:GUIDed:CONFig:LOAD[:IMMediate]? <string>  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:CONFig:LOAD:DESCription? <string>

Applicable Models: All Models (Read-Only) Returns a text description (string)
of the calibration settings contained in the specified filename. No changes
are committed. If no path name is provided, the file is loaded from the VNA
document folder (D: or Public Documents/Network Analyzer).  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<string> |  File name for the calibration configuration. Use the full path name, file name, and .CFD suffix, enclosed in quotes.  
Examples |  SENS:CORR:COLL:GUID:CONF:LOAD:DESC? "C:\Users\Public\Documents\Network Analyzer\myconfig.cfd"  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:CONFig:SAVE <string>

Applicable Models: All Models (Read-Write) Save the current guided calibration
settings to file. If no path name is provided, the file is saved in the VNA
document folder (D: or Public Documents/Network Analyzer). This command should
be sent after the calibration settings have been committed using
SENS:CORR:COLL:GUID:INITiate:IMMediate.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<string> |  File name for the calibration configuration. Use the full path name, file name, and .CFD suffix, enclosed in quotes.  
Examples |  SENS:CORR:COLL:GUID:CONF:SAVE "C:\Users\Public\Documents\Network Analyzer\myconfig.cfd"  
Query Syntax |  SENS<ch>:CORRection:COLLect:GUIDed:CONFig:SAVE? <string>  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:GUIDed:CONNector:CATalog?

Applicable Models: All (Read only) Returns a list of valid connectors based on the connector descriptions of the available cal kits. Use an item from the returned list to specify a connector for SENS:CORR:COLL:GUID:CONN:PORT Here are the more common connector types: |  W-band waveguide V-band waveguide U-band waveguide R-band waveguide Q-band waveguide K-band waveguide P-band waveguide X-band waveguide 7-16 female 7-16 male |  Type B Type A (50) female Type A (50) male Type F (75) female Type F (75) male Type N (75) female Type N (75) male Type N (50) female Type N (50) male |  1.00 mm female 1.00 mm male 1.85 mm male 1.85 mm female 2.92 mm female 2.92 mm male APC 2.4 female APC 2.4 male APC 3.5 female APC 3.5 male APC 7  
---|---|---  
  
Examples |  SENS:CORR:COLL:GUID:CONN:CAT?  
Returns: Type N (50) female, Type N (50) male, APC 7 (50), 3.5 mm (50) male,
3.5 mm (50) female, User Connector A  
Return Type |  Comma separated string values  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:CONNector:PORT<pnum>[:SELect] <conn>

Applicable Models: All (Read-Write) Specifies a DUT connector type for every
port during the Guided Calibration procedure. Valid DUT connector names are
stored within calibration kits. Some cal kits may include both male and female
DUT connectors. Therefore, specifying the DUT connector gender may be
required. The VNA remembers previous Guided Cal settings. Therefore, for
completeness, unused ports can either be defined as "Not used" or use the
SENS:CORR:COLL:GUID:ABORt command to clear all ports. The ABORt command is a
more thorough approach and more convenient. See [Guided Cal
examples.](../../GPIB_Example_Programs/SCPI_Example_Programs.htm)

  * A single port with a valid <conn> name indicates a 1-Port calibration will be performed. 
  * Two ports with valid <conn> names indicate either a 2-Port SOLT or [TRL](../../../S3_Cals/TRL_Calibration.md) calibration will be performed depending on the standards definition found within the cal kit and the capability of the VNA.
  * Three ports with valid <conn> names indicate a 3-Port calibration will be performed, and so forth.

|  Follow these steps to ensure port connectors are specified correctly:

  1. Use [SENS:CORR:COLL:GUID:CONN:CAT?](CorrGuided.md#gConnCat) to query available connectors before specifying the port connector.
  2. Set a connector type for each port using this command.
  3. Perform a query of this command. If the connector type was incorrectly entered, an error will be returned.
  4. Specify the cal kit to use for each port with [SENS:CORR:COLL:GUID:CKIT:PORT](CorrGuided.md#gKit)

  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<pnum> |  Any existing port number. If unspecified, value is set to 1.  
<conn> |  String - DUT connector type to connect with VNA port <pnum>. Case-sensitive.  
Examples |  'Specifying a 2-port cal (1 & 2) on a 4-port VNA SENS:CORR:COLL:GUID:CONN:PORT1 'Type N (50) female'  
SENS:CORR:COLL:GUID:CONN:PORT2 'Type N (50) male'  
SENS:CORR:COLL:GUID:CONN:PORT3 'Not used'  
SENS:CORR:COLL:GUID:CONN:PORT4 'Not used'  
Query Syntax |  SENSe:CORRection:COLLect:GUIDed:CONNector:PORT<pnum>[:SELect]?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:DATA STAN<n>, <meas parameter>, [<ECal
state num>],<data>

Applicable Models: All (Read-Write) Sets and returns the measurement data for
a specified measurement parameter of a particular step of a guided cal (and
for a specific state of an ECal if the step is an ECal step). The measurement
data is complex real-and-imaginary pairs where the number of points is the
current number of points on the channel, and is in ASCII or binary format as
dictated by the current setting of the [FORMat:DATA](../Format_SCPI.md#fd)
command. The query returns measurement data once it has been uploaded. The Cal
Wizard will also perform the acquisition as in a normal calibration an then
use the query to see the data per ECal state. Note: This command only applies
to cals of standard S-parameter channels.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
STAN<n> |  Choose from:STAN1, STAN2, etc. through STANn where n is the number of cal standard connection steps for the calibration. Note: You do not necessarily have to invoke these connection steps in sequential order.  
<meas parameter> |  Measurement parameters for standard S-parameter channels.  
<data> |  Measurement data to upload.  
[<ECal state num>] |  ECal state number.  
Examples |  SENSe:CORRection:COLLect:GUIDed:DATA STAN1,"S11",3,-1.40827238560E-001,+2.33575403690E-001,-8.62407535315E-002,+1.97563484311E-001,-3.09373617172E-001,-3.19083780050E-002,-2.91508108377E-001,-1.58155187964E-001,-2.40630045533E-001,-2.95877635479E-001,-1.10904276371E-001,-3.70426654816E-001,+6.89683631063E-002,-3.54430228472E-001,+9.91653800011E-002,-3.55183511972E-001,+4.09932315350E-001,-2.48026609421E-001,+3.73078525066E-001,-5.87668754160E-002,+5.06927728653E-001,+9.91396754980E-002,+3.50351631641E-001,+2.56966352463E-001,+9.62104797363E-002,+4.53149110079E-001,-3.36435511708E-002,+3.78106325865E-001,-2.88381099701E-001,+3.05592954159E-001,-2.96310603619E-001,+1.54096364975E-001,-4.68389958143E-001,+4.40414100885E-002,-1.57085657120E-001,-6.15487955511E-002,-1.97938442230E-001,-1.97066932917E-001,-2.88984715939E-001,-1.64536476135E-001,+1.04563377798E-001,-3.01358193159E-001,-1.15329414606E-001,-3.01511257887E-001,+1.76867023110E-001,-3.13728988171E-001,+2.52688616514E-001,-3.10592085123E-001,+3.16383123398E-001,-2.51693539321E-002,+5.51517367363E-001,-3.37228141725E-002,-5.16818091273E-002,+2.94606477022E-001,+4.42426577210E-002,+6.23966455460E-001,-2.10833102465E-001,+8.56095775962E-002,-3.56811732054E-001,+3.87589573860E-001,-5.81349851564E-003,-4.00106996298E-001,-4.85193997622E-001,-2.21789374948E-001,+5.65891504288E-001,-2.02025130391E-001,+1.32879754528E-002,-1.02828487754E-001,+3.49758952856E-001,+4.49306488037E-001,+5.84089420736E-002,+9.62211638689E-002,-4.81228590012E-001,+3.52717667818E-001,-2.72483140230E-001,-1.59653365612E-001,-2.63482809067E-001,-1.27529203892E-001,+7.02303647995E-002,-6.81156396866E-001,-1.32705345750E-001,-2.89749443531E-001,+2.88871675730E-001,-4.64907467365E-001,+8.61295536160E-002,+3.34163904190E-002,+1.99998915195E-001,+5.55351190269E-002,+8.01121890545E-001,+1.85898199677E-001,+7.81627893448E-001,+6.67621552944E-001,-4.65975850821E-002,-4.60099279881E-001,+7.00241029263E-002,+2.37143054605E-001,+3.89812327921E-002,+2.88123339415E-002,-3.25421810150E-001,+7.22536623478E-001,+2.27582111955E-001,+1.39539033175E-001 See an example that uses this command.  
Query Syntax |  SENSe:CORRection:COLLect:GUIDed::DATA? STAN<n>, <meas parameter>, [<ECal state num>]  
Return Type |  Depends on [FORMat:DATA](../Format_SCPI.md#fd)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:DATA:CATalog? STAN<n>,<state Number>

Applicable Models: All (Read-only) Returns a comma-delimited CSV string of
measurement parameters (with parameter names) for STANn at State x. The
measurement parameters have to be measured in the specified step number of a
guided calibration. If the parameter name is a not an S-parameter, an
underscore is inserted (for example, b1/a1,1 becomes b1/a1_1). Note: This
command only applies to cals of standard S-parameter channels. Note: Double
commas may exist in the return string if a testset is not used in the
configuration.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
STAN<n> |  Choose from:STAN1, STAN2, etc. through STANn where n is the number of cal standard connection steps for the calibration. Note: You do not necessarily have to invoke these connection steps in sequential order.  
<state Number> |  Specifies a state number.  
Examples |  SENS:CORR:COLL:GUID:DATA:CAT? STAN1,1 ",S11" SENS:CORR:COLL:GUID:DATA:CAT? STAN1,9 "dual_1_2,S11,dual_1_2,S21,dual_1_2,S12,dual_1_2,S22,dual_1_2,a2/a1_1,dual_1_2,a1/a2_2" (In this case, "dual_1_2" refers to a testset path) See an example that uses this command.  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:DESCription? <step>

Applicable Models: All (Read-only) Returns the connection description for the
specified calibration step.  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<step> |  A number from 1 to the number of steps required to complete the calibration (Use SENS:CORR:COLL:GUID:STEP? to query the number of steps )  
Examples |  SENS:CORR:COLL:GUID:DESC? 10 'Returns:  
Connect APC 7 Open to port3  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:DISPlay:SMITh <bool>

Applicable Models: All (Read-Write) Applies Smith Chart to the display format
during a Guided Calibration. It is supported for standard, NF and NFX.
classes.  After sending this command, send
SENSe<ch>:CORRection:COLLect:GUIDed:PACQuire STAN<n> to show the calibration
window. For Cal All, it is supported only for a channel that satisfies one of
the following conditions:

  * The channel is not set to an independent calibration channel and Split Cal is disabled.
  * The channel for Standard or NF class

  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<bool> |  Choose from: ON (or 1) - The display format is Smith Chart OFF (or 0) - The display format is Log Mag  
Examples |  SENS:CORR:COLL:GUID:DISP:SMIT 1 sense2:correction:collect:guided:display:smith 0  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:DISPlay:SMITh?  
Default |  OFF  
  
* * *

## SENSe:CORRection:COLLect:GUIDed:DISPlay:WINDow:AOFF

Applicable Models: All (Write-only) Clears the flags for windows to be shown
during calibrations. To flag a window to be shown see
[SENS:CORR:COLL:GUID:DISP:WIND](CorrGuided.md#DispWindStat).  This command is
equivalent with
[SENSe:CORRection:COLLect:DISPlay:WINDow:AOFF.](Sense_Correction.md#CalWindowAoff)  
---  
Examples |  SENS:CORR:COLL:GUID:DISP:WIND:AOFF sense:correction:collect:guided:display:window:aoff [See an example using this command.](../../GPIB_Example_Programs/Show_Custom_Window_during_Calibration.md)  
Query Syntax |  Not Applicable  
Default |  Not Applicable  
  
## SENSe:CORRection:COLLect:GUIDed:DISPlay:WINDow<wNum>[:STATe] <bool>

Applicable Models: All (Write-only) Set the 'show' state of the window to be
displayed during a calibration to view the measurements/channels. [Learn
more](../../../S3_Cals/Calibration_Wizard.htm#CalWindow).  When this command
is sent, the specified window is 'flagged' to be shown during calibration. The
flag is cleared when the window is closed. A Preset or Instrument State Recall
also closes the window. If the same window number is reopened, this command
must be sent again to show the window during a calibration. The flag is NOT
saved with an instrument state. Send this command for each additional window
to show during a calibration. This command is equivalent with
[SENSe:CORRection:COLLect:DISPlay:WINDow.](Sense_Correction.md#CalWindowState)  
---  
Parameters |   
<wNum> |  Window number to show during a calibration. The calibration window will also be shown with this window. The window must already be created. Use [DISPlay:CATalog?](../Display.md#cat) to read all existing window numbers.  
<bool> |  Window state. Choose from: ON (or 1) - Show the specified window during calibration. OFF (or 0) - Do NOT show the specified window during calibration.  
Examples |  SENS:CORR:COLL:GUID:DISP:WIND1 1 sense:correction:collect:guided:display:window2:state off [See an example using this command.](../../GPIB_Example_Programs/Show_Custom_Window_during_Calibration.md)  
Query Syntax |  Not Applicable  
Default |  OFF  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:DMATch:APPLy[:IMMediate] [string]

Applicable Models: N522xB, N523xB, N524xB (Write-only) Specifies a Delta Match
Cal Set to be used for delta match correction. If the User-performed Cal Set
GUID or Name is not specified, then the Global Delta Match Cal Set is applied.
An error is returned if the specified Cal Set does not meet the following
Delta Match criteria:

  * Must have been performed using ECal or as a guided mechanical cal (not Unguided).
  * Must have the same start freq, stop freq, and number of points as the channel being calibrated.
  * Must calibrate the ports that are required by the TRL or Unknown Thru cal as indicated by [SENS:CORR:COLL:GUID:DMATch:APPLy:PORTs?](CorrGuided.md#DmatchApplyPorts).

The Global Delta Match Cal can ALWAYS be applied. [Learn more about Delta
match calibration.](../../../S3_Cals/TRL_Calibration.htm#4Port) See example of
a complete [Global Delta Match
calibration.](../../GPIB_Example_Programs/Perform_Global_Delta_Match_Cal.htm)
See example where [Delta Match is applied to a
calibration](../../GPIB_Example_Programs/Perform_Unknown_Thru_or_TRL_Cal.htm).  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
[string] |  Optional argument. GUID or Name of the User-performed Delta Match Cal Set to apply. If unspecified, the Global Delta Match Cal Set is applied.  
Examples |  SENS:CORR:COLL:GUID:DMAT:APPL sense:correction:collect:guided:dmatch:apply:immediate "{2B893E7A-971A-11d5-8D6C-00108334AE96}" SENS:CORR:COLL:GUID:DMAT:APPL "MyDMatchCalset"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:DMATch:APPLy:PORTs?

Applicable Models: N522xB, N523xB, N524xB (Read-only) Returns the port numbers
for which delta match correction is required. 0 (zero) is returned if the Cal
does NOT require Delta Match correction for one of the following reasons:

  * The Cal does NOT involve Unknown THRU or TRL. You specify this using [SENS:CORR:COLL:GUID:METH <UNKN | TRL>](CorrGuided.md#gMETHod).
  * The Cal DOES involve Unknown THRU or TRL, but the delta match data can be calculated by the Unknown Thru or TRL Cal. [Learn how this is possible.](../../../S3_Cals/TRL_Calibration.md#4Port) However, you can force the Cal to use the Delta Match data from a Cal Set.

[Learn more about Delta match
calibration.](../../../S3_Cals/TRL_Calibration.htm#4Port) See example of a
complete [Delta Match
calibration.](../../GPIB_Example_Programs/Perform_Global_Delta_Match_Cal.htm)  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
Examples |  SENS:CORR:COLL:GUID:APPL:PORT? 'Returns:  
1,2,3  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:DMATch[:INITiate] <conn>,<cKit>

Applicable Models: N522xB, N523xB, N524xB (Write-only) Initiates a global
delta match calibration.  [Learn more about Global Delta Match
calibration.](../../../S3_Cals/TRL_Calibration.htm#4Port) See example of a
complete [Delta Match
calibration.](../../GPIB_Example_Programs/Perform_Global_Delta_Match_Cal.htm)  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<conn> |  String. Connector type for port 1. All other ports are set automatically.  
<cKit> |  String Cal Kit for all ports. If incorrectly entered while writing, an error is returned.  
Examples |  SENS:CORR:COLL:GUID:DMAT APC 3.5 female,"85052B"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:ECAL:ACQ <cal method>. <port list>,
[calset]

Applicable Models: All

(Write only) Execute the Ecal calibration with specified Ecal using
SENS:CORR:COLL:GUID:ECAL:SEL. If ECal module is not specified, the first Ecal
in the list is used. This command must be overlapped because it can be quite
slow to finish an ecal. Otherwise, the client will time out and will be unable
to poll for completion. Therefore, the command must be followed with either a
*OPC? or a *OPC and serial poll.  
---  
Parameters |   
<ch> |  Channel to be calibrated, depending on the CHAN:MODE setting. If unspecified, value is set to 1.  
<cal method> |  String Calibration Method. SOLT: using defined through SOLR: using undefined through ERESponse: Enhanced Response  
<port list> |  Array Port number to be calibrated. If enhanced response (ERESponse) is selected, the first port number is the stimulus port and the second port number is the response port.  
[calset] |  Optional argument. Cal Set name If NOT specified, behavior depends on the [SENS:CORR:PREFerence:CSET:SAVE](Sense_Correction.md#CsetSave) setting. If specified, choose an existing Cal Set, either by name or by GUID.

  * By Cal Set name: include quotes.
  * Query all Cal Set GUIDs with [SENS:CORR:CSET:CAT?](CorrCset.md#catalog)

An error is reported if the Cal Set is not found. The Cal Set is either
supplemented or overwritten depending on the method, connectors, and ports
selected. [Learn more about Cal Sets.](../../../S3_Cals/Cal_Sets.md)  
Examples |  ' Full 2 port cal with defined through for ports 2 and 3 SENS:CORR:COLL:GUID:ECAL:ACQ SOLT,2,3 ' Enhance Response Cal for ports 4 (Stimulus) and 1 (Response) SENS:CORR:COLL:GUID:ECAL:ACQ ERES,4,1 ' Full 2 port cal with calset and undefined through for ports 1 to 4 SENS:CORR:COLL:GUID:ECAL:ACQ SOLR,1,2,3,4,"MyCalSet"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:ECAL[:SELect] <ecal kit>

Applicable Models: All

(Read-Write) Specifies the Ecal Kit for Ecal Calibration. This is a new
command that specifies the ECal kit to be used in the new 1-shot ECal
execution command. If not specified, the 1-shot command will internally select
the top one from the connected ECal kits (like the basic cal and start cal
dialogs are doing.) The top ecal kit in the list can be ordered either by an
internal module number or alphabetically. This default selection will allow
the user to use generic test code but only if there is only one ECal
connected.  
---  
Parameters |   
<ch> |  Channel to be calibrated, depending on the CHAN:MODE setting. If unspecified, value is set to 1.  
<ecal kit> |  Ecal kit to be used for the specified port. Case-sensitive. Include the characterization name in the <kit> string. Use SENSe:CORR:COLL:GUID:CKIT:CAT? to read the list of characterizations available in the module and in VNA disk memory. If two or more identical ECal modules are connected to the VNA, the serial number must be included to distinguish the ECal modules.  
Examples |  ' Standard ECal modules SENS:CORR:COLL:GUID:ECAL "N4691-60004 ECal" ' Non-factory ECal characterizations are specified as follows: SENS:CORR:COLL:GUID:ECAL "N4691-60004 User 1 ECal" ' When two or more ECal modules with the same model number are ' connected, also specify the serial number as follows: SENS:CORR:COLL:GUID:ECAL "N4691-60004 ECal 01234" ' When Disk Memory ECal user characterizations are used, ' specify both the User char and the serial number as follows: SENS:CORR:COLL:GUID:ECAL "N4691-60004 MyDskChar ECal 01234"  
Query Syntax |  SENSe:CORRection:COLLect:GUIDed:ECAL[:SELect]?  
Return Type |  String - If the <kit> parameter was incorrectly entered while writing, an error will be returned.  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:ETERms:COMPute [cal set name]

Applicable Models: All (Write-only) Computes the error correction terms, turns
Correction ON, and saves the calibration to an existing, specified Cal Set.
The cal acquisition process does not conclude as with the
[SAVE](CorrGuided.md#gSave) command. This command leaves the cal acquisition
in memory to allow re-measuring/re-computing. To conclude the cal acquisition
process, use the SENS:CORR:COLL:GUID:ABOR. command. [Learn all about Cal
Sets.](../../../S3_Cals/Cal_Sets.htm) Note: This command is NOT supported for
application channels (Gain Compression, SMC/VMC, Noise Figure, IMD and so
forth). Use [SENS:CORR:COLL:GUID:SAVE](CorrGuided.md#gSave) and save to a cal
register. You can then use [SENS:CORR:CSET:COPY](CorrCset.md#copy) to copy
the cal register to a named Cal Set.

  * Use this command instead of specifying the optional name or GUID argument in [SENS:CORR:COLL:GUID:INIT](CorrGuided.md#gInit).
  * Use [SENS:CORRection:CSET](CorrCset.md) commands to get names of existing Cal Sets.
  * The cal data is also saved to the channel Cal Register.
  * If all of the required standards have not been measured, the calibration will not complete properly.

### For Calibrate All Channels

When this command is used during a Cal All session, the <cal set name>
argument sets the User Cal Set prefix. All generated Cal Sets will be preceded
with this string name.

  * Cal Set prefix can also be set using [SYST:CAL:ALL:CSET:PREFix](../SystCalAll.md#csetPrefix). When the Cal Set prefix has already been set with [SYST:CAL:ALL:CSET:PREFix](../SystCalAll.md#csetPrefix), this command overwrites it.
  * When <cal set name> is an empty string, a User Cal Set will not be saved. Only Cal Registers will be saved.

  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<cal set name> |  String - Name of an existing Cal Set to be overwritten. See [Calibrate All Channels](CorrGuided.md#CalAll) note (above).  
Examples |  SENS:CORR:COLL:GUID:ETER:COMP "{2B893E7A-971A-11d5-8D6C-00108334AE96}" sense:correction:collect:guided:eterms:compute "MyCalSet"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:ETERms:LOAD[:CSET] <cset>,<calPort>
[,csPort]

Applicable Models: All (Write-only) Loads 1-port error terms from a Cal Set
into the current Guided Cal sequence. When the Cal steps are recomputed,
connection steps are removed due to the loading of the error terms. This
command must be sent after the INIT command. This command was implemented to
facilitate calibrating a large matrix of external ports and most users will
not need to use this command. [See example of how to use this
command.](../../GPIB_Example_Programs/Load_Eterms_into_Cal_Sequence.htm)  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<cset> |  String Name of User Cal Set in which the error terms reside.  
<pnum> |  Integer Port number of the current cal to receive error terms.  
[csPort] |  Integer Optional argument. Port number associated with the error terms in the Cal Set. If unspecified, the same port number as <calPort> is used.  
Examples |  [See example](../../GPIB_Example_Programs/Load_Eterms_into_Cal_Sequence.md)  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:INITiate[:IMMediate] [string][,
bool][,char]

Applicable Models: All (Write-only) Initiates a guided calibration.

  * The VNA determines the measurements needed to perform the calibration using the settings specified from the SENS:CORR:COLL:GUID:CONN:PORT and SENS:CORR:COLL:GUID:CKIT:PORT commands.
  * After this command is executed, subsequent commands can be used to query the number of measurement steps, issue the acquisition commands, query the connection description strings, and subsequently complete a guided calibration. [See example calibration programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md).

  
---  
Parameters |   
<ch> |  Channel to be calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
[string] |  Optional argument. Cal Set name or GUID enclosed in quotes. If NOT specified, behavior depends on the [SENS:CORR:PREFerence:CSET:SAVE](Sense_Correction.md#CsetSave) setting. If specified, choose an existing Cal Set, either by name or by GUID.

  * By Cal Set name: include quotes.
  * Query all Cal Set GUIDs with [SENS:CORR:CSET:CAT?](CorrCset.md#catalog)

An error is reported if the Cal Set is not found. The Cal Set is either
supplemented or overwritten depending on the method, connectors, and ports
selected. [Learn more about Cal Sets.](../../../S3_Cals/Cal_Sets.md)  
[bool] |  Optional argument. To set this argument, also set the first optional argument. See example below. OFF (0)  If Cal Set stimulus settings differ from the existing channel, do not change channel stimulus settings. The Cal Set is saved to the current setting of the [SENS:CORR:PREF:CSET:SAVE](Sense_Correction.md#CsetSave) command. This is the default setting if not specified. ON (1) If Cal Set stimulus settings differ from the existing channel, change the channel stimulus settings to match the Cal Set settings.  
[char] |  Optional argument. To set this argument, also set the first two optional arguments. See example below. SYNChronous \- blocks further SCPI commands while processing this command.. (default setting). ASYNchronous \- does NOT block further SCPI commands while processing this command. [Learn more about this argument](../../Learning_about_GPIB/Understanding_Command_Synchronization.md#Synch)  
Examples |  SENS:CORR:COLL:GUID:INIT 'set first optional argument SENS:CORR:COLL:GUID:INIT "MyCalSet" 'set two optional arguments SENS:CORR:COLL:GUID:INIT " ",1 'set all optional arguments SENS:CORR:COLL:GUID:INIT "MyCalSet",1,ASYN  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:ISOLation:AVERage:INCRement <num>

Applicable Models: All (Read-Write) Specifies amount to increment (increase)
the channels averaging factor during measurement of isolation standards in a
guided calibration. Note: If the channel has averaging turned OFF and the
value of <num> is greater than 1, averaging will be turned ON only during the
isolation measurements and with the averaging factor equal to <num>.  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the CHAN:MODE setting. If unspecified, value is set to 1.  
<num> |  Amount to increment the averaging factor for the isolation measurement. The maximum averaging factor for the channel is 65536 (2^16).  
Examples |  'Measure isolation on all paths for the cal SENS:CORR:COLL:GUID:ISOL ALL 'Remove the port pairs 1-to-2 and 1-to-3 from the list of paths on which to measure isolation sense:correction:collect:guided:isolation:paths REMove,1,2,1,3  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:ISOLation:AVERage:INCRement?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  8 - If this command is NOT sent, but isolation is measured, then averaging will be turned ON with factor set to 8 during the isolation measurements.  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:ISOLation[:PATHs] <char>[,<p1a, p1b,
p2a, p2b>]

Applicable Models: All (Read-Write) Specifies the paths (port pairs) to make
isolation measurements on during a guided calibration.  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the CHAN:MODE setting. If unspecified, value is set to 1.  
<char> |  ALL Measure isolation on all pairings of the ports that are to be calibrated. NONE Do not measure isolation on any pairing of the ports to be calibrated. (Default behavior). ADD Add one or more specific pairings of ports to the list of port pairings for which isolation will be measured. REMove Remove one or more specific pairings of ports from the list of port pairings for which isolation will be measured. If many paths are to be measured, it may be easier to first send ALL, then REMove and specify the paths to remove.  
<p1a, p2a...> |  For use when <char> is ADD or REMove. Specify Port numbers in pairs:

  * For 3-port cals, specify up to 3 pairs.
  * For 4-port cals, specify up to 6 pairs.

p1a, p1b (Path1 - port A and port B) p2a, p2b (Path2 - port A and port B) p3a,
p3b (Path3 - port A and port B)  
Examples |  'Measure isolation on all paths for the cal SENS:CORR:COLL:GUID:ISOL ALL 'Remove the port pairs 1-to-2 and 1-to-3 from the list of paths on which to measure isolation sense:correction:collect:guided:isolation:paths REMove,1,2,1,3  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:ISOLation:PATHs? Note: if isolation is not be measured on any of the paths, the query returns 0  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0 - Isolation not measured on any paths.  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:ITERations:COUNt? <step>

Applicable Models: All (Read-only) Designed to be used for an iterative cal
standard such as a sliding load, this command returns the number of iterative
measurement acquisitions that has been made for the specified step. Zero (0)
is returned if the step has not yet been measured. For most cal steps that
have already been measured, this command returns 1. Set
SENS:CORR:COLL:GUID:PREF:SLID ITER to count acquisition steps.  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the CHAN:MODE setting. If unspecified, value is set to 1.  
<step> |  Guided Cal step number for which the acquisition number will be returned. Use [SENS:CORR:COLL:GUID:STEP?](CorrGuided.md#gSteps) to query the number of steps in the calibration.  
Examples |  SENS:CORR:COLL:GUID:ITER:COUN? 4 'Example return: 5 [See example program](../../GPIB_Example_Programs/Perform_a_Guided_Cal_with_Sliding_Load.md)  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:ITERations:MINimum? <step>

Applicable Models: All (Read-only) Designed to be used for an iterative cal
standard such as a sliding load, this command returns the minimum number of
required iterative measurement acquisitions for the specified step. For most
connection steps this will return 1, but for an iterative cal standard such as
a sliding load, it will return a number such as 5. Set
[SENS:CORR:COLL:GUID:PREF:SLID ITER](CorrGuided.md#PrefSliding) to count
acquisition steps.  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<step> |  Guided Cal step number for which to return the number of iterative measurement acquisitions that have been made. Use [SENS:CORR:COLL:GUID:STEP?](CorrGuided.md#gSteps) to query the number of steps in the calibration.  
Examples |  SENS:CORR:COLL:GUID:ITER:MIN? 4 'Example return: 5 [See example program](../../GPIB_Example_Programs/Perform_a_Guided_Cal_with_Sliding_Load.md)  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:ITERations:RESet <step>

Applicable Models: All (Write-only) Resets the specified guided cal connection
step as unmeasured. This clears all previous measurements made for that step.  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<step> |  Guided Cal step number to reset. Use [SENS:CORR:COLL:GUID:STEP?](CorrGuided.md#gSteps) to query the number of steps in the calibration.  
Examples |  SENS:CORR:COLL:GUID:ITER:RESet? 4 [See example program](../../GPIB_Example_Programs/Perform_a_Guided_Cal_with_Sliding_Load.md)  
Return Type |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:LIST:COUNt?

Applicable Models: All (Read-only) Returns the number of measurement steps
required to complete the current guided calibration. This command is the same
as the SENS:CORR:COLL:GUID:STEP command.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
Examples |  SENS:CORR:COLL:GUID:LIST:COUN?  
sense2:correction:collect:guided:list:count?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:LIST:STEP<ListCount>:COUNt?

Applicable Models: All (Read-only) Returns the number of standards for
step[n]. This is generally 1 unless the standard is an isolation standard or a
composite standard.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<ListCount> |  Step number from 1 to 1000.  
Examples |  SENS:CORR:COLL:GUID:LIST:STEP:COUN?  
sense2:correction:collect:guided:list:step1:count?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:LIST:STEP<ListCount>:DESCription?

Applicable Models: All (Read-only) Returns the step description.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<ListCount> |  Step number from 1 to 1000.  
Examples |  SENS:CORR:COLL:GUID:LIST:STEP:DESC?  
sense2:correction:collect:guided:list:step1:description?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:LIST:STEP<ListCount>:LABel?

Applicable Models: All (Read-only) Returns the label for the complete standard
used in the step. If the standard is a composite standard, the label is for
the composite device.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<ListCount> |  Step number from 1 to 1000.  
Examples |  SENS:CORR:COLL:GUID:LIST:STEP:LAB?  
sense2:correction:collect:guided:list:step1:label?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:LIST:STEP<ListCount>:PORTs?

Applicable Models: All (Read-only) Returns the number of ports on the standard
used in the step. If the standard is a composite standard, the number of ports
applies to the composite. So if the composite standard is an offset line
connected to a load, the composite device is a 1 port device.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<ListCount> |  Step number from 1 to 1000.  
Examples |  SENS:CORR:COLL:GUID:LIST:STEP:PORT?  
sense2:correction:collect:guided:list:step1:ports?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

##
SENSe<ch>:CORRection:COLLect:GUIDed:LIST:STEP<ListCount>:STANdard<StandardCount>:LABel?

Applicable Models: All (Read-only) Returns the label for the one of the
standards used in the step. If the step contains only a single standard, the
response to this query is identical to SENS:CORR:COLL:GUID:LIST:STEP:LAB?  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<ListCount> |  Step number from 1 to 1000.  
<StandardCount> |  Standard number from 1 to 3.  
Examples |  SENS:CORR:COLL:GUID:LIST:STEP:STAN:LAB?  
sense2:correction:collect:guided:list:step1:standard2:label?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

##
SENSe<ch>:CORRection:COLLect:GUIDed:LIST:STEP<ListCount>:STANdard<StandardCount>:PORTs?

Applicable Models: All (Read-only) Returns the number of ports on one of the
standard used in the step. If the step contains only a single standard, the
response to this query is identical to SENS:CORR:COLL:GUID:LIST:STEP:PORT?  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<ListCount> |  Step number from 1 to 1000.  
<StandardCount> |  Standard number from 1 to 3.  
Examples |  SENS:CORR:COLL:GUID:LIST:STEP:STAN:PORT?  
sense2:correction:collect:guided:list:step1:standard2:ports?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

##
SENSe<ch>:CORRection:COLLect:GUIDed:LIST:STEP<ListCount>:STANdard<StandardCount>:STYPe?

Applicable Models: All (Read-only) Returns the enumeration for the type of standard that describes one of the standard devices used in the step. If the step contains only a single standard, the response to this query is identical to SENS:CORR:COLL:GUID:LIST:STEP:STYP? The following list of enumerations is currently defined: OPEN | SHORt | LOAD | REFLection | THRU | LINE | ECAL | ISOLation | COMPosite | SENSor | PHASeref | MIXer  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<ListCount> |  Step number from 1 to 1000.  
<StandardCount> |  Standard number from 1 to 3.  
Examples |  SENS:CORR:COLL:GUID:LIST:STEP:STAN:STYP?  
sense2:correction:collect:guided:list:step1:standard2:stype?  
Return Type |  Enumeration  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OPEN  
  
* * *

##
SENSe<ch>:CORRection:COLLect:GUIDed:LIST:STEP<ListCount>:STANdard<StandardCount>:TPORts?

Applicable Models: All (Read-only) Returns the list of VNA test ports to which
one of the standards is attached. If the step contains only a single standard,
the response to this query is identical to
SENS:CORR:COLL:GUID:LIST:STEP:TPORts?  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<ListCount> |  Step number from 1 to 1000.  
<StandardCount> |  Standard number from 1 to 3.  
Examples |  SENS:CORR:COLL:GUID:LIST:STEP:STAN:TPOR?  
sense2:correction:collect:guided:list:step1:standard2:tports?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:LIST:STEP<ListCount>:STYPe?

Applicable Models: All (Read-only) Returns the enumeration for the type of standard device used in the step. The following list of enumerations is currently defined: OPEN | SHORt | LOAD | REFLection | THRU | LINE | ECAL | ISOLation | COMPosite | SENSor | PHASeref | MIXer  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<ListCount> |  Step number from 1 to 1000.  
Examples |  SENS:CORR:COLL:GUID:LIST:STEP:STYP?  
sense2:correction:collect:guided:list:step1:stype?  
Return Type |  Enumeration  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OPEN  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:LIST:STEP<ListCount>:TPORts?

Applicable Models: All (Read-only) Returns the list of VNA test ports to which
the standard(s) in this step is attached.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<ListCount> |  Step number from 1 to 1000.  
Examples |  SENS:CORR:COLL:GUID:LIST:STEP:TPOR?  
sense2:correction:collect:guided:list:step1:tports?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:GUIDed:METHod <char> Superseded

Applicable Models: All This command is replaced with
[SENS:CORR:COLL:GUID:PATH:CMEThod](CorrGuided.md#PathCmethod) and
[SENS:CORR:COLL:GUID:PATH:TMEThod.](CorrGuided.md#PathTMethod) (Read-Write)
Selects from one of several algorithms available for performing the THRU
portion of a guided calibration. [Learn more about THRU
methods.](../../../S3_Cals/Calibration_THRU_Methods.htm)  
---  
Parameters |   
<char> |  DEFAULT \- Informs guided calibrations to use the default algorithm when computing the number of needed standards acquisition steps. (default selection if omitted.) ADAP \- Use the adapter removal algorithm FLUSH \- Use with insertable devices. UNKN \- Use the Unknown THRU algorithm with calibrations for non-insertable devices. DEFined \- Use the THRU definition that you stored in the cal kit file, or ECal module. TRL \- Select TRL Cal Type for guided cals. Valid for "TRL ready" Cal Kits with properly assigned TRL cal classes. SOLT \- Select SOLT Cal Type for guided cals. Valid for any kit with properly assigned SOLT cal classes.  
Examples |  SENS:CORR:COLL:GUID:METH ADAP  
sense:correction:collect:guided:method unkn  
Query Syntax |  SENSe:CORRection:COLLect:GUIDed:METHod?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  DEFAULT  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:PACQuire STAN<n>

Applicable Models: All (Write-only) Show the [Cal
Window](../../../S3_Cals/Calibration_Wizard.htm#CalWindow), and optionally one
or more other specific windows before acquiring a Cal standard. This command
will cause the Cal Window to display the specific measurements that are to be
made for that particular Cal standard to facilitate the connection of
standards.  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
STAN<n> |  Choose from:STAN1, STAN2, etc. through STANn where n is the number of cal standard connection steps for the calibration. Note: You do not necessarily have to invoke these connection steps in sequential order.  
Examples |  SENS:CORR:COLL:GUID:PACQuire STAN2 sense:correction:collect:guided:pacquire STAN5 [See an example that uses this command.](../../GPIB_Example_Programs/Show_Custom_Window_during_Calibration.md)  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:PATH:CMEThod
<port1>,<port2>,<caltype1[,caltype2]>

Applicable Models: All Note: This command replaces
[SENS:CORR:COLL:GUID:METH](CorrGuided.md#gMETHod). (Read-Write) Specifies the
calibration method for each port pair. Note: Sending this command will
overwrite the VNAs SmartCal determinations for the most accurate cal method
for your connector settings and Cal Kits. Send this command ONLY if you have a
deliberate reason for overwriting the SmartCal logic. You can send the query
form of this command to learn the cal method determined by SmartCal. See [Thru
Pairs Sequence](CorrGuided.htm#THRUPairs) to learn how to send this and other
Thru commands. After sending this command, send the query form to be sure that
the command was accepted. If not, then the chosen Cal method is not compatible
with the specified Thru method. For example, if the specified Thru method is
Unknown Thru, an attempt to set Enhanced Response Cal should be rejected.
[Learn more about Thru
Methods.](../../../S3_Cals/Calibration_THRU_Methods.htm)  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<port1> |  First port of the pair to be calibrated.  
<port2> |  Second port of the pair to be calibrated.  
<caltype1[caltype2]> |  (String) Cal type for the port pair, enclosed in a single pair of quotes. NOT case-sensitive. caltype1 Choose from:

  * TRL
  * SOLT
  * QSOLTN
  * EnhRespN
  * TransRespN

For the last two arguments, replace N with the port to be used as the source
port, which MUST be one of the port pair. caltype2 Optional argument. Use only
when performing an adapter removal cal on the pair. This argument specifies
the Cal type on the second port. Caltype1 then specifies the Cal type of the
first port. Choose from the same arguments as caltype1.  
Examples |  SENS:CORR:COLL:GUID:PATH:CMEThod 2,3,"QSOLT2" sense:correction:collect:guided:path:cmethod 2,3,"solt,trl"  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:PATH:CMEThod? <port1>,<port2> If only one caltype is returned then its NOT adapter removal.  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  The most accurate Cal method for the current cal.  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:PATH:TMEThod
<port1>,<port2>,<thruType1[,thruType2]>

Applicable Models: All Note: This command replaces
[SENS:CORR:COLL:GUID:METH](CorrGuided.md#gMETHod). (Read-Write) Specifies the
calibration THRU method for each port pair. Note: Sending this command will
overwrite the VNAs SmartCal determination for the thru method. Send this
command ONLY if you have a deliberate reason for overwriting the SmartCal
logic.  You can send the query form of this command to learn the THRU method
determined by SmartCal. See [Thru Pairs Sequence](CorrGuided.md#THRUPairs) to
learn how to send this and other Thru commands. [Learn more about Thru
methods.](../../../S3_Cals/Calibration_THRU_Methods.htm)  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<port1> |  First port of the port pair to be calibrated.  
<port2> |  Second port of the port pair to be calibrated.  
<thruType1[,thruType2]> |  (String) Thru methods for port pair, enclosed in a single pair of quotes. NOT case-sensitive. thruType1 Calibration Thru method. Choose from:

  * Defined Thru Measures a Thru for which there is a stored definition in the Cal kit of the lowest-numbered port of the pair. For example, if the port pair is 1,2, then the cal kit for port 1 MUST contain a Defined Thru.
  * Zero Thru Measures a Zero length Thru, also known as Flush-Thru.
  * Undefined Thru (Also known as Unknown Thru) A Thru type for which there is NOT a stored definition in the Cal Kit. Valid ONLY for SOLT cal type.
  * Undefined Thru using a Defined Thru (ECal modules ONLY) Measures the internal Thru as an Unknown Thru.

thruType2 Optional argument. Use ONLY when Adapter Removal Cal is specified
for the pair using
[SENS:CORR:COLL:GUID:PATH:CMEThod](CorrGuided.md#PathCmethod). When
specifying ThruType2, this is the only valid argument: "Defined Thru, Defined
Thru"  
Examples |  SENS:CORR:COLL:GUID:PATH:TMEThod 2,3,"Zero Thru"  
sense:correction:collect:guided:path:tmethod 2,3,"Defined Thru,Defined Thru"  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:PATH:TMEThod? <port1>,<port2> Always returns two parts: If the second part of the string is empty, adapter removal is NOT being performed. If the string is "Defined Thru, Defined Thru", adapter removal IS being performed.  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  The most accurate Thru method for the current cal.  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:PCAL:APPLy <bool>

Applicable Models: All (Read-Write) When enabled, and the following conditions
are met, the user's existing source power calibration array will be used when
acquiring calibration standard data:

  * The user is performing a vector calibration only (no power).
  * A valid source cal is present in the channel being calibrated.
  * The user has elected to enable this feature (via GUI or SCPI).

Note: This command MUST be sent AFTER setting up the connectors and kits for
the calibration session. Otherwise, the firmware can not determine which ports
are going to be used in the calibration session. Therefore, it can not check
if there is an applicable power calibration, because power calibrations are
per port.  
  
If this command is sent before setting connectors and kits, the following
error is displayed:  
  
+3068,"The request to use existing source cal array during calibration was
refused."  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<bool> |  Choose from: OFF (0)  Do not use existing source power calibration array when acquiring calibration standard data: ON (1)  Use existing source power calibration array when acquiring calibration standard data:  
Examples |  SENS:CORR:COLL:GUID:PCAL:APPL 1  
sense2:correction:collect:guided:pcal:apply 0  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:PCAL:APPLy?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:PORTs?

Applicable Models: All (Read-only) Returns the list of ports being calibrated
by an active calibration session.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
Examples |  SENS:CORR:COLL:GUID:PORT?  
sense2:correction:collect:guided:ports?  
Return Type |  List of numbers  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:PREFerence:SLIDingload <char>

Applicable Models: All (Read-Write) Specifies the behavior for guided cal
steps that involve a sliding load in a cal that is about to be performed. Send
this command BEFORE sending the Guided INIT command. Although the term
'Preference' is used in the command, this is NOT a VNA preference. This
setting does NOT survive instrument preset or reboot. It remains ONLY for the
duration of the Guided Cal.  
---  
Parameters |   
<char> |  Behavior when measurements of sliding load are acquired. Choose from: DIALog \- The Sliding load dialog box appears when the acquire command is received for a sliding load step. All slide positions are measured (with a user-interface prompt) from a single invocation of the acquire command. ITERate - Each invocation of the acquire command for a sliding load step measures a single slide position and increments the slide position counter. No Move Sliding Load prompt is presented on the VNA screen.  
Examples |  SENS:CORR:COLL:GUID:PREF:SLID ITER [See example program](../../GPIB_Example_Programs/Perform_a_Guided_Cal_with_Sliding_Load.md)  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:PREFerence:SLIDingload?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  DIALog  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:SAVE[:IMMediate] [bool]

Applicable Models: All (Write-only) Completes the guided cal by computing the
error correction terms, turning Correction ON, and saving the calibration to a
Cal Set. If all of the required standards have not been measured, the
calibration will not complete properly. [Learn all about Cal
Sets.](../../../S3_Cals/Cal_Sets.htm)  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
[bool] |  Optional argument. If unspecified, the default behavior is the current VNA preference setting of [SENSe:CORRection:PREFerence:CSET:SAVE](Sense_Correction.md#CsetSave). OFF (0)  Save cal data ONLY to a Cal Register. ON (1) Save cal data to a Cal Register and a User Cal Set. The filename is automatically generated.

  * For application channels (Gain Compression, SMC/VMC, Noise Figure, IMD and so forth), this command saves ONLY to a Cal Register. Use [SENS:CORR:CSET:COPY](CorrCset.md#copy) to copy the cal register to a named calset.
  * For a [Calibrate All Channels](../../../S3_Cals/Calibrate_All_Channels.md) session, this argument is ignored. Instead, use [SYST:CAL:ALL:CSET:PREFix](../SystCalAll.md#csetPrefix).

  
Examples |  SENS:CORR:COLL:GUID:SAVE  
sense2:correction:collect:guided:save:immediate 0  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:SAVE:CSET <cal set name or guid>

Applicable Models: All (Write-only) Completes the guided cal by computing the
error correction terms, turning Correction ON, and saving the calibration to
an existing, specified Cal Set. This command performs the same function as
[SENSe:CORRection:COLLect:GUIDed:SAVE](CorrGuided.md#gSave), except this
command allows the name or GUID of the Cal Set to be specified. [Learn all
about Cal Sets.](../../../S3_Cals/Cal_Sets.htm) Note: This command is NOT
supported for application channels (Gain Compression, SMC/VMC, Noise Figure,
IMD and so forth). Use [SENS:CORR:COLL:GUID:SAVE](CorrGuided.md#gSave) and
save to a cal register. You can then use
[SENS:CORR:CSET:COPY](CorrCset.md#copy) to copy the cal register to a named
Cal Set.

  * Use this command instead of specifying the optional name or GUID argument in [SENS:CORR:COLL:GUID:INIT](CorrGuided.md#gInit).
  * Use [SENS:CORRection:CSET](CorrCset.md) commands to get names or GUIDs of existing Cal Sets.
  * The cal data is also saved to the channel Cal Register.
  * If all of the required standards have not been measured, the calibration will not complete properly.

### For Calibrate All Channels

When this command is used during a Cal All session, the <cal set name>
argument sets the User Cal Set prefix. All generated Cal Sets will be preceded
with this string name.

  * Cal Set prefix can also be set using [SYST:CAL:ALL:CSET:PREFix](../SystCalAll.md#csetPrefix). When the Cal Set prefix has already been set with [SYST:CAL:ALL:CSET:PREFix](../SystCalAll.md#csetPrefix), this command overwrites it.
  * When <cal set name> is an empty string, a User Cal Set will not be saved. Only Cal Registers will be saved.

  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<cal set name or guid> |  String - Name (or GUID of an existing Cal Set) of Cal Set to be saved. If the Cal Set already exists, it will be overwritten. If specifying a GUID, curly brackets must be included. See [Calibrate All Channels](CorrGuided.md#CalAll) note (above).  
Examples |  SENS:CORR:COLL:GUID:SAVE:CSET "{2B893E7A-971A-11d5-8D6C-00108334AE96}" sense:correction:collect:guided:save:cset "MyCalSet"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:STATes[:CATalog]? STAN<n>

Applicable Models: All (Read-only) Returns an array of ecal states used for
the standard number.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
STAN<n> |  Choose from:STAN1, STAN2, etc. through STANn where n is the number of cal standard connection steps for the calibration. Note: You do not necessarily have to invoke these connection steps in sequential order.  
Examples |  SENS:CORR:COLL:GUID:STAT? STAN1  
Return Type |  String  
Default |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:STEPs?

Applicable Models: All (Read-only) Returns the number of measurement steps
required to complete the current guided calibration. This command is sent
after the SENS:CORR:COLL:GUID:INIT, SENS:CORR:COLL:GUID:CONN:PORT and
SENS:CORR:COLL:GUID:CKIT:PORT commands.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
Examples |  SENS:CORR:COLL:GUID:STEP?  
sense2:correction:collect:guided:steps?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:GUIDed:SWEep:CHANnel:AOFF

Applicable Models: All (Write-only) Clears ALL flags for channels to sweep
during calibration. To flag a channel, see
[SENS:CORR:COLL:GUID:SWE:CHAN](CorrGuided.md#SweepChan).  This is equivalent
with [SENS:CORR:COLL:SWE:CHAN:AOFF](Sense_Correction.md#CalWindowSweepAoff).  
---  
Examples |  SENS:CORR:COLL:GUID:SWE:CHAN:AOFF sense:correction:collect:guided:sweep:channel:aoff  
Default |  Not applicable  
  
* * *

## SENSe<cnum>:CORRection:COLLect:GUIDed:SWEep:CHANnel<cnum2>[:STATe] <bool>

Applicable Models: All (Write-only) Specifies an alternate channel (other than
the calibration channel) to be viewed while using the calibration wizard.
When this command is sent, the <cnum2> channel is 'flagged' to be swept during
calibration.  The flag is cleared when the channel is deleted, if the
Measurement Class is changed, or if all measurements are deleted from the
channel. If the same channel number is recreated, this command must be sent
again to sweep the channel during a calibration. The flag is NOT saved with an
instrument state. A Preset or Instrument State Recall deletes the channel.
This is equivalent with
[SENSe:CORRection:COLLect:SWEep:CHANnel](Sense_Correction.md#CalWinSweepChan).
Note: This command is intended to be used in conjunction with the interactive
calibration wizard.  
---  
Parameters |   
<cnum> |  The channel to be calibrated. If unspecified, value is set to 1.  
<cnum2> |  The channel to sweep when waiting to measure a standard. This channel must already exist with at least one measurement in the channel. If this channel is in continuous sweep mode, it must have the same attenuator settings and path configuration (PNA-X only).  
<bool> |  Channel sweep state. Choose from: ON (or 1) - Sweep the channel during calibration. OFF (or 0) - Do NOT sweep the channel during calibration.  
Examples |  SENS:CORR:COLL:GUID:SWE:CHAN2 1 sense2:correction:collect:guided:sweep:channel3:state off  
Query Syntax |  Not Applicable  
Default |  OFF  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:THRU:PORTs <t1a, t1b, t2a, t2b, t3a,
t3b...>

Applicable Models: All (Read-Write) For calibrating more than 2-ports ONLY.
Specifies the port pairs for the Thru connections of the calibration. Send the
query form of this command to learn the Thru pairs determined by SmartCal.
Note: Sending this command will overwrite the VNAs SmartCal determinations for
the thru ports. Send this command ONLY if you have a deliberate reason for
overwriting the SmartCal logic. See [Thru Pairs
Sequence](CorrGuided.htm#THRUPairs) to learn how to send this and other Thru
commands.  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<t1a,t1b...> |  Always specify port numbers in pairs: For example: 1,2 or 1,2,1,3

  * For 3-port cals, specify two or three pairs.
  * For 4-port cals, specify from three up to six pairs.

  
Examples |  SENS:CORR:COLL:GUID:THRU:PORT 1,2,1,3,1,4 '4-port measurement sense:correction:collect:guided:thru:ports 1,2,2,3 '3-port measurement  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:THRU:PORTs?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Port pairings that were used in the previous cal.  
  
### THRU Pairs sequence

The SmartCal logic always determines the best calibration based on your
specified connectors and ports.

The following three commands overwrite the SmartCal logic. Send these commands
ONLY if you have a deliberate reason for overwriting the SmartCal logic.

  * [sens:corr:coll:guid:thru:ports](CorrGuided.md#pairs) <p1, p2>

  * [sens:corr:coll:guid:path:tmet](CorrGuided.md#PathTMethod) <p1,p2, thrutype>

  * [sens:corr:coll:guid:path:cmet](CorrGuided.md#PathCmethod) <p1,p2, calmethod>

When sending one or more of these commands, they must be sent in the following
sequence with the other commands listed here.

Note: The GUID:INIT command is sent before and after these commands.

  1. [sens:corr:coll:guid:conn:port(n)](CorrGuided.md#gConSelect)

  2. [sens:corr:coll:guid:ckit:port](CorrGuided.md#gKit)[(n)](CorrGuided.md#gConSelect)

  3. [sens:corr:coll:guid:init](CorrGuided.md#gInit)

  4. [sens:corr:coll:guid:thru:ports](CorrGuided.md#pairs) <p1, p2>

  5. [sens:corr:coll:guid:path:tmet](CorrGuided.md#PathTMethod) <p1,p2, thrutype>

  6. [sens:corr:coll:guid:path:cmet](CorrGuided.md#PathCmethod) <p1,p2, calmethod>

  7. [sens:corr:coll:guid:path:cmet](CorrGuided.md#PathCmethod)? <p1,p2> (recommended)

  8. [sens:corr:coll:guid:init](CorrGuided.md#gInit)

* * *

##
SENSe<ch>:CORRection:COLLect:GUIDed:UNCertainty:CHARacterize:CABLe[:INITiate]
<pNum>,<iterations>

Applicable Models: N522xB, N523xB, N524xB (Write-only) Initializes a cable
repeatability characterization for the specified channel and port. [Learn more
about Dynamic Uncertainty.](../../../S3_Cals/Dynamic_Uncertainty.htm) The
following existing commands are then used to perform the initialized
repeatability or noise characterization:
SENSe<ch>:CORRection:COLLect:GUIDed:STEPs?
SENSe<ch>:CORRection:COLLect:GUIDed:DESCription? <stepNum>
SENSe<ch>:CORRection:COLLect:GUIDed:ITERations:MINimum? <stepNum>
SENSe<ch>:CORRection:COLLect:GUIDed:ACQuire <stepNum>
SENSe<ch>:CORRection:COLLect:GUIDed:ITERations:COUNt? <stepNum>
SENSe<ch>:CORRection:COLLect:GUIDed:ITERations:RESet <stepNum>
SENSe<ch>:CORRection:COLLect:GUIDed:SAVE[:IMMediate]
SENSe<ch>:CORRection:COLLect:GUIDed:ABORt  
---  
Parameters |   
<ch> |  Channel number of the characterization, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<pNum> |  VNA port number on which the cable repeatability is to be performed.  
<iterations> |  Number of Iterative connections of the standards to be measured for the characterization.  
Examples |  SENS1:CORR:COLL:GUID:UNC:CHAR:CABL 2,5 [See example program](../../GPIB_Example_Programs/Dynamic_Uncertainty.md)  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1  
  
* * *

##
SENSe<ch>:CORRection:COLLect:GUIDed:UNCertainty:CHARacterize:NOISe[:INITiate]
<firstPort>,<secondPort>,<iterations>

Applicable Models: N522xB, N523xB, N524xB (Write-only) Initializes a noise
characterization for the specified channel and ports. [Learn more about
Dynamic Uncertainty.](../../../S3_Cals/Dynamic_Uncertainty.htm) The following
existing commands are used to perform the initialized noise characterization:
SENSe<ch>:CORRection:COLLect:GUIDed:STEPs?
SENSe<ch>:CORRection:COLLect:GUIDed:DESCription? <stepNum>
SENSe<ch>:CORRection:COLLect:GUIDed:ITERations:MINimum? <stepNum>
SENSe<ch>:CORRection:COLLect:GUIDed:ACQuire <stepNum>
SENSe<ch>:CORRection:COLLect:GUIDed:ITERations:COUNt? <stepNum>
SENSe<ch>:CORRection:COLLect:GUIDed:ITERations:RESet <stepNum>
SENSe<ch>:CORRection:COLLect:GUIDed:SAVE[:IMMediate]
SENSe<ch>:CORRection:COLLect:GUIDed:ABORt  
---  
Parameters |   
<ch> |  Channel number of the characterization, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<firstPort> |  First VNA port number on which the noise characterization is to be performed.  
<secondPort> |  Second VNA port number on which the noise characterization is to be performed.  
<iterations> |  Number of Iterative measurements to be made for each connected standard.  
Examples |  SENS1:CORR:COLL:GUID:UNC:CHAR:NOIS 1,2,5 [See example program](../../GPIB_Example_Programs/Dynamic_Uncertainty.md)  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:UNCertainty[:ENABle] <bool>

Applicable Models: N522xB, N523xB, N524xB (Write-Read) Sets and returns the
ON/OFF state which determines if the calibration that is about to be performed
will support Dynamic Uncertainty for S-Parameters (Opt. S93015A/B).  Dynamic
Uncertainty for S-Parameters is supported ONLY for calibrations on standard
S-Parameter channels. Calibrations performed with that feature enabled do NOT
support the use of ALL traditional GUIDed calibration commands.  Then these
existing commands are used for performing calibration:
SENSe<ch>:CORRection:COLLect:GUIDed:CKIT:PORT<pnum>[:SELect] <kit>
SENSe<ch>:CORRection:COLLect:GUIDed:INITiate[:IMMediate] [string][,
bool][,char] SENSe<ch>:CORRection:COLLect:GUIDed:STEPs?
SENSe<ch>:CORRection:COLLect:GUIDed:DESCription? <stepNum>
SENSe<ch>:CORRection:COLLect:GUIDed:ACQuire <stepNum>
SENSe<ch>:CORRection:COLLect:GUIDed:SAVE[:IMMediate] where these commands
might also optionally be used in performing the calibration:
SENSe<ch>:CORRection:COLLect:GUIDed:CKIT:PORT<pnum>:CATalog?
SENSe<ch>:CORRection:COLLect:GUIDed:ABORt
[SENSe:CORRection:PREFerence:ECAL:ORIentation[:STATe]
<ON|OFF>](Sense_Correction.htm#Orie) [SENSe:CORRection:PREFerence:ECAL:PMAP
<module>, <string>](Sense_Correction.htm#Pmap) Dynamic Uncertainty must be
enabled using this command before starting the calibration procedure because
this command controls the way connectors and calkits are assigned to ports
during calibration. Therefore, this command must be enabled before any of the
following commands to ensure that the connector and calkit settings will be
set/queried correctly:
SENSe<ch>:CORRection:COLLect:GUIDed:CKIT:PORT<pnum>[:SELect] <kit>
SENSe<ch>:CORRection:COLLect:GUIDed:CKIT:CATalog?
SENSe<ch>:CORRection:COLLect:GUIDed:CONNector:PORT<pnum>[:SELect] <conn>
SENSe<ch>:CORRection:COLLect:GUIDed:CONNector:CATalog?  
---  
Parameters |   
<bool> |  Enable ON/OFF state. Choose from: **ON** or **1**  The next calibration INITialized for the channel will support Dynamic Uncertainties for S-Parameters. **OFF** or **0** -\- The next calibration INITialized for the channel will NOT support Dynamic Uncertainties for S-Parameters.  
Examples |  SENS1:CORR:COLL:GUID:UNC ON [See example program](../../GPIB_Example_Programs/Dynamic_Uncertainty.md)  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:UNCertainty[:ENABle]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

