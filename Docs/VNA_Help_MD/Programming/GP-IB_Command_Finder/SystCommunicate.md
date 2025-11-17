# SYSTem:COMMunicate Commands

* * *

Controls and queries settings that affect the VNA system.

SYSTem:COMMunicate: DRIVe | ENABle? ECAL | CATalog? | CLISt? | COUNt? | DMEMory | CLEar | IMPort | EXPort | [SNP](SystCommunicate.md#SYSTem:COMMunicate:ECAL:EXPort:SNP) | INFormation? | KNAMe:INFormation? | LIST? | PATH:COUNt? GPIB | PMETer | CATalog? | ADDRess | RDEVice | CLOSe | OPEN | READ? | RESet | WBINary | WBLock | WRITe LAN:HOSTname PSENsor TCPip:CONTrol? USB:PMETer:CAT? VISA | RDEVice | CLOSe | FIND? | OPEN | READ? | RESet | TIMeout | WBINary | WRITe  
---  
  
Click on a keyword to view the command details.

See Also

  * [Referring to Traces Channels Windows and Meas Using SCPI](../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.md)

  * [Example Programs](../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## SYSTem:COMMunicate:DRIVe:ENABle?

Applicable Models: All (Read-only) Returns whether or not the Enable Remote
Drive Access is checked in the Remote Interface dialog. When checked allows
access to the hard disk.  
---  
Examples | SYST:COMM:DRIV:ENAB?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:COMMunicate:ECAL:CATalog?

Applicable Models: All (Read-only) Returns the ID string of ECals that are
connected to the VNA USB. Use the list to select a Ecal for Ecal calibration.  
---  
Examples | SYST:COMM:ECAL:CAT? system:communicate:ecal:catalog?  
Return Type | Comma-delimited strings.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## SYSTem:COMMunicate:ECAL<mod>:CLISt?

Applicable Models: All (Read-only) Returns a list of characterizations stored
in the specified ECal module.  
---  
Parameters |   
<mod> | ECal module from which to read user characterization numbers. Choose from 1 to 50. If unspecified, value is set to 1.  
Examples | Module 1 contains User Characterizations 1 and 3. SYST:COMM:ECAL:CLIST? 'Returns the following (0 always indicates the factory characterization): 0,1,3  
Return Type | Numeric list, separated by commas.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:COMMunicate:ECAL:COUNt?

Applicable Models: All (Read-only) Returns the number of installed cal kits.  
---  
Examples | SYST:COMM:ECAL:COUNt?  
Query Syntax | SYST:COMM:ECAL:COUNt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:COMMunicate:ECAL:DMEMory:CLEar <kitName>

Applicable Models: All (Write-only) Deletes user characterizations from VNA
disk memory.  
---  
Parameters |   
<kitName> | Optional String argument. ECal Model, User Characterization name \+ " ECal", and serial number of the ECal module, separated by spaces. See examples below. If unspecified, ALL User Characterizations that are stored in VNA disk memory are deleted.  
Examples | 'These examples all use "MyUserChar" as the User characterization name. 'The "My User Char" characterization is deleted from disk memory. SYST:COMM:ECAL:DMEM:CLE "N4433A MyUserChar ECal 00001" 'All User characterizations are deleted from disk memory. SYST:COMM:ECAL:DMEM:CLE  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:COMMunicate:ECAL:DMEMory:IMPort <file>

Applicable Models:All (Write-only) After the VNA disk memory is
[Exported](Sense/CorrCKIT_SCPI.md#EcalExport) to a file, use this command to
Import the file into VNA disk memory, which allows the User Characterization
to be used with the VNA and ECal module. Note: An ECal confidence check can
NOT be performed remotely from User Characterizations that are stored on the
VNA disk.  
---  
Parameters |   
<file> | String. Full path and file name of file that was exported.  
Examples | SYST:COMM:ECAL:DMEM:IMP "c:\users\public\network analyzer\ECal User Characterizations/myDiskUserChar.euc"  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:COMMunicate:ECAL:EXPort <kit>[,<file>][,<NewName>]]

Applicable Models: All (Write-only) Saves an existing ECal characterization to
a file. Use this command to archive the user characterization or to move the
characterization to a different VNA for use with the specified ECal module.
After exporting the user characterization, use SYST:COMM:ECAL:DMEM:IMPort to
make the user characterization available for use.  
---  
Parameters |   
<kit> | String. Not case sensitive. ECal Model, User char name + " ECal", and serial number of the ECal module used for the characterization, separated by spaces. See examples below. If the model and serial number of the module is not found, an error is returned.  
[<file>] | Optional String argument. Path and filename of the user characterization. If not specified, the file is saved using characterization name + ".euc". If the path is not specified, it is stored in C:\Program Files(x86)\Keysight\Network Analyzer\ECal User Characterizations\\. The extension ".euc" is appended if one is not specified.  
[<NewName>] | Optional String argument. This allows you to change the name for the User Characterization. When specified, the new name is saved in the file with the characterization. If unspecified, the existing user characterization name is saved. Note: If this argument is specified, the second argument (<file>) must also be specified.  
Examples | 'These examples all use "MyUserChar" as the User characterization name. 'All parameters specified SYST:COMM:ECAL:EXP "N4433A MyUserChar ECal 00001","myUserChar.euc","NewUserChar" 'First two parameters are specified system:communicate:ecal:export "N4691B MyUserChar ECal 00500","myUserChar.euc" 'Only first parameter is specified SYST:COMM:ECAL:EXP "N4433A MyUserChar ECal 00001"  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:COMMunicate:ECAL:EXPort:SNP <kit>,<ecalState>,<snpFileName>

Applicable Models: All (Write-only) Read S parameter of ECal Thru from the
ECal memory and save it as s2p file.  
---  
Parameters |   
<kit> | String. Not case sensitive. ECal Model, User char name + " ECal", and serial number of the ECal module used for the characterization, separated by spaces. See examples below. If the model and serial number of the module is not found, an error is returned.  
<ecalState> | ECal transmission path. Choose from AB, AC, AD, BA, BC, BD, CA, CB, CD, DA, DB or DC. Not case sensitive.  
<snpFileName> | Path and filename of the output s2p file name.  
Examples | SYST:COMM:ECAL:EXP "N4433A ECal 00001","BC","D:\ecalthru.s2p"  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:COMMunicate:ECAL<mod>:INFormation? [<char>]

Applicable Models: All (Read-only) Reads the identification and
characterization information from the specified ECal module. Note: To read
user-characterization information that is stored in VNA disk memory, then use
SYST:COMM:ECAL:KNAM:INF?  
---  
Parameters |   
<mod> | ECal module from which to read characterizations. Choose from 1 through 50. If unspecified, value is set to 1. Do NOT assume the <mod> number is the order in which ECal modules were connected. Use SYST:COMM:ECAL:LIST? to read a list of <mod> numbers of currently-attached ECal modules.  
<char> | Optional argument. Specifies which characterization to read information from. If not specified, value is set to CHAR0. Choose from:

  * CHAR0 Factory characterization (data that was stored in the ECal module by Keysight)
  * CHAR1 User characterization #1
  * CHAR2 User characterization #2
  * \- through -
  * CHAR12 User characterization #12

  
Examples | SYST:COMM:ECAL2:INFormation? char5 'Example return string: "ModelNumber: 85092-60007, SerialNumber: 01386, ConnectorType: N5FN5F, PortAConnector: Type N (50) female, PortBConnector: Type N (50) female, MinFreq: 30000, MaxFreq: 9100000000, NumberOfPoints: 250, Calibrated: July 4 2002"  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:COMMunicate:ECAL:KNAMe:INFormation? <kitName>

Applicable Models: All (Read-only) Reads the identification and
characterization information from the specified ECal module or VNA disk
memory. [Learn more about User Characterization in VNA Disk
Memory.](../../S3_Cals/ECal_User_Characterization.htm#DiskMemoryDiag)  
---  
Parameters |   
<kitName> | String. ECal model and characterization to read information from, enclosed in quotes, in the following format: <model> <name> ECal <serial number> Where: <model>: Always required <name>:

  * For the factory characterization, do not specify.
  * For a user-characterization stored in the module, use User <n> in the string, where <n> is the user-characterization number. Not case sensitive. Separate User and <n> with a space.
  * For a user-characterization stored in VNA disk memory, use <charName> from [SENS:CORR:CKIT:ECAL:CHAR:DMEM:SAVE <charName>](Sense/ECalCharacterize.md#dmemSave)

ECal \- not case sensitive <serial number>: Optional. Include when two or more
ECal modules with same model number are attached to the VNA, Each item is
separated with a space.  
Examples | 'For a factory characterization in module memory:  
SYST:COMM:ECAL:KNAM:INF? "N4433A ECal" 'For user characterization in module
memory with optional serial number:  
SYST:COMM:ECAL:KNAM:INF? "N4433A User 1 ECal 00028" 'For user characterization
"foo" in disk memory:  
SYST:COMM:ECAL:KNAM:INF? "N4433A foo ECal 00028" 'Example return string:
"ModelNumber: N4433A, SerialNumber: 00028, ConnectorType: N5FN5F,
PortAConnector: Type N (50) female, PortBConnector: Type N (50) female,
MinFreq: 30000, MaxFreq: 9100000000, NumberOfPoints: 250, Calibrated: July 4
2002"  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:COMMunicate:ECAL:LIST?

Applicable Models: All (Read-only) Returns a list of index numbers for ECal
modules that are currently attached to the VNA. Use these numbers (called
<mod> in VNAHelp) to refer to the ECal module using SCPI commands.  
---  
Examples | SYST:COMM:ECAL:LIST? 'If 2 modules are attached to the VNA  
'then the returned list will be: +1,+2 'If NO modules are attached to the VNA  
'then the returned list will be: +0  
Return Type | Numeric list, separated by commas.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:COMMunicate:ECAL<n>:PATH:COUNt? <path>

Applicable Models: All (Read-only) Returns the number of unique states that
exist for the specified path name on the selected ECal module. This command
performs exactly the same function as
[CONT:ECAL:MOD:PATH:COUNt?](Control.md#ECalPathCount) Use the
[CONT:ECAL:MOD:PATH:STAT](Control.md#EcalPathState) command to set the module
into one of those states.  Use
[SENS:CORR:CKIT:ECAL:PATH:DATA?](Sense/CorrCKIT_SCPI.md#EcalPathData) to read
the data for a state.  
---  
Parameters |   
<n> | USB number of the ECal module. Choose from 1 to 50. If unspecified (only one ECal module is connected to the USB), <n> is set to 1. If two or more modules are connected, use SYST:COMM:ECAL:LIST? to determine how many, and SYST:COMM:ECAL:INF? to verify their identities.  
<path> | Name of the path for which to read number of states. Choose from: Reflection paths

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

  
Examples | SYST:COMM:ECAL:PATH:COUNt?  
system:communicate:ecal:path:count?  
Return Type | Integer  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:COMMunicate:GPIB:PMETer[:ADDRess] <num> Superseded

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA Note: This command
is replaced with SYST:COMM:PSENsor (Read-Write) Specifies the GPIB address of
the power meter to be used in a source power calibration. When performing a
source power cal, the VNA will search VISA interfaces that are configured in
the Keysight IO LIbraries on the VNA.  
---  
Parameters |   
<num> | GPIB address of the power meter. Choose any integer between 0 and 30.  
Examples | SYST:COMM:GPIB:PMET 13 system:communicate:gpib:pmeter:address 14  
Query Syntax | SYSTem:COMMunicate:GPIB:PMETer[:ADDRess]?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 13  
  
* * *

## SYSTem:COMMunicate:GPIB:PMETer:CATalog? <optional bool>

Applicable Models: All (Read-only) Returns the ID string of power meters /
sensors that are connected to the VNA via GPIB. Optionally, the visa address
is returned. Use the list to select a power sensor for a [source power
cal.](../../S3_Cals/PwrCalibration.htm#SourceDiag)  
---  
Parameters |   
<optional bool> | Choose from: ON or 1 - Returns the visa address. OFF or 0 - Does not return the visa address.  
Examples | SYST:COMM:GPIB:PMET:CAT? ON system:communicate:gpib:pmeter:catalog?  
Return Type | Comma-delimited strings. Two power sensor strings are separate by a semicolon.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SYSTem:COMMunicate:GPIB:RDEVice:CLOSe <ID>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Write only) Closes
the remote GPIB session. This command should be sent when ending every
successful OPEN session.  
---  
Parameters |   
<ID> | Session identification number that was returned with the OPEN? command.  
Examples | [See an example program](../GPIB_Example_Programs/GPIB_Pass_Through.md)  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:COMMunicate:GPIB:RDEVice:OPEN <bus>, <addr>, <timeout>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-Write)
Initiates a GPIB pass-through session. First send this OPEN command, then send
the OPEN query to read the session ID number. An existing GPIB pass-through
session remains open after an instrument preset. To learn more about GPIB
pass-through capability, see the [example
program.](../GPIB_Example_Programs/GPIB_Pass_Through.htm)  
---  
Parameters |   
<bus> | Bus ID number. You can find the USB-GPIB adapter bus number by looking at the dialog that appears when the USB-GPIB device is connected. Error 1073 indicates the bus or address number is incorrect. Use 0 (zero) when connected using a GPIB cable to the VNA controller port.  
<addr> | GPIB Address of the device to be controlled  
<timeout> | The amount of time (in milliseconds) to wait for a response from the remote device after sending a command. A "timeout" error is displayed after this time has passed without a response.  
Examples | [See an example program](../GPIB_Example_Programs/GPIB_Pass_Through.md)  
Query Syntax | SYSTem:COMMunicate:GPIB:RDEVice:OPEN? Returns the session identification number that is used when communicating with this device.  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:COMMunicate:GPIB:RDEVice:READ? <ID>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Returns
data from the GPIB pass-through device.  
---  
Parameters |   
<ID> | Session identification number that was returned with the OPEN? command.  
Examples | [See an example program](../GPIB_Example_Programs/GPIB_Pass_Through.md)  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:COMMunicate:GPIB:RDEVice:RESet

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Write-only)
Performs the same function as
[SYST:COMM:GPIB:RDEV:CLOS](SystCommunicate.md#close) except that ALL pass-
through sessions are closed.  
---  
Examples | SYST:COMM:GPIB:RDEV:RES  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:COMMunicate:GPIB:RDEVice:WBINary <ID>,<data>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Write-only) Sends
data to a GPIB pass-through device. This command requires a header that
specifies the size of the data to be written. The header (described below) is
not passed along to the device. Use this command if too many embedded quotes
prevent you from using [SYST:COMM:GPIB:RDEV:WRIT](SystCommunicate.md#write).
Use [SYST:COMM:GPIB:RDEV:OPEN](SystCommunicate.md#open) to open the pass
through session.  
---  
Parameters |   
<ID> | Session identification number that was returned with the OPEN? command.  
<data> | Data to be sent to the GPIB pass-through device. Use the following syntax: #<num digits><byte count><data bytes><NL><END> <num_digits> specifies how many digits are contained in <byte_count> <byte_count> specifies how many data bytes will follow in <data bytes>  
Examples | SYSTem:COMMunicate:GPIB:RDEVice:WBINary 101,#17ABC+XYZ<nl><end> # \- always sent before data. 1 \- specifies that the byte count is one digit (7). 7 \- specifies the number of data bytes that will follow, not counting <NL><END>. ABC+XYZ \- Data block <nl><end> \- always sent at the end of block data. The following example sends a line feed at the end. SYST:COMM:GPIB:RDEV:WBIN 1,#210SYST:PRES<EOL> The <EOL> represents your linefeed character.  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:COMMunicate:GPIB:RDEVice:WBLock <ID>,<data>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Write-only) Same as
SYSTem:COMM:GPIB:RDEV:WBIN (above) but the header IS passed along to the
device. Use this command if too many embedded quotes prevent you from using
SYST:COMM:GPIB:RDEV:WRIT.  
---  
Parameters |   
<ID> | Session identification number that was returned with the OPEN? command.  
<data> | Data to be sent to the GPIB pass-through device. See previous command.  
Examples | See previous example.  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:COMMunicate:GPIB:RDEVice:WRITe <ID>,<string>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Write-only) Sends
ASCII string data to the GPIB pass-through device. A line feed is NOT appended
to the string data. To send a line feed, see the example in
SYST:COMM:GPIB:RDEV:WBIN.  
---  
Parameters |   
<ID> | Session identification number that was returned with the OPEN? command.  
<string> | Commands to be sent to the GPIB pass-through device.  
Examples | [See an example program](../GPIB_Example_Programs/GPIB_Pass_Through.md)  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:COMMunicate:LAN:HOSTname?

Applicable Models: All (Read-only) Returns the LAN hostname that is visible in
the Help, About Network Analyzer dialog box. [Learn
more.](../../S0_Start/HelpAbout.htm) This is the same information that is
visible on the [LXI compliance dialog](../../S0_Start/LXI_Compliance.md#LAN).  
---  
Parameters | None  
Example | SYST:COMM:LAN:HOSTname?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## SYSTem:COMMunicate:PSENsor <char>, <string>

Applicable Models: All This command replaces SYST:COMM:GPIB:PMET:ADDR. (Read-
Write) Specifies the type and location of the power meter to be used in a
source power calibration.  
---  
Parameters |   
<char> | Type of power meter/ sensor. Choose from:

  * GPIB GPIB power meter
  * USB USB power sensor or USB power sensor
  * LAN LAN enabled power meter
  * ANY  Any VISA resource string or a visa alias

  
<string> | For GPIB, address of the power meter. Choose any integer between 0 and 30. For USB, the ID string of the power meter or power sensor. Use SYST:COMM:USB:PMET:CAT? to see a list of ID strings of connected power meters and sensors. For LAN, the hostname or IP address of the power meter. For ANY, any VISA resource string or a visa alias.  
Examples | SYST:COMM:PSEN gpib, "14" system:communicate:psensor usb, "Keysight Technologies,U2000A,MY12345678" syst:comm:psen lan, "mymeter.Keysight.com" syst:comm:psen any, "TCPIP0::mymeter.Keysight.com::5025::SOCKET"  
Query Syntax | SYSTem:COMMunicate:PSENsor?  
Return Type | Character / String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | GPIB  
  
* * *

## SYSTem:COMMunicate:USB:PMETer:CATalog? <optional bool>

Applicable Models: All (Read-only) Returns the ID string of power meters /
sensors that are connected to the VNA USB. Optionally, the visa address is
returned. Use the list to select a power sensor for a [source power
cal.](../../S3_Cals/PwrCalibration.htm#SourceDiag) These meter/sensor ID
strings can NOT be used as the resource string for configuring a USB-based
PMAR ([SYST:CONF:EDEV:IOConfig](SystConfigExternalDevice.md#ioconf)).  
---  
Parameters |   
<optional bool> | Choose from: ON or 1 - Returns the visa address. OFF or 0 - Does not return the visa address.  
Examples | SYST:COMM:USB:PMET:CAT?  
"Agilent Technologies,U2002A,MY51240014"
system:communicate:usb:pmeter:catalog? ON  
"Agilent
Technologies,U2002A,MY51240014;USB0::2391::11288:MY51240014::0::INSTR"  
Return Type | Comma-delimited strings. Two power sensor strings are separate by a semicolon.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SYSTem:COMMunicate:TCPip:CONTrol?

Applicable Models: All (Read-only) Queries the TCP/IP port number to use for
opening a TCP/IP socket control connection to the VNA. The control connection
is used for two purposes:

  1. To perform a Device Clear operation on the VNA
  2. To detect when a Service Request (SRQ) event occurs on the VNA.

The port number can range from 5000 to 5099. The VNA will skip over 5025 as it
is being used for the primary socket connection. To detect an SRQ, your
program sends the appropriate commands via the regular socket connection to
set up for a SRQ event to occur the same sequence of commands as if you were
sending them via GPIB. You write your program so that while your program is
doing SCPI transactions on the standard socket connection, a second thread of
execution in your program detects the SRQ on the control connection and
responds to the event. When the SRQ event occurs, the VNA sends a SRQ +xxx/n
message on the control connection (where /n is linefeed character, ASCII value
10 decimal). The xxx value in the SRQ +xxx/n string is the IEEE 488.2 status
byte at the time the SRQ was generated. So listening for that on the control
connection is how your program detects the event. If for your socket
communication youre using a software API that provides for asynchronous
communication via a callback mechanism (for example, if youre using Microsofts
winsock API, or their .NET Socket class as in the example program below), in
that case your listener execution thread is created implicitly for you so your
program doesnt have to create one explicitly. Note: If this SCPI query is sent
to the VNA via a SCPI parser other than a TCP/IP socket connection (for
example, if sent via GPIB), the query is not applicable in that case and will
return value of 0.  
---  
Parameters | None  
Example | [See example program](../GPIB_Example_Programs/Socket_Client.md)  
Return Type | Integer  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## SYSTem:COMMunicate:VISA:RDEVice:CLOSe <ID>

Applicable Models: N522xB, N523xB, N524xB, E5080A (Write only) Closes the
specified remote VISA session. VISA sessions should always be closed when you
are finished communicating with the remote device. Use this command to close
(end) each VISA session that was opened successfully using the OPEN command.
If you have more than one open session, and need to close them all at the same
time, it may be faster and easier to use the RESet command.  
---  
Parameters |   
<ID> | VISA session number (see SYST:COMM:VISA:RDEV:OPEN[?]).  
Examples | SYST:COMM:VISA:RDEV:CLOS 1 system:communicate:visa:rdevice:close 2  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:COMMunicate:VISA:RDEVice:FIND? <VISA regex> [,<ADDRess|ALIas>]

Applicable Models: All (Read-only) Returns a comma separated list of either
VISA address strings or aliases.  
---  
Parameters |   
<VISA regex> | (String) VISA regular expressions are expressions defined by the user to find devices that have been set up on the VISA interface. The following are examples of VISA regular expressions: | Interface | Expression  
---|---  
GPIB | GPIB[0-9]*::?*INSTR  
PXI | PXI?*INSTR  
VXI | VXI?*INSTR  
GPIB-VXI | GPIB-VXI?*INSTR  
GPIB and GPIB-VXI | GPIB?*INSTR  
All VXI | ?*VXI[0-9]*::?*INSTR  
ASRL | ASRL[0-9]*::?*INSTR  
All | ?*INSTR or ?*  
  
Note that using "INSTR" in the VISA regular expression finds "instruments." To
search all interfaces, use "?*".  
  
<ADDRess|ALIas> | Optional. Determines whether addresses or aliases are returned. Note: The list of aliases may have less‒or more‒entries than the list of addresses because not all addresses will have aliases, and one address can have more than one alias.  
Examples | SYST:COMM:VISA:RDEV:FIND? "?*",ADDR system:communicate:visa:rdevice:find? '?*INSTR',alias  
Return Type | Variant  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Addresses returned if no return-type specified  
  
* * *

## SYSTem:COMMunicate:VISA:RDEVice:OPEN <addr>, <timeout>

Applicable Models: N522xB, N523xB, N524xB, E5080A (Read-Write) Initiates a
VISA pass-through session for a device. Immediately after successfully sending
this command, send an OPEN? query to retrieve the unique session ID that is to
be used whenever communicating with the device. Pass-through sessions can be
closed by using the CLOSe command, the RESet command, or by properly shutting
down the instrument or the analyzer application. Presetting the instrument
will not close existing pass-through sessions. Note: **When opening a socket
session (addresses of type: TCPIP[board]::host address::port::SOCKET) , you
must use the appropriate VISA Address for the identifier argument. Using an
alias to open a socket session is not currently supported. Aliases are allowed
for all other types of supported sessions.**  
---  
Parameters |   
<addr> | VISA Address or alias name of the device to be controlled  
<timeout> | The amount of time (in milliseconds) to wait for a response from the remote device after sending a command. A "timeout" error is displayed after this time has passed without a response.  
Examples | SYST:COMM:VISA:RDEV:OPEN 'TCPIP0::A-N5242A-10096::hislip1::INSTR',1000 system:communicate:visa:rdevice:open 'MyAliasName',7000  
Query Syntax | SYSTem:COMMunicate:VISA:RDEVice:OPEN? Returns the VISA session identification number to be used when communicating with this device.  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

##  SYSTem:COMMunicate:VISA:RDEVice:READ? <ID>

Applicable Models: N522xB, N523xB, N524xB, E5080A (Read-only) Returns data
from the VISA pass-through device.  
---  
Parameters |   
<ID> | VISA session number (see SYST:COMM:VISA:RDEV:OPEN[?]).  
Examples | SYST:COMM:VISA:RDEV:READ? 1 system:communicate:visa:rdevice:read? 3  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:COMMunicate:VISA:RDEVice:RESet

Applicable Models: N522xB, N523xB, N524xB, E5080A (Write-only) Closes all
currently open VISA pass-through sessions. See also CLOSe to close only one
session at a time.  
---  
Examples | SYST:COMM:VISA:RDEV:RES  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:COMMunicate:VISA:RDEVice:TIMeout <ID>, <timeout>

Applicable Models: All (Read-Write) Sets or returns the timeout value (in
milliseconds) for VISA pass-through commands for the specified VISA session
ID.  
---  
Parameters |   
<ID> | VISA session number that was returned with the OPEN? command.  
<timeout> | The amount of time (in milliseconds) to wait for a response from the remote device after sending a command. A "timeout" error is displayed after this time has passed without a response.  
Examples | SYST:COMM:VISA:RDEV:TIM 1,6000 system:communicate:visa:rdevice:timeout 3,6000  
Query Syntax | SYSTem:COMMunicate:VISA:RDEVice:TIMeout? <ID> Returns the timeout value for the specified session ID.  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 2000  
  
* * *

## SYSTem:COMMunicate:VISA:RDEVice:WBINary <ID>,<data>

Applicable Models: N522xB, N523xB, N524xB, E5080A (Write-only) Sends data to a
VISA pass-through device. This command requires a header that specifies the
size of the data to be written. The header (described below) is not passed
along to the device.  
---  
Parameters |   
<ID> | VISA session number (see SYST:COMM:VISA:RDEV:OPEN[?]).  
<data> | Data to be sent to the VISA pass-through device. Use the following syntax: #<num digits><byte count><data bytes><NL><END> <num_digits> specifies how many digits are contained in <byte_count> <byte_count> specifies how many data bytes will follow in <data bytes>  
Examples | SYSTem:COMMunicate:VISA:RDEVice:WBINary 1,#17ABC+XYZ<nl><end> # \- always sent before data. 1 \- specifies that the byte count is one digit (7). 7 \- specifies the number of data bytes that will follow, not counting <NL><END>. ABC+XYZ \- Data block <nl><end> \- always sent at the end of block data. The following example sends a line feed at the end. SYST:COMM:VISA:RDEV:WBIN 1,#210SYST:PRES<EOL> The <EOL> represents your linefeed character.  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:COMMunicate:VISA:RDEVice:WRITe <ID>,<string>

Applicable Models: N522xB, N523xB, N524xB, E5080A (Write-only) Sends ASCII
string data to the VISA pass-through device. If sending a command that returns
data, follow with the READ? query.  
---  
Parameters |   
<ID> | VISA session number (see SYST:COMM:VISA:RDEV:OPEN[?]).  
<string> | Commands to be sent to the VISA pass-through device.  
Examples | SYST:COMM:VISA:RDEV:WRIT 1,'*IDN?' system:communicate:visa:rdevice:write 2,'SYST:PRES'  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

