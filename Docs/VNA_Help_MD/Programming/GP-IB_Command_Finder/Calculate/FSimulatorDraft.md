# Calculate:FSimulator:Draft Commands

CALCulate:FSIMulator:DRAFt: | [APPLy](FSimulatorDraft.md#Apply) | CIRCuit: | ADD | CATalog? | DELete | DEVice | PORTs | ARRay | REVerse | EMBED | TYPE | FILE | EXTRapolate | MODify | NEXT? | PARameter | C | C2 | DELay | G | G2 | L | L2 | LOSS | VALue | R | R2 | RIN | ROUT | Z0 | RESet | STATe | VNA | PORTs | [DISCard](FSimulatorDraft.md#Discard) | EXTension:PORT: | DELay | DISTance | VALue | UNIT |[ END](FSimulatorDraft.md#ExtPortEnd) | LOSS | FREQuency | VALue | STATe | [MEDium](FSimulatorActive.md#ExtPortMed) | WAVEguide | FCUToff | COUPle | VELocity | FACTor | COUPle | DCLoss:VALue | STATe | [SAVE](FSimulatorDraft.md#Save) |SECTion | CIRCuit | ENABle | EXTension | ENABle | ZCONversion | ENABle | ZCONversion | DIFFerential | STATe | BPORt  
| COMPLex | SCALar | :LPORt  
| COMPLex | SCALar | COMMonmode | STATe | BPORt  
| COMPLex | SCALar | LPORt<pnum>  
| COMPLex | SCALar | SENDed:PORT | STATe | COMPLex | SCALar  
---  
  
See Also

  * [Learn about Using Fixture Simulator](../../Using_Fixture_Simulator.md)

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

Critical Note: CALCulate commands act on the selected measurement. You can
select one measurement for each channel using
[Calc:Par:MNUM](Parameter.md#MnumSel) or
[Calc:Par:Select](Parameter.md#cps). [Learn
more](../../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.htm).

  * [CALC:PAR:CAT?](Parameter.md#cpc) alone can NOT be used to return a balanced measurement parameter. If a balanced measurement transform is being performed, then additional querying of the CALC:FSIM system is required to determine the balanced parameter type. [See an example.](../../GPIB_Example_Programs/Create_a_Balanced_Measurement_using_SCPI.md)

  * BPORt versus LPORt commands \- For each command in this subsystem that includes a BPORt keyword, there is an LPORt equivalent. The commands are identical except for the way in which the balanced / logical port numbers are specified:

  *     * The BPORt commands refer to the Balanced port number. There can only be up to two balanced ports. This method is compatible with the ENA network analyzer.

    * The LPORt commands refer to the Logical port number. A balanced port can appear as either logical port 1, 2, or 3. These are the references as they appear in the front-panel user interface.

## CALCulate<cnum>:FSIMulator:DRAFt:APPLy

Applicable Models: All (Write only) Copies the draft fixture to active
fixture. Exact same functionality as
[CALC:FSIM:APPL](FSimulatorActive.md#APPLy)  
---  
Parameters | Not applicable  
Example | CALC:FSIM:DRAF:APPL calculate:fsimulator:draft:apply  
Return Type | Not applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:ADD <block type>, <fixt port
count>

Applicable Models: All (Write only) Create a block of the specified block type
with the specified fixture port count. By default, this block will be created
on the VNA Port 1 with "de-embed". It can be moved and changed to "embed" with
commands below.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
<block type> |  | FILe | SNP File Block (valid parameters: FILE, FILE:EXTRapolate)  
---|---  
RLGLoop | Ground Loop (Shunt L circuit model) (valid parameters: R, L, C, G)  
RCGLoop | Ground Loop (Shunt C circuit model) (valid parameters: R, L, C, G)  
CGGLoop | Ground Loop (Shunt C circuit model, but for convenience, user can specifier G instead of R) (valid parameters: R, L, C, G)  
FGLoop | Ground Loop (valid parameters: FILE, FILE:EXTRapolate, file must be S1P file)  
SLPC | Port Matching Circuit: Series L - Shunt C (valid parameters: R, R2, L, C,G, G2)  
PCSL | Port Matching Circuit: Shunt C - Series L (valid parameters: R, R2, L, C, G, G2)  
PLSC | Port Matching Circuit: Shunt L - Series C (valid parameters: R, R2, L, C, G, G2)  
SCPL | Port Matching Circuit: Series C - Shunt L (valid parameters: R, R2, L, C, G, G2)  
PLPC | Port Matching Circuit: Shunt L - Shunt C (valid parameters: R, R2, L, C, G, G2)  
SCPC | Port Matching Circuit: Series C - Shunt/ C (valid parameters: R, R2, L, L2, C, C2, G, G2)  
PCSC | Port Matching Circuit: Shunt C - Series C (valid parameters: R, R2, L, L2, C, C2, G, G2)  
SLPL | Port Matching Circuit: Series L - Shunt L (valid parameters: R, R2, L, L2, C, C2, G, G2)  
PLSL | Port Matching Circuit: Shunt L - Series L (valid parameters: R, R2, L, L2, C, C2, G, G2)  
ILINe | Ideal Line. For this block type, user can specify delay and loss value.  
TRANsformer  | Transformer Circuit. For this block type, User can specify Rin and Rout values to represent a transformer.  
D4PMatching | Differential Matching Circuit: PLPC  
D4PFile | Differential Matching Circuit: File Type (S2P)  
<fixt port count> | Number of port of block  
Examples | CALC:FSIM:DRAF:CIRC:ADD SLPC,2 calculate2:fsimulator:draft:circuit:add SLPC,2  
Query Syntax | Not Applicable  
Return Type | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit:CATalog?

Applicable Models: All (Read only) Returns a comma-separated list of circuit
numbers created in the draft circuit.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
Examples | CALC:FSIM:DRAF:CIRC:CAT? calculate2:fsimulator:draft:circuit:catalog?  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit:CATalog?  
Return Type | comma-separated string  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:DELete

Applicable Models: All (Write only) Deletes the specified circuit.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
Examples | CALC:FSIM:DRAF:CIRC:DEL calculate2:fsimulator:draft:circuit:delete  
Query Syntax | Not Applicable  
Return Type | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:DEVice:PORTs[:ARRay] <port
list - in, out>

Applicable Models: All (Read-Write) Sets the Device ports for the specified
circuit. The number of ports must be even and correspond to the number of
ports of the fixture. This command can be used to reverse or change the order
of ports in an SNP file.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
Examples | CALC:FSIM:DRAF:CIRC:DEV:PORT 2,1 calculate2:fsimulator:draft:circuit:device:ports:array 2,1  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:DEVice:PORTs[:ARRay]?   
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:DEVice:PORTs:REVerse <bool>

Applicable Models: All (Read-Write) Sets whether or not to reverse the ports
on an existing S2P file.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<bool> | Choose from: ON or 1 - Reverse the ports. OFF or 0 - Do not reverse the ports.  
<circN> | Circuit Number  
Examples | CALC:FSIM:DRAF:CIRC:DEV:PORT:REV ON calculate2:fsimulator:draft:circuit:device:ports:reverse 1  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:DEVice:PORTs:REVerse?  
Return Type | Boolean   
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:EMBED:TYPE <embed | deembed>

Applicable Models: All (Read-Write) Sets whether the circuit should be
embedded or de-embedded. Valid for all block Types. The block is created using
CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>. Setting a value not used by the selected circuit will have no affect.
[Learn more](../../../S3_Cals/Fixture_Simulator.md#Matching).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<char> | Choose from : EMBed \- Add Network circuit. DEEMbed \- Remove Network circuit  
<circN> | Circuit Number  
Examples | CALC:FSIM:DRAF:CIRC:EMBED:TYPE EMBED calculate2:fsimulator:draft:circuit:embed:type deembed   
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:EMBED:TYPE?  
Return Type | character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | EMBed  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:FILE <filename>

Applicable Models: All (Read-Write) Sets the filename. Valid blocks: FILe,
D4PFile, FGLoop The block is created using
CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>. Setting a value not used by the selected circuit will have no affect.
[Learn more](../../../S3_Cals/Fixture_Simulator.md#Matching).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<filename> | File name and extension (.s2P) of the de-embedding circuit. Files are stored in the default folder "D:\". To recall from a different folder, specify the full path name.  
<circN> | Circuit Number  
Examples | CALC:FSIM:DRAF:CIRC:FILE 'myFile.s2P' calculate2:fsimulator:draft:circuit:file "D:\myFile.s2P"  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:FILE?  
Return Type | string  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:FILE:EXTRapolate <bool>

Applicable Models: All (Read-Write) Sets whether or not extrapolation is
allowed. Valid blocks: FILe, D4PFile, FGLoop.  The block is created using
CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>. Setting a value not used by the selected circuit will have no affect.
[Learn more](../../../S3_Cals/Fixture_Simulator.md#Matching).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<bool> | Choose from: ON or 1 - Turns Extrapolation ON OFF or 0 - Turns Extrapolation OFF  
<circN> | Circuit Number  
Examples | CALC:FSIM:DRAF:CIRC:FILE:EXTR ON calculate2:fsimulator:draft:circuit:file:extrapolate 1  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:FILE:EXTRapolate?  
Return Type | Boolean   
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:FILE:MODify <enum>

Applicable Models: All (Read-Write) Sets all reflection and crosstalk
parameters on the DUT side to zero. [Learn
more](../../../S3_Cals/Fixture_Simulator.htm#Modify). The block is created
using CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>. Setting a value not used by the selected circuit will have no affect.
[Learn more](../../../S3_Cals/Fixture_Simulator.md#Matching).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<enum> | Choose from: NONE - Does not modify the block. NREFlect - Sets all reflection parameters on the DUT-side to zero. NXTalk \- Sets all reflection and crosstalk parameters on the DUT-side to zero.  
<circN> | Circuit Number  
Examples | CALC:FSIM:DRAF:CIRC:FILE:MOD NONE  calculate2:fsimulator:draft:circuit:file:modify nreflect  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:FILE:MODify?  
Return Type | Enumeration  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | NONE  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:NEXT?

Applicable Models: All (Read only) Returns the next free circuit number than
be used to create a new circuit block  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
Examples | CALC:FSIM:DRAF:CIRC:NEXT? calculate2:fsimulator:draft:circuit:next?  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit:NEXT?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:C <value>

Applicable Models: All (Read-Write) Sets the capacitance (C) circuit element
for the specified circuit. Valid blocks: RLGLoop, RCGLoop, CGGLoop, SLPC,
PCSL, PLSC, SCPL, PLPC, SCPC, PCSC, SLPL, PLSL. The block is created using
CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>. Setting a value not used by the selected circuit will have no affect.
[Learn more](../../../S3_Cals/Fixture_Simulator.md#Matching).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<value> | Capacitance value in farads. Choose a value between -1E18 to 1E18  
<circN> | Circuit Number  
Examples | CALC:FSIM:DRAF:CIRC:PAR:C 0.00002  calculate2:fsimulator:draft:circuit:parameter:C 0.00002   
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:C?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:C2 <value>

Applicable Models: All (Read-Write) Sets the capacitance (C2) circuit element
for the specified circuit. Valid blocks: SLPC, PCSL, PLSC, SCPL, PLPC, SCPC,
PCSC, SLPL, PLSL The block is create using
CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>. Setting a value not used by the selected circuit will have no affect.
[Learn more](../../../S3_Cals/Fixture_Simulator.md#Matching).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<value> | Capacitance value in farads. Choose a value between -1E18 to 1E18  
<circN> | Circuit Number  
Examples | CALC:FSIM:DRAF:CIRC:PAR:C2 0.00002  calculate2:fsimulator:draft:circuit:parameter:C2 0.00002   
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:C2?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:DELay <num>

Applicable Models: All (Read-Write) Sets port extension delay in time. Valid
blocks: ILIN. The block is create using
CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>. Setting a value not used by the selected circuit will have no affect.
[Learn more](../../../S3_Cals/Fixture_Simulator.md#Matching).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<num> | The port extension in seconds; may include suffix. Choose a number between: -1E18 and 1E18  
<circN> | Circuit Number  
Examples | CALC:FSIM:DRAF:CIRC:PAR:DEL 2MS  calculate2:fsimulator:draft:circuit:parameter:delay .00025   
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:DEL?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:G <value>

Applicable Models: All (Read-Write) Sets the conductance (G) circuit element
for the specified circuit. Valid blocks: RLGLoop, RCGLoop, CGGLoop, SLPC,
PCSL, PLSC, SCPL, PLPC, SCPC, PCSC, SLPL, PLSL. The block is create using
CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>. Setting a value not used by the selected circuit will have no affect.
[Learn more](../../../S3_Cals/Fixture_Simulator.md#Matching).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<value> | Conductance value in siemens. Choose a value between -1E18 to 1E18  
<circN> | Circuit Number  
Examples | CALC:FSIM:DRAF:CIRC:PAR:G 0.00002  calculate2:fsimulator:draft:circuit:parameter:g 0.00002   
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:G?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:G2 <value>

Applicable Models: All (Read-Write) Sets the conductance (G2) circuit element
for the specified circuit. Valid blocks: SLPC, PCSL, PLSC, SCPL, PLPC, SCPC,
PCSC, SLPL, PLSL The block is create using
CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>. Setting a value not used by the selected circuit will have no affect.
[Learn more](../../../S3_Cals/Fixture_Simulator.md#Matching).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<value> | Conductance value in siemens. Choose a value between -1E18 to 1E18  
<circN> | Circuit Number  
Examples | CALC:FSIM:DRAF:CIRC:PAR:G2 0.00002  calculate2:fsimulator:draft:circuit:parameter:g2 0.00002   
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:G2?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:L <value>

Applicable Models: All (Read-Write) Sets the inductance (L) circuit element
for the specified circuit. Valid blocks: RLGLoop, RCGLoop, CGGLoop, SLPC,
PCSL, PLSC, SCPL, PLPC, SCPC, PCSC, SLPL, PLSL. The block is create using
CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>. Setting a value not used by the selected circuit will have no affect.
[Learn more](../../../S3_Cals/Fixture_Simulator.md#Matching).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<value> | Inductance value in henries. Choose a value between -1E18 to 1E18  
<circN> | Circuit Number  
Examples | CALC:FSIM:DRAF:CIRC:PAR:L 0.00002  calculate2:fsimulator:draft:circuit:parameter:l 0.00002   
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:L?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:L2 <value>

Applicable Models: All (Read-Write) Sets the inductance (L2) circuit element
for the specified circuit. Valid blocks: SLPC, PCSL, PLSC, SCPL, PLPC, SCPC,
PCSC, SLPL, PLSL The block is create using
CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>. Setting a value not used by the selected circuit will have no affect.
[Learn more](../../../S3_Cals/Fixture_Simulator.md#Matching).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<value> | Inductance value in henries. Choose a value between -1E18 to 1E18  
<circN> | Circuit Number  
Examples | CALC:FSIM:DRAF:CIRC:PAR:L2 0.00002  calculate2:fsimulator:draft:circuit:parameter:l2 0.00002   
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:L2?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:LOSS:VALue <num>

Applicable Models: All (Read-Write) Sets the loss at DC. Valid blocks: ILIN.
The block is create using CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD
<block type>, <fixt port count>. Setting a value not used by the selected
circuit will have no affect. [Learn
more](../../../S3_Cals/Fixture_Simulator.htm#Matching).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<num> | Loss in dB. Choose a value between -90 and 90.  
<circN> | Circuit Number  
Examples | CALC:FSIM:DRAF:CIRC:PAR:LOSS:VAL 1.5  calculate2:fsimulator:draft:circuit:parameter:loss:value .1   
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:LOSS:VALue?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:R <value>

Applicable Models: All (Read-Write) Sets the resistance (R) circuit element
for the specified circuit. Valid blocks: RLGLoop, RCGLoop, CGGLoop, SLPC,
PCSL, PLSC, SCPL, PLPC, SCPC, PCSC, SLPL, PLSL. The block is create using
CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>. Setting a value not used by the selected circuit will have no affect.
[Learn more](../../../S3_Cals/Fixture_Simulator.md#Matching).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<value> | Resistance value in ohms. Choose a value between -1E18 to 1E18  
<circN> | Circuit Number  
Examples | CALC:FSIM:DRAF:CIRC:PAR:R 0.00002  calculate2:fsimulator:draft:circuit:parameter:r 0.00002   
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:R?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:R2 <value>

Applicable Models: All (Read-Write) Sets the resistance (R2) circuit element
for the specified circuit. Valid blocks: SLPC, PCSL, PLSC, SCPL, PLPC, SCPC,
PCSC, SLPL, PLSL The block is create using
CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>. Setting a value not used by the selected circuit will have no affect.
[Learn more](../../../S3_Cals/Fixture_Simulator.md#Matching).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<value> | Resistance value in ohms. Choose a value between -1E18 to 1E18  
<circN> | Circuit Number  
Examples | CALC:FSIM:DRAF:CIRC:PAR:R2 0.00002  calculate2:fsimulator:draft:circuit2:parameter:r2 0.00002   
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:R2?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:RIN <value>

Applicable Models: All (Read-Write) Sets the resistance (R) value at input of
transformer (real only). Valid blocks: TRANs The block is create using
CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>. Setting a value not used by the selected circuit will have no affect.
[Learn more](../../../S3_Cals/Fixture_Simulator.md#Matching).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<value> | Resistance value in ohms. Choose a value between -1E18 to 1E18  
<circN> | Circuit Number  
Examples | CALC:FSIM:DRAF:CIRC:PAR:RIN 0.00002  calculate2:fsimulator:draft:circuit2:parameter:rin 0.00002   
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:RIN?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:ROUT <value>

Applicable Models: All (Read-Write) Sets the resistance (R) value at output of
transformer (real only). Valid blocks: TRANs The block is create using
CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>. Setting a value not used by the selected circuit will have no affect.
[Learn more](../../../S3_Cals/Fixture_Simulator.md#Matching).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<value> | Resistance value in ohms. Choose a value between -1E18 to 1E18  
<circN> | Circuit Number  
Examples | CALC:FSIM:DRAF:CIRC:PAR:ROUT 0.00002  calculate2:fsimulator:draft:circuit2:parameter:rout 0.00002   
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:ROUT?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:Z0 <value>

Applicable Models: All (Read-Write) Sets the impedance (Z0) for the ideal
block (scalar value). Valid blocks: ILIN. The block is create using
CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>. Setting a value not used by the selected circuit will have no affect.
[Learn more](../../../S3_Cals/Fixture_Simulator.md#Matching).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<value> | Impedance value in ohms. Choose a value between -1E18 to 1E18  
<circN> | Circuit Number  
Examples | CALC:FSIM:DRAF:CIRC:PAR:Z0 0.00002  calculate2:fsimulator:draft:circuit:parameter:z0 0.00002   
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:PARameter:Z0?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 50  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit:RESet

Applicable Models: All (Write only) Resets the circuit section to preset
values Note: This command impacts the circuits and the port extensions. It
does not change any impedance conversion values.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
Examples | CALC:FSIM:DRAF:CIRC:RES calculate2:fsimulator:draft:circuit:reset  
Query Syntax | Not Applicable  
Return Type | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:STATe <bool>

Applicable Models: All (Read-Write) Turns the circuit ON and OFF. Valid for
all block types The block is create using
CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:ADD <block type>, <fixt port
count>. Setting a value not used by the selected circuit will have no affect.
[Learn more](../../../S3_Cals/Fixture_Simulator.md#Matching).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<bool> | Choose from: ON or 1 - Turns the circuit ON OFF or 0 - Turns the circuit OFF  
<circN> | Circuit Number  
Examples | CALC:FSIM:DRAF:CIRC:STAT ON calculate2:fsimulator:draft:circuit1:state off  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit<circN>:VNA:PORTs <port list>

Applicable Models: All (Read-Write) Sets the VNA ports for the specified
circuit.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<circN> | Circuit Number  
Examples | CALC:FSIM:DRAF:CIRC:VNA:PORT 2 calculate2:fsimulator:draft:circuit2:vna:ports 2  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:CIRCuit[n]:VNA:PORTs?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:FSIMulator:DRAFt:DISCard

Applicable Models: All (Write only) Copies the active fixture into
scratch/draft fixture (discards changes on scratch/draft fixture)  
---  
Parameters | Not applicable  
Example | CALC:FSIM:DRAF:DISC calculate:fsimulator:draft:discard  
Return Type | Not applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>:DELay <value>

Applicable Models: All (Read-Write) Sets and returns the delay value in time
at the specified port. Note: This command affects ALL measurements on the
specified channel.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1.  
<pnum> | Port Number that will receive the delay setting. If unspecified, value is set to 1.  
<value> | The port extension in seconds; may include suffix. Choose a number between: -1E18 and 1E18e.   
Examples | CALC:FSIM:DRAF:EXT:PORT1:DEL 0.02  
calculate:fsimulator:draft:extension:port2:delay .003  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>:DELay?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>:DISTance:UNIT <char>

Applicable Models: All (Read-Write) Sets and returns the units for specifying
port extension delay in physical length (distance).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1.  
<pnum> | Port Number. This number is ignored and all ports have the same setting.  
<char> | Units for delay in distance. Choose from:

  * METer
  * FEET
  * INCH

  
Examples | CALC:FSIM:DRAF:EXT:PORT2:DIST:UNIT MET  
calculate:fsimulator:draft:extension:port3:distance:unit inch  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT:DISTance:UNIT?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | METer  
  
* * *

## CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>:DISTance:VALue
<value>

Applicable Models: All (Read-Write) Sets and returns the port extension delay
in physical length (distance).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1.  
<pnum> | Port Number that will receive the delay setting. If unspecified, value is set to 1.  
<value> | Physical length of fixture of added transmission line. First specify units with :[CALC:FSIM:DRAF:EXT:PORT:DIST:UNIT](FSimulatorDraft.md#ExtPortDistUnit)  
Examples | CALC:FSIM:DRAF:EXT:PORT1:DIST:VAL 12  
calculate:fsimulator:draft:extension:port2:distance:value .003  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>:DISTance:VALue?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>:END

Applicable Models: All (Write Only) Moves the port extension block to the
left-most side of the circuit sections. This command allows the port
extensions to be moved around in the circuit . This command should be executed
after adding the other block. Because adding the block resets the port
extension block position.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1.  
<pnum> | Port Number that will receive the delay setting. If unspecified, value is set to 1.  
Examples | CALC:FSIM:DRAF:EXT:PORT1:END  
calculate:fsimulator:draft:extension:port2:end  
Query Syntax | Not applicable  
Return Type | Not applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>:LOSS<n>:FREQuency
<value>

Applicable Models: All (Read-Write) Sets and returns the frequency for the
Freq and Loss pair number and for the specified port number. [Learn about Loss
Compensation values.](../../../S3_Cals/Port_Extensions.htm#LossCompensation)  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number that will receive the freq/loss settings. If unspecified, value is set to 1.  
<n> | Freq and Loss pair number. Choose from 1 or 2. If unspecified, value is set to 1.  
<value> | Frequency value. Choose a frequency within the frequency span of the VNA.  
Examples | CALC:FSIM:DRAF:EXT:PORT1:LOSS2:FREQ 10E9  
calculate:fsimulator:draft:extension:port2:loss1:frequency 2E10  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>:LOSS<n>:FREQuency?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>:LOSS<n>:VALue <value>

Applicable Models: All (Read-Write) Sets and returns the Loss value for the
specified port number. [Learn about Loss Compensation
values.](../../../S3_Cals/Port_Extensions.htm#LossCompensation) Note: This
command affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number that will receive the Freq/Loss settings. If unspecified, value is set to 1.  
<n> | Loss "Use" number. Choose from 1 or 2. If unspecified, value is set to 1.  
<value> | Loss in dB. Choose a value between -90 and 90  
Examples | CALC:FSIM:DRAF:EXT:PORT:LOSS1:VAL 1 calculate:fsimulator:draft:extension:port2:loss2:value .1  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>:LOSS<n>:VALue?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>:LOSS<n>[:STATe]
<bool>

Applicable Models: All (Read-Write) Sets and returns the ON/OFF state for the
Freq and Loss pair number and for the specified port number. [Learn about Loss
Compensation values.](../../../S3_Cals/Port_Extensions.htm#LossCompensation)
Note: This command affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number that will receive the Freq/Loss settings. If unspecified, value is set to 1.  
<n> | Freq and Loss pair. Choose from 1 or 2. If unspecified, value is set to 1.  
<value> | State of Freq and Loss values for port extension. 0 or OFF Specified Freq and Loss values are OFF 1 or ON Specified Freq and Loss values are ON  
Examples | CALC:FSIM:DRAF:EXT:PORT:LOSS:STAT 0  
calculate:fsimulator:draft:extension:port2:loss2:state on  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>:LOSS<n>:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>:DCLoss:VALue <value>

Applicable Models: All (Read-Write) Sets and returns the Port Loss at DC value
for the specified port number. [Learn about Loss Compensation
values.](../../../S3_Cals/Port_Extensions.htm#LossCompensation) Note: This
command affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port number to receive Loss value. If unspecified, value is set to 1.  
<value> | Loss in dB. Choose a value between -90 and 90  
Examples | CALC:FSIM:DRAF:EXT:PORT:DCL:VAL 1.5 calculate:fsimulator:draft:extension:port2:dcloss:value .1  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>:DCLoss:VALue?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>:MEDium <char>

Applicable Models: All (Read-Write) Sets and returns the media type of the
added fixture or transmission line. See also
[SENS:CORR:EXT:PORT:SYSMedia](../Sense/CorrExtension.md#sysMedia) Note: This
command affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number. This number is ignored and all ports have the same setting.  
<char> | Medium type. Choose from:

  * COAX
  * WAVEguide

  
Examples | CALC:FSIM:DRAF:EXT:PORT:MED COAX calculate:fsimulator:draft:extension:port2:medium waveguide  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>:MEDium?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | COAX  
  
* * *

## CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>:WAVEguide:FCUToff
<value>

Applicable Models: All (Read-Write) Sets and returns the cuttoff (minimum)
frequency of the added waveguide fixture or transmission line.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number for which media type is being set. If unspecified, value is set to 1.  
<value> | Cutoff frequency in Hz. This value is ignored when [CALC:FSIM:DRAF:EXT:PORT:MED](FSimulatorDraft.md#ExtPortMed) is set to COAX for the same port.  
Examples | CALC:FSIM:DRAF:EXT:PORT:WAVE:FCUT 1e8 calculate:fsimulator:draft:extension:port2:waveguide:cutoff 100Mhz  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>:WAVEguide:FCUToff?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | System Media Cutoff Frequency  
  
* * *

## CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>:WAVEguide:COUPle
<bool>

Applicable Models: All (Read-Write) Sets and returns the state of coupling
with the system Velocity Factor value. [Learn
more.](../../../S3_Cals/Port_Extensions.htm#PortDiag) Note: This command
potentially affects ALL measurements on the VNA.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number. This number is ignored and all ports have the same setting.  
<bool> | Coupling state. Choose from:

  * ON (or 1) - Velocity Factor is coupled with the system setting.
  * OFF (or 0) - Velocity Factor is NOT coupled with the system setting.

  
Examples | CALC:FSIM:DRAF:EXT:PORT:WAVE:COUP 1 calculate:fsimulator:draft:extension:port2:waveguide:couple off  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>:WAVEguide:COUPle?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1 or ON (Coupled)  
  
* * *

## CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>:VELocity:FACtor
<value>

Applicable Models: All (Read-Write) Sets and returns the velocity factor of
the fixture or added transmission line.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number for which velocity factor is being set. If unspecified, value is set to 1.  
<value> | Velocity Factor. Set [SENS:CORR:EXT:PORT:SYSV](../Sense/CorrExtension.md#sysVelocity) to use the system velocity factor.  
Examples | CALC:FSIM:DRAF:EXT:PORT:VEL:FAC .6 calculate:fsimulator:draft:extension:port2:velocity:factor 1  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>:VELocity:FACtor?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | System Velocity Factor  
  
* * *

## CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>:VELocity:COUPle
<bool>

Applicable Models: All (Read-Write) Sets and returns the state of coupling
with the system Velocity Factor value. [Learn
more.](../../../S3_Cals/Port_Extensions.htm#PortDiag) Note: This command
potentially affects ALL measurements on the VNA.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number. This number is ignored and all ports have the same setting.  
<bool> | Coupling state. Choose from:

  * ON (or 1) - Velocity Factor is coupled with the system setting.
  * OFF (or 0) - Velocity Factor is NOT coupled with the system setting.

  
Examples | CALC:FSIM:DRAF:EXT:PORT:VEL:COUP 1 calculate:fsimulator:draft:extension:port2:velocity:couple off  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>:VELocity:COUPle?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1 or ON (Coupled)  
  
* * *

## CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>[:STATe] <bool>

Applicable Models: All (Read-Write) Sets and returns the state of port
extension for the specified
port[.](../../../S3_Cals/Port_Extensions.md#PortDiag) Note: This command
potentially affects ALL measurements on the VNA.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<pnum> | Port Number for which port extension is being set. If unspecified, value is set to 1.  
<bool> | Port extension state. Choose from:

  * ON (or 1) - Port extension is on
  * OFF (or 0) - Port extension is off.

  
Examples | CALC:FSIM:DRAF:EXT:PORT:STAT 1 calculate:fsimulator:draft:extension:port2:state off  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:EXTension:PORT<pnum>[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:FSIMulator:DRAFt:SAVE <snpName>

Applicable Models: All (Write only) Saves SNP file corresponding to the entire
scratch/draft fixture.  
---  
Parameters |   
<snpName> | String - snp file name. Appends ".sNp" depending on num ports  
Example | CALC:FSIM:DRAF:SAVE "myFixure" calculate:fsimulator:draft:save "D:\myfixture"  
Return Type | Not applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:SECTion:CIRCuit:ENABle <ON | OFF>

Applicable Models: All (Read-Write) Turns all circuits ON or OFF for all
ports.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<ON | OFFl> | ON (or 1) - turns all circuits ON. OFF (or 0) -turns all circuits OFF.  
Examples | CALC:FSIM:DRAF:SECT:CIRC:ENAB ON calculate2:fsimulator:draft:section:circuit:enable off  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:SECTionCIRCuit:ENABle?  
Return Type | Boolean (1 = ON, 0 = OFF)   
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:SECTion:EXTension:ENABle <ON | OFF>

Applicable Models: All (Read-Write) Turns port extensions ON or OFF for all
ports.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<ON | OFFl> | ON (or 1) - turns port extensions ON. OFF (or 0) - turns port extensions OFF.  
Examples | CALC:FSIM:DRAF:SECT:EXT:ENAB ON calculate2:fsimulator:draft:section:extension:enable off  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:SECTion:EXTension:ENABle?  
Return Type | Boolean (1 = ON, 0 = OFF)   
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:SECTion:ZCONversion:ENABle <ON | OFF>

Applicable Models: All (Read-Write) Turns all ZConversions ON or OFF (both SE
and BAL).  Note: This command affects ALL measurements on the specified
channel.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<ON | OFFl> | ON (or 1) - turns all ZConversions ON. OFF (or 0) - turns all ZConversions OFF.  
Examples | CALC:FSIM:DRAF:SECT:ZCON:ENAB ON calculate2:fsimulator:draft:section:zconversion:enable off  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:SECTion:ZCONversion:ENABle?  
Return Type | Boolean (1 = ON, 0 = OFF)   
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:DIFFerential:STATe <bool>

Applicable Models: All (Read-Write) Sets the differential port impedance
conversion function ON/OFF. Must also set the fixture simulator function to ON
using [CALC:FSIM:STAT.](FSimulator.md#FSimState) See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<bool> | State of the differential port impedance conversion function. Choose from OFF (or 0) Differential port impedance conversion OFF ON (or 1) Differential port impedance conversion ON  
Examples | CALC:FSIM:DRAF:ZCON:DIFF:STAT 1  
calculate2:fsimulator:draft:zconversion:DIFFerential:state off  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:DIFFerential:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:DIFFerential:BPORt<pnum>:COMPLex
<real>,<img>

Applicable Models: All (Read-Write) Sets the complex impedance value for the
differential port impedance conversion function. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<pnum> | Balanced port number. Choose from 1 to 999. Note: See Balanced port versus Logical port.  
<real> | Real part of the Impedance value in Units. Choose a number between 0 and 1E18  
<img> | Imaginary part of the Impedance value in Units. Choose a number between 0 and 1E18.  
Examples | CALC:FSIM:DRAF:ZCON:DIFF:BPOR2:COMPL 200,10  
calculate2:fsimulator:draft:zconversion:differential:bport2:complex 20,3  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:DIFFerential:BPORt<pnum>:COMPlex?  
Return Type | Comma-separated numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0,0  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:DIFFerential:BPORt<pnum>:SCALar
<value>

Applicable Models: All (Read-Write) Sets the real part of impedance value for
the differential port impedance conversion function. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<pnum> | Balanced port number. Choose from 1 to 999. Note: See Balanced port versus Logical port.  
<value> | Real part of the Impedance value in Units. Choose a number between 0 and 1E18  
Examples | CALC:FSIM:DRAF:ZCON:DIFF:BPOR2:SCAL 200,10  
calculate2:fsimulator:draft:zconversion:differential:bport2:scalar 20,3  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:DIFFerential:BPORt<pnum>:SCALer?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:DIFFerential:LPORt<pnum>:COMPLex
<real>,<img>

Applicable Models: All (Read-Write) Sets the complex impedance value for the
differential mode port impedance conversion function. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<pnum> | Logical port number. Choose from 1 to 999. Note: See Balanced port versus Logical port.  
<real> | Real part of the Impedance value in Units. Choose a number between 0 and 1E18  
<img> | Imaginary part of the Impedance value in Units. Choose a number between 0 and 1E18.  
Examples | CALC:FSIM:DRAF:ZCON:DIFF:LPOR2:COMPL 200,10  
calculate2:fsimulator:draft:zconversion:differential:lport2:complex 20,3  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:DIFFerential:LPORt<pnum>:COMPlex?  
Return Type | Comma-separated numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0,0  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:DIFFerential::LPORt<pnum>:SCALar
<value>

Applicable Models: All (Read-Write) Sets the real part of impedance value for
the differential:mode port impedance conversion function. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<pnum> | logical port number. Choose from 1 to 999. Note: See Balanced port versus Logical port.  
<value> | Real part of the Impedance value in Units. Choose a number between 0 and 1E18  
Examples | CALC:FSIM:DRAF:ZCON:COMM:LPOR2:DiFF 200,10  
calculate2:fsimulator:draft:zconversion:differential:lport2:scalar 20,3  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:DIFFerential::LPORt<pnum>:SCALer?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:COMMonmode:STATe <bool>

Applicable Models: All (Read-Write) Sets the common mode port impedance
conversion function ON/OFF. Must also set the fixture simulator function to ON
using [CALC:FSIM:STAT.](FSimulator.md#FSimState) See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<bool> | State of the differential port impedance conversion function. Choose from OFF (or 0) Differential port impedance conversion OFF ON (or 1) Differential port impedance conversion ON  
Examples | CALC:FSIM:DRAF:ZCON:COMM:STAT 1  
calculate2:fsimulator:draft:zconversion:commonmode:state off  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:COMMonmode:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:COMMonmode:BPORt<pnum>:COMPLex
<real>,<img>

Applicable Models: All (Read-Write) Sets the complex impedance value for the
common mode port impedance conversion function. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<pnum> | Balanced port number. Choose from 1 to 999. Note: See Balanced port versus Logical port.  
<real> | Real part of the Impedance value in Units. Choose a number between 0 and 1E18  
<img> | Imaginary part of the Impedance value in Units. Choose a number between 0 and 1E18.  
Examples | CALC:FSIM:DRAF:ZCON:COMM:BPOR2:COMPL 200,10  
calculate2:fsimulator:draft:zconversion:commonmode:bport2:complex 20,3  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:COMMonmode:BPORt<pnum>:COMPlex?  
Return Type | Comma-separated numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0,0  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:COMMonmode:BPORt<pnum>:SCALar
<value>

Applicable Models: All (Read-Write) Sets the real part of impedance value for
the common mode port impedance conversion function. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<pnum> | Balanced port number. Choose from 1 to 999. Note: See Balanced port versus Logical port.  
<value> | Real part of the Impedance value in Units. Choose a number between 0 and 1E18  
Examples | CALC:FSIM:DRAF:ZCON:COMM:BPOR2:SCAL 200  
calculate2:fsimulator:draft:zconversion:commonmode:bport2:scalar 20  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:COMMonmode:BPORt<pnum>:SCALer?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:COMMonmode:LPORt<pnum>:COMPLex
<real>,<img>

Applicable Models: All (Read-Write) Sets the complex impedance value for the
common mode port impedance conversion function. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<pnum> | Logical port number. Choose from 1 to 999. Note: See Balanced port versus Logical port.  
<real> | Real part of the Impedance value in Units. Choose a number between 0 and 1E18  
<img> | Imaginary part of the Impedance value in Units. Choose a number between 0 and 1E18.  
Examples | CALC:FSIM:DRAF:ZCON:COMM:LPOR2:COMPL 200,10  
calculate2:fsimulator:draft:zconversion:commonmode:lport2:complex 20,3  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:COMMonmode:LPORt<pnum>:COMPlex?  
Return Type | Comma-separated numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0,0  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:COMMonmode:LPORt<pnum>:SCALar
<value>

Applicable Models: All (Read-Write) Sets the real part of impedance value for
the common mode port impedance conversion function. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<pnum> | logical port number. Choose from 1 to 999. Note: See Balanced port versus Logical port.  
<value> | Real part of the Impedance value in Units. Choose a number between 0 and 1E18  
Examples | CALC:FSIM:DRAF:ZCON:COMM:LPOR2:SCAL 200  
calculate2:fsimulator:draft:zconversion:commonmode:lport2:scalar 20  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:COMMonmode:LPORt<pnum>:SCALer?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:SENDed:PORT<pnum>:STATe <bool>

Applicable Models: All (Read-Write) Sets the single-ended impedance conversion
function ON/OFF. Must also set the fixture simulator function to ON using
[CALC:FSIM:STAT.](FSimulator.md#FSimState) See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<pnum> | Port number. Choose from 1 to 999.  
<bool> | State of the single-ended port impedance conversion function. Choose from OFF (or 0) single-ended port impedance conversion OFF ON (or 1) single-ended port impedance conversion ON  
Examples | CALC:FSIM:DRAF:ZCON:SEND:PORT3:STAT 1  
calculate2:fsimulator:draft:zconversion:sended:port2:state off  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:SENDed:PORT:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:SENDed:PORTpnum>:COMPLex
<real>,<img>

Applicable Models: All (Read-Write) Sets the complex impedance value for the
single-ended port impedance conversion function. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<pnum> | Pport number. Choose from 1 to 999.  
<real> | Real part of the Impedance value in Units. Choose a number between 0 and 1E18  
<img> | Imaginary part of the Impedance value in Units. Choose a number between 0 and 1E18.  
Examples | CALC:FSIM:DRAF:ZCON:SEND:POR2:COMPL 200,10  
calculate2:fsimulator:draft:zconversion:sended:port2:complex 20,3  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:SENDed:PORT<pnum>:COMPlex?  
Return Type | Comma-separated numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0,0  
  
* * *

CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:SENDed:PORT<pnum>:SCALer <val>

Applicable Models: All (Read-Write) Sets the real part of impedance value for
the single-ended port impedance conversion function. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<pnum> | Pport number. Choose from 1 to 999.  
<val> | Real part of the Impedance value in Units. Choose a number between 0 and 1E18  
Examples | CALC:FSIM:DRAF:ZCON:SEND:PORT:SCAL 0  
calculate2:fsimulator:draft:zconversion:sended:port2:scalar 20,3  
Query Syntax | CALCulate<cnum>:FSIMulator:DRAFt:ZCONversion:SENDed:PORT<pnum>:SCALer?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

