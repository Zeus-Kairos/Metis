# DUT Control

When you use the PXI VNAs, you can control the M9341B 8 bit IO through the VNA
firmware. The following commands are available when the launcher includes the
M9341B.

SENSe:DUTControl:M9341:[MODule] | [[:STATe]](DUTControl.md#module) | [:IOTYpe](DUTControl.md#IOTYpe) | [:LEVel](DUTControl.md#Level) | :PIO | [:TYPE](DUTControl.md#PIOType) | [:LEVel](DUTControl.md#PIOLev) | :RFFE | [:CLOCk](DUTControl.md#Clock) | :CSEQuence | [:SADDress](DUTControl.md#Sadress) | [:TYPE](DUTControl.md#CseqType) | [:BCOunt](DUTControl.md#CseqBco) | [:ADDRess](DUTControl.md#CseqAddr) | [[:WRITe]:DATA](DUTControl.md#CseqWri) | [:READ:DATA](DUTControl.md#CseqReadData) | [:COUNt](DUTControl.md#CseqCoun)  
---  
  
Click on a keyword to view the command details.

* * *

## SENSe<cnum>:DUTControl:M9341[:MODule<mod>][:STATe] <bool>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the DUT Control
function state for each channel.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9341B. The number starts from 1 for the leftmost module of M9341B.  
<bool> | Module control state. Choose from: O or OFF \- Skips to control the M9341A/B at the specified channel. 1 or ON \- Enables to control the M9341A/B at the specified channel.  
Examples | SENS:DUTC:M9341  
sense2:dutcontrol:m9341?  
Query Syntax | :SENSe<cnum>:DUTControl:M9341[:MODule<mnum>][:STATe]?  
Return Type | Boolean  
Default | OFF or 0  
  
* * *

## :SENSe<cnum>:DUTControl:M9341[:MODule<mod>]:IOTYpe<iogroup> <iofunc>

Applicable Models: All PXIe VNAs (Read-Write) Sets and returns I/O function
type of the 8 bit Input/Output pins, for each I/O group.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9341B. The number starts from 1 for the leftmost module of M9341B.  
<iogroup> | IO group number. Value range, 1 to 4. 1: Group 1 (pins No. 1 and 2) 2: Group 2 (pins No. 3 and 4) 3: Group 3 (pins No. 5 and 6) 4: Group 4 (pins No. 7 and 8)  
<iofunc> | set the IO function for the io group. <PARallel | RFFE>.  
Examples | SENS:DUTC:M9341:IOTY1 PAR  
sense2:dutcontrol:m9341:module2:iotype RFFE  
Return Type | Char  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | PARallel  
  
* * *

## :SENSe<cnum>:DUTControl:M9341[:MODule<mod>]:LEVel <lvl>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the output
voltage level of the M9341B 8bit I/O  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9341B. The number starts from 1 for the leftmost module of M9341B.  
<lvl> | IO level in volt. Value range: 0.9 to 3.5. Step 0.05.  
Examples | SENS:DUTC:M9341:LEV 1.5  
sense2:dutcontrol:m9341:module2:level?  
Query Syntax | :SENSe<cnum>:DUTControl:M9341[:MODule<mnum>]:LEVel?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1.2  
  
* * *

## :SENSe<cnum>:DUTControl:M9341[:MODule<mod>]:PIO<iopin>:TYPE <dir>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the signal
direction type of Parallel IO, for each IO pin. This setting is valid when the
io pin function is selected as parallel IO.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9341B. The number starts from 1 for the leftmost module of M9341B.  
<iopin> | IO pin number  
<dir> | IO direction. Choose from: IN or OUT  
Examples | SENS:DUTC:M9341:PIO:TYPE IN  
sense2:dutcontrol:m9341:module2:pio2:type?  
Query Syntax | :SENSe<cnum>:DUTControl:M9341[:MODule<mnum>]:PIO<iopin>:TYPE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OUT  
  
* * *

## :SENSe<cnum>:DUTControl:M9341[:MODule<mod>]:PIO<iopin>:LEVel <lvl>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the signal level
of IO pin, high or low. This setting is valid when the io pin function is
selected as parallel IO. If the IO type is IN, this command shall be a read-
only command. Write command will cause error.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9341B. The number starts from 1 for the leftmost module of M9341B.  
<iopin> | IO pin number  
<lvlr> | Signal level. Choose from: HIGH or LOW  
Examples | SENS:DUTC:M9341:PIO:LEV LOW  
sense2:dutcontrol:m9341:module2:pio2:level?  
Query Syntax | :SENSe<cnum>:DUTControl:M9341[:MODule<mnum>]:PIO<iopin>:LEVel?  
Return Type | Char  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | LOW  
  
* * *

## :SENSe<cnum>:DUTControl: M9341[:MODule<mod>]:RFFE:CLOCk <clk>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the RFFE clock
rate.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9341B. The number starts from 1 for the leftmost module of M9341B.  
<clk> | Clock rate in Hz. Value range, 25kHz to 25000kHz. Possible values are 50000/n, with integer n, 2000 to 2. User can use suffix such as kHz and so on.  
Examples | :SENS:DUTC:M9341:RFFE:CLOCk 25KHZ sense2:dutcontrol:m9341:module2:rffe:clock?  
Query Syntax | :SENSe<cnum>:DUTControl: M9341[:MODule<mnum>]:RFFE:CLOCk?  
Return Type | numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 50000  
  
* * *

##
:SENSe<cnum>:DUTControl:M9341[:MODule<mod>]:RFFE<rffech>:CSEQuence<csnum>:SADDress
<adrs>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the secondary
address (SA in GUI) for the specified command sequence.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9341B. The number starts from 1 for the leftmost module of M9341B.  
<rffech> | RFFE channel number. 1 to 4  
<csnum> | RFFE command sequence number. 1 to 16.  
<adrs> | DUT RFFE secondary address. 0 to 15.  
Examples | :SENS:DUTC:M9341:RFFE:CSEQ:SADD 2 sense2:dutcontrol:m9341:module2:rffe:csequence2:saddress?  
Query Syntax | :SENSe<cnum>:DUTControl:M9341[:MODule<mnum>]:RFFE<rffech>:CSEQuence<csnum>:SADDress?  
Return Type | numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

##
:SENSe<cnum>:DUTControl:M9341[:MODule<mod>]:RFFE<rffech>:CSEQuence<csnum>:TYPE
<typ>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the command
sequence type for the specified command sequence.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9341B. The number starts from 1 for the leftmost module of M9341B.  
<rffech> | RFFE channel number. 1 to 4  
<csnum> | RFFE command sequence number. 1 to 16.  
<adrs> | RFFE command sequence type. Choose from: R0WRite: Register 0 Write RREad: Register Read RWRite: Register Write ERRead: Extended Register Read ERWRite : Extended Register Write  
Examples | :SENS:DUTC:M9341:RFFE:CSEQ:TYPE R0WR sense2:dutcontrol:m9341:module2:rffe:csequence2:type?  
Query Syntax | :SENSe<cnum>:DUTControl:M9341[:MODule<mnum>]:RFFE<rffech>:CSEQuence<csnum>:TYPE?  
Return Type | Char  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | RREad  
  
* * *

##
:SENSe<cnum>:DUTControl:M9341[:MODule<mod>]:RFFE<rffech>:CSEQuence<csnum>:BCOunt
<byt>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the byte count
for the specified command sequence.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9341B. The number starts from 1 for the leftmost module of M9341B.  
<rffech> | RFFE channel number. 1 to 4  
<csnum> | RFFE command sequence number. 1 to 16.  
<byt> | Byte Count value. Integer value. The value range is coupled with command sequence type setting. | Command sequence type | Byte count range  
---|---  
Register 0 Write Register Read Register Write | 1  
Extended Register Write Extended Register Read | 1 to 16  
  
Examples | :SENS:DUTC:M9341:RFFE:CSEQ:BCO 4 sense2:dutcontrol:m9341:module2:rffe:csequence2:bcount?  
Query Syntax | :SENSe<cnum>:DUTControl:M9341[:MODule<mnum>]:RFFE<rffech>:CSEQuence<csnum>:BCOUnt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

##
SENSe<cnum>:DUTControl:M9341[:MODule<mod>]:RFFE<rffech>:CSEQuence<csnum>:ADDRess
<adrs>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the address value
for the specified command sequence..  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9341B. The number starts from 1 for the leftmost module of M9341B.  
<rffech> | RFFE channel number. 1 to 4  
<csnum> | RFFE command sequence number. 1 to 16.  
<adrs> | Address value. Integer value. The value range is coupled with command sequence type setting. | Command sequence type | Byte count range  
---|---  
Register 0 Write | 0 (fixed)  
Register Read Register Write | #h00 to #h1F (0-31)  
Extended Register Write Extended Register Read | #h00 to #hFF (0-255)  
  
Examples | :SENS:DUTC:M9341:RFFE:CSEQ:ADDR 2 sense2:dutcontrol:m9341:module2:rffe:csequence2:address?  
Query Syntax | :SENSe<cnum>:DUTControl:M9341[:MODule<mnum>]:RFFE<rffech>:CSEQuence<csnum>:ADDRess?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

##
SENSe<cnum>:DUTControl:M9341[:MODule<mnum>]:RFFE<rffech>:CSEQuence<csnum>[:WRITe]:DATA
<data>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the data values
for the specified command sequence. This command works if the command sequence
type is Register 0 Write or Register Write or Extended Register Write.
If the command sequence type is Register Read or Extended Register Read,
this command will cause error.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9341B. The number starts from 1 for the leftmost module of M9341B.  
<rffech> | RFFE channel number. 1 to 4  
<csnum> | RFFE command sequence number. 1 to 16.  
<adrs> | comma separated list of data values. The value length is coupled with byte count setting. If data list length does not match with byte count setting, write command will cause error.  
Examples | :SENS:DUTC:M9341:RFFE:CSEQ:WRIT:DATA 10 sense2:dutcontrol:m9341:module2:rffe:csequence2:write:data?  
Query Syntax | :SENSe<cnum>:DUTControl:M9341[:MODule<mnum>]:RFFE<rffech>:CSEQuence<csnum>[:WRITe]:DATA?  
Return Type | Comma separated numeric values  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

##
SENSe<cnum>:DUTControl:M9341[:MODule<mnum>]:RFFE<rffech>:CSEQuence<csnum>:READ:DATA?

Applicable Models: All PXIe VNAs (Read only) Reads the data and parity value
pairs from DUT for the specified command sequence.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9341B. The number starts from 1 for the leftmost module of M9341B.  
<rffech> | RFFE channel number. 1 to 4  
<csnum> | RFFE command sequence number. 1 to 16.  
Examples | :SENS:DUTC:M9341:RFFE:CSEQ:READ:DATA? sense2:dutcontrol:m9341:module2:rffe:csequence2:read:data?  
Query Syntax | :SENSe<cnum>:DUTControl:M9341[:MODule<mnum>]:RFFE<rffech>:CSEQuence<csnum>:READ:DATA?  
Return Type | Comma separated numeric values, list of data and parity pairs. Ex. Byte count is 3 case, return values are below: [data#1],[parity#1],[data#2],[parity#2],[data#3],[parity#3]  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

##
SENSe<cnum>:DUTControl:M9341[:MODule<mnum>]:RFFE<rffech>:CSEQuence<csnum>:COUNt
<cnt>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the the number of
RFFE Command Sequence. If user set the larger value than previously set, new
RFFE command sequences will be added with the default parameter value.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9341B. The number starts from 1 for the leftmost module of M9341B.  
<rffech> | RFFE channel number. 1 to 4  
<cnt> | RFFE Command Sequence count. 1 to 16.  
Examples | :SENS:DUTC:M9341:RFFE:CSEQ:COUN 10 sense2:dutcontrol:m9341:module2:rffe:csequence2:count?  
Query Syntax | :SENSe<cnum>:DUTControl:M9341[:MODule<mnum>]:RFFE<rffech>:CSEQuence<csnum>:COUNt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

