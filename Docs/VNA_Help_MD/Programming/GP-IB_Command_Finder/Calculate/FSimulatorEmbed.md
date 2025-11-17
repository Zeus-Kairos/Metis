# Calculate:FSimulator:Embed Commands

* * *

Specifies settings for embedding and de-embedding balanced (4-port) fixturing
circuits.

CALCulate:FSIMulator:EMBed: NETWork: | [FILename](FSimulatorEmbed.md#Filename) | [PMAP](FSimulatorEmbed.md#pmap) | [TYPE](FSimulatorEmbed.md#type) [STATe](FSimulatorEmbed.md#state) TOPology: | [A:PORTs](FSimulatorEmbed.md#topA) | [B:PORTs](FSimulatorEmbed.md#topB) | [C:PORTs](FSimulatorEmbed.md#topC) | D:PORTs [TYPE](FSimulatorEmbed.md#TopType)  
---  
  
Click a blue keyword to view the command details.

See Also

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

Critical Note: CALCulate commands act on the selected measurement. You can
select one measurement for each channel using
[Calc:Par:MNUM](Parameter.md#MnumSel) or
[Calc:Par:Select](Parameter.md#cps). [Learn
more](../../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.htm).

* * *

CALCulate<cnum>:FSIMulator:EMBed:NETWork<n>:FILename <string> Superseded

Applicable Models: All The command set of
[CALCulate:FSIMulator:EMBed:XXXX](FSimulatorEmbed.md) is changed to
[CALCulate:FSIMulator:DRAFt:CIRCuit:YYYY](FSimulatorDraft.md) and
[CALCulate<cnum>:FSIMulator::CIRCuit:YYYY?](FSimulatorActive.md) Learn about
[Using Fixture Simulator](../../Using_Fixture_Simulator.md). (Read-Write)
Specifies the 4-port touchstone file (*.s4p) in which the network to embed or
de-embed resides. Following this command, send CALC:FSIM:EMB:NETW:TYPE. If the
specified file does not exist, an error occurs when type command is sent.
Learn about 4-port network embedding.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<n> | Network position. Choose from 1 or 2.  
<string> | File name and extension (.s4P) of the circuit. Files are stored in the "D:\" drive. To recall from a different folder, specify the full path name.  
Examples | 10 calculate2:fsimulator:embed:network2:filename "D:\myFile.s4P" 20 calculate2:fsimulator:embed:network2:type embed  
Query Syntax | CALCulate<cnum>:FSIMulator:EMBed:NETWork<n>:FILename?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

CALCulate<cnum>:FSIMulator:EMBed:NETWork<n>:PMAP <inA>,<inB>,<outA>,<outB>
Superseded

Applicable Models: All The command set of
[CALCulate:FSIMulator:EMBed:XXXX](FSimulatorEmbed.md) is changed to
[CALCulate:FSIMulator:DRAFt:CIRCuit:YYYY](FSimulatorDraft.md) and
[CALCulate<cnum>:FSIMulator::CIRCuit:YYYY?](FSimulatorActive.md) Learn about
[Using Fixture Simulator](../../Using_Fixture_Simulator.md). (Read-Write) Set
and return the port mapping for a 4-port SNP file to be embedded. Learn about
4-port network embedding.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<n> | Network position. Choose from 1 or 2.  
<inA> <inB> <outA> <outB> | Port Mapping. Use four port numbers in any order.  
Example | CALC:FSIM:EMB:NETW1:PMAP 1,3,2,4  
Query Syntax | CALCulate<cnum>:FSIMulator:EMBed:NETWork<n>:PMAP?  
Return Type | Comma-separated numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1,2,3,4  
  
* * *

CALCulate<cnum>:FSIMulator:EMBed:NETWork<n>:TYPE <char> Superseded

Applicable Models: All The command set of
[CALCulate:FSIMulator:EMBed:XXXX](FSimulatorEmbed.md) is changed to
[CALCulate:FSIMulator:DRAFt:CIRCuit:YYYY](FSimulatorDraft.md) and
[CALCulate<cnum>:FSIMulator::CIRCuit:YYYY?](FSimulatorActive.md) Learn about
[Using Fixture Simulator](../../Using_Fixture_Simulator.md). (Read-Write)
Specify the type of processing to take place on the specified 4-port network.
First specify the network filename with
[CALC:FSIM:EMB:NETW:FIL](FSimulatorEmbed.md#Filename). Learn about 4-port
network embedding.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<n> | Network position. Choose from 1 or 2.  
<char> | Processing type. Choose from : NONE \- The same as disabling. EMBed \- Add Network circuit. DEEMbed \- Remove Network circuit.  
Example | 10 CALC:FSIM:EMB:NETW2:FIL 'myFile.s4p' 20 CALC:FSIM:EMB:NETW2:TYPE EMBed  
Query Syntax | CALCulate<cnum>:FSIMulator:EMBed:NETWork<n>:TYPE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | NONE  
  
* * *

CALCulate<cnum>:FSIMulator:EMBed:STATe <bool> Superseded

Applicable Models: All This command is changed to [CALCulate:FSIMulator:DRAFt:SECTion:CIRCuit:ENABle <ON | OFF>](FSimulatorDraft.md#SectCircEnab) and [CALCulate:FSIMulator:SECTion:CIRCuit:ENABle?](FSimulatorActive.md#SectCircEnab) Learn about [Using Fixture Simulator](../../Using_Fixture_Simulator.md). (Read-Write) Turns ON or OFF 4-port Network Embedding/De-embedding for all ports on the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<bool> | Choose from: ON or 1 - Turns 4-port Network Embedding/De-embedding ON OFF or 0 - Turns 4-port Network Embedding/De-embedding OFF  
Examples | CALC:FSIM:EMB:STAT 1  
calculate2:fsimulator:embed:state 0  
Query Syntax | CALCulate<cnum>:FSIMulator:EMBed:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

CALCulate<cnum>:FSIMulator:EMBed:TOPology:A:PORTs <p1>,<p2> Superseded

Applicable Models: All The command set of [CALCulate:FSIMulator:EMBed:XXXX](FSimulatorEmbed.md) is changed to [CALCulate:FSIMulator:DRAFt:CIRCuit:YYYY](FSimulatorDraft.md) and [CALCulate<cnum>:FSIMulator::CIRCuit:YYYY?](FSimulatorActive.md) Learn about [Using Fixture Simulator](../../Using_Fixture_Simulator.md). (Read-Write) Specifies the VNA port connections when topology A is selected. Specify topology using [CALC:FSIM:EMBed:TYPE](FSimulatorEmbed.md#TopType). | ![](../../../assets/images/FSim4PortEmbTopA.gif)  
---  
Topology A  
  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<p1> | VNA Port number assigned to a in above graphic.  
<p2> | VNA Port number assigned to b in above graphic.  
Examples | CALC:FSIM:EMB:TOP:A:PORT 2,1  
calculate2:fsimulator:embed:topology:a:ports 1,2  
Query Syntax | CALCulate<cnum>:FSIMulator:EMBed:TOPology:A:PORTs?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1,2  
  
* * *

CALCulate<cnum>:FSIMulator:EMBed:TOPology:B:PORTs <p1>,<p2>,<p3> Superseded

Applicable Models: All  The command set of [CALCulate:FSIMulator:EMBed:XXXX](FSimulatorEmbed.md) is changed to [CALCulate:FSIMulator:DRAFt:CIRCuit:YYYY](FSimulatorDraft.md) and [CALCulate<cnum>:FSIMulator::CIRCuit:YYYY?](FSimulatorActive.md) Learn about [Using Fixture Simulator](../../Using_Fixture_Simulator.md). (Read-Write) Specifies the VNA port connections when topology B is selected. Specify topology using [CALC:FSIM:EMBed:TYPE](FSimulatorEmbed.md#TopType). | ![](../../../assets/images/FSim4PortEmbTopB.gif)  
---  
Topology B  
  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<p1> | VNA Port number assigned to a in above graphic.  
<p2> | VNA Port number assigned to b in above graphic.  
<p3> | VNA Port number assigned to c in above graphic.  
Examples | CALC:FSIM:EMB:TOP:B:PORT 2,1,4  
calculate2:fsimulator:embed:topology:b:ports 1,2,3  
Query Syntax | CALCulate<cnum>:FSIMulator:EMBed:TOPology:B:PORTs?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1,2,3  
  
* * *

CALCulate<cnum>:FSIMulator:EMBed:TOPology:C:PORTs <p1>,<p2>,<p3>,<p4>
Superseded

Applicable Models: All The command set of [CALCulate:FSIMulator:EMBed:XXXX](FSimulatorEmbed.md) is changed to [CALCulate:FSIMulator:DRAFt:CIRCuit:YYYY](FSimulatorDraft.md) and [CALCulate<cnum>:FSIMulator::CIRCuit:YYYY?](FSimulatorActive.md) Learn about [Using Fixture Simulator](../../Using_Fixture_Simulator.md). (Read-Write) Specifies the VNA port connections when topology C is selected. Specify topology using [CALC:FSIM:EMBed:TYPE](FSimulatorEmbed.md#TopType). | ![](../../../assets/images/FSim4PortEmbTopC.gif)  
---  
Topology C  
  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<p1> | VNA Port number assigned to a in above graphic.  
<p2> | VNA Port number assigned to b in above graphic.  
<p3> | VNA Port number assigned to c in above graphic.  
<p4> | VNA Port number assigned to d in above graphic.  
Examples | CALC:FSIM:EMB:TOP:C:PORT 2,1,4,3  
calculate2:fsimulator:embed:topology:c:ports 1,2,3,4  
Query Syntax | CALCulate<cnum>:FSIMulator:EMBed:TOPology:C:PORTs?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1,2,3,4  
  
* * *

CALCulate<cnum>:FSIMulator:EMBed:TOPology:D:PORTs <p1>,<p2>,<p3>,<p4>...<pN>
Superseded

Applicable Models: All The command set of
[CALCulate:FSIMulator:EMBed:XXXX](FSimulatorEmbed.md) is changed to
[CALCulate:FSIMulator:DRAFt:CIRCuit:YYYY](FSimulatorDraft.md) and
[CALCulate<cnum>:FSIMulator::CIRCuit:YYYY?](FSimulatorActive.md) Learn about
[Using Fixture Simulator](../../Using_Fixture_Simulator.md). (Read-Write)
Specifies the VNA port connections for VNAs having greater than 4 ports.
Specify topology using [CALC:FSIM:EMBed:TYPE](FSimulatorEmbed.md#TopType).
Learn more.  
---  
Parameters |   
<cnum> | Channel number of the measurement.  
<p1>,<p2>,<p3>,<p4>...<pN> | VNA port number assignment.  
Examples | CALC:FSIM:EMB:TOP:D:PORT 2,1,4,3,6,5,8,7  
calculate2:fsimulator:embed:topology:d:ports 1,2,3,4,5,6,7,8  
Query Syntax | CALCulate<cnum>:FSIMulator:EMBed:TOPology:D:PORTs?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

CALCulate<cnum>:FSIMulator:EMBed:TYPE <char> Superseded

Applicable Models: All The command set of
[CALCulate:FSIMulator:EMBed:XXXX](FSimulatorEmbed.md) is changed to
[CALCulate:FSIMulator:DRAFt:CIRCuit:YYYY](FSimulatorDraft.md) and
[CALCulate<cnum>:FSIMulator::CIRCuit:YYYY?](FSimulatorActive.md) Learn about
[Using Fixture Simulator](../../Using_Fixture_Simulator.md). (Read-Write)
Specifies the VNA / DUT topology. Learn more about these and other VNA/DUT
configurations.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<char> | VNA / DUT topology. Choose from:

  * [A](FSimulatorEmbed.md#topA) \- 2 PNA/DUT Ports
  * [B](FSimulatorEmbed.md#topB) \- 3 PNA/DUT Ports
  * [C](FSimulatorEmbed.md#topC) \- 4 PNA/DUT Ports
  * D \- >4 VNA/DUT Ports

Click links to see topologies and port assignment commands.  
Examples | CALC:FSIM:EMB:TYPE A  
calculate2:fsimulator:embed:type c  
Query Syntax | CALCulate<cnum>:FSIMulator:EMBed:TYPE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | A  
  
* * *

