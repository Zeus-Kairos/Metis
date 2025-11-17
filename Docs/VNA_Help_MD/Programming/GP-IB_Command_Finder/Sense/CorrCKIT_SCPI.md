# Sense:Correction:CKIT Commands

* * *

Manages the list of cal kits that are installed in the VNA.

SENSe:CORRecion:CKIT [CLEar](CorrCKIT_SCPI.md#clear) [COUNt?](CorrCKIT_SCPI.md#count) ECAL | [CHARacterize More commands](ECalCharacterize.md) | [CLISt?](CorrCKIT_SCPI.md#Clist) | DMEMory | [CLEar](CorrCKIT_SCPI.md#dmemClear) | [IMPort](CorrCKIT_SCPI.md#dmemImport) | [EXPort](CorrCKIT_SCPI.md#EcalExport) | [INFormation](CorrCKIT_SCPI.md#ECALInf) | KNAMe | [INFormation](CorrCKIT_SCPI.md#knameInf) | [LIST?](CorrCKIT_SCPI.md#List) | [ORIent?](CorrCKIT_SCPI.md#Orient) | PATH | [COUNt?](CorrCKIT_SCPI.md#ECalPathCount) | [DATA?](CorrCKIT_SCPI.md#EcalPathData) | PCHeck? | TEMPrature | [CONDition](CorrCKIT_SCPI.md#ECalTempCond) | [[:VALue]](CorrCKIT_SCPI.md#EcalTempVal) [EXPort](CorrCKIT_SCPI.md#Export) [IMPort](CorrCKIT_SCPI.md#import) [INITialize](CorrCKIT_SCPI.md#initialize) [LOAD](CorrCKIT_SCPI.md#load)  
---  
  
  * Click on a red keyword to view the command details.

  * Red is a superseded command

  * New [See Calibrating the VNA Using SCPI](../../Learning_about_GPIB/Calibrating_the_Analyzer_Using_SCPI.md)

  * [Learn about Modifying Cal Kits](../../../S3_Cals/ModifyCalKits.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## SENSe:CORRection:CKIT:CLEar[:IMMediate] [ckit]

Applicable Models: All (Write-only) Deletes installed cal kits.  
---  
Parameters |   
[ckit] |  Optional String. Cal Kit to delete. If not specified, all VNA Cal kits are deleted, including custom kits.  
Examples |  SENS:CORR:CKIT:CLE sense:correction:ckit:clear:immediate "85052B"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe:CORRection:CKIT:COUNt?

Applicable Models: All (Read-only) Returns the number of installed cal kits.  
---  
Examples |  SENS:CORR:CKIT:COUNt?  
Query Syntax |  SENS:CORR:CKIT:COUNt?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe:CORRection:CKIT:ECAL<mod>:CLISt?

Applicable Models: All (Read-only) Returns a list of characterizations stored
in the specified ECal module.  
---  
Parameters |   
<mod> |  ECal module from which to read user characterization numbers. Choose from 1 to 254. If unspecified, value is set to 1.  
Examples |  Module 1 contains User Characterizations 1 and 3. SENSe:CORRection:CKIT:ECAL:CLIST? 'Returns the following (0 always indicates the factory characterization): 0,1,3  
Return Type |  Numeric list, separated by commas.  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe:CORRection:CKIT:ECAL<mod>:DMEMory:CLEar <kitName>

Applicable Models: All (Write-only) Deletes user characterizations from VNA
disk memory.  
---  
Parameters |   
<mod> |  ECal module from which to read user characterization numbers. Choose from 1 to 254. If unspecified, value is set to 1.  
<kitName> |  Optional String argument. ECal Model, User Characterization name + " ECal", and serial number of the ECal module, separated by spaces. See examples below. If unspecified, ALL User Characterizations that are stored in VNA disk memory are deleted.  
Examples |  'These examples all use "MyUserChar" as the User characterization name. 'The "My User Char" characterization is deleted from disk memory. SENS:CORR:CKIT:ECAL:DMEM:CLE "N4433A MyUserChar ECal 00001" 'All User characterizations are deleted from disk memory. SENS:CORR:CKIT:ECAL:DMEM:CLE  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe:CORRection:CKIT:ECAL<mod>:DMEMory:IMPort <file>

Applicable Models: All (Write-only) After the VNA disk memory is
[Exported](CorrCKIT_SCPI.md#EcalExport) to a file, use this command to Import
the file into VNA disk memory, which allows the User Characterization to be
used with the VNA and ECal module. Note: An ECal confidence check can NOT be
performed remotely from User Characterizations that are stored on the VNA
disk.  
---  
Parameters |   
<mod> |  ECal module from which to read user characterization numbers. Choose from 1 to 254. If unspecified, value is set to 1.  
<file> |  String. Full path and file name of file that was exported.  
Examples |  SENS:CORR:CKIT:ECAL:DMEM:IMP "D:\myDiskUserChar.euc"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe:CORRection:CKIT:ECAL<mod>:EXPort <kit>[,<file>][,<NewName>]]

Applicable Models: All (Write-only) Saves an existing ECal characterization to
a file. Use this command to archive the user characterization or to move the
characterization to a different VNA for use with the specified ECal module.
After exporting the user characterization, use
[SENS:CORR:CKIT:ECAL:DMEM:IMPort](CorrCKIT_SCPI.md#dmemImport) to make the
user characterization available for use.  
---  
Parameters |   
<mod> |  ECal module from which to read user characterization numbers. Choose from 1 to 254. If unspecified, value is set to 1.  
<kit> |  String. Not case sensitive. ECal Model, User char name + " ECal", and serial number of the ECal module used for the characterization, separated by spaces. See examples below. If the model and serial number of the module is not found, an error is returned.  
[<file>] |  Optional String argument. Path and filename of the user characterization. If not specified, the file is saved using characterization name + ".euc". If the path is not specified, it is stored in C:\ProgramData\Keysight\Network Analyzer\ECal User Characterizations\\. The extension ".euc" is appended if one is not specified.  
[<NewName>] |  Optional String argument. This allows you to change the name for the User Characterization. When specified, the new name is saved in the file with the characterization. If unspecified, the existing user characterization name is saved. Note: If this argument is specified, the second argument (<file>) must also be specified.  
Examples |  'These examples all use "MyUserChar" as the User characterization name. 'All parameters specified SENS:CORR:CKIT:ECAL:EXP "N4433A MyUserChar ECal 00001","myUserChar.euc","NewUserChar" 'First two parameters are specified sense:correction:ckit:ecal:export "N4691B MyUserChar ECal 00500","myUserChar.euc" 'Only first parameter is specified SENS:CORR:CKIT:ECAL:EXP "N4433A MyUserChar ECal 00001"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe:CORRection:CKIT:ECAL<mod>:INFormation? [<char>]

Applicable Models: All (Read-only) Reads the identification and
characterization information from the specified ECal module. Note: To read
user-characterization information that is stored in VNA disk memory, then use
[SENS:CORR:CKIT:ECAL:KNAM:INF?](CorrCKIT_SCPI.md#knameInf)  
---  
Parameters |   
<mod> |  ECal module from which to read characterizations. Choose from 1 through 254. If unspecified, value is set to 1. Do NOT assume the <mod> number is the order in which ECal modules were connected. Use [SENS:CORR:CKIT:ECAL:LIST?](CorrCKIT_SCPI.md#List) to read a list of <mod> numbers of currently-attached ECal modules.  
<char> |  Optional argument. Specifies which characterization to read information from. If not specified, value is set to CHAR0. Choose from:

  * CHAR0 Factory characterization (data that was stored in the ECal module by Keysight)
  * CHAR1 User characterization #1
  * CHAR2 User characterization #2
  * \- through -
  * CHAR12 User characterization #12

  
Examples |  SENS:CORR:CKIT:ECAL2:INFormation? char5 'Example return string: "ModelNumber: 85092-60007, SerialNumber: 01386, ConnectorType: N5FN5F, PortAConnector: Type N (50) female, PortBConnector: Type N (50) female, MinFreq: 30000, MaxFreq: 9100000000, NumberOfPoints: 250, Calibrated: July 4 2002"  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe:CORRection:CKIT:ECAL<mod>:KNAMe:INFormation? <kitName>

Applicable Models: All (Read-only) Reads the identification and
characterization information from the specified ECal module or VNA disk
memory. [Learn more about User Characterization in VNA Disk
Memory.](../../../S3_Cals/ECal_User_Characterization.htm#DiskMemoryDiag)  
---  
Parameters |   
<mod> |  ECal module from which to read user characterization numbers. Choose from 1 to 254. If unspecified, value is set to 1.  
<kitName> |  String. ECal model and characterization to read information from, enclosed in quotes, in the following format: <model> <name> ECal <serial number> Where: <model>: Always required <name>:

  * For the factory characterization, do not specify.
  * For a user-characterization stored in the module, use User <n> in the string, where <n> is the user-characterization number. Not case sensitive. Separate User and <n> with a space.
  * For a user-characterization stored in VNA disk memory, use <charName> from [SENS:CORR:CKIT:ECAL:CHAR:DMEM:SAVE <charName>](ECalCharacterize.md#dmemSave)

ECal \- not case sensitive <serial number>: Optional. Include when two or more
ECal modules with same model number are attached to the VNA, Each item is
separated with a space.  
Examples |  'For a factory characterization in module memory:  
SENS:CORR:CKIT:ECAL:KNAM:INF? "N4433A ECal" 'For user characterization in
module memory with optional serial number:  
SENS:CORR:CKIT:ECAL:KNAM:INF? "N4433A User 1 ECal 00028" 'For user
characterization "foo" in disk memory:  
SENS:CORR:CKIT:ECAL:KNAM:INF? "N4433A foo ECal 00028" 'Example return string:
"ModelNumber: N4433A, SerialNumber: 00028, ConnectorType: N5FN5F,
PortAConnector: Type N (50) female, PortBConnector: Type N (50) female,
MinFreq: 30000, MaxFreq: 9100000000, NumberOfPoints: 250, Calibrated: July 4
2002"  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe:CORRection:CKIT:ECAL<mod>:LIST?

Applicable Models: All (Read-only) Returns a list of index numbers for ECal
modules that are currently attached to the VNA. Use these numbers (called
<mod> in VNAHelp) to refer to the ECal module using SCPI commands.  
---  
<mod> |  ECal module from which to read user characterization numbers. Choose from 1 to 254. If unspecified, value is set to 1.  
Examples |  SENS:CORR:CKIT:ECAL:LIST? 'If 2 modules are attached to the VNA  
'then the returned list will be: +1,+2 'If NO modules are attached to the VNA  
'then the returned list will be: +0 [See example program using this
command](../../GPIB_Example_Programs/Set_ECal_States.htm).  
Return Type |  Numeric list, separated by commas.  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:CKIT:ECAL<mod>:ORIent? <pnaPort>[,<charN>]

Applicable Models: All (Read-only) Returns the ECal port that is connected to
the specified VNA port. A calibration does not have to be in process.  To
check if a specific VNA port is connected to a specific ECal port, use
SENSe<ch>:CORRection:CKIT:ECAL<mod>:PCHeck? <vnaPort>,<ecalPort>[,<charN>].  
---  
<ch> |  Channel number that contains the frequency range to be calibrated.  
<mod> |  ECal module number. Choose from 1 through 254. If unspecified (only one ECal module is connected to the USB), <n> is set to 1. If two or more modules are connected, use [SENS:CORR:CKIT:ECAL:LIST?](CorrCKIT_SCPI.md#List) to determine how many, and [SENS:CORR:CKIT:ECAL:INF?](CorrCKIT_SCPI.md#ECALInf) to verify their identities.  
<pnaPort> |  VNA port number.  
<charN> |  Optional argument. If unspecified, factory data (CHAR0) is used. User Characterization number that matches the physical adapters/fixtures that are on the ECal module. This aids in determining the orientation of the ECal module. Choose from:

  * CHAR0 Factory characterization (data that was stored in the ECal module by Keysight)
  * CHAR1 User characterization #1
  * CHAR2 User characterization #2

and so forth up to:

  * CHAR12 User characterization #12

Beginning with A.08.33, up to 12 User Characterizations can be stored in a
single ECal module. Previous releases allowed up to 5. [Learn
more.](../../../S3_Cals/ECal_User_Characterization.htm#Overview)  
Examples |  SENS1:CORR:CKIT:ECAL1:ORI? 2 sense2:correction:ckit,ecal1:orient? 2, char2  
Return Type |  The returned ECal port number is a 1-based number: 1 = Port A, 2 = Port B, 3 = Port C, 4 = Port D. Zero (0) is returned when the auto-orientation routine is unable to resolve the orientation.  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe:CORRection:CKIT:ECAL<mod>:PATH:COUNt? <path>

Applicable Models: All (Read-only) Returns the number of unique states that
exist for the specified path name on the selected ECal module.  This command
performs exactly the same function as
[CONT:ECAL:MOD:PATH:COUNt?](../Control.md#ECalPathCount) Use the
[CONT:ECAL:MOD:PATH:STAT](../Control.md#EcalPathState) command to set the
module into one of those states.  Use
[SENS:CORR:CKIT:ECAL:PATH:DATA?](CorrCKIT_SCPI.md#EcalPathData) to read the
data for a state.  
---  
Parameters |   
<mod> |  USB number of the ECal module. Choose from 1 to 254. If unspecified (only one ECal module is connected to the USB), <n> is set to 1. If two or more modules are connected, use [SENS:CORR:CKIT:ECAL:LIST?](CorrCKIT_SCPI.md#List) to determine how many, and [SENS:CORR:CKIT:ECAL:INF?](CorrCKIT_SCPI.md#ECALInf) to verify their identities.  
<path> |  Name of the path for which to read number of states. Choose from: Reflection paths

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

  
Examples |  CONT:ECAL:MOD:PATH:COUNt?  
control:ecal:module2:path:count?  
Return Type |  Integer  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:CKIT:ECAL<mod>:PATH:DATA? <path>, <stateNum>[,<char>]

Applicable Models: All (Read-only) Returns the data for a state from the
memory of the selected ECal module. The returned data is interpolated if
necessary to have the same stimulus values as the specified channel <ch>.

  * For a reflection path state, the data is reflection S-parameter data. The number of values equals the number of stimulus points on the channel multiplied by 2 (because they are complex numbers).
  * For a transmission path state, the data is all 4 S-parameters of the state. The number of values returned is 4 times that of a reflection state.

The data is returned in the same format as
[CALC:MEAS:DATA:SNP?](../Calculate/MeasureDATA.md#CALCulate:MEASure:DATA:SNP:PORTs)
Note: This command returns SNP data without header information, and in
columns, not in rows as .SnP files. This means that the data returned from
this command sends all frequency data, then all Sx1 magnitude or real data,
then all Sx1 phase or imaginary data, and so forth.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<mod> |  Optional argument. USB number of the ECal module. Choose from 1 through 254. If unspecified (only one ECal module is connected to the USB), <num> is set to 1. If two or more modules are connected, use [SENS:CORR:CKIT:ECAL:LIST?](CorrCKIT_SCPI.md#List) to determine how many, and [SENS:CORR:CKIT:ECAL:INF?](CorrCKIT_SCPI.md#ECALInf) to verify their identities.  
<path> |  Name of the path for which to read number of states. Choose from: Reflection paths

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

  
<stateNum> |  Number of the state to set. Refer to the following table to associate the <stateNum> with a state in your ECal module. In addition, [CONT:ECAL:MOD:PATH:COUNt?](../Control.md#ECalPathCount) returns the number of states in the specified ECal module. |  <stateNum> |  N4432A and  
N4433A States |  N4431A States |  N469x and N755x States** |  8509x States  
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
  
<char> |  Optional argument. Specifies which characterization within the ECal module to read information from. If not specified, value is set to CHAR0. Choose from:

  * CHAR0 Factory characterization (data that was stored in the ECal module by Keysight)
  * CHAR1 User characterization #1
  * CHAR2 User characterization #2

and so forth up to:

  * CHAR12 User characterization #12

  
Examples |  SENS:CORR:CKIT:ECAL1:PATH:DATA? A,1  
Return Type |  S1P or S2P  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:CKIT:ECAL<mod>:PCHeck? <vnaPort>,<ecalPort>[,<charN>]

Applicable Models: All (Read-only) This command checks if a specific VNA port
is connected to specific ECal port and returns 1 when it is connected.  To
detect which ECal port is connected to a VNA port, use
SENS:CORR:COLL:CKIT:ECAL:ORIend? <vna_port> [,<user_char>].  
---  
<ch> |  Channel number that contains the frequency range to be calibrated.  
<mod> |  ECal module number. Choose from 1 through 254. If unspecified (only one ECal module is connected to the USB), <n> is set to 1. If two or more modules are connected, use [SENS:CORR:CKIT:ECAL:LIST?](CorrCKIT_SCPI.md#List) to determine how many, and [SENS:CORR:CKIT:ECAL:INF?](CorrCKIT_SCPI.md#ECALInf) to verify their identities.  
<vnaPort> |  VNA port number.  
<ecalPort> |  ECAL port number.  
<charN> |  Optional argument. If unspecified, factory data (CHAR0) is used. User Characterization number that matches the physical adapters/fixtures that are on the ECal module. This aids in determining the orientation of the ECal module. Choose from:

  * CHAR0 Factory characterization (data that was stored in the ECal module by Keysight)
  * CHAR1 User characterization #1
  * CHAR2 User characterization #2

and so forth up to:

  * CHAR12 User characterization #12

Beginning with A.08.33, up to 12 User Characterizations can be stored in a
single ECal module. Previous releases allowed up to 5. [Learn
more.](../../../S3_Cals/ECal_User_Characterization.htm#Overview)  
Examples |  SENS:CORR:COLL:CKIT:ECAL:PCH? 2,4  
Return Type |  Boolean (0 or 1).  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:CKIT:ECAL<mod>:TEMPerature:CONDition

Applicable Models: All (Read-only) Reads the temperature condition at
microcircuit in the specified ECal module. The returned value is either COLD,
NOMinal, HOT, or UNKNown. If the ECal module does not support this quer,
UNKNown will be returned.  
---  
<ch> |  Channel number. This parameter is ignored..  
<mod> |  ECal module number. Choose from 1 through 254. If unspecified (only one ECal module is connected to the USB), <n> is set to 1. If two or more modules are connected, use [SENS:CORR:CKIT:ECAL:LIST?](CorrCKIT_SCPI.md#List) to determine how many, and [SENS:CORR:CKIT:ECAL:INF?](CorrCKIT_SCPI.md#ECALInf) to verify their identities. This number may not be the order in which ECal modules were connected.  
Examples |  SENS:CORR:CKIT:ECAL2:TEMPerature:CONDtion? COLD  
Return Type |  Enum {COLD|NOMinal|HOT|UNKNOwn}  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:CKIT:ECAL<mod>:TEMPerature[:VALue]

Applicable Models: All (Read-only) Reads the temperature at microcircuit in
the specified ECal module. If the ECal module does not support this query, a
temperature of -999.0°C will be returned.  
---  
<ch> |  Channel number. This parameter is ignored..  
<mod> |  ECal module number. Choose from 1 through 254. If unspecified (only one ECal module is connected to the USB), <n> is set to 1. If two or more modules are connected, use [SENS:CORR:CKIT:ECAL:LIST?](CorrCKIT_SCPI.md#List) to determine how many, and [SENS:CORR:CKIT:ECAL:INF?](CorrCKIT_SCPI.md#ECALInf) to verify their identities. This number may not be the order in which ECal modules were connected.  
Examples |  SENS:CORR:CKIT:ECAL2:TEMPerature? +3.06752624512E+001 SENS:CORR:CKIT:ECAL3:TEMPerature? -9.99000000000E+002  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe:CORRection:CKIT:EXPort <kit>[,<file>]

Applicable Models: All (Write-only) Saves an existing cal kit definitions to a
file. Use this command to archive or move a user-defined or modified cal kit
to a different VNA. After exporting the cal kit, use
[SENS:CORR:CKIT:IMPort](CorrCKIT_SCPI.md#import) to make the cal kit
available for use on the VNA. This command provides the same behavior as the
Installed Kits - Save As button on the [Edit VNA Cal
Kits](../../../S3_Cals/ModifyCalKits.htm#EditKitDiagHelp) dialog.  
---  
Parameters |   
<kit> |  String. Not case sensitive. Name of the cal kit to export, as seen in the Cal Kits field of the [Select DUT Connectors and Cal Kits](../../../S3_Cals/Calibration_Wizard.md#GuidConnKit) dialog of a SMART Cal.  
<file> |  Optional String argument. Path and filename to where the Cal Kit file is to be saved. If not specified, the file is saved using <kit> \+ ".ckt". If the path is not specified, it is stored in C:/Program Files/Keysight/Network Analyzer/PNACalKits/User.  
Examples |  'File unspecified SENS:CORR:CKIT:EXP "MyCalKit" 'Both parameters are specified sense:correction:ckit:export "MyCalKit","C:\myBackupCalKit.ckt"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe:CORRection:CKIT:IMPort <string>

Applicable Models: All (Write-only) Imports the specified cal kit (.ckt file)
and appends the imported kit to the end of the list of kits.  Note: Although
there is no limit to the number of cal kits that can be imported, during an
[Unguided cal](../../../S3_Cals/Calibration_Wizard.md#unguided), you can
access ONLY mechanical cal kits #1 through #95.  
---  
Parameters |   
<string> |  Path and cal kit name.  
Examples |  SENSe:CORRection:CKIT:IMPort "c:\users\public\public documents\network analyzer\documents/85033D.ckt"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe:CORRection:CKIT:INITialize[:IMMediate] [ckit]

Applicable Models: All (Write-only) Restores default factory installed cal
kits. This command also selects kit number 1, as you would using
[SENS:CORR:COLL:CKIT:SEL 1](CorrCollCKIT.md#scccs). Therefore, if you intend
to work with a Cal Kit remotely, select the Cal Kit AFTER sending this
command.  Note: This command can also delete all existing User-defined Cal
Kits. However, if saved using Save As, these kits can be restored in the same
manner as after a VNA firmware upgrade. [Learn more about saving modified Cal
Kits.](../../../S3_Cals/ModifyCalKits.htm#EditKitDiagHelp)  
---  
Parameters |   
[ckit] |  Optional String. Cal Kit to restore. If not specified, all VNA factory Cal kits are restored.  
Examples |  SENS:CORR:CKIT:INITialize sense:correction:ckit:initialize:immediate "85052B"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe:CORRection:CKIT:LOAD <string>

Applicable Models: All (Write-only) Loads the specified collection of cal kits
from a .wks file. You can make your own collection of cal kits from the
[Advanced Modify Cal Kit](../../../S3_Cals/ModifyCalKits.md) menu.  
---  
Parameters |   
<string> |  Path and file name of the cal kit collection.  
Examples |  sense:correction:ckit:load "C:\ProgramData\Keysight\Network Analyzer\PnaCalKits\factory\wMyCalKits.wks"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

