# Sense:Multiplexer Commands

* * *

Controls External Test Sets (N44xx, E5092A, "Z", and "H" series).

SENSe:MULTiplexer: ADDRess ALLPorts CATalog? COUNt? DISPlay INCount? LABel OUTPut | A|B|C|D[DATA] | A|B|C|D:VOLTage[DATA] | [DATA] PORT | CATalog? | SELect STATe TSET9 | OUTPut | PORT1 | PORT2 | PORT3 | PORT4 TYPE  
---  
  
Click on a keyword to view the command details.

Red commands are [superseded](../../Replacement_Commands.md).

See Also

  * [See an example program](../../GPIB_Example_Programs/External_Test_Set_using_SCPI.md) using these commands.

  * [Learn about External Test Set Control](../../../System/External_Testset_Control.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## SENSe:MULTiplexer<id>:ADDRess <address>

Applicable Models: N522xB, N523xB, N524xB,E5080A (Read-Write) Sets and returns
the address for the external test set at the specified ID. This command should
be immediately preceded by the [SENSe:MULT:TYPE](Multiplexer.md#type)
command. Note: This command is not applicable to the E509xA USB test sets, on
which the address is set by DIP switches on the rear panel.  
---  
Parameters |   
<id> | Id of the external test set. If unspecified, Id is assumed to be 1. Must be previously set by the [SENSe:MULT:TYPE](Multiplexer.md#type) command.  
<address> | Integer The test set address.

  * For a GPIB test set (N44xx and some specials), this is the GPIB address.
  * For a test set I/O test set (some specials), it is the position of the test set in the chain (starting at 0).

  
Examples | SENS:MULT1:TYPE "Z5623A_K66" ' use K66 test set, and reference it through ID 1 SENS:MULT1:ADDR 0 ' first test set in sequence ' All subsequent commands using SENS:MULT1 will refer to this test set  
Query Syntax | SENSe:MULTiplexer<id>:ADDRess?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<cnum>:MULTiplexer<id>:ALLPorts <string>

Applicable Models: N522xB, N523xB, N524xB, E5080A (Read-Write) Sets or gets
the port selections for all available ports on the specified channel.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1.  
<id> | Id of the external test set. If unspecified, Id is assumed to be 1. Must be previously set by the [SENSe:MULT:TYPE](Multiplexer.md#type) command.  
<string> | Comma-separated list of port selections, one for each port. Each port selection must correspond to one of the values returned by SENS:MULT:PORT:CAT?. Do NOT include + and - .  
Examples | ' for channel 5 and test set 1, set port 1 to T1, ' port 2 to A, port 3 to R2+, port 4 to R3-. SENS5:MULT1:ALLP "T1,A,R2,R3 "  
Query Syntax | SENSe<cnum>:MULTiplexer<id>:ALLPorts?  
Return Type | STRING  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:MULTiplexer:CATalog?

Applicable Models: N522xB, N523xB, N524xB, E5080A (Read-Only) Returns a comma-
separated list of the external test sets models that are currently supported.
Choose one of these items to send [SENS:MULT1:TYPE.](Multiplexer.md#type)  
---  
Examples | SENS:MULT:CAT?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:MULTiplexer<id>:COUNt?

Applicable Models: N522xB, N523xB, N524xB, E5080A (Read-Only) Returns the
total number of ports of the specified test set. Returns 0 if no test set is
connected (GPIB test sets only).  
---  
Parameters |   
<id> | Id of the external test set. If unspecified, Id is assumed to be 1. Must be previously set by the [SENSe:MULT:TYPE](Multiplexer.md#type) command.  
Examples | SENS:MULT1:COUN?  
sense:multiplexer2:count?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:MULTiplexer<id>:DISPlay[:STATe] <bool>

Applicable Models: N522xB, N523xB, N524xB, E5080B, E5081A, M980xA (Read-Write)
Turns ON and OFF the display of the test set control status bar. This status
bar indicates the test set that is being controlled and the current port
mappings of the active channel. Note: To use this command with the M980xA PXI
VNA, the firmware version must be A.15.xx.xx and above, and the S94702A AMX
VNA Plugin license is required. This command is effective only in the standard
class.  
---  
Parameters |   
<id> | Id of the external test set. If unspecified, Id is assumed to be 1.  
<bool> | ON(1) Turns ON when in multiport mode. OFF (0) Turns OFF when not in multiport mode.  
Examples | SENS:MULT1:DISP 1  
sense:multiplexer2:display:state on  
Query Syntax | SENSe:MULTiplexer<id>:DISPlay[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF (0)  
  
* * *

## SENSe:MULTiplexer<id>:INCount?

Applicable Models: N522xB, N523xB, N524xB, E5080B, E5081A, M980xA (Read-Only)
Returns the number of test set input ports (VNA connection ports).  Note: To
use this command with the M980xA PXI VNA, the firmware version must be
A.15.xx.xx and above, and the S94702A AMX VNA Plugin license is required.  
---  
Parameters |   
<id> | Id of the external test set. If unspecified, Id is assumed to be 1.  
Examples | SENS3:MULT1:INC? ' returns the number of input ports for test set 1 on channel 3  
Return Type | Numeric   
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<cnum>:MULTiplexer:LABel <string>

Applicable Models: N522xB, N523xB, N524xB, E5080A (Read-Write) Sets and
returns the display label for the testset on the specified channel. The label
appears in a status bar at the bottom of the VNA display when
[SENS:MULT:DISP](Multiplexer.md#display) is set to ON. Note: This command
does not apply to the use of the E509xA test sets.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1.  
<string> | Display label text.  
Examples | SENS3:MULT:LAB 'High-power output'  
Query Syntax | SENSe<cnum>:MULTiplexer:LABel?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<cnum>:MULTiplexer<id>:OUTPut:<grp>[:DATA] <num>

Applicable Models: N522xB, N523xB, N524xB, E5080B, E5081A, M980xA (Read-Write)
Sets or returns the output port data for specified group of the E5092A's
control lines. The output port data is set at the beginning of each sweep of
the specified channel. Note: To use this command with the M980xA PXI VNA, the
firmware version must be A.15.xx.xx and above, and the S94702A AMX VNA Plugin
license is required. This command can be used only in the standard class.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1.  
<id> | Id of the external test set either 1 or 2. If unspecified, Id is assumed to be 1.   
<grp> | A | B | C | D  
<num> | An integer specifying the decimal value of the control line. Values are obtained by adding weights from the following table that correspond to individual lines. The output port data range is between 0 to 255 (0=All lines are turned OFF and 255 all lines are turned ON). | Line | Weight  
---|---  
1 | 1  
2 | 2  
3 | 4  
4 | 8  
5 | 16  
6 | 32  
7 | 64  
8 | 128  
Examples | SENS:MULT1:STAT ON SENS3:MULT1:OUTP:B 8 ' let the control line B output the data 8 at the beginning of channel-3 sweep.  
Query Syntax | SENSe<cnum>:MULTiplexer<id>:OUTPut:<grp>[:DATa]?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## SENSe<cnum>:MULTiplexer<id>:OUTPut:<grp>:VOLTage[:DATA] <volt>

Applicable Models: N522xB, N523xB, N524xB, E5080B, E5081A, M980xA (Read-Write)
Sets or returns the output voltage for specified group of the E5092A's control
lines. The output voltage is set at the beginning of each sweep of the
specified channel. Note: To use this command with the M980xA PXI VNA, the
firmware version must be A.15.xx.xx and above, and the S94702A AMX VNA Plugin
license is required. This command is effective only in the standard class.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1.  
<id> | Id of the external test set either 1 or 2. If unspecified, Id is assumed to be 1.   
<grp> | A | B | C | D  
<volt> | Output voltage range for <grp> is between 0 to 5.2V and resolution is 10mV.  
Examples | SENS:MULT1:STAT ON SENS3:MULT1:OUTP:B:VOLT 4.2 ' set the control line B voltage to 4.2 V at the beginning of channel-3 sweep.  
Query Syntax | SENSe<cnum>:MULTiplexer<id>:OUTPut:<grp>:VOLtage[:DATa]?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 V  
  
* * *

## SENSe<cnum>:MULTiplexer<id>:OUTPut[:DATa] <num>

Applicable Models: N522xB, N523xB, N524xB, E5080B, E5081A, M980xA (Read-Write)
Sets or returns the control line value for the specified channel. The output
port data is set at the beginning of each sweep of the specified channel. If
this command is used when the test set is the E5092A, it reads/writes data
just for "group A" of the test set's output lines. Note: To use this command
with the M980xA PXI VNA, the firmware version must be A.15.xx.xx and above,
and the S94702A AMX VNA Plugin license is required.This command is effective
only in the standard class.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1.  
<id> | Id of the external test set. If unspecified, Id is assumed to be 1.   
<numr> | An integer specifying the decimal value of the control line. Values are obtained by adding weights from the following table that correspond to individual lines. | Line | Weight  
---|---  
1 | 1  
2 | 2  
3 | 4  
4 | 8  
5 | 16  
6 | 32  
7 | 64  
8 | 128  
  
Note:

  * The E5092A interprets SENS:MULT1:OUTP 0 as all lines OFF.

Refer to your test set documentation for setting control line values.  
---  
  
Examples | SENS:MULT1:STAT ON SENS3:MULT1:OUTP 48  ' let the control line output the data 48 at the beginning of channel-3 sweep.  
Query Syntax | SENSe<cnum>:MULTiplexer<id>:OUTPut[:DATa]?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:MULTiplexer<id>:PORT<pnum>:CATalog?

Applicable Models: N522xB, N523xB, N524xB, E5080B, E5081A, M980xA (Read-Only)
Returns a comma-separated list of valid measurement port selections for the
specified VNA connection port. Note: To use this command with the M980xA PXI
VNA, the firmware version must be A.15.xx.xx and above, and the S94702A AMX
VNA Plugin license is required.  
---  
Parameters |   
<id> | Id of the external test set. If unspecified, Id is assumed to be 1\.   
<pnum> | The VNA connection port number (1 to 4) for which to return the valid test set measurement port selections.  If the E5092As configuration is E5092_28, this parameter specifies the individual switch number (1 to 4: SP4T switches, 5 to 10: SPDT switches).  
Examples | SENS:MULT1:PORT3:CAT? ' returns the valid port selections for port 3  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<cnum>:MULTiplexer<id>:PORT<pnum>:SELect <string>

Applicable Models: N522xB, N523xB, N524xB, E5080B, E5081A, M980xA (Write-Only)
Sets a port mapping for a single port. The test set RF measurement path is
switched at the beginning of each sweep of the specified channel. If this
command creates a conflict with an existing port, the VNA will resolve the
conflict. Note: To use this command with the M980xA PXI VNA, the firmware
version must be A.15.xx.xx and above, and the S94702A AMX VNA Plugin license
is required. This command is effective only in the standard class.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, value is set to 1.  
<id> | Id of the external test set. If unspecified, Id is assumed to be 1\.   
<pnum> | The VNA connection port number (1 to 4). If the E5092As configuration is E5092_28, this parameter specifies the individual switch number (1 to 4: SP4T switches, 5 to 10: SPDT switches).  
<string> | The label of the E5092As measurement port.  If the E5092As configuration is E5092_28, this parameter specifies the label of individual switch connection. Refer to the following table. Labels of E5092As measurement ports in E5092_13 / 16 / 22 / X10 modes |  | Port 1 | Port 2 | Port 3 | Port 4  
---|---|---|---|---  
E5092_13 | A,T1,T2,T3 (1A,8COM,9COM,10COM) | T1,T2,T3,T4 (8COM,9COM,10COM,2D) | R1,R2,R3,R4 (3A,3B,3C,3D) | R1,R2,R3,R4 (4A,4B,4C,4D)  
E5092_16 | A1,A2,A3,A4 (1A,1B,1C,1D) | B1,B2,B3,B4 (2D,2A,2B,2C) | R1,R2,R3,R4 (3A,3B,3C,3D) | R1,R2,R3,R4 (4A,4B,4C,4D)  
E5092_22 | A1,A2,A3,A4,A5,A6 (5A,5B,6A,6B,1C,1D) | A7,A8,A9,A10,A11 (8A,8B,2B,2C,2D) | B1,B2,B3,B4,B5,B6 (3A,9A,9B,10A,10B,3D) | B7,B8,B9,B10,B11 (4A,4B,7A,7B,4D)  
E5092_X10 | 1,3,5,7 (5COM,6COM,7COM,1D) | 2,4,6,8 (8COM,9COM,10COM,2D) | 2,4,6,10 (8COM,9COM,10COM,3D) | 1,3,5,9 (5COM,6COM,7COM,4D)  
  
Labels of E5092As individual switch connections in E5092_28 mode

PORT1 (switch1) | PORT2 (switch2) | PORT3 (switch3) | PORT4 (switch4)  
---|---|---|---  
A,B,C,D (1A,1B,1C,1D) | A,B,C,D (2A,2B,2C,2D) | A,B,C,D (3A,3B,3C,3D) | A,B,C,D (4A,4B,4C,4D)  
PORT5 (switch5) | PORT6 (switch6) | PORT7 (switch7) | PORT8 (switch8)  
A,B (5A,5B) | A,B (6A,6B) | A,B (7A,7B) | A,B (8A,8B)  
PORT9 (switch9) | PORT10 (switch10) |   
A,B (9A,9B) | A,B (10A,10B)  
  
Examples | SENS1:MULT1:STAT ON  SENS1:MULT1:TYP 'E5092_22' SENS1:MULT1:PORT1:SEL 'A2' ' set E5092A to 22-port config and let port-1 be connected to 'A2' at the beginning of channel-1 sweep.  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:MULTiplexer<id>:STATe <bool>

Applicable Models: N522xB, N523xB, N524xB, E5080B, E5081A, M980xA (Read-Write)
Enables and disables (ON/OFF) the port mapping and control line output of the
specified test set. Turning this state on will let the E5092As paths be
switched at the beginning of the sweep for the channel specified by <cnum> of
SENS<cnum>:MULT<id>:PORT<pnum>:SEL <string>.  If the specified test set is not
connected or not ON, then setting State ON will report an error. All other
properties can be set when the test set is not connected. When this command is
set to ON, then the display of the test set status bar
([SENS:MULT:DISP](Multiplexer.md#display)) is also set to ON. Note: To use
this command with the M980xA PXI VNA, the firmware version must be A.15.xx.xx
and above, and the S94702A AMX VNA Plugin license is required.  
This command is effective only in the standard class.  
---  
Parameters |   
<id> | Id of the external test set. If unspecified, Id is assumed to be 1.   
<bool> | ON(1) Enables test set control. OFF (0) Disables test set control.  
Examples | SENS:MULT1:STAT 1  
sense2:multiplexer2:state on  
Query Syntax | SENSe<cnum>:MULTiplexer<id>:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF (0)  
  
* * *

## SENSe<cnum>:MULTiplexer<id>:TSET9:OUTPut[:DATA] <data> Superseded

Applicable Models: N522xB, N523xB, N524xB, E5080A Note: This command is
replaced with [SENS:MULT:OUTP](Multiplexer.md#TSOutputData) (Read-Write) Sets
the control lines of the specified E5091A. Control lines, provided through a
E5091A front panel connector, are used to control external equipment such as a
part handler. See your E5091A documentation to learn more about control lines.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, value is set to 1.  
<id> | Id of the E5091A test set. Choose from 1 or 2. [Learn how to set ID value](../../../S2_Opt/Crosstalk.md#Swp).  
<data> | Data value used to set control lines. Values are obtained by adding weights from the following table that correspond to individual lines. HIGH =1; LOW=0. | Line | Weight  
---|---  
1 | 1  
2 | 2  
3 | 4  
4 | 8  
5 | 16  
6 | 32  
7 | 64  
8 | 128  
  
0 - Sets all lines low

255 - Sets all lines high  
  
Examples | 'The following sets line 3 and 4 high. All other lines low. SENS:MULT1:TSET9:OUTP 12  
Query Syntax | SENSe<cnum>:MULTiplexer<id>:TSET9:OUTPut[:DATA]?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## SENSe<cnum>:MULTiplexer<id>:TSET9:PORT1 <char> Superseded

Applicable Models: N522xB, N523xB, N524xB, E5080A Note: This command is
replaced with [SENS:MULT:ALLPorts](Multiplexer.md#AllPorts) which sets ALL
ports to the specified outputs. (Read-Write) Switches Port 1 of the specified
E5091A to one of the available outputs.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<id> | Id of the E5091A test set. Choose from 1 or 2. [Learn how to set ID value](../../../S2_Opt/Crosstalk.md#Swp).  
<char> | Output port to be switched to. Choose from: A T1 \- (If Port 2 already is connected to T1, then Port 2 will be switched to T2.)  
Examples | SENS:MULT1:TSET9:PORT1 A  
Query Syntax | SENSe<cnum>:MULTiplexer<id>:TSET9:PORT1?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | A  
  
* * *

## SENSe<cnum>:MULTiplexer<id>:TSET9:PORT2 <char> Superseded

Applicable Models: N522xB, N523xB, N524xB, E5080A Note: This command is
replaced with [SENS:MULT:ALLPorts](Multiplexer.md#AllPorts) which sets ALL
ports to the specified outputs. (Read-Write) Switches Port 2 of the specified
E5091A to one of the available outputs.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<id> | Id of the E5091A test set. Choose from 1 or 2. [Learn how to set ID value](../../../S2_Opt/Crosstalk.md#Swp).  
<char> | Output port to be switched to. Choose from: T1 \- If Port 1 already is connected to T1, then Port 1 will be switched to A. T2  
Examples | SENS:MULT1:TSET9:PORT2 T2  
Query Syntax | SENSe<cnum>:MULTiplexer<id>:TSET9:PORT2?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | T1  
  
* * *

## SENSe<cnum>:MULTiplexer<id>:TSET9:PORT3 <char> Superseded

Applicable Models: N522xB, N523xB, N524xB, E5080A Note: This command is
replaced with [SENS:MULT:ALLPorts](Multiplexer.md#AllPorts) which sets ALL
ports to the specified outputs. (Read-Write) Switches Port 3 of the specified
E5091A to one of the available outputs.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<id> | Id of the E5091A test set. Choose from 1 or 2. [Learn how to set ID value](../../../S2_Opt/Crosstalk.md#Swp).  
<char> | Output port to be switched to. Choose from: R1 (R1+) R2 (R2+) R3 (R3+) If option 007 (7port), R2 is selected.  
Examples | SENS:MULT1:TSET9:PORT3 R2  
Query Syntax | SENSe<cnum>:MULTiplexer<id>:TSET9:PORT3?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | R1  
  
* * *

## SENSe<cnum>:MULTiplexer<id>:TSET9:PORT4 <char> Superseded

Applicable Models: N522xB, N523xB, N524xB, E5080A Note: This command is
replaced with [SENS:MULT:ALLPorts](Multiplexer.md#AllPorts) which sets ALL
ports to the specified outputs. (Read-Write) Switches Port 4 of the specified
E5091A to one of the available outputs.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<id> | Id of the E5091A test set. Choose from 1 or 2. [Learn how to set ID value](../../../S2_Opt/Crosstalk.md#Swp).  
<char> | Output port to be switched to. Choose from: R1 (R1-) R2 (R2-) R3 (R3-) If option 007 (7port), R2 is selected.  
Examples | SENS:MULT1:TSET9:PORT4 R2  
Query Syntax | SENSe<cnum>:MULTiplexer<id>:TSET9:PORT4?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | R1  
  
* * *

## SENSe:MULTiplexer<id>:TYPe <name>

Applicable Models: N522xB, N523xB, N524xB, E5080B, E5081A, M980xA (Read-Write)
Specifies the configuration of the E5092A test set. Note: To use this command
with the M980xA PXI VNA, the firmware version must be A.15.xx.xx and above,
and the S94702A AMX VNA Plugin license is required.  
---  
Parameters |   
<name> | String The name of the type of test set. Must be one of the items in the list returned by the [SENSe:MULT:CATalog?](Multiplexer.md#Catalog) query  E5092_13, E5092_16, E5092_22, E5092_28, E5092_X10  
<id> | Id of the external test set. Set by this command. Use consecutive values starting at 1.  
Examples | SENS:MULT1:TYPE E5092_22 ' set E5092A to 22-port config.  
Query Syntax | SENSe:MULTiplexer<id>:TYPe?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

