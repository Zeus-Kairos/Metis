# Control:Multiplexer Commands

Controls the E5092A Configurable Multiport Test Set.

CONTrol:MULTiplexer: OUTPut | A|B|C|D[DATA] | A|B|C|D:VOLTage[DATA] PORT | [:SELect]  
---  
  
Click on a keyword to view the command details.

See Also

  * [Learn about External Test Set Control](../../System/External_Testset_Control.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## CONTrol:MULTiplexer<id>:OUTPut:<grp>[:DATA] <num>

Applicable Models: N522xB, N523xB, N524xB, E5080B, M980xA (Read-Write) Sets or
returns the output port data for specified group with id of the E5092A
multiport test set. Notes:  
This command performs an **immediate** setting of the specified data on the
indicated test set, as opposed to the
**[SENSe<cnum>:MULTiplexer<id>:OUTPut:<grp>[:DATA]
<num>](Sense/Multiplexer.htm#GrpData)** command which sets the data only at
the beginning of each sweep of the specified channel number cnum. To use
this command with the M980xA PXI VNA, the firmware version must be A.15.xx.xx
and above, and the S94702A AMX VNA Plugin license is required.  
---  
Parameters |   
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
Examples | CONT:MULT1:STAT OFF CONT:MULT1:OUTP:B 8 ' immediately output 8 from control line B.  
Query Syntax | CONTrol:MULTiplexer<id>:OUTPut:<grp>[:DATa]?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CONTrol:MULTiplexer<id>:OUTPut:<grp>:VOLTage[:DATA] <volt>

Applicable Models: N522xB, N523xB, N524xB, E5080B, M980xA (Read-Write) Sets or
returns the output voltage for specified group with id of the E5092A multiport
test set. Notes:  
This command performs an **immediate** setting of the specified voltage on the
indicated test set, as opposed to the
**[SENSe<cnum>:MULTiplexer<id>:OUTPut:<grp>:VOLTage[:DATA]
<volt>](Sense/Multiplexer.htm#GrpVoltage)** command which sets the voltage
only at the beginning of each sweep of the specified channel number cnum. To
use this command with the M980xA PXI VNA, the firmware version must be
A.15.xx.xx and above, and the S94702A AMX VNA Plugin license is required.  
---  
Parameters |   
<id> | Id of the external test set either 1 or 2. If unspecified, Id is assumed to be 1.   
<grp> | A | B | C | D  
<volt> | Output voltage range for <grp> is between 0 to 5.2V and resolution is 10mV.  
Examples | CONT:MULT1:STAT OFF CONT:MULT1:OUTP:B:VOLT 4.2 ' immediately set control line B voltage to 4.2 volt.  
Query Syntax | CONTrol:MULTiplexer<id>:OUTPut:<grp>:VOLtage[:DATa]?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 V  
  
* * *

## CONTrol:MULTiplexer<id>:PORT<pnum>[:SELect] <string>

Applicable Models: N522xB, N523xB, N524xB, E5080B, M980xA (Write-Only) Sets
the multiport test set port. If this command creates a conflict with an
existing port, the VNA will resolve the conflict. Notes:  
This command performs an **immediate** setting of the specified port on the
indicated test set, as opposed to the
**[SENSe<cnum>:MULTiplexer<id>:PORT<pnum>:SELect
<string>](Sense/Multiplexer.htm#PortSelect)** command which sets the port only
at the beginning of each sweep of the specified channel number cnum. To use
this command with the M980xA PXI VNA, the firmware version must be A.15.xx.xx
and above, and the S94702A AMX VNA Plugin license is required.  
---  
Parameters |   
<id> | Id of the external test set. If unspecified, Id is assumed to be 1\. Must be previously set by the [SENSe:MULT:TYPE](Sense/Multiplexer.md#type) command.  
<pnum> | The VNA connection port number (1 to 4).  If the E5092As configuration is E5092_28, this parameter specifies the individual switch number (1 to 4: SP4T switches, 5 to 10: SPDT switches).  
<string> | The label of the E5092As measurement port.  If the E5092As configuration is E5092_28, this parameter specifies the connection of the individual switch. Refer to the table of SENS:MULT:PORT:SEL.  
Examples | CONT:MULT1:STAT OFF  CONT:MULT1:TYP 'E5092_22' CONT:MULT1:PORT1:SEL 'A2' ' set E5092A to 22-port config and immediately connect port1 to 'A2'.  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

