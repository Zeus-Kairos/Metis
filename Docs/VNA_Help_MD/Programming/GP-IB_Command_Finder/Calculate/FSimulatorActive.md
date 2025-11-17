# Calculate:FSimulator Active Commands

CALCulate:FSIMulator: [APPLy](FSimulatorActive.md#APPLy) CIRCuit: | CATalog | DEVice | PORTs | [:ARRay] | REVerse | EMBED | TYPE | FILE | EXTRapolate | MODify? | PARameter | C | C2 | DELay | G | G2 | L | L2 | LOSS | VALue | R | R2 | RIN | ROUT | Z0 | STATe | VNA | PORTs | EXTension:PORT: | [DELay](FSimulatorActive.md#ExtPortDel) | DISTance | [VALue](FSimulatorActive.md#ExtPortDistVal) | [UNIT](FSimulatorActive.md#ExtPortDistUnit) | LOSS | [FREQuency](FSimulatorActive.md#ExtPortLossFreq) | [VALue](FSimulatorActive.md#ExtPortLossVal) | [STATe](FSimulatorActive.md#ExtPortLoss) | [MEDium](FSimulatorActive.md#ExtPortMed) | WAVEguide | [FCUToff](FSimulatorActive.md#ExtPortWaveFcut) | [COUPle](FSimulatorActive.md#ExtPortWaveCoup) | VELocity | [FACTor](FSimulatorActive.md#ExtPortVelFac) | [COUPle](FSimulatorActive.md#ExtPortVelCoup) | [DCLoss:VALue](FSimulatorActive.md#ExtPortDclVAL) | [STATe](FSimulatorActive.md#ExtPortStat) | POWER | COMPensate | MODE | PORT | COMPensate | STATe | [SAVE](FSimulatorActive.md#SAVE) | SECTion |CIRCuit | ENABle | EXTension | ENABle | ZCONversion | ENABle | TOPology | LOAD | SAVE | ZCONversion | DIFFerential | [:STATe](FSimulatorActive.md#ZconDiffStat) | :BPORt  
|[:COMPLex](FSimulatorActive.md#ZconDiffBportComp) |[:SCALar](FSimulatorActive.md#ZconDiffBportScal) | :LPORt  
|:COMPLex |:SCALar | COMMonmode | :[STATe](FSimulatorActive.md#ZconCommStat) | :BPORt  
|:COMPLex |:SCALar | :LPORt<pnum>  
|:COMPLex |:SCALar | SENDed:PORT | [:STATe](FSimulatorActive.md#ZconSendPortStat) | :COMPLex | [:SCALar](FSimulatorActive.md#ZconSendPortScal)  
---  
  
See Also

  * [Learn about Using Fixture Simulator](../../Using_Fixture_Simulator.md)

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

## CALCulate<cnum>:FSIMulator:APPLy

Applicable Models: All (Write only) Copies the draft fixture to active
fixture. Exact same functionality as
[CALC:FSIM:DRAFT:APPL](FSimulatorDraft.md#Apply)  
---  
Parameters | Not applicable  
Example | CALC:FSIM:APPL calculate:fsimulatorapply  
Return Type | Not applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

CALCulate<cnum>:FSIMulator:CIRCuit:CATalog?

Applicable Models: All (Read only) Returns a comma-separated list of circuit
numbers created in the draft circuit.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
Examples | CALC:FSIM:CIRC:CAT? calculate2:fsimulator:circuit:catalog?  
Query Syntax | CALCulate<cnum>:FSIMulator:CIRCuit:CATalog?  
Return Type | comma-separated string  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

CALCulate<cnum>:FSIMulator:CIRCuit<circN>:DEVice:PORTs[:ARRay]? <port list -
in, out>

Applicable Models: All (Read only) Returns the Device ports for the specified
circuit.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
Examples | CALC:FSIM:CIRC:DEV:PORT? calculate2:fsimulator:circuit:device:ports?  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:DEVice:PORTs[:ARRay]?   
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

CALCulate<cnum>:FSIMulator:CIRCuit<circN>:DEVice:PORTs:REVerse?

Applicable Models: All (Read only) Returns whether or not the ports on an
existing S2P file are reversed.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
Examples | CALC:FSIM:CIRC:DEV:PORT:REV? calculate2:fsimulator:circuit:device:ports:reverse?  
Query Syntax | CALCulate<cnum>:FSIMulator:CIRCuit<circN>:DEVice:PORTs:REVerse?  
Return Type | Boolean   
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

CALCulate<cnum>:FSIMulator:CIRCuit<circN>:EMBED:TYPE?

Applicable Models: All (Read only) Returns whether the circuit is embedded or
de-embedded. Valid for all block Types The block is create using
[CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>](FSimulatorDraft.htm#CircAdd). Setting a value not used by the selected
circuit will have no affect. Learn more.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
Examples | CALC:FSIM:CIRC:EMBED:TYPE? calculate2:fsimulator:circuit:embed:type?  
Query Syntax | CALCulate<cnum>:FSIMulator:CIRCuit<circN>:EMBED:TYPE?  
Return Type | character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | EMBed  
  
* * *

CALCulate<cnum>:FSIMulator:CIRCuit<circN>:FILE?

Applicable Models: All (Read only) Returns the filename. Valid blocks: FILe,
D4PFile, FGLoop The block is create using
[CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>](FSimulatorDraft.htm#CircAdd). Setting a value not used by the selected
circuit will have no affect. Learn more.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
Examples | CALC:FSIM:CIRC:FILE? calculate2:fsimulator:circuit:file?  
Query Syntax | CALCulate<cnum>:FSIMulator:CIRCuit<circN>:FILE?  
Return Type | string  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

CALCulate<cnum>:FSIMulator:CIRCuit<circN>:FILE:EXTRapolate?

Applicable Models: All (Read only) Returns whether or not extrapolation is
allowed (TRUE/FALSE). Valid blocks: FILe, D4PFile, FGLoop.  The block is
create using [CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>,
<fixt port count>](FSimulatorDraft.htm#CircAdd). Setting a value not used by
the selected circuit will have no affect. Learn more.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
Examples | CALC:FSIM:CIRC:FILE:EXTR? calculate2:fsimulator:circuit:file:extrapolate?  
Query Syntax | CALCulate<cnum>:FSIMulator:CIRCuit<circN>:FILE:EXTRapolate?  
Return Type | Boolean   
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

CALCulate<cnum>:FSIMulator:CIRCuit<circN>:FILE:MODify?

Applicable Models: All (Read-only) Returns the current state of the Modify
setting (NONE, NREFlect, or NXTalk). Set the Modify state using the
[CALCulate:FSIMulator:DRAFt:CIRCuit:FILE:MODify](FSimulatorDraft.md#CALCulate:FSIMulator:DRAFt:CIRCuit:FILE:MODify)
command. [Learn more](../../../S3_Cals/Fixture_Simulator.md#Modify). The
block is create using [CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block
type>, <fixt port count>](FSimulatorDraft.htm#CircAdd). Setting a value not
used by the selected circuit will have no affect. Learn more.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
Examples | CALC:FSIM:CIRC:FILE:MOD? calculate2:fsimulator:circuit:file:modify?  
Query Syntax | CALCulate<cnum>:FSIMulator:CIRCuit<circN>:FILE:MODify?  
Return Type | Enumeration  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | NONE  
  
* * *

CALCulate<cnum>:FSIMulator:CIRCuit<circN>:PARameter:C?

Applicable Models: All (Read only) Returns the capacitance (C) circuit element
for the specified circuit. Valid blocks: RLGLoop, RCGLoop, CGGLoop, SLPC,
PCSL, PLSC, SCPL, PLPC, SCPC, PCSC, SLPL, PLSL. The block is create using
[CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>](FSimulatorDraft.htm#CircAdd). Setting a value not used by the selected
circuit will have no affect. Learn more.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
Examples | CALC:FSIM:CIRC:PAR:C? calculate2:fsimulator:circuit:parameter:C?  
Query Syntax | CALCulate<cnum>:FSIMulato:CIRCuit<circN>:PARameter:C?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:CIRCuit<circN>:PARameter:C2?

Applicable Models: All (Read only) Returns the capacitance (C2) circuit
element for the specified circuit. Valid blocks: SLPC, PCSL, PLSC, SCPL, PLPC,
SCPC, PCSC, SLPL, PLSL The block is create using
[CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>](FSimulatorDraft.htm#CircAdd). Setting a value not used by the selected
circuit will have no affect. Learn more.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
Examples | CALC:FSIM:CIRC:PAR:C2? calculate2:fsimulator:circuit:parameter:C2?  
Query Syntax | CALCulate<cnum>:FSIMulator:CIRCuit<circN>:PARameter:C2?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:CIRCuit<circN>:PARameter:DELay ?

Applicable Models: All (Read only) Returns port extension delay in time. Valid
blocks: ILIN. The block is create using
[CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>](FSimulatorDraft.htm#CircAdd). Setting a value not used by the selected
circuit will have no affect. Learn more.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
Examples | CALC:FSIM:CIRC:PAR:DEL? calculate2:fsimulator:circuit:parameter:delay?  
Query Syntax | CALCulate<cnum>:FSIMulator:CIRCuit<circN>:PARameter:DEL?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:CIRCuit<circN>:PARameter:G?

Applicable Models: All (Read only) Returns the conductance (G) circuit element
for the specified circuit. Valid blocks: RLGLoop, RCGLoop, CGGLoop, SLPC,
PCSL, PLSC, SCPL, PLPC, SCPC, PCSC, SLPL, PLSL. The block is create using
[CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>](FSimulatorDraft.htm#CircAdd). Setting a value not used by the selected
circuit will have no affect. Learn more.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
Examples | CALC:FSIM:CIRC:PAR:G? calculate2:fsimulator:circuit:parameter:g?  
Query Syntax | CALCulate<cnum>:FSIMulator:CIRCuit<circN>:PARameter:G?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:CIRCuit<circN>:PARameter:G2?

Applicable Models: All (Read only) Returns the conductance (G2) circuit
element for the specified circuit. Valid blocks: SLPC, PCSL, PLSC, SCPL, PLPC,
SCPC, PCSC, SLPL, PLSL The block is create using
[CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>](FSimulatorDraft.htm#CircAdd). Setting a value not used by the selected
circuit will have no affect. Learn more.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
Examples | CALC:FSIM:CIRC:PAR:G2? calculate2:fsimulator:circuit:parameter:g2?  
Query Syntax | CALCulate<cnum>:FSIMulator:CIRCuit<circN>:PARameter:G2?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:CIRCuit<circN>:PARameter:L?

Applicable Models: All (Read only) Returns the inductance (L) circuit element
for the specified circuit. Valid blocks: RLGLoop, RCGLoop, CGGLoop, SLPC,
PCSL, PLSC, SCPL, PLPC, SCPC, PCSC, SLPL, PLSL. The block is create using
[CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>](FSimulatorDraft.htm#CircAdd). Setting a value not used by the selected
circuit will have no affect. Learn more.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
Examples | CALC:FSIM:CIRC:PAR:L? calculate2:fsimulator:circuit:parameter:l?  
Query Syntax | CALCulate<cnum>:FSIMulator:CIRCuit<circN>:PARameter:L?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:CIRCuit<circN>:PARameter:L2?

Applicable Models: All (Read only) Returns the inductance (L2) circuit element
for thecspecified circuit. Valid blocks: SLPC, PCSL, PLSC, SCPL, PLPC, SCPC,
PCSC, SLPL, PLSL The block is create using
[CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>](FSimulatorDraft.htm#CircAdd). Setting a value not used by the selected
circuit will have no affect. Learn more.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
Examples | CALC:FSIM:CIRC:PAR:L2? calculate2:fsimulator:circuit:parameter:l2?  
Query Syntax | CALCulate<cnum>:FSIMulator:CIRCuit<circN>:PARameter:L2?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:CIRCuit<circN>:PARameter:LOSS:VALue?

Applicable Models: All (Read only) Returns the loss at DC. Valid blocks: ILIN.
The block is create using [CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD
<block type>, <fixt port count>](FSimulatorDraft.htm#CircAdd). Setting a value
not used by the selected circuit will have no affect. Learn more.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
Examples | CALC:FSIM:CIRC:PAR:LOSS:VAL? calculate2:fsimulator:circuit:parameter:loss:value?  
Query Syntax | CALCulate<cnum>:FSIMulator:CIRCuit<circN>:PARameter:LOSS:VALue?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:CIRCuit<circN>:PARameter:R?

Applicable Models: All (Read only) Returns the resistance (R) circuit element
for the specified circuit. Valid blocks: RLGLoop, RCGLoop, CGGLoop, SLPC,
PCSL, PLSC, SCPL, PLPC, SCPC, PCSC, SLPL, PLSL. The block is create using
[CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>](FSimulatorDraft.htm#CircAdd). Setting a value not used by the selected
circuit will have no affect. Learn more.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
Examples | CALC:FSIM:CIRC:PAR:R? calculate2:fsimulator:circuit:parameter:r?  
Query Syntax | CALCulate<cnum>:FSIMulator:CIRCuit<circN>:PARameter:R?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:CIRCuit<circN>:PARameter:R2?

Applicable Models: All (Read only) Returns the resistance (R2) circuit element
for the specified circuit. Valid blocks: SLPC, PCSL, PLSC, SCPL, PLPC, SCPC,
PCSC, SLPL, PLSL The block is create using
[CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>](FSimulatorDraft.htm#CircAdd). Setting a value not used by the selected
circuit will have no affect. Learn more.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
Examples | CALC:FSIM:CIRC:PAR:R2? calculate2:fsimulator:circuit:parameter:r2?  
Query Syntax | CALCulate<cnum>:FSIMulator:CIRCuit<circN>:PARameter:R2?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:CIRCuit<circN>:PARameter:RIN?

Applicable Models: All (Read only) Returns the resistance (R) value at input
of transformer (real only). Valid blocks: TRANs The block is create using
[CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>](FSimulatorDraft.htm#CircAdd). Setting a value not used by the selected
circuit will have no affect. Learn more.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
Examples | CALC:FSIM:DRAF:CIRC:PAR:RIN? calculate2:fsimulator:draft:circuit:parameter:rin?  
Query Syntax | CALCulate<cnum>:FSIMulator:CIRCuit<circN>:PARameter:RIN?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:CIRCuit<circN>:PARameter:ROUT?

Applicable Models: All (Read only) Returns the resistance (R) value at output
of transformer (real only). Valid blocks: TRANs The block is create using
[CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>](FSimulatorDraft.htm#CircAdd). Setting a value not used by the selected
circuit will have no affect. Learn more.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
Examples | CALC:FSIM:CIRC:PAR:ROUT? calculate2:fsimulator:circuit:parameter:rout?  
Query Syntax | CALCulate<cnum>:FSIMulator:CIRCuit<circN>:PARameter:ROUT?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:CIRCuit<circN>:PARameter:Z0?

Applicable Models: All (Read only) Returns the Impedance (Z0) for the ideal
block (scalar value). Valid blocks: ILIN. The block is create using
[CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>](FSimulatorDraft.htm#CircAdd). Setting a value not used by the selected
circuit will have no affect. Learn more.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
Examples | CALC:FSIM:CIRC:PAR:Z0? calculate2:fsimulator:circuit:parameter:z0?  
Query Syntax | CALCulate<cnum>:FSIMulator:CIRCuit<circN>:PARameter:Z0?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:CIRCuit<circN>:STATe?

Applicable Models: All (Read only) Returns the circuit ON/OFF. Valid for all
block types The block is create using
[CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>](FSimulatorDraft.htm#CircAdd). Setting a value not used by the selected
circuit will have no affect. Learn more.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
Examples | CALC:FSIM:CIRC:STAT? calculate2:fsimulator:circuit:state?  
Query Syntax | CALCulate<cnum>:FSIMulator:CIRCuit<circN>:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

CALCulate<cnum>:FSIMulator:CIRCuit<circN>:VNA:PORTs? <port list>

Applicable Models: All (Read only) Returns the VNA ports for the specified
circuit.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
Examples | CALC:FSIM:CIRC:VNA:PORT? calculate2:fsimulator:circuit:vna:ports?  
Query Syntax | CALCulate<cnum>:FSIMulator:CIRCuit<circN>:VNA:PORTs?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:FSIMulator:EXTension:PORT<pnum>:DELay

Applicable Models: All (Read-Write) Returns the delay value in time at the
specified port. Note: This command affects ALL measurements on the specified
channel.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1.  
<pnum> | Port Number that will receive the delay setting. If unspecified, value is set to 1.  
<value> | The port extension in seconds; may include suffix. Choose a number between: -1E18 and 1E18e.   
Examples | CALC:FSIM:EXT:PORT1:DEL?  
calculate:fsimulator:extension:port2:delay?  
Query Syntax | CALCulate<cnum>:FSIMulator:EXTension:PORT<pnum>:DELay?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:FSIMulator:EXTension:PORT<pnum>:DISTance:UNIT

Applicable Models: All (Read-only) Returns the units for specifying port
extension delay in physical length (distance).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1.  
<pnum> | Port Number. This number is ignored and all ports have the same setting.  
<char> | Units for delay in distance. Choose from:

  * METer
  * FEET
  * INCH

  
Examples | CALC:FSIM:EXT:PORT2:DIST:UNIT?  
calculate:fsimulator:extension:port3:distance:unit?  
Query Syntax | CALCulate<cnum>:FSIMulator:EXTension:PORT:DISTance:UNIT?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | METer  
  
* * *

## CALCulate<cnum>:FSIMulator:EXTension:PORT<pnum>:DISTance:VALue

Applicable Models: All (Read-only) Returns the port extension delay in
physical length (distance).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1.  
<pnum> | Port Number that will receive the delay setting. If unspecified, value is set to 1.  
<value> | Physical length of fixture of added transmission line.   
Examples | CALC:FSIM:EXT:PORT1:DIST:VAL?  
calculate:fsimulator:extension:port2:distance:value?  
Query Syntax | CALCulate<cnum>:FSIMulator:EXTension:PORT<pnum>:DISTance:VALue?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:FSIMulator:EXTension:PORT<pnum>:LOSS<n>:FREQuency

Applicable Models: All (Read-only) Returns the frequency for the Freq and Loss
pair number and for the specified port number. [Learn about Loss Compensation
values.](../../../S3_Cals/Port_Extensions.htm#LossCompensation)  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number that will receive the freq/loss settings. If unspecified, value is set to 1.  
<n> | Freq and Loss pair number. Choose from 1 or 2. If unspecified, value is set to 1.  
<value> | Frequency value. Choose a frequency within the frequency span of the VNA.  
Examples | CALC:FSIM:EXT:PORT1:LOSS2:FREQ?  
calculate:fsimulator:extension:port2:loss1:frequency?  
Query Syntax | CALCulate<cnum>:FSIMulator:EXTension:PORT<pnum>:LOSS<n>:FREQuency?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:FSIMulator:EXTension:PORT<pnum>:LOSS<n>:VALue

Applicable Models: All (Read-only) Returns the Loss value for the specified
port number. [Learn about Loss Compensation
values.](../../../S3_Cals/Port_Extensions.htm#LossCompensation) Note: This
command affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number that will receive the Freq/Loss settings. If unspecified, value is set to 1.  
<n> | Loss "Use" number. Choose from 1 or 2. If unspecified, value is set to 1.  
<value> | Loss in dB. Choose a value between -90 and 90  
Examples | CALC:FSIM:EXT:PORT:LOSS1:VAL? calculate:fsimulator:extension:port2:loss2:value?  
Query Syntax | CALCulate<cnum>:FSIMulator:EXTension:PORT<pnum>:LOSS<n>:VALue?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:FSIMulator:EXTension:PORT<pnum>:LOSS<n>[:STATe]

Applicable Models: All (Read-only) Returns the ON/OFF state for the Freq and
Loss pair number and for the specified port number. [Learn about Loss
Compensation values.](../../../S3_Cals/Port_Extensions.htm#LossCompensation)
Note: This command affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number that will receive the Freq/Loss settings. If unspecified, value is set to 1.  
<n> | Freq and Loss pair. Choose from 1 or 2. If unspecified, value is set to 1.  
<value> | State of Freq and Loss values for port extension. 0 or OFF Specified Freq and Loss values are OFF 1 or ON Specified Freq and Loss values are ON  
Examples | CALC:FSIM:EXT:PORT:LOSS:STAT?  
calculate:fsimulator:extension:port2:loss2:state?  
Query Syntax | CALCulate<cnum>:FSIMulator:EXTension:PORT<pnum>:LOSS<n>[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:FSIMulator:EXTension:PORT<pnum>:DCLoss:VALue

Applicable Models: All (Read-only) Returns the Port Loss at DC value for the
specified port number. [Learn about Loss Compensation
values.](../../../S3_Cals/Port_Extensions.htm#LossCompensation) Note: This
command affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port number to receive Loss value. If unspecified, value is set to 1.  
<value> | Loss in dB. Choose a value between -90 and 90  
Examples | CALC:FSIM:EXT:PORT:DCL:VAL? calculate:fsimulator:extension:port2:dcloss:value?  
Query Syntax | CALCulate<cnum>:FSIMulator:EXTension:PORT<pnum>:DCLoss:VALue?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:FSIMulator:EXTension:PORT<pnum>:MEDium

Applicable Models: All (Read-only) Reurns the media type of the added fixture
or transmission line. See also
[SENS:CORR:EXT:PORT:SYSMedia](../Sense/CorrExtension.md#sysMedia) Note: This
command affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number. This number is ignored and all ports have the same setting.  
<char> | Medium type. Choose from:

  * COAX
  * WAVEguide

  
Examples | CALC:FSIM:EXT:PORT:MED? calculate:fsimulator:extension:port2:medium?  
Query Syntax | CALCulate<cnum>:FSIMulator:EXTension:PORT<pnum>:MEDium?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | COAX  
  
* * *

## CALCulate<cnum>:FSIMulator:EXTension:PORT<pnum>:WAVEguide:FCUToff

Applicable Models: All (Read-only) Returns the cuttoff (minimum) frequency of
the added waveguide fixture or transmission line.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number for which media type is being set. If unspecified, value is set to 1.  
<value> | Cutoff frequency in Hz. This value is ignored when [CALC:FSIM:EXT:PORT:MED](FSimulatorActive.md#ExtPortMed) is set to COAX for the same port.  
Examples | CALC:FSIM:EXT:PORT:WAVE:FCUT? calculate:fsimulator:extension:port2:waveguide:cutoff?  
Query Syntax | CALCulate<cnum>:FSIMulator:EXTension:PORT<pnum>:WAVEguide:FCUToff?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:FSIMulator:EXTension:PORT<pnum>:WAVEguide:COUPle

Applicable Models: All (Read-only) Returns the state of coupling with the
system Velocity Factor value. [Learn
more.](../../../S3_Cals/Port_Extensions.htm#PortDiag) Note: This command
potentially affects ALL measurements on the VNA.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number. This number is ignored and all ports have the same setting.  
<bool> | Coupling state. Choose from:

  * ON (or 1) - Velocity Factor is coupled with the system setting.
  * OFF (or 0) - Velocity Factor is NOT coupled with the system setting.

  
Examples | CALC:FSIM:EXT:PORT:WAVE:COUP? calculate:fsimulator:extension:port2:waveguide:couple?  
Query Syntax | CALCulate<cnum>:FSIMulator:EXTension:PORT<pnum>:WAVEguide:COUPle?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1 or ON (Coupled)  
  
* * *

## CALCulate<cnum>:FSIMulator:EXTension:PORT<pnum>:VELocity:FACtor

Applicable Models: All (Read-only) Returns the velocity factor of the fixture
or added transmission line.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number for which velocity factor is being set. If unspecified, value is set to 1.  
<value> | Velocity Factor. Set [SENS:CORR:EXT:PORT:SYSV](../Sense/CorrExtension.md#sysVelocity) to use the system velocity factor.  
Examples | CALC:FSIM:EXT:PORT:VEL:FAC? calculate:fsimulator:extension:port2:velocity:factor?  
Query Syntax | CALCulate<cnum>:FSIMulator:EXTension:PORT<pnum>:VELocity:FACtor?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:FSIMulator:EXTension:PORT<pnum>:VELocity:COUPle

Applicable Models: All (Read-only) Returns the state of coupling with the
system Velocity Factor value. [Learn
more.](../../../S3_Cals/Port_Extensions.htm#PortDiag) Note: This command
potentially affects ALL measurements on the VNA.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number. This number is ignored and all ports have the same setting.  
<bool> | Coupling state. Choose from:

  * ON (or 1) - Velocity Factor is coupled with the system setting.
  * OFF (or 0) - Velocity Factor is NOT coupled with the system setting.

  
Examples | CALC:FSIM:EXT:PORT:VEL:COUP? calculate:fsimulator:extension:port2:velocity:couple?  
Query Syntax | CALCulate<cnum>:FSIMulator:EXTension:PORT<pnum>:VELocity:COUPle?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1 or ON (Coupled)  
  
* * *

## CALCulate<cnum>:FSIMulator:EXTension:PORT<pnum>[:STATe]

Applicable Models: All (Read-only) Returns the state of port extension for the
specified port[.](../../../S3_Cals/Port_Extensions.md#PortDiag) Note: This
command potentially affects ALL measurements on the VNA.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number for which port extension is being set. If unspecified, value is set to 1.  
<bool> | Port extension state. Choose from:

  * ON (or 1) - Port extension is on
  * OFF (or 0) - Port extension is off.

  
Examples | CALC:FSIM:EXT:PORT:STAT? calculate:fsimulator:extension:port2:state?  
Query Syntax | CALCulate<cnum>:FSIMulator:EXTension:PORT<pnum>[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:FSIMulator:POWer:COMPensate:MODE <char>

Applicable Models: All (Read-Wrrite) Adjust the source power compensation for
gain/loss through ALL fixture components or through DEEMbed components
only.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<char> | Mode selection. Choose from:

  * ALL
  * DEEMbed

  
Examples | CALC:FSIM:POW:COMP:MODE ALL calculate:fsimulator:power:compensate:mode deembed  
Query Syntax | CALCulate<cnum>:FSIMulator:POWer:COMPensate:MODE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ALL  
  
* * *

## CALCulate<cnum>:FSIMulator:POWer:PORT<pnum>:COMPensate[:STATe] <bool>

Applicable Models: All (Read-Wrrite) Sets and returns on power compensation
for the active fixture  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number for which port extension is being set. If unspecified, value is set to 1.  
<bool> | power compensation state. Choose from:

  * ON (or 1) - Power compensation is on
  * OFF (or 0) - Power compensation is off.

  
Examples | CALC:FSIM:POW:PORT:COMP ON calculate:fsimulator:power:port:compensate:state 0  
Query Syntax | CALCulate<cnum>:FSIMulator:POWer:PORT[p]:COMPensate[:STATe ]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:FSIMulator:SAVE <snpName>

Applicable Models: All (Write only) Saves SNP file corresponding to the entire
active fixture.  
---  
Parameters |   
<snpName> | String - snp file name. Appends ".sNp" depending on num ports  
Example | CALC:FSIM:SAVE "myFixure" calculate:fsimulator:save "D:\myfixture"  
Return Type | Not applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

CALCulate<cnum>:FSIMulator:SECTion:CIRCuit:ENABle?

Applicable Models: All (Read only) Returns all circuits ON/OFF for all ports.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
Examples | CALC:FSIM:SECT:CIRC:ENAB? calculate2:fsimulator:section:circuit:enable?  
Query Syntax | CALCulate<cnum>:FSIMulator:SECTionCIRCuit:ENABle?  
Return Type | Boolean (1 = ON, 0 = OFF)   
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

CALCulate<cnum>:FSIMulator:SECTion:EXTension:ENABle?

Applicable Models: All (Read only) Returns the port extensions ON/OFF for all
ports.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
Examples | CALC:FSIM:SECT:EXT:ENAB? calculate2:fsimulator:section:extension:enable?  
Query Syntax | CALCulate<cnum>:FSIMulator:SECTion:EXTension:ENABle?  
Return Type | Boolean (1 = ON, 0 = OFF)   
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

CALCulate<cnum>:FSIMulator:SECTion:ZCONversion:ENABle?

Applicable Models: All (Read only) Returns all ZConversions ON/OFF (both SE
and BAL).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
Examples | CALC:FSIM:SECT:ZCON:ENAB? calculate2:fsimulator:section:zconversion:enable?  
Query Syntax | CALCulate<cnum>:FSIMulator:SECTion:ZCONversion:ENABle?  
Return Type | Boolean (1 = ON, 0 = OFF)   
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## CALCulate<cnum>:FSIMulator:TOPology:LOAD <fileName>

Applicable Models: All (Write only) Loads an active fixture from a file.  
---  
Parameters |   
<fileName> | Fixture topology file name.  
Example | CALC:FSIM:TOP:LOAD "example.topo" calculate:fsimulator:topology:load "example.topo"  
Return Type | Not applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:FSIMulator:TOPology:SAVE <fileName>

Applicable Models: All (Write only) Saves the current active fixture topology
to a file.  
---  
Parameters | Not applicable  
<fileName> | Fixture topology file name.  
Example | CALC:FSIM:TOP:SAVE "example.topo" calculate:fsimulator:topology:save "example.topo"  
Return Type | Not applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

CALCulate<cnum>:FSIMulator:ZCONversion:DIFFerential:STATe

Applicable Models: All (Read Only) Returns the differential port impedance
conversion function ON/OFF.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:FSIM:ZCON:DIFF:STAT?  
calculate2:fsimulator:zconversion:DIFFerential:state?  
Query Syntax | CALCulate<cnum>:FSIMulator:ZCONversion:DIFFerential:STATe?  
Return Type | Boolean 0 Differential port impedance conversion OFF 1 Differential port impedance conversion ON  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:ZCONversion:DIFFerential:BPORt<pnum>:COMPLex

Applicable Models: All (Read-Only) Returns the complex impedance value for the
differential port impedance conversion function.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<pnum> | Balanced port number. Choose from 1 to 999. Note: See [Balanced port versus Logical port](FSimulatorDraft.md#BPORt Lport).  
Examples | CALC:FSIM:ZCON:DIFF:BPOR2:COMPL?   
calculate2:fsimulator:zconversion:differential:bport2:complex?  
Query Syntax | CALCulate<cnum>:FSIMulator:ZCONversion:DIFFerential:BPORt<pnum>:COMPlex?  
Return Type | Numeric <real>,<img> Real part of the Impedance value in Units, Imaginary part of the Impedance value in Units.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0,0  
  
* * *

CALCulate<cnum>:FSIMulator:ZCONversion:DIFFerential:BPORt<pnum>:SCALar

Applicable Models: All (Read Only) Returns the real part of impedance value
for the differential port impedance conversion function.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<pnum> | Balanced port number. Choose from 1 to 999. Note: See [Balanced port versus Logical port](FSimulatorDraft.md#BPORt Lport).  
Examples | CALC:FSIM:ZCON:DIFF:BPOR2:SCAL 200,10  
calculate2:fsimulator:zconversion:differential:bport2:scalar 20,3  
Query Syntax | CALCulate<cnum>:FSIMulator:ZCONversion:DIFFerential:BPORt<pnum>:SCALer?  
Return Type | Numeric Real part of the Impedance value in Units  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

CALCulate<cnum>:FSIMulator:ZCONversion:DIFFerential:LPORt<pnum>:COMPLex

Applicable Models: All (Read Only) Returns the complex impedance value for the
common mode port impedance conversion function.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<pnum> | Logical port number. Choose from 1 to 999. Note: See [Balanced port versus Logical port](FSimulatorDraft.md#BPORt Lport).  
Examples | CALC:FSIM:ZCON:DiFF:LPOR2:COMPL?  
calculate2:fsimulator:zconversion:differential:lport2:complex?  
Query Syntax | CALCulate<cnum>:FSIMulator:ZCONversion:DIFFerential:LPORt<pnum>:COMPlex?  
Return Type | Numeric <real>,<img> Real part of the Impedance value in Units, Imaginary part of the Impedance value in Units  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0,0  
  
* * *

CALCulate<cnum>:FSIMulator:ZCONversion:DIFFerential:LPORt<pnum>:SCALar

Applicable Models: All (Read Write) Returns the real part of impedance value
for the differential mode port impedance conversion function. See [Critical
Note](FSimulatorDraft.htm#Critical)  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<pnum> | logical port number. Choose from 1 to 999. Note: See [Balanced port versus Logical port](FSimulatorDraft.md#BPORt Lport).  
Examples | CALC:FSIM:ZCON:DIFF:LPOR2:SCAL?  
calculate2:fsimulator:zconversion:differential:lport2:scala?  
Query Syntax | CALCulate<cnum>:FSIMulator:ZCONversion:DIFFerential:LPORt<pnum>:SCALer?  
Return Type | Numeric Real part of the Impedance value in Units  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

CALCulate<cnum>:FSIMulator:ZCONversion:COMMonmode:STATe

Applicable Models: All (Read Only) Returns the common mode port impedance
conversion function ON/OFF.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:FSIM:ZCON:COMM:STAT?  
calculate2:fsimulator:zconversion:commonmode:state?  
Query Syntax | CALCulate<cnum>:FSIMulator:COMMonmode:DIFFerential:STATe?  
Return Type | Boolean 0 Common mode port impedance conversion OFF 1 Common mode port impedance conversion ON  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:ZCONversion:COMMonmode:BPORt<pnum>:COMPLex

Applicable Models: All (Read-Write) Returns the complex impedance value for
the common mode port impedance conversion function.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<pnum> | Balanced port number. Choose from 1 to 999. Note: See [Balanced port versus Logical port.](FSimulatorDraft.md#BPORt Lport)  
Examples | CALC:FSIM:ZCON:COMM:BPOR2:COMPL?  
calculate2:fsimulator:zconversion:commonmode:bport2:complex?  
Query Syntax | CALCulate<cnum>:FSIMulator:ZCONversion:COMMonmode:BPORt<pnum>:COMPlex?  
Return Type | Numeric <real>,<img> Real part of the Impedance value in Units, Imaginary part of the Impedance value in Units  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0,0  
  
* * *

CALCulate<cnum>:FSIMulator:ZCONversion:COMMonmode:BPORt<pnum>:SCALar

Applicable Models: All (Read Only) Returns the real part of impedance value
for the common mode port impedance conversion function.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<pnum> | Balanced port number. Choose from 1 to 999. Note: See [Balanced port versus Logical port.](FSimulatorDraft.md#BPORt Lport)  
Examples | CALC:FSIM:ZCON:COMM:BPOR2:SCAL?  
calculate2:fsimulator:zconversion:commonmode:bport2:scalar?  
Query Syntax | CALCulate<cnum>:FSIMulator:ZCONversion:COMMonmode:BPORt<pnum>:SCALer?  
Return Type | Numeric Real part of the Impedance value in Units  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

CALCulate<cnum>:FSIMulator:ZCONversion:COMMonmode:LPORt<pnum>:COMPLex

Applicable Models: All (Read Only) Returns the complex impedance value for the
common mode port impedance conversion function.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<pnum> | Logical port number. Choose from 1 to 999. Note: See [Balanced port versus Logical port.](FSimulatorDraft.md#BPORt Lport)  
Examples | CALC:FSIM:ZCON:COMM:LPOR2:COMPL?  
calculate2:fsimulator:zconversion:commonmode:lport2:complex?  
Query Syntax | CALCulate<cnum>:FSIMulator:ZCONversion:COMMonmode:LPORt<pnum>:COMPlex?  
Return Type | Numeric <real>,<img> Real part of the Impedance value in Units, Imaginary part of the Impedance value in Units.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0,0  
  
* * *

CALCulate<cnum>:FSIMulator:ZCONversion:COMMonmode:LPORt<pnum>:SCALar

Applicable Models: All (Read Only) Returns the real part of impedance value
for the common mode port impedance conversion function.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<pnum> | logical port number. Choose from 1 to 999. Note: See [Balanced port versus Logical port.](FSimulatorDraft.md#BPORt Lport)  
Examples | CALC:FSIM:ZCON:COMM:LPOR2:SCAL?  
calculate2:fsimulator:zconversion:commonmode:lport2:scalar?  
Query Syntax | CALCulate<cnum>:FSIMulator:ZCONversion:COMMonmode:LPORt<pnum>:SCALer?  
Return Type | Numeric, Real part of the Impedance value in Units.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

CALCulate<cnum>:FSIMulator:ZCONversion:SENDed:PORt<pnum>:STATe

Applicable Models: All (Read Only) Returns the single-ended impedance
conversion function ON/OFF. Must also set the fixture simulator function to ON
using [CALC:FSIM:STAT.](FSimulator.md#FSimState)  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<pnum> | Port number. Choose from 1 to 999.  
Examples | CALC:FSIM:ZCON:SEND:PORT3:STAT?  
calculate2:fsimulator:zconversion:sended:port2:state?  
Query Syntax | CALCulate<cnum>:FSIMulator:ZCONversion:SENDed:PORt:STATe?  
Return Type | Boolean 0 single-ended port impedance conversion OFF 1 single-ended port impedance conversion ON  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

CALCulate<cnum>:FSIMulator:ZCONversion:SENDed:PORt<pnum>:COMPLex

Applicable Models: All (Read Only) Returns the complex impedance value for the
single-ended port impedance conversion function.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<pnum> | Pport number. Choose from 1 to 999.  
Examples | CALC:FSIM:ZCON:SEND:POR2:COMPL?  
calculate2:fsimulator:zconversion:sended:port2:complex?  
Query Syntax | CALCulate<cnum>:FSIMulator:ZCONversion:SENDed:PORt<pnum>:COMPlex?  
Return Type | Numeric <real>, <img> Real part of the Impedance value in Units, Imaginary part of the Impedance value in Units.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0,0  
  
* * *

CALCulate<cnum>:FSIMulator:ZCONversion:SENDed:PORT<pnum>:SCALer

Applicable Models: All (Read Only) Returns the real part of impedance value
for the single-ended port impedance conversion function. See [Critical
Note](FSimulatorDraft.htm#Critical)  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<pnum> | Pport number. Choose from 1 to 999.  
Examples | CALC:FSIM:ZCON:SEND:PORT:SCAL?  
calculate2:fsimulator:zconversion:sended:port2:scalar?  
Query Syntax | CALCulate<cnum>:FSIMulator:ZCONversion:SENDed:PORT<pnum>:SCALer?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1

