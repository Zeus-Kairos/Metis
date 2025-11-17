# Calculate:FSimulator Commands

* * *

Specifies settings and fixturing for Balanced Measurements.

CALCulate:FSIMulator [Active More commands](FSimulatorActive.md) [BALun More
commands](FSimulatorBalun.htm) [DRAFt More commands](FSimulatorDraft.md)
[EMBed More commands](FSimulatorEmbed.md) [GLOop More
commands](FSimulatorGLoop.htm) LEGacy? [SENDed More
commands](FSimulatorSend.htm) [SNP:EXTRapolate](FSimulator.md#extrapolate)
[STATe](FSimulator.md#FSimState)  
---  
  
Click a keyword to view the command details.

See Also

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

CALCulate<cnum>:FSIMulator:LEGacy?

Applicable Models: All (Read only) Returns TRUE if user is only using legacy
SCPI fixture commands. If the user has used the GUI or new SCPI commands to
create a fixture, it will return FALSE.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
Examples | CALC:FSIM:LEG? calculate2:fsimulator:legacy?  
Query Syntax | CALCulate<cnum>:FSIMulator:LEGacy?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | TRUE  
  
* * *

CALCulate<cnum>:FSIMulator:SNP:EXTRapolate <bool> Superseded

Applicable Models: All Note: This command is changed to
[CALCulate:FSIMulator:CIRCuit:FILE:EXTrapolate](FSimulatorActive.md#CircFileExtr)[
](FSimulatorDraft.htm#SectCircEnab)Learn about [Using Fixture
Simulator](../../Using_Fixture_Simulator.htm). (Read-Write) Turns ON and OFF
SNP file extrapolation for both 2-port and 4-port embedding/de-embedding.
Learn more. Note: This command affects ALL measurements on the specified
channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<bool> | Choose from: ON or 1 - Turns Extrapolation ON OFF or 0 - Turns Extrapolation OFF  
Examples | CALC:FSIM:SNP:EXTR 1  
calculate2:fsimulator:snp:extrapolate 0  
Query Syntax | CALCulate<cnum>:FSIMulator:SNP:EXTRapolate?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

CALCulate<cnum>:FSIMulator:STATe <bool>

Applicable Models: All (Read-Write) Turns all three fixturing functions (de-
embedding, port matching, impedance conversion) ON or OFF for all ports on the
specified channel. Does not affect port extensions. Note: This command affects
ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<bool> | Choose from: ON or 1 - Turns Fixturing ON OFF or 0 - Turns Fixturing OFF  
Examples | CALC:FSIM:STAT 1  
calculate2:fsimulator:state 0  
Query Syntax | CALCulate<cnum>:FSIMulator:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:DTOPology <device>, <topology>

Applicable Models: E5080A, M9485A

(Write-only) Defines the device type and the topology for a balanced
measurement. This command will replace the following commands:
[CALC:FSIM:BAL:TOP:SBAL[:PPOR]](FSimulatorBalun.md#topSBAL)
[CALC:FSIM:BAL:TOP:SSB[:PPOR]](FSimulatorBalun.md#topSSB)
[CALC:FSIM:BAL:TOP:BBAL[:PPOR]](FSimulatorBalun.md#topBBAL)
[CALC:FSIM:BAL:TOP:BALS[:PPOR]](FSimulatorBalun.md#topBALS)  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<device> | (String) Device type for the balanced measurement. B means the Balanced port; S means the Single-ended port. Choose from: B  1 port balanced device (2 ports) BB  Balanced \- Balanced device (4 ports) BS  Balanced \- Single-ended device (3 ports) SB  Single-ended \- Balanced device (3 ports) SSB  Single-ended \- Single-ended - Balanced device (4 ports)  
<topology> | (Int array) Physical port numbers mapped to the logical ports, separated by ,. B (Balanced) requires 2 physical port numbers: <nPos>, <nNeg>. S (Single-ended) requires 1 physical port number.  
Examples | CALC:DTOP "SB", 2, 1, 4 calculate:dtopology "SB", 2, 1, 4  
Query Syntax | CALCulate<cnum>:DTOPology <device>, <topology>?  
Return Type | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:PARameter:BALun[:STATe] <bool>

(Read-Write) Sets or gets a balanced measurement state.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mnum> | Measurement number for each measurement. There must be a selected measurement on the trace. If unspecified, <mnum> is set to 1.  
<bool> | ON or 1 - Balanced Transform ON. OFF or 0 - Balanced Transform OFF.  
Examples | CALC2:MEAS3:PAR:BAL ON  
calculate2:measure:parameter:balun:state off  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:PARameter:BALun[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF or 0  
  
* * *

