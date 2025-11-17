# SENSe:CORR:CKIT:ECAL:CHARacterize Commands

* * *

Controls the settings used to perform an ECal User Characterization. These
commands do NOT perform the calibration that is required before measuring the
ECal module. An S-Parameter channel must already be calibrated. [Learn
more](ECalCharacterize.htm#Init).

SENSe:CORR:CKIT:ECAL:CHARacterize: [ACQuire](ECalCharacterize.md#acquire) [CNUMber](ECalCharacterize.md#Cnumber) CONNector | [CATalog?](ECalCharacterize.md#ConnCat) | [PORT<n>[:SELect]](ECalCharacterize.md#ConnPortSelect) DESCription | [PORT<n>[:SELect]](ECalCharacterize.md#DescPort) | [[STEP]?](ECalCharacterize.md#DescStep) | [USER](ECalCharacterize.md#descUser) | [VNA](ECalCharacterize.md#DescVNA) DMEMory | [SAVE](ECalCharacterize.md#dmemSave) [ID](ECalCharacterize.md#ID) [INITiate](ECalCharacterize.md#Init) INSitu | [ENABle](ECalCharacterize.md#InsituEnable) | [[STATe]](ECalCharacterize.md#InsituState) [SAVE](ECalCharacterize.md#save) [STEPs?](ECalCharacterize.md#steps)  
---  
  
Click on a keyword to view the command details.

Notes:

These commands provide for the following:

  * Measure the ECal module with adapters, cables, or fixtures to be included in the User Characterization.

  * Allow descriptive text to be entered.

  * Save the User Characterization to the ECal module or VNA disk memory. Up to 12 User Characterizations can be stored in an ECal module. [Learn more.](../../../S3_Cals/ECal_User_Characterization.md#SelModandLocation)

You can NOT perform a remote User Characterization of a 4-port ECal module
using a 2-port VNA. This can only be done from the front panel user interface.

### See Also

  * Example \- [Perform an ECal User Characterization](../../GPIB_Example_Programs/Perform_an_ECal_User_Characterization.md)

  * [Learn about ECal User Characterization](../../../S3_Cals/ECal_User_Characterization.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## SENSe<ch>:CORRection:CKIT:ECAL<mod>:CHARacterize:ACQuire STAN<step>

Applicable Models: All (Write-only) Initiates the measurement of the ECal
module. The user characterization process must have been initiated first using
[SENS:CORR:CKIT:ECAL:CHAR:INIT](ECalCharacterize.md#Init). Currently, only
ONE step is required to measure the ECal module. Note: This command is an
overlapped command. When
[*OPC](../../Learning_about_GPIB/Understanding_Command_Synchronization.md#opc)
is issued with it, the OPC bit in the VNAs Standard Event Status Register is
not set until this command has completed its operation. [Learn
more.](../../Learning_about_GPIB/Understanding_Command_Synchronization.htm)  
---  
Parameters |   
<ch> | Channel number being calibrated. If unspecified, value is set to 1. Channel number being calibrated.  
<mod> | ECal module from which to read user characterization numbers. Choose from 1 to 254. If unspecified, value is set to 1.  
<step> | Integer User characterization step number to be measured.  
Examples | SENS:CORR:CKIT:ECAL:CHAR:ACQ STAN1, *OPC  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:CORRection:CKIT:ECAL<mod>:CHARacterize:CNUMber <n>

Applicable Models: All (Read-Write) Sets and reads the number to which the
User Characterization will be stored in the ECal module. The number must be
set before sending [SENS:CORR:CKIT:ECAL:CHAR:INIT](ECalCharacterize.md#Init)
or the default value (1) will be used. This command is NOT necessary when
saving the User Characterization to the VNA disk memory.  
---  
Parameters |   
<ch> | Channel number being calibrated. If unspecified, value is set to 1  
<mod> | ECal module from which to read user characterization numbers. Choose from 1 to 254. If unspecified, value is set to 1.  
<n> | User Characterization number. Choose a value between 1 and 12.  
Examples | SENSe:CORR:CKIT:ECAL:CHAR:CNUM 2  
Query Syntax | SENSe<ch>:CORRection:CKIT:ECAL:CHARacterize:CNUMber?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## SENSe:CORRection:CKIT:ECAL<mod>:CHARacterize:CONNector:CATalog?

Applicable Models: All (Read-only) Returns a list of connector names that are
valid for use with user-characterized ECal modules. Use an item from the
returned list to specify a connector for
[SENS:CORR:CKIT:ECAL:CHAR:CONN:PORT](ECalCharacterize.md#ConnPortSelect). Use
only factory-defined connector types when you store a user characterization to
VNA disk memory.  
---  
Parameters |   
<mod> | ECal module from which to read user characterization numbers. Choose from 1 to 254. If unspecified, value is set to 1.  
Examples | SENS:CORR:CKIT:ECAL:CHAR:CONN:CAT? 'Example returned string: "APC 3.5 male, APC 3.5 female, Type N (50) female, Type N (50) male, APC 7, Type A (50), Type B"  
Return Type | Comma-separated string  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:CORRection:CKIT:ECAL<mod>:CHARacterize:CONNector:PORT<n>[:SELect]
<string>

Applicable Models: All (Read-Write) Specifies a connector type name for every
ECal module port used during the user characterization. Valid connector names
are returned using
[SENS:CORR:CKIT:ECAL:CHAR:CONN:CAT?](ECalCharacterize.md#ConnCat) This
command refers to the ECal ports by number instead of letter (1 = Port A, 2 =
Port B, and so forth). The connector names should be set for the ports before
sending [SENS:CORR:CKIT:ECAL:CHAR:INIT](ECalCharacterize.md#Init). The
following steps could be followed to ensure port connectors are specified
correctly:

  1. Use [SENS:CORR:CKIT:ECAL:CHAR:CONN:CAT?](ECalCharacterize.md#ConnCat) to query available connectors before specifying the port connector.
  2. Specify a connector type using this command. If the <string> parameter was incorrectly entered, an error will be returned.

Note: Use only factory-defined connector types when you store a user
characterization to VNA disk memory.  
---  
Parameters |   
<ch> | Channel number being calibrated. If unspecified, value is set to 1  
<mod> | ECal module from which to read user characterization numbers. Choose from 1 to 254. If unspecified, value is set to 1.  
<n> | ECal test port number for which a connector type will be specified. Choose 1 to 2 for a 2-port ECal module, 1 through 4 for a 4-port module.  
<string> | ECal connector type and gender (if applicable). When the User Characterization is to be stored in the ECal module, then the connector type is limited to a Factory-defined connector type. [See the list](../../../S3_Cals/Connectors_Tab.md#Connectors). When the User Characterization is to be stored in VNA disk memory, then the connector type can also be a User-defined connector type.  
Examples | SENS:CORR:CKIT:ECAL:CHAR:CONN:PORT2 "APC 3.5 female"  
Query Syntax | SENSe<ch>:CORRection:CKIT:ECAL:CHARacterize:CONNector:PORT<n>[:SELect]?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | "No adapter"  
  
* * *

## SENSe<ch>:CORRection:CKIT:ECAL<mod>:CHARacterize:DESCription[:STEP]?
<stepN>

Applicable Models: All (Read-only) Returns the connection description for the
specified step of the ECal user characterization process. The user
characterization process must have been initiated first using
[SENS:CORR:CKIT:ECAL:CHAR:INIT.](ECalCharacterize.md#Init)  
---  
Parameters |   
<ch> | Channel number being calibrated. If unspecified, value is set to 1  
<mod> | ECal module from which to read user characterization numbers. Choose from 1 to 254. If unspecified, value is set to 1.  
<stepN> | Integer - User characterization step number for which a description will be returned. Use [SENS:CORR:CKIT:ECAL:CHAR:STEP?](ECalCharacterize.md#steps) to query the number of steps.  
Examples | SENSe:CORR:CKIT:ECAL:CHAR:DESC? 2 ''Example return string: Connect ECal Module Ports A and B to PNA Ports 1 and 2  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:CORRection:CKIT:ECAL<mod>:CHARacterize:DESCription:USER <string>

Applicable Models: All (Read-Write) Sets and reads the description of the
person and/or company who is producing the ECal user characterization. This
description is stored with the characterization. Set this description before
sending [SENS:CORR:CKIT:ECAL:CHAR:INIT](ECalCharacterize.md#Init) or the
default (empty string) will be used.  
---  
Parameters |   
<ch> | Channel number being calibrated. If unspecified, value is set to 1  
<mod> | ECal module from which to read user characterization numbers. Choose from 1 to 254. If unspecified, value is set to 1.  
<string> | Descriptive text, limited to 19 characters maximum.  
Examples | SENSe:CORR:CKIT:ECAL:CHAR:DESC:USER "John Doe, Acme Inc."  
Query Syntax | SENSe<ch>:CORRection:CKIT:ECAL:CHARacterize:DESCription:USER?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | " " (Empty String)  
  
* * *

## SENSe<ch>:CORRection:CKIT:ECAL<mod>:CHARacterize:DESCription:VNA <string>

Applicable Models: All (Read-Write) Sets and reads a description of the Vector
Network Analyzer used to perform the User Characterization. This description
is stored with the user characterization. Set this description before sending
[SENS:CORR:CKIT:ECAL:CHAR:INIT](ECalCharacterize.md#Init) or the default
(empty string) will be used.  
---  
Parameters |   
<ch> | Channel number being calibrated. If unspecified, value is set to 1  
<mod> | ECal module from which to read user characterization numbers. Choose from 1 to 254. If unspecified, value is set to 1.  
<string> | Descriptive text, limited to 14 characters maximum.  
Examples | SENSe:CORR:CKIT:ECAL:CHAR:DESC:VNA "My PNA"  
Query Syntax | SENSe<ch>:CORRection:CKIT:ECAL:CHARacterize:DESCription:VNA?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | " " (Empty String)  
  
* * *

##
SENSe<ch>:CORRection:CKIT:ECAL<mod>:CHARacterize:DESCription:PORT<n>[:SELect]
<string>

Applicable Models: All (Read-Write) For each port of the ECal module that is
going to be characterized, sets and reads the description of the adapters,
cable, or fixture to be included in the user characterization. This command
refers to the ECal ports by number instead of letter (1 = Port A, 2 = Port B,
and so forth). This description is stored with the user characterization. Set
this description before sending
[SENS:CORR:CKIT:ECAL:CHAR:INIT](ECalCharacterize.md#Init) or the default
(empty string) will be used.  
---  
Parameters |   
<ch> | Channel number being calibrated. If unspecified, value is set to 1  
<mod> | ECal module from which to read user characterization numbers. Choose from 1 to 254. If unspecified, value is set to 1.  
<n> | ECal port number. Choose 1 to 2 for a 2-port ECal module, 1 to 4 for a 4-port module.  
<string> | Descriptive text, limited to 24 characters maximum.  
Examples | SENSe:CORR:CKIT:ECAL:CHAR:DESC:PORT1 "3.5 mm adapter, SN 00001"  
Query Syntax | SENSe<ch>:CORRection:CKIT:ECAL:CHARacterize:DESCription:PORT<n>[:SELect]?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | " " (Empty String)  
  
* * *

## SENSe<ch>:CORRection:CKIT:ECAL<mod>:CHARacterize:DMEMory:SAVE <charName>

Applicable Models: All (Write-only) Completes an ECal user characterization by
writing the characterization data to the VNA disk. To write the
characterization data to the ECal module, use
[SENS:CORR:CKIT:ECAL:CHAR:SAVE](ECalCharacterize.md#save). A User
Characterization can be saved to both VNA disk memory and ECal module memory.
Use this <charName> for performing future calibrations with this User
Characterization. See
[SENS:CORR:CKIT:ECAL:KNAM:INF?](CorrCKIT_SCPI.md#knameInf) Note: An ECal
confidence check can NOT be performed remotely from User Characterizations
that are stored on the VNA disk.  
---  
Parameters |   
<ch> | Channel number being calibrated. If unspecified, value is set to 1.  
<mod> | ECal module from which to read user characterization numbers. Choose from 1 to 254. If unspecified, value is set to 1.  
<charName> | String. User characterization name. Although there is no limit to the number of characters, only about 10 characters appear in the Cal Wizard dialog when selecting a user characterization for use.  
Examples | SENS:CORR:CKIT:ECAL:CHAR:DMEM:SAVE "DUT1 User Char"  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:CORRection:CKIT:ECAL<mod>:CHARacterize:ID <model, sn>

Applicable Models: All (Read-Write) Selects the model and serial number of the
ECal module to be characterized. This command does not Set the model and
serial number of the ECal module.  
---  
Parameters |   
<ch> | Channel number being calibrated. If unspecified, value is set to 1  
<mod> | ECal module from which to read user characterization numbers. Choose from 1 to 254. If unspecified, value is set to 1.  
<model, sn> | Model and serial number of the ECal module to be characterized.  
Examples | SENSe:CORR:CKIT:ECAL:CHAR:ID "N4433A,00001"  
Query Syntax | SENSe<ch>:CORRection:CKIT:ECAL:CHARacterize:ID?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | " " (Empty String)  
  
* * *

## SENSe<ch>:CORRection:CKIT:ECAL<mod>:CHARacterize:INITiate [bool]

Applicable Models: All (Write-only) Initiates an ECal User Characterization.
The specified channel number must be an S-parameter measurement channel. The
channel must already be calibrated using the same, or greater number of VNA
ports as the ECal module. Also, the calibrated VNA ports must begin with Port
1 and use sequential port numbers. After this command is executed, subsequent
commands can be used to query the number of measurement steps, issue the
acquisition commands, query the connection description strings, and
subsequently complete an Ecal User characterization.  
---  
Parameters |   
<ch> | Channel number of a calibrated S-parameter channel. If unspecified, value is set to 1  
<mod> | ECal module from which to read user characterization numbers. Choose from 1 to 254. If unspecified, value is set to 1.  
[bool] | Optional argument. If unspecified, value is set to 1. ON (or 1) Check ECal memory to ensure that a new characterization with the channels current number of points will fit in the module memory. Select for User Characterizations to be stored in internal ECal memory. OFF (or 0) Skip the check. Select for User Characterizations to be stored to VNA disk memory.  
Examples | SENS:CORR:CKIT:ECAL:CHAR:INIT sense2:correction:ckit:ecal:characterize:initiate off  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:CORRection:CKIT:ECAL<mod>:CHARacterize:INSitu:ENABle?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Returns
whether the device that was specified by
[SENS:CORR:CKIT:ECAL:CHAR:ID](ECalCharacterize.md#ID) is a CalPod module,
which is capable of being characterized as an in-situ device. [Learn
more](../../../S3_Cals/CalPod_as_ECal.htm#InSitu).  
---  
Parameters |   
<ch> | Channel number being calibrated. If unspecified, value is set to 1.  
<mod> | ECal module from which to read user characterization numbers. Choose from 1 to 254. If unspecified, value is set to 1.  
Examples | SENS:CORR:CKIT:ECAL:CHAR:INSitu:ENABle?  
Return Type | Boolean 1  Device is a CalPod module 0  Device is NOT a CalPod module  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:CORRection:CKIT:ECAL<mod>:CHARacterize:INSitu[:STATe] <bool>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write) Sets or
returns whether the device (CalPod module) that was specified by
[SENS:CORR:CKIT:ECAL:CHAR:ID](ECalCharacterize.md#ID) will be characterized
as an in situ device. [Learn
more](../../../S3_Cals/CalPod_as_ECal.htm#InSitu).  
---  
Parameters |   
<ch> | Channel number being calibrated. If unspecified, value is set to 1.  
<mod> | ECal module from which to read user characterization numbers. Choose from 1 to 254. If unspecified, value is set to 1.  
<bool> | In situ state. Choose from: ON (or 1) \- Characterize the CalPod module as an in situ device. OFF (or 0) Do NOT characterize the CalPod module as an in situ device.  
Examples | SENS:CORR:CKIT:ECAL:CHAR:INSitu 1  
Query Syntax | SENSe<ch>:CORRection:CKIT:ECAL:CHARacterize:INSitu[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON or 1  
  
* * *

## SENSe<ch>:CORRection:CKIT:ECAL<mod>:CHARacterize:SAVE

Applicable Models: All (Write-only) Completes an ECal user characterization by
writing the characterization data to the ECal module memory. To write the
characterization data to VNA disk memory, use
[SENS:CORR:CKIT:ECAL:CHAR:DMEM:SAVE](ECalCharacterize.md#dmemSave). A User
Characterization can be saved to both VNA disk memory and ECal module memory.
Note: This command is an overlapped command. When
[*OPC](../../Learning_about_GPIB/Understanding_Command_Synchronization.md#opc)
is issued with it, the OPC bit in the VNAs Standard Event Status Register is
not set until this command has completed its operation. [Learn
more.](../../Learning_about_GPIB/Understanding_Command_Synchronization.htm)  
---  
Parameters |   
<ch> | Channel number being calibrated. If unspecified, value is set to 1.  
<mod> | ECal module from which to read user characterization numbers. Choose from 1 to 254. If unspecified, value is set to 1.  
Examples | SENS:CORR:CKIT:ECAL:CHAR:SAVE, *OPC  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:CORRection:CKIT:ECAL<mod>:CHARacterize:STEPs?

Applicable Models: All (Read-only) Returns the number of steps required to
measure the ECal module. Currently, only ONE is required.  
---  
Parameters |   
<ch> | Channel number being calibrated. If unspecified, value is set to 1  
<mod> | ECal module from which to read user characterization numbers. Choose from 1 to 254. If unspecified, value is set to 1.  
Examples | SENS:CORR:CKIT:ECAL:CHAR:STEP?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

