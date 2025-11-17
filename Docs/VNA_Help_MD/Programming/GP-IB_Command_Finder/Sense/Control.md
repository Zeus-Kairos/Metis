# Control

When you use the E5080B/81A, you can control the Interface control through the
VNA firmware.

SENSe:CONTrol: | [:STATe] | :DWELl | :HANDler | [:DATA] | [:STATe] | :DIO | [:STATE] | :VIO | :LEVel | :IMMediate | :IOTYpe | :PIO | :TYPE | :LEVel | :RFFE | :CLOCk | :CSEQuence | :SADDress | :TYPE | :BCOunt | :ADDRess | [:WRITe]:DATA | :READ:DATA | :COUNt | :MACRo | [:STATe] | :COMMand | :FILE | :PATH | :ARGuments  
---  
  
Click on a keyword to view the command details.

* * *

## SENSe<cnum>:CONTrol:[:STATe] <bool>

Applicable Models: E5080B, E5081A (Read-Write) Sets and read the state of
interface control for all channels. Channel number is ignored.  
---  
Parameters |   
<cnum> | Channel number.  
<bool> | Module control state. Choose from: O or OFF \- Interface control port signals won't be sent. 1 or ON \- Interface control port signals will be sent.  
Examples | SENS:CONT  
sense2:control?  
Query Syntax | :SENSe<cnum>:CONTrol:[:STATe]?   
Return Type | Boolean  
Default | OFF or 0  
Preset | 0  
Save or Recall | Yes  
  
* * *

## SENSe<cnum>:CONTrol:DWELl <char>, <num>

Applicable Models: E5080B, E5081A (Read-Write) Sets and read the delay time
between the time all interface control port signals and all commands sent and
the one measurements start. Set independently per channel and for forward and
reverse sweep. Not set per IO type.  
---  
Parameters |   
<cnum> | Channel number.  
<char> | Character \- when to send remote commands. Choose from: AFTer \- After the channel sweep ends. BEFore \- Before the channel sweep starts.  
<num> | Wait time in milliseconds. Any positive integer is allowed.  
Examples | SENS:CONT:DWEL BEF 10  
sense2:control:dwell?  
Query Syntax | :SENSe<cnum>:CONTrol:DWELl? <char>  
Return Type | Character  
Default | 0  
Preset | 0  
Save or Recall | Yes  
  
* * *

## SENSe<cnum>:CONTrol:HANDler:<grp>[:DATA] <char>, <num>

Applicable Models: E5080B, E5081A (Read-Write) Sends values to the respective
Handler I/O port (A-D). Although ports C and D are normally bidirectional,
ONLY Output mode is allowed using the Interface Control feature. It cannot
read from these, or any other ports.  
---  
Parameters |   
<cnum> | Channel number.  
<grp> | Port identifier to set bits for. Choose from: A, B, C and D.  
<char> | Character \- when to send remote commands. Choose from: AFTer \- After the channel sweep ends. BEFore \- Before the channel sweep starts.  
<num> | The number of the data bits to set. The range of the value is determined as follows.  Port A: 0 - 255 Port B: 0 - 255 Port C: 0 - 15 Port D: 0 - 15  
Examples | SENS:CONT:HAND:B AFT, 255  
sense2:control:handler:B? after  
Query Syntax | :SENSe<cnum>:CONTrol:HANDler:<grp>[:DATA]? <char>  
Return Type | Numeric  
Default | 0  
Preset | 0  
Save or Recall | Yes  
  
* * *

## SENSe<cnum>:CONTrol:HANDler[:STATE] <char>, <bool>

Applicable Models: E5080B, E5081A (Read-Write) Set and read the control
function state for each channel. If ON, Handler I/O port signals will be sent
before the beginning of the sweep or after the end of the sweep. If OFF, these
signals will not be changed.  
---  
Parameters |   
<cnum> | Channel number.  
<char> | Character \- when to send remote commands. Choose from: AFTer \- After the channel sweep ends. BEFore \- Before the channel sweep starts.  
<bool> | Choose from: ON (1) \- Handler I/O port signals will be sent. OFF (0) \- Handler I/O port signals won't be sent.  
Examples | SENS:CONT:HAND AFT, ON  
sense2:control:handler? after  
Query Syntax | :SENSe<cnum>:CONTrol:HANDler[:STATe]? <char>  
Return Type | Boolean  
Default | 1  
Preset | 1  
Save or Recall | Yes  
  
* * *

## SENSe<cnum>:CONTrol:DIO<id>[:STATe] <char>, <bool>

Applicable Models: E5080B, E5081A (Read-Write) Set and read the control
function state for each channel. If ON, DUT control signals will be sent
before the beginning of the sweep or after the end of the sweep. If OFF, then
DUT signals will not be changed.  
---  
Parameters |   
<cnum> | Channel number.  
<id> | DIO number, 1 or 2  
<char> | Character \- when to send remote commands. Choose from: AFTer \- After the channel sweep ends. BEFore \- Before the channel sweep starts.  
<bool> | Function enable or disable control. Choose from: ON or OFF  
Examples | SENS:CONT:DIO1 AFT, ON  
sense2:control:dio1? after  
Query Syntax | :SENSe<cnum>:CONTrol:DIO<id>[:STATe]? <char>  
Return Type | Boolean (1= ON, 0= OFF)  
Default | OFF  
  
* * *

## SENSe<cnum>:CONTrol:DIO<id>:VIO[:STATe] <char>, <bool>

Applicable Models: E5080B, E5081A (Read-Write) Set and read the VIO function
state for each channel. If ON, then VIO's voltage is set to the value which is
determined by SENSe:CONTrol:DIO:LEVel before the beginning of the sweep or
after the end of he sweep. If OFF, the VIO's voltage is disabled.  
---  
Parameters |   
<cnum> | Channel number.  
<id> | DIO number, 1 or 2  
<char> | Character \- when to send remote commands. Choose from: AFTer \- After the channel sweep ends. BEFore \- Before the channel sweep starts.  
<bool> | Function enable or disable control. Choose from: ON or OFF  
Examples | SENS:CONT:DIO1:VIO AFT, OFF  
sense2:control:dio1:vio? after  
Query Syntax | :SENSe<cnum>:CONTrol:DIO<id>:VIO[:STATe]? <char>  
Return Type | Boolean (1= ON, 0= OFF)  
Default | ON  
  
* * *

## SENSe<cnum>:CONTrol:DIO<id>:LEVel <char>, <num>

Applicable Models: E5080B, E5081A (Read-Write) Specifies IO level of the DUT
Control DIO1 or DIO2's 8-bit IO. The value of AFTer is overwritten by the one
of BEFore and vice versa due to set the same value to both AFTer and BEFore.  
---  
Parameters |   
<cnum> | Channel number.  
<id> | DIO number, 1 or 2  
<char> | Character \- when to send remote commands. Choose from: AFTer \- After the channel sweep ends. BEFore \- Before the channel sweep starts.  
<num> | IO level in volt. Value range, 0.9 to 3.5, step 0.05.  
Examples | SENS:CONT:DIO1:VIO AFT, OFF  
sense2:control:dio1:vio? after  
Query Syntax | :SENSe<cnum>:CONTrol:DIO<id>:LEVel? <char>  
Return Type | Numeric  
Default | 1.2  
  
Note: The default value definition comes from MIPI RFFE standard. Referring to
the VIO Supply Pin Requirements, 1.2V is the minimum typical voltage value of
the definition.

* * *

## SENSe<cnum>:CONTrol:DIO<id>:IMMediate <char>

Applicable Models: E5080B, E5081A (Write only) Specifies parameter set of DUT
Control function for each channel. And, fetch E5080B Hardware status values
(PIO input state, RFFE read command results) and stores the values in Firmware
variables. If executed, the DUT signals will be sent immediately. It doesn't
matter if Enable DUT Control is ON or OFF.  
---  
Parameters |   
<cnum> | Channel number.  
<id> | DIO number, 1 or 2  
<char> | Character \- when to send remote commands. Choose from: AFTer \- After the channel sweep ends. BEFore \- Before the channel sweep starts.  
Examples | SENS:CONT:DIO1:IMM BEF  
Query Syntax | Not applicable  
Default | Not applicable  
  
* * *

## SENSe<cnum>:CONTrol:DIO<id>:IOTYpe<iogroup> <char>, <enum>

Applicable Models: E5080B, E5081A (Read-Write) Specifies IO function type of
the 8-bit IO pin, for each IO group. IO group1 is IO pin 1 and 2, group2 is
pin 3 and 4, group3 is pin 5 and 6, group4 is pin 7 and 8.  
---  
Parameters |   
<cnum> | Channel number.  
<id> | DIO number, 1 or 2  
<iogroup> | IO group number. Value range, 1 to 4.  
<char> | Character \- when to send remote commands. Choose from: AFTer \- After the channel sweep ends. BEFore \- Before the channel sweep starts.  
<enum> | Set the IO function for the IO group. Choose from: PARallel or RFFE  
Examples | SENS:CONT:DIO1:IOTY AFT, RFFE  
sense2:control:dio1:ioty1? after  
Query Syntax | :SENSe<cnum>:CONTrol:DIO<id>:IOTYpe<iogroup>? <char>  
Return Type | Character  
Default | PARallel  
  
* * *

## SENSe<cnum>:CONTrol:DIO<id>:PIO<iopin>:TYPE <char>, <enum>

Applicable Models: E5080B, E5081A (Read-Write) Set or read the signal
direction type of Parallel IO, for each IO pin.. This setting is valid when
the IO pin function is selected as parallel IO.  
---  
Parameters |   
<cnum> | Channel number.  
<id> | DIO number, 1 or 2  
<iopin> | IO pin number.  
<char> | Character \- when to send remote commands. Choose from: AFTer \- After the channel sweep ends. BEFore \- Before the channel sweep starts.  
<enum> | IO direction. Choose from: IN or OUT  
Examples | SENS:CONT:DIO1:PIO:TYPE AFT, IN  
sense2:control:dio1:pio2:type? after  
Query Syntax | :SENSe<cnum>:CONTrol:DIO<id>:PIO<iopin>:TYPE? <char>  
Return Type | Character  
Default | OUT  
  
* * *

## SENSe<cnum>:CONTrol:DIO<id>:PIO<iopin>:LEVel <char>, <enum>

Applicable Models: E5080B, E5081A (Read-Write) Set or read the signal level of
IO pin, high or low. This setting is valid when the IO pin function is
selected as parallel IO. If the IO type is IN, this command shall be a read-
only command. Write command will cause error.  
---  
Parameters |   
<cnum> | Channel number.  
<id> | DIO number, 1 or 2  
<iopin> | IO pin number.  
<char> | Character \- when to send remote commands. Choose from: AFTer \- After the channel sweep ends. BEFore \- Before the channel sweep starts.  
<enum> | Signal level. Choose from: HIGH or LOW  
Examples | SENS:CONT:DIO1:PIO:LEV AFT, HIGH  
sense2:control:dio1:pio7:level? after  
Query Syntax | :SENSe<cnum>:CONTrol:DIO<id>:PIO<iopin>:LEVel? <char>  
Return Type | Character  
Default | LOW  
  
* * *

## SENSe<cnum>:CONTrol:DIO<id>:RFFE:CLOCk <char>, <num>

Applicable Models: E5080B, E5081A (Read-Write) Set or read the RFFE clock
rate.  
---  
Parameters |   
<cnum> | Channel number.  
<id> | DIO number, 1 or 2  
<char> | Character \- when to send remote commands. Choose from: AFTer \- After the channel sweep ends. BEFore \- Before the channel sweep starts.  
<num> | Clock rate in Hz. Value range, 25kHz to 25000kHz. Possible values are (50000/n) kHz, with integer n, 2000 to 2.  
Examples | SENS:CONT:DIO1:RFFE:CLOC AFT, 25000  
sense2:control:dio1:rffe:clock? after  
Query Syntax | :SENSe<cnum>:CONTrol:DIO<id>:RFFE:CLOCk? <char>  
Return Type | Numeric  
Default | 50000  
  
Note: The default value is the minimum integer value of clock rate, which
meets the RFFE standard frequency range.

* * *

## SENSe<cnum>:CONTrol:DIO<id>:RFFE<rffech>:CSEQuence<csnum>:SADDress <char>,
<num>

Applicable Models: E5080B, E5081A (Read-Write) Set or read the secondary
address (SA in GUI) for the specified command sequence.  
---  
Parameters |   
<cnum> | Channel number.  
<id> | DIO number, 1 or 2  
<rffech> | RFFE channel number. 1 to 4.  
<csnum> | RFFE command sequence number. 1 to 16.  
<char> | Character \- when to send remote commands. Choose from: AFTer \- After the channel sweep ends. BEFore \- Before the channel sweep starts.  
<num> | DUT RFFE secondary address. 0 to 15.  
Examples | SENS:CONT:DIO1:RFFE:CSEQ:SADD AFT, 2  
sense2:control:dio1:rffe1:csequence2:saddress? after  
Query Syntax | :SENSe<cnum>:CONTrol:DIO<id>:RFFE<rffech>:CSEQuence<csnum>:SADDress? <char>  
Return Type | Numeric  
Default | 0  
  
* * *

## SENSe<cnum>:CONTrol:DIO<id>:RFFE<rffech>:CSEQuence<csnum>:TYPE <char>,
<enum>

Applicable Models: E5080B, E5081A (Read-Write) Set or read the command
sequence type for the specified command sequence.  
---  
Parameters |   
<cnum> | Channel number.  
<id> | DIO number, 1 or 2  
<rffech> | RFFE channel number. 1 to 4.  
<csnum> | RFFE command sequence number. 1 to 16.  
<char> | Character \- when to send remote commands. Choose from: AFTer \- After the channel sweep ends. BEFore \- Before the channel sweep starts.  
<enum> | RFFE command sequence type. Choose from:  R0WRite: Register 0 Write RREad: Register Read RWRite: Register Write ERRead: Extended Register Read ERWRite : Extended Register Write  
Examples | SENS:CONT:DIO1:RFFE:CSEQ:TYPE AFT, R0WR  
sense2:control:dio1:rffe1:csequence2:type? after  
Query Syntax | :SENSe<cnum>:CONTrol:DIO<id>:RFFE<rffech>:CSEQuence<csnum>:TYPE? <char>  
Return Type | Character  
Default | RREad  
  
* * *

## SENSe<cnum>:CONTrol:DIO<id>:RFFE<rffech>:CSEQuence<csnum>:BCOunt <char>,
<num>

Applicable Models: E5080B, E5081A (Read-Write) Set and read the byte count for
the specified command sequence.  
---  
Parameters |   
<cnum> | Channel number.  
<id> | DIO number, 1 or 2  
<rffech> | RFFE channel number. 1 to 4.  
<csnum> | RFFE command sequence number. 1 to 16.  
<char> | Character \- when to send remote commands. Choose from: AFTer \- After the channel sweep ends. BEFore \- Before the channel sweep starts.  
<num> | Byte Count value. Integer value. The value range is coupled with command sequence type setting. | Command sequence type | Byte count range  
---|---  
Register 0 Write Register Read Register Write | 1 (fixed)  
Extended Register Write Extended Register Read | 1 to 16  
  
Examples | SENS:CONT:DIO1:RFFE:CSEQ:BCO AFT, 4  
sense2:control:dio1:rffe1:csequence2:bcount? after  
Query Syntax | :SENSe<cnum>:CONTrol:DIO<id>:RFFE<rffech>:CSEQuence<csnum>:BCOunt? <char>  
Return Type | Numeric  
Default | 1  
  
* * *

## SENSe<cnum>:CONTrol:DIO<id>:RFFE<rffech>:CSEQuence<csnum>:ADDRess <char>,
<num>

Applicable Models: E5080B, E5081A (Read-Write) Set and read the address value
for the specified command sequence.  
---  
Parameters |   
<cnum> | Channel number.  
<id> | DIO number, 1 or 2  
<rffech> | RFFE channel number. 1 to 4.  
<csnum> | RFFE command sequence number. 1 to 16.  
<char> | Character \- when to send remote commands. Choose from: AFTer \- After the channel sweep ends. BEFore \- Before the channel sweep starts.  
<num> | Address value. Integer value. The value range is coupled with command sequence type setting. | Command sequence type | Byte count range  
---|---  
Register 0 Write | 0 (fixed)  
Register Read Register Write | #h00 to #h1F (0-31)  
Extended Register Write Extended Register Read | #h00 to #hFF (0-255)  
  
Examples | SENS:CONT:DIO1:RFFE:CSEQ:ADDR AFT, 4  
sense2:control:dio1:rffe1:csequence2:address? after  
Query Syntax | :SENSe<cnum>:CONTrol:DIO<id>:RFFE<rffech>:CSEQuence<csnum>:ADDRess? <char>  
Return Type | Numeric  
Default | 0  
  
* * *

## SENSe<cnum>:CONTrol:DIO<id>:RFFE<rffech>:CSEQuence<csnum>[:WRITe]:DATA
<char>, <data>

Applicable Models: E5080B, E5081A (Read-Write) Set and read the data values
for the specified command sequence. This command works if the command sequence
type is Register 0 Write or Register Write or Extended Register Write.
If the command sequence type is Register Read or Extended Register Read,
this command will cause error.  
---  
Parameters |   
<cnum> | Channel number.  
<id> | DIO number, 1 or 2  
<rffech> | RFFE channel number. 1 to 4.  
<csnum> | RFFE command sequence number. 1 to 16.  
<char> | Character \- when to send remote commands. Choose from: AFTer \- After the channel sweep ends. BEFore \- Before the channel sweep starts.  
<data> | Comma separated list of data values. The value length is coupled with byte count setting. If data list length does not match with byte count setting, write command will cause error.  
Examples | SENS:CONT:DIO1:RFFE:CSEQ:WRIT:DATA AFT, 10  
sense2:control:dio1:rffe1:csequence2:write:data? after  
Query Syntax | :SENSe<cnum>:CONTrol:DIO<id>:RFFE<rffech>:CSEQuence<csnum>[:WRITe]:DATA? <char>  
Return Type | Comma separated numeric values  
Default | 0  
  
* * *

## SENSe<cnum>:CONTrol:DIO<id>:RFFE<rffech>:CSEQuence<csnum>:READ:DATA? <char>

Applicable Models: E5080B, E5081A (Read only) Read the data and parity value
pairs from DUT for the specified command sequence.  
---  
Parameters |   
<cnum> | Channel number.  
<id> | DIO number, 1 or 2  
<rffech> | RFFE channel number. 1 to 4.  
<csnum> | RFFE command sequence number. 1 to 16.  
<char> | Character \- when to send remote commands. Choose from: AFTer \- After the channel sweep ends. BEFore \- Before the channel sweep starts.  
Examples | SENS:CONT:DIO1:RFFE:CSEQ:READ:DATA? AFT  
sense2:control:dio1:rffe1:csequence2:read:data? after  
Query Syntax | :SENSe<cnum>:CONTrol:DIO<id>:RFFE<rffech>:CSEQuence<csnum>:READ:DATA? <char>  
Return Type | Comma separated numeric values, list of data and parity pairs. Ex. Byte count is 3 case, return values are below: [data#1],[parity#1],[data#2],[parity#2],[data#3],[parity#3]  
Default | Not applicable  
  
* * *

## SENSe<cnum>:CONTrol:DIO<id>:RFFE<rffech>:CSEQuence:COUNt <char>

Applicable Models: E5080B, E5081A (Read-Write) Set and read the RFFE Command
Sequence count. If user set the larger value than previously set, new RFFE
Command Sequences will be added with default parameter value.  
---  
Parameters |   
<cnum> | Channel number.  
<id> | DIO number  
<rffech> | RFFE channel number. 1 to 4.  
<char> | Character \- when to send remote commands. Choose from: AFTer \- After the channel sweep ends. BEFore \- Before the channel sweep starts.  
Examples | SENS:CONT:DIO1:RFFE:CSEQ:COUN AFT  
sense2:control:dio1:rffe1:csequence:count? after  
Query Syntax | :SENSe<cnum>:CONTrol:DIO<id>:RFFE<rffech>:CSEQuence:COUNt? <char>  
Return Type | Numeric  
Default | 0  
  
* * *

## SENSe<cnum>:CONTrol:MACRo[:STATe] <char>, <bool>

Applicable Models: E5080B, E5081A, N522xB, N523xB, N524xB (Read-Write) Enables
or disables software interface controls.  
---  
Parameters |   
<cnum> | Channel number.  
<char> | Character \- when to send remote commands. Choose from: AFTer \- After the channel sweep ends. BEFore \- Before the channel sweep starts.  
<bool> | ON or 1 \- Turns software interface control ON. OFF or 0 \- Turns software interface control OFF.  
Examples | SENS:CONT:MACR AFT, ON  
sense2:control:macro? after  
Query Syntax | :SENSe<cnum>:CONTrol:MACRo[:STATe]? <char>  
Return Type | Boolean  
Default | OFF  
  
* * *

## SENSe<cnum>:CONTrol:MACRo:COMMand <char>, <cmdList>

Applicable Models: E5080B, E5081A, N522xB, N523xB, N524xB (Read-Write) Set and
read SCPI commands with target GPIB addresses (numbers) or VISA addresses. The
specified SCPI commands are sent to the target instruments before the first
trace on the channel begins sweeping. It is the end users responsibility to
use this command.  
---  
Parameters |   
<cnum> | Channel number.  
<char> | Character \- when to send remote commands. Choose from: AFTer \- After the channel sweep ends. BEFore \- Before the channel sweep starts.  
<cmdList> | The string of \n separates a pair of GPIB/VISA addresses and SCPI commands, and the string of   separates GPIB/VISA address and SCPI in the following format; address1 command1\naddress2 command2\n   
Examples | SENS:CONT:MACR:COMM AFT  
sense2:control:macro? after  
Query Syntax | :SENSe<cnum>:CONTrol:MACRo:COMMand? <char>  
Return Type | String of comma-separated GPIB/VISA addresses and SCPI commands  
Default | " "  
  
* * *

## SENSe<cnum>:CONTrol:MACRo:FILE:PATH <char>, <path>

Applicable Models: E5080B, E5081A, N522xB, N523xB, N524xB (Read-Write) Set and
read a file path to a macro. The macro is executed before the first trace on
the channel begins sweeping. It is the end users responsibility to use this
command. Its needed to check the check box of Enable Drive Access in the
SCPI dialog to execute the actual macro file.  
---  
Parameters |   
<cnum> | Channel number.  
<char> | Character \- when to send remote commands. Choose from: AFTer \- After the channel sweep ends. BEFore \- Before the channel sweep starts.  
<path> | Command line strings   
Examples | SENS:CONT:MACR:FILE:PATH AFT, "cscript D:\temp\test.vbs"   
sense2:control:file:path? after  
Query Syntax | :SENSe<cnum>:CONTrol:MACRo:FILE:PATH? <char>  
Return Type | String   
Default | " "  
  
* * *

## SENSe<cnum>:CONTrol:MACRo:FILE:ARGuments <char>, <arg>

Applicable Models: E5080B, E5081A, N522xB, N523xB, N524xB (Read-Write) Set and
read arguments for a macro. The macro is executed before the first trace on
the channel begins sweeping. It is the end users responsibility to use this
command. Its needed to check the check box of Enable Drive Access in the
SCPI dialog to execute the actual macro file.  
---  
Parameters |   
<cnum> | Channel number.  
<char> | Character \- when to send remote commands. Choose from: AFTer \- After the channel sweep ends. BEFore \- Before the channel sweep starts.  
<arg> | Arguments for a macro  
Examples | SENS:CONT:MACR:FILE:ARG AFT, "localhost"   
sense2:control:file? after  
Query Syntax | :SENSe<cnum>:CONTrol:MACRo:FILE:ARGuments? <char>  
Return Type | String   
Default | " "

