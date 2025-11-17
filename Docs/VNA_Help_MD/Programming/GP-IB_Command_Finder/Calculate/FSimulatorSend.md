# Calculate:FSimulator:Sended Commands

* * *

Specifies settings for embedding and de-embedding Single-Ended (2-port)
fixturing circuits.

CALCulate:FSIMulator:SENDed: DEEMbed PORT
[SNP:REVerse](FSimulatorSend.md#ReversePorts)
[[TYPE]](FSimulatorSend.md#deembedType)
[USER:FILename](FSimulatorSend.md#deembedFileName)
[STATe](FSimulatorSend.md#DeemState) [OORDer](FSimulatorSend.md#oorder)
PMCircuit PORT PARameters [C](FSimulatorSend.md#pmcC)
[G](FSimulatorSend.md#pmcG) [L](FSimulatorSend.md#pmcL)
[R](FSimulatorSend.md#pmcR) [[TYPE]](FSimulatorSend.md#pmcType)
[USER:FILename](FSimulatorSend.md#pmcFileName)
[STATe](FSimulatorSend.md#PMCState)
[POWer:PORT:COMPensation](FSimulatorSend.md#PowerPortComp) ZCONversion PORT
[IMAG](FSimulatorSend.md#ZImag) [REAL](FSimulatorSend.md#ZReal)
[Z0[:R]](FSimulatorSend.md#ZReal) [STATe](FSimulatorSend.md#ZState)  
---  
  
Click on a keyword to view the command details.

See Also

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * Learn about Fixturing

  * [Set Port Extensions with SCPI](../Sense/Sense_Correction.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

Note: CALC:FSIM commands affect ALL measurements on the specified channel.

* * *

CALCulate<cnum>:FSIMulator:SENDed:DEEMbed:PORT<n>:SNP:REVerse <bool>
Superseded

Applicable Models: All The command set of
[CALCulate:FSIMulator:SENDed:DEEMbed:PORT:XXXX](FSimulatorSend.md) is changed
to [CALCulate:FSIMulator:DRAFt:CIRCuit:YYYY](FSimulatorDraft.md) and
[CALCulate<cnum>:FSIMulator::CIRCuit:YYYY?](FSimulatorActive.md) Learn about
[Using Fixture Simulator](../../Using_Fixture_Simulator.md). (Read-Write) Set
and read whether or not to reverse ports on a 2-port fixture or adapter to be
de-embedded. Learn more.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<port> | VNA port number to which SNP file is to be de-embedded.  
<bool> | Choose from: ON or 1 - Reverse ports OFF or 0 - Do NOT Reverse ports  
Examples | CALC:FSIM:SEND:DEEM:PORT1:SNP:REV 1  
calculate2:fsimulator:sended:deembed:port2:snp:reverse 0  
Query Syntax | CALCulate<cnum>:FSIMulator:SENDed:DEEMbed:PORT<n>:SNP:REVerse?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

CALCulate<cnum>:FSIMulator:SENDed:DEEMbed:PORT<n>[:TYPE] <char> Superseded

Applicable Models: All The command set of
[CALCulate:FSIMulator:SENDed:DEEMbed:PORT:XXXX](FSimulatorSend.md) is changed
to [CALCulate:FSIMulator:DRAFt:CIRCuit:YYYY](FSimulatorDraft.md) and
[CALCulate<cnum>:FSIMulator::CIRCuit:YYYY?](FSimulatorActive.md) Learn about
[Using Fixture Simulator](../../Using_Fixture_Simulator.md). (Read-Write)
Select whether or not to load a 2-port De-embedding circuit model for the
specified port number. Circuit model USER is valid when an associated .s2p
file is specified with
[CALC:FSIM:SEND:DEEM:PORT1:USER:FILename.](FSimulatorSend.md#deembedFileName)
Note: This command affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<port> | Port number to receive circuit model.  
<char> | Choose from: NONE - Port does not have a circuit model. USER - Circuit model for the port will be loaded from VNA drive.  
Examples | CALC:FSIM:SEND:DEEM:PORT1 USER  
calculate2:fsimulator:sended:deembed:port2:type none  
Query Syntax | CALCulate<cnum>:FSIMulator:SENDed:DEEMbed:PORT<n>[:TYPE]?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | None  
  
* * *

CALCulate<cnum>:FSIMulator:SENDed:DEEMbed:PORT<n>:USER:FILename <string>
Superseded

Applicable Models: All The command set of
[CALCulate:FSIMulator:SENDed:DEEMbed:PORT:XXXX](FSimulatorSend.md) is changed
to [CALCulate:FSIMulator:DRAFt:CIRCuit:YYYY](FSimulatorDraft.md) and
[CALCulate<cnum>:FSIMulator::CIRCuit:YYYY?](FSimulatorActive.md) Learn about
[Using Fixture Simulator](../../Using_Fixture_Simulator.md). (Read-Write)
Specifies the filename of the circuit model to be used for de-embedding.
Circuit model is applied when both [CALC:FSIM:SEND:DEEM:PORT1
USER](FSimulatorSend.htm#deembedType) is selected and the filename is
specified with this command. Note: This command affects ALL measurements on
the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<port> | Port number to receive circuit model.  
<string> | File name and extension (.s2P) of the de-embedding circuit. Files are stored in the default folder "D:\". To recall from a different folder, specify the full path name.  
Examples | CALC:FSIM:SEND:DEEM:PORT1:USER:FIL 'myFile.s2P'  
calculate2:fsimulator:deembed:port2:user:file "D:\myFile.s2P"  
Query Syntax | CALCulate<cnum>:FSIMulator:SENDed:DEEMbed:PORT<n>:USER:FILename?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

CALCulate<cnum>:FSIMulator:SENDed:DEEMbed:STATe <bool> Superseded

Applicable Models: All This command is changed to [CALCulate:FSIMulator:DRAFt:SECTion:CIRCuit:ENABle <ON | OFF>](FSimulatorDraft.md#SectCircEnab) , [CALCulate:FSIMulator:SECTion:CIRCuit:ENABle?](FSimulatorActive.md#SectCircEnab) Learn about [Using Fixture Simulator](../../Using_Fixture_Simulator.md). (Read-Write) Turns de-embedding ON or OFF for all ports on the specified channel. Note: This command affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<bool> | Choose from: ON or 1 - Turns de-embedding ON OFF or 0 - Turns de-embedding OFF  
Examples | CALC:FSIM:SEND:DEEM:STAT 1  
calculate2:fsimulator:sended:deembed:state 0  
Query Syntax | CALCulate<cnum>:FSIMulator:SENDed:DEEMbed:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

CALCulate<cnum>:FSIMulator:SENDed:OORDer <a,b,c,d>

Applicable Models: All (Read-Write) Sets and returns the order in which
Single-ended Fixture Operations occur. Learn more about these operations.
Note: The operation for ground loop embedding and ground loop de-embedding
will always occur as the 3rd step. It cannot be moved. By default, this is
after the 2-Port DeEmbedding operation. Note: This command affects ALL
measurements on the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<a,b,c,d> | Order of operations, where: 0 \- Port Extension operation 1 \- 2-Port DeEmbedding operation 2 \- Port Matching operation 3 \- Arbitrary Impedance operation  
Examples | CALC:FSIM:SEND:OORD 1,2,3,0  
calculate2:fsimulator:sended:oorder 1,2,3,0  
Query Syntax | CALCulate<cnum>:FSIMulator:SENDed:OORDer?  
Return Type | Comma-separated values  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0,1,2,3  
  
* * *

CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:PORT<n>:PARameters:C <value>
Superseded

Applicable Models: All The command set of
CALCulate:FSIMulator:SENDed:PMCircuit:PORT:XXXX is changed to
[CALCulate:FSIMulator:DRAFt:CIRCuit:YYYY](FSimulatorDraft.md) and
[CALCulate<cnum>:FSIMulator::CIRCuit:YYYY?](FSimulatorActive.md) Learn about
[Using Fixture Simulator](../../Using_Fixture_Simulator.md). (Read-Write)
Sets and returns the value for the 'C' (Capacitance) circuit element for a
port matching circuit model to simulate on port 'n'. The port matching circuit
model is selected using
CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:PORT<n>[:TYPE]<char>. You can
specify C, C1, or C2 based on the selected port matching circuit model.
Setting a value not used by the selected circuit will have no affect. Learn
more. There are three steps to set up a port matching circuit model simulation
on a specified port:

  1. Select the port matching circuit model to simulate using CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:PORT<n>[:TYPE]<char>.
  2. Set the values for R (Resistance), G (Conductance), C (Capacitance), and L (Inductance) corresponding to the selected port matching circuit model.
  3. Turn the feature on using CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:STATe to simulate the circuit and compute the measurement as if the circuit were attached to the port.

Note: This command affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<n> | Port number to receive value.  
<value> | Capacitance value in farads. Choose a value between -1E18 to 1E18  
Examples | CALC:FSIM:SEND:PMC:PORT1:PAR:C 0.00002  
calculate2:fsimulator:sended:pmcircuit:port2:parameters:c 0.00003  
Query Syntax | CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:PORT<n>:PARameters:C?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:PORT<n>:PARameters:G <value>
Superseded

Applicable Models: All The command set of
CALCulate:FSIMulator:SENDed:PMCircuit:PORT:XXXX is changed to
[CALCulate:FSIMulator:DRAFt:CIRCuit:YYYY](FSimulatorDraft.md) and
[CALCulate<cnum>:FSIMulator::CIRCuit:YYYY?](FSimulatorActive.md) Learn about
[Using Fixture Simulator](../../Using_Fixture_Simulator.md). (Read-Write)
Sets and returns the value for the 'G' (Conductance) circuit element for a
port matching circuit model to simulate on port 'n'. The port matching circuit
model is selected using
CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:PORT<n>[:TYPE]<char>. You can
specify G, G1, or G2 based on the selected port matching circuit model.
Setting a value not used by the selected circuit will have no affect. Learn
more. There are three steps to set up a port matching circuit model simulation
on a specified port:

  1. Select the port matching circuit model to simulate using CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:PORT<n>[:TYPE]<char>.
  2. Set the values for R (Resistance), G (Conductance), C (Capacitance), and L (Inductance) corresponding to the selected port matching circuit model.
  3. Turn the feature on using CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:STATe to simulate the circuit and compute the measurement as if the circuit were attached to the port.

Note: This command affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<n> | Port number to receive value.  
<value> | Conductance value in siemens. Choose a value between -1E18 to 1E18  
Examples | CALC:FSIM:SEND:PMC:PORT1:PAR:G 0.00002  
calculate2:fsimulator:sended:pmcircuit:port2:parameters:g 0.00003  
Query Syntax | CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:PORT<n>:PARameters:G?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:PORT<n>:PARameters:L <value>
Superseded

Applicable Models: All The command set of
CALCulate:FSIMulator:SENDed:PMCircuit:PORT:XXXX is changed to
[CALCulate:FSIMulator:DRAFt:CIRCuit:YYYY](FSimulatorDraft.md) and
[CALCulate<cnum>:FSIMulator::CIRCuit:YYYY?](FSimulatorActive.md) Learn about
[Using Fixture Simulator](../../Using_Fixture_Simulator.md). (Read-Write)
Sets and returns the value for the 'L' (Inductance) circuit element for a port
matching circuit model to simulate on port 'n'. The port matching circuit
model is selected using
CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:PORT<n>[:TYPE]<char>. You can
specify L, L1, or L2 based on the selected port matching circuit model.
Setting a value not used by the selected circuit will have no affect. Learn
more. There are three steps to set up a port matching circuit model simulation
on a specified port:

  1. Select the port matching circuit model to simulate using CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:PORT<n>[:TYPE]<char>.
  2. Set the values for R (Resistance), G (Conductance), C (Capacitance), and L (Inductance) corresponding to the selected port matching circuit model.
  3. Turn the feature on using CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:STATe to simulate the circuit and compute the measurement as if the circuit were attached to the port.

Note: This command affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<n> | Port number to receive value.  
<value> | Inductance value in henries. Choose a value between -1E18 to 1E18  
Examples | CALC:FSIM:SEND:PMC:PORT1:PAR:L 0.00002  
calculate2:fsimulator:sended:pmcircuit:port2:parameters:l 0.00003  
Query Syntax | CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:PORT<n>:PARameters:L?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:PORT<n>:PARameters:R <value>
Superseded

Applicable Models: All The command set of
CALCulate:FSIMulator:SENDed:PMCircuit:PORT:XXXX is changed to
[CALCulate:FSIMulator:DRAFt:CIRCuit:YYYY](FSimulatorDraft.md) and
[CALCulate<cnum>:FSIMulator::CIRCuit:YYYY?](FSimulatorActive.md) Learn about
[Using Fixture Simulator](../../Using_Fixture_Simulator.md). (Read-Write)
Sets and returns the value for the 'R' (Resistance) circuit element for a port
matching circuit model to simulate on port 'n'. The port matching circuit
model is selected using
CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:PORT<n>[:TYPE]<char>. You can
specify R, R1, or R2 based on the selected port matching circuit model.
Setting a value not used by the selected circuit will have no affect. Learn
more. There are three steps to set up a port matching circuit model simulation
on a specified port:

  1. Select the port matching circuit model to simulate using CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:PORT<n>[:TYPE]<char>.
  2. Set the values for R (Resistance), G (Conductance), C (Capacitance), and L (Inductance) corresponding to the selected port matching circuit model.
  3. Turn the feature on using CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:STATe to simulate the circuit and compute the measurement as if the circuit were attached to the port.

Note: This command affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<n> | Port number to receive value.  
<value> | Resistance value in ohms. Choose a value between -1E18 to 1E18  
Examples | CALC:FSIM:SEND:PMC:PORT1:PAR:R 0.00002  
calculate2:fsimulator:sended:pmcircuit:port2:parameters:r 0.00003  
Query Syntax | CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:PORT<n>:PARameters:R?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:PORT<n>[:TYPE] <char> Superseded

Applicable Models: All The command set of
CALCulate:FSIMulator:SENDed:PMCircuit:PORT:XXXX is changed to
[CALCulate:FSIMulator:DRAFt:CIRCuit:YYYY](FSimulatorDraft.md) and
[CALCulate<cnum>:FSIMulator::CIRCuit:YYYY?](FSimulatorActive.md) Learn about
[Using Fixture Simulator](../../Using_Fixture_Simulator.md). (Read-Write)
Select whether or not to load a 2 port matching circuit model for the
specified port number. Circuit model USER is valid when an associated .s2p
file is specified with
[CALC:FSIM:SEND:PMC:PORT1:USER:FIL](FSimulatorSend.md#pmcFileName). Note:
This command affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<n> | Port number to receive circuit model.  
<char> | Circuit model. Choose from NONE No circuit model SLPC Series L - Parallel C PCSL Parallel C - Series L PLSC Parallel L - Series C SCPL Series C - Parallel L PLPC Parallel L - Parallel C SCPC Series C - Parallel C PCSC Parallel C - Series C SLPL Series L - Parallel L PLSL Parallel L - Series L USER Load S2P file  
Examples | CALC:FSIM:SEND:PMC:PORT1:USER  
calculate2:fsimulator:sended:pmcircuit:port2:type slpc  
Query Syntax | CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:PORT<n>[:TYPE]?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | None \- No circuit model  
  
* * *

CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:PORT<n>:USER:FILename <string>
Superseded

Applicable Models: All The command set of
CALCulate:FSIMulator:SENDed:PMCircuit:PORT:XXXX is changed to
[CALCulate:FSIMulator:DRAFt:CIRCuit:YYYY](FSimulatorDraft.md) and
[CALCulate<cnum>:FSIMulator::CIRCuit:YYYY?](FSimulatorActive.md) Learn about
[Using Fixture Simulator](../../Using_Fixture_Simulator.md). (Read-Write)
Specifies the filename of the circuit model to be used for port matching.
Circuit model is applied when both CALC:FSIM:SEND:PMC:PORT1 USER is selected
and the filename is specified with this command. Note: This command affects
ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<port> | Port number to receive circuit model.  
<string> | File name and extension (.s2P) of the de-embedding circuit. Files are stored in the default folder "D:\". To recall from a different folder, specify the full path name.  
Examples | CALC:FSIM:SEND:PMC:PORT1:USER:FIL 'myFile.s2P'  
calculate2:fsimulator:pmcircuit:port2:user:file "D:\myFile.s2P"  
Query Syntax | CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:PORT<n>:USER:FILename?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:STATe <bool> Superseded

Applicable Models: All Note: This command is changed to [CALCulate:FSIMulator:DRAFt:SECTion:CIRCuit:ENABle <ON | OFF>](FSimulatorDraft.md#SectCircEnab) and [CALCulate:FSIMulator:SECTion:CIRCuit:ENABle?](FSimulatorActive.md#SectCircEnab) Learn about [Using Fixture Simulator](../../Using_Fixture_Simulator.md). (Read-Write) Turns Port Matching ON or OFF for all ports on the specified channel. Note: This command affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<bool> | Choose from: ON or 1 - Turns Port Matching ON OFF or 0 - Turns Port Matching OFF  
Examples | CALC:FSIM:SEND:PMC:STAT 1  
calculate2:fsimulator:sended:pmcircuit:state 0  
Query Syntax | CALCulate<cnum>:FSIMulator:SENDed:PMCircuit:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

CALCulate<cnum>:FSIMulator:SENDed:POWer:PORT<n>:COMPensation <bool> Superseded

Applicable Models: All Note: This command is changed to
[CALCulate:FSIMulator:POWer:PORT[p]:COMPensate[:STATe]](FSimulatorActive.md#PowPortComp)[
](FSimulatorDraft.htm#SectCircEnab)Learn about [Using Fixture
Simulator](../../Using_Fixture_Simulator.htm). (Read-Write) Adjusts the source
power at the specified port by the combined amount of loss through ALL enabled
fixturing operations. Use this function to set the power level at the DUT
input. Learn more. Note: This command affects ALL measurements on the
specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<port> | Port number to receive power compensation.  
<bool> | Choose from: ON or 1 - Compensate source power OFF or 0 - Do NOT compensate source power  
Examples | CALC:FSIM:SEND:POW:PORT1:COMP 1  
calculate2:fsimulator:power:port2:compensation off  
Query Syntax | CALCulate<cnum>:FSIMulator:SENDed:POWer:PORT<n>:COMPensation?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

CALCulate<cnum>:FSIMulator:SENDed:ZCONversion:PORT<n>:IMAG <value> Superseded

Applicable Models: All The command set of
[CALCulate:FSIMulator:SENDed:ZCONversion:PORT:XXXX](FSimulatorSend.md) is
changed to
[CALCulate:FSIMulator:DRAFt:ZCONversion:SENDed:PORT:YYYY](FSimulatorDraft.md)
and [CALCulate:FSIMulator:ZCONversion:SENDed:PORT:YYYY?](FSimulatorActive.md)
Learn about [Using Fixture Simulator](../../Using_Fixture_Simulator.md).
(Read-Write) Sets and returns the Imaginary portion of the impedance value for
the specified single-ended port. Use
[CALC:FSIM:SEND:ZCON:PORT:REAL](FSimulatorSend.md#ZReal) to set the real
value. Or use [CALC:FSIM:SEND:ZCON:PORT:Z0](FSimulatorSend.md#ZValue) to set
both values together. Note: This command affects ALL measurements on the
specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<n> | Port number to receive value.  
<value> | Imaginary impedance value. Choose a value between -1E18 and 1E18  
Examples | CALC:FSIM:SEND:ZCON:PORT1:IMAG 75  
calculate2:fsimulator:sended:zconversion:port2:imag 150  
Query Syntax | CALCulate<cnum>:FSIMulator:SENDed:ZCONversion:PORT<n>:IMAG?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:SENDed:ZCONversion:PORT<n>:REAL <value> Superseded

Applicable Models: All The command set of
[CALCulate:FSIMulator:SENDed:ZCONversion:PORT:XXXX](FSimulatorSend.md) is
changed to
[CALCulate:FSIMulator:DRAFt:ZCONversion:SENDed:PORT:YYYY](FSimulatorDraft.md)
and [CALCulate:FSIMulator:ZCONversion:SENDed:PORT:YYYY?](FSimulatorActive.md)
Learn about [Using Fixture Simulator](../../Using_Fixture_Simulator.md).
(Read-Write) Sets and returns the Real portion of the impedance value for the
specified single-ended port. Use
[CALC:FSIM:SEND:ZCON:PORT:IMAG](FSimulatorSend.md#ZImag) to set the imaginary
value. Or use [CALC:FSIM:SEND:ZCON:PORT:Z0](FSimulatorSend.md#ZValue) to set
both values together. Note: This command affects ALL measurements on the
specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<n> | Port number to receive value.  
<value> | Real Impedance value in ohms. Choose a value between 0 to 1E7  
Examples | CALC:FSIM:SEND:ZCON:PORT1:REAL 51  
calculate2:fsimulator:sended:zconversion:port2:real 75  
Query Syntax | CALCulate<cnum>:FSIMulator:SENDed:ZCONversion:PORT<n>:REAL?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 50  
  
* * *

CALCulate<cnum>:FSIMulator:SENDed:ZCONversion:PORT<n>:Z0[:R] <value>
Superseded

Applicable Models: All The command set of
[CALCulate:FSIMulator:SENDed:ZCONversion:PORT:XXXX](FSimulatorSend.md) is
changed to
[CALCulate:FSIMulator:DRAFt:ZCONversion:SENDed:PORT:YYYY](FSimulatorDraft.md)
and [CALCulate:FSIMulator:ZCONversion:SENDed:PORT:YYYY?](FSimulatorActive.md)
Learn about [Using Fixture Simulator](../../Using_Fixture_Simulator.md).
(Read-Write) Sets and returns the Real portion of the impedance value for the
specified single-ended port. The imaginary portion is automatically set to
0.0. To set both values separately, use
[CALC:FSIM:SEND:ZCON:PORT:REAL](FSimulatorSend.md#ZReal) and
[CALC:FSIM:SEND:ZCON:PORT:IMAG](FSimulatorSend.md#ZImag). Note: This command
affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<n> | Port number to receive value.  
<value> | Port Impedance value in ohms. Choose a value between 0 to 1E7  
Examples | CALC:FSIM:SEND:ZCON:PORT1:Z0 51  
calculate2:fsimulator:sended:zconversion:port2:z0:r 75  
Query Syntax | CALCulate<cnum>:FSIMulator:SENDed:ZCONversion:PORT<n>:Z0[:R]?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 50  
  
* * *

CALCulate<cnum>:FSIMulator:SENDed:ZCONversion:STATe <bool> Superseded

Applicable Models: All This command is changed to [CALCulate:FSIMulator:DRAFt:SECTion:ZCONversion:ENABle <ON | OFF>](FSimulatorDraft.md#SecZconEnab) and [CALCulate:FSIMulator:SECTion:ZCONversion:ENABle?](FSimulatorActive.md#SectZconEnab) Learn about [Using Fixture Simulator](../../Using_Fixture_Simulator.md). (Read-Write) Turns Port Impedance ON or OFF for all ports on the specified channel. Note: This command affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<bool> | Choose from: ON or 1 - Turns Port Impedance ON OFF or 0 - Turns Port Impedance OFF  
Examples | CALC:FSIM:SEND:ZCON:STAT 1  
calculate2:fsimulator:sended:zconversion:state 0  
Query Syntax | CALCulate<cnum>:FSIMulator:SENDed:ZCONversion:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

