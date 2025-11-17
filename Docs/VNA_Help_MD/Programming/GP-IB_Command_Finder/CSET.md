# CSET Commands

* * *

Manages several aspects of Cal Sets.

CSET: | [CATalog?](CSET.md#CAT) | COPY | [DALL](CSET.md#DALL) | [DATE?](CSET.md#Date) | [DELete](CSET.md#delete) | [EXISts?](CSET.md#Exists) | ETERm: | CATalog? | [:DATA] | FORMat? | LEAKage | CATalog? | REMove | X:VALues | FIXTure: | [CASCade](CSET.md#FIXTureCASCade) | [CHARacterize](CSET.md#fixtureCharacter) | [DEEMbed](CSET.md#deembed) | [EMBed](CSET.md#embed) | ENR:EMBed | REVerse | ZERO | FREQuency  
| [BWIDth](CSET.md#FreqBwid) | [CONVeter](CSET.md#FreqConv) | [SEGMent](CSET.md#FreqSegm) | [SWEPT](CSET.md#FreqSwept) | ITEM: | CATalog? | DATA? | PROPerties | [CATalog](CSET.md#Prop:Cat) | DELay? | DELay:PAIRs? | [PATH:CONFig:CATalog](CSET.md#PropPathConfCat) | [POINts](CSET.md#PropPoin) | PORT | [ATTENuation](CSET.md#PropPortAtten) | [CATalog](CSET.md#PropPortCat) | [GAIN](CSET.md#PropPortGain) | [POWer](CSET.md#PropPortPow) | [SECurity:LEVel](CSET.md#PropSecLev) | SWEep | [MODE](CSET.md#PropSweMode) | [TYPE](CSET.md#PropSweType) | STANdard | CATalog? | [:DATA] | X:VALues | [TIME?](CSET.md#time) | VALidate?  
---  
  
Click on a keyword to view the command details.

Note: There is no user-interface equivalent for some of these commands.

See Also

  * [Example Programs](../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## CSET:CATalog?

Applicable Models: All This command replaces
[SENS:CORR:CSET:CAT?](Sense/CorrCset.md#catalog) (Read-only) Returns the
names of Cal Sets stored on the VNA.  
---  
Parameters |  None  
Examples |  CSET:CAT? Returns: "CalSet_0913,CalSet_1,CalSet_2,CalSet_3,CalSet_4,CH1_CALREG,CH31_CALR EG,MyCalAll_SMC_002,MyCalAll_STD_001"  
Return Type |  Comma-separated string of names  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:COPY <string>,<string>

Applicable Models: All (Write-only) Creates a new Cal Set and copies the
current Cal Set data into it. Use this command to manipulate data on a Cal Set
without corrupting the original cal data.  
---  
Parameters |   
<string>,<string> |  The first string is the name of the current Cal Set. The second string is the name of the new Cal Set copy.  
Examples |  CSET:COPY 'My2Port','My2PortCopy'  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:DALL

Applicable Models: All (Write-only) Deletes ALL Cal Sets from the VNA,
including phase reference and Global Delta Match Cal Sets.  
---  
Parameters |  None  
Examples |  CSET:DALL  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:DATE? <string>

Applicable Models: All (Read-only) Returns the (year, month, day) that the
specified Cal Set was last saved.

### See Also

[MMEM:DATE?](Memory.md#Date) [MMEM:TIME?](Memory.md#Time)
[CSET:TIME?](CSET.md#time)  
---  
Parameters |   
<string> |  Cal Set name.  
Examples |  CSET:DATE? "CalSet_11" 'Returns: +2013,+5,+1  
Return Type |  Comma-separated integers.  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:DELete <string>

Applicable Models: All This command replaces
[SENS:CORR:CSET:DELete](Sense/CorrCset.md#delete) (Write-only) Deletes the
specified Cal Set from the VNA.

  * If the Cal Set is currently being used by a channel, the Cal Set is deleted and correction for the channel is turned off.
  * If the Cal Set is not found, no error is returned.

  
---  
Parameters |   
<string> |  Name of the Cal Set to delete. Not case-sensitive.  
Examples |  CSET:DEL "MyCalSet"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:EXISts? <string>

Applicable Models: All (Read-only) Returns whether or not the specified Cal
Set exists on the VNA.  
---  
Parameters |   
<string> |  Name or GUID of the Cal Set enclosed in quotes. The GUID must also be enclosed in curly brackets.  
Examples |  dim check check = CSET:EXISts? "MyCalSet" check = CSET:EXISts? "{7C4EEA5E-40D2-4D70-A048-33BFFE704163}"  
Return Type |  Boolean ON or 1 \- Cal Set exists. OFF or 0 \- Cal Set does NOT exist.  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:ETERm:CATalog? <CSET Name>[,<errorTermFilter>]

Applicable Models: All (Read-only) Returns a list of error term names for the
given Cal Set.  
---  
Parameters |   
<CSET Name> |  (String) Name of Cal Set to query.  
<errorTermFilter> |  **(Optional argument) CSET:ETER:CAT? <CSETName>, <errorTermFilter>** will return only the error term names with the filter string in them. For example, if it is a full 2-port cal, then **CSET:ETER:CAT? <CSETName>, cross** would return all Crosstalk(n,n) error terms. (Note that the filter is not case sensitive.) Entering CSET:ETER:CAT? <CSETName> "" or CSET:ETER:CAT? <CSETName> will return all error terms for the given Cal Set.  
Examples |  CSET:ETER:CAT? "CalSet_1" CSET:ETER:CAT? "CalSet_1", "trans"  
Return Type |  Variant  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:ETERm[:DATA] <CSET Name>,<ETerm Name>,<data>

Applicable Models: All (Read-Write) Sets and returns the error term data
(real, imaginary pairs) for the given Cal Set and error term name.  
---  
Parameters |   
<CSET Name> |  (String) Name of Cal Set to manipulate.  
<ETerm Name> |  (String) Name used to identify an error term in the Cal Set.  
<data> |  (Block) Error term data - a real/imaginary data pair for each data point.  
Examples |  CSET:ETER "CalSet_1","Directivity(1,1)", 0.237,-1.422, 0.513, 0.895  
CSET:ETER? "CalSet_1","Directivity(1,1)" 'read  
Query Syntax |  CSET:ETERm:DATA? <CSET Name>,<ETerm Name>  
Return Type |  Block data  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:ETERm:FORMat? <term name>,<rcv port>,<src port>[,<rcvPort
gainstate>][,<srcPort gainstate>]

Applicable Models: All (Read-only) Returns switched gain error terms. Switched
gain error terms have a suffix on the term name to identify the receiver gain
states that apply to the term. For example:

  * TransmissionTracking(2,1)
  * TransmissionTracking(2,1)[0,1]
  * TransmissionTracking(2,1)[1,0]
  * TransmissionTracking(2,1)[1,1]

  
---  
Parameters |   
<term name> |  (String) Name used to identify an error term.  
<rcv port> |  Receiver port number.  
<src port> |  Source port number.  
<rcvPort gainstate> |  Receiver port gain state.  
<srcPort gainstate> |  Source port gain state.  
Examples |  CSET:ETER:FORM? "TransmissionTracking",2,1,0,0 CSET:ETER:FORM? "TransmissionTracking",2,1,0,1 CSET:ETER:FORM? "TransmissionTracking",2,1,1,0 CSET:ETER:FORM? "TransmissionTracking",2,1,1,1  
Return Type |  Variant  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:ETERm:LEAKage:CATalog? <CSetName>

Applicable Models: All (Read-only) Returns a comma-separated string containing
the leaky coefficients named LeakageAA, :LeakageAB, LeakageBA, LeakageBB  
---  
Parameters |   
<CSetName> |  (String) Name of Cal Set to query.  
Examples |  CSET:ETER:LEAK:CAT? "MyCalSet"  
Return Type |  String. Example "LeakageAA(1,1), LeakageAA(2,1) ......., LeakageBB(2,1), :LeakageBB(2,2)"  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:ETERm:LEAKage:REMove <CSET Name>

Applicable Models: All (Write-only) Removes all leaky terms from calset  
---  
Parameters |   
<CSET Name> |  (String) Name of Cal Set to query.  
Examples |  CSET:ETER:LEAK:REM "MyCalSet"  
Return Type |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:ETERm:X:VALues <CSET Name>,<ETerm Name>,<freqlist>

Applicable Models: All (Read-Write) Sets and returns the x-axis frequencies
for the given Cal Set and error term name. **_This command requires that the
error term already be in existence either from a calibration session or having
been created withCSET:ETER:DATA._** **_T his command requires that the
frequency array length match the existing size of the error term. For
example_**** _, if the error term is 3 buckets long (3 complex numbers), then
the frequency list must be 3 values long._**  
---  
Parameters |   
<CSET Name> |  (String) Name of Cal Set to manipulate.  
<ETerm Name> |  (String) Name used to identify an error term in the Cal Set.  
<freqlist> |  (Block) X-axis frequencies associated with the error term.  
Examples |  'Query error term data from calset named "Calset1"  
CSET:ETER:DATA? "Calset7","Directivity(1,1)" 'If needed, change or upload the
data for the "Directivity" error term (example of a three point eterm)  
CSET:ETER:DATA
"Calset7","Directivity(1,1)",-3.86251918972E-002,+5.34659661353E-002,+2.90613174438E-002,-2.16645095497E-002,-1.38868670911E-003,+3.30922640860E-002
'Query what the frequency values are for the error term  
CSET:ETER:X:VAL? "Calset7","Directivity(1,1)" 'If needed, change the frequency
values for the error term  
CSET:ETER:X:VAL
"Calset7","Directivity(1,1)",1.00000000000E+007,1.42450000000E+008,2.74900000000E+008  
Query Syntax |  CSET:ETERm:X:VALues? <CSET Name>,<ETerm Name>  
Return Type |  Block data  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:FIXTure:CASCade <s2p1>,<s2p2>,<s2pResult>,<char>

Applicable Models: All (Write-only) Combines the losses and phase shift of two
S2P files into a single S2P file. [Learn
more.](../../S3_Cals/Cal_Plane_Manager.htm#Cascade)  
---  
Parameters |   
<s2p1> |  (String) Path and filename of one of the S2P files to be combined.  
<s2p2> |  (String) Path and filename of the other S2P file to be combined.  
<s2pResult> |  (String) Path and filename of the combined S2P file.  
<char> |  (Character) Format. Choose from:

  * REIM - Real, imaginary data pairs
  * LOG - Log magnitude, phase
  * LINear - Linear magnitude, phase

  
Examples |  CSET:FIXT:CASC "D:\a.s2p","D:\b.s2p","D:\c.s2p",LOG  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:FIXTure:CHARacterize <cs1>,<cs2>,<port>,<s2p>,<char>[,<phase pivot>]

Applicable Models: All (Write-only) Characterizes a fixture based on two Cal
Sets. The stimulus settings of the two Cal Sets do NOT have to be identical,
but they MUST have a common frequency range for interpolation. A new S2P file
is created. [Learn more about Cal Plane
Manager.](../../S3_Cals/Cal_Plane_Manager.htm)  
---  
Parameters |   
<cs1> |  (String) Name of an existing Cal Set 1 which describes the cal closest to the VNA. The Cal Set must reside on the VNA.  
<cs2> |  (String) Name of an existing Cal Set 2 which describes the cal closest to the DUT. The Cal Set must reside on the VNA.  
<port> |  (Numeric) Port number described in the Cal Sets.  
<s2p> |  (String) Name of the S2P file containing the adapter/fixture characterization.  
<char> |  (Character) Choose the data format for the resulting s2p file:

  * REIM - Real, imaginary data pairs
  * LOG - Log magnitude, phase
  * LINear - Linear magnitude, phase

  
[<phase pivot>] |  (Numeric) Optional argument. The phase pivot point specifies the center of the phase window. It is normally 1 Pi wide. The default value of 0° should be adequate for the majority of adapters. [Learn more](../../S3_Cals/Cal_Plane_Manager.md#Phase).  
Examples |  CSET:FIXT:CHAR "CalSet1","CalSet2",1,"Fixture.s2p",REIM cset:fixture:characterize "CalSet1","CalSet2",2,"Fixture.s2p",LOG,90  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:FIXTure:DEEMbed <cs1>,<cs2>,<s2p>,<port>, <compPwr>[,extrap]

Applicable Models: All (Write-only) De-embeds a fixture from an existing Cal
Set based on an S2P file. A new Cal Set is created with the effects of the
fixture removed.  When the new Cal Set is applied to a channel, the effects of
fixturing are removed from the measurement data. Do NOT enable fixturing. The
effects of the fixture are removed when the new Cal Set is selected and
correction is turned ON.  
---  
Parameters |   
<cs1> |  (String) Name of an existing Cal Set which resides on the VNA.  
<cs2> |  (String) Name of new Cal Set which contains updated error terms with fixture de-embedded.  
<s2p> |  (String) Name of the S2P file which characterizes the adapter/fixture.  
<port> |  (Numeric) Port number from which fixture will be de-embedded.  
<compPwr> |  (Boolean) ON (1) \- When the Cal Set contains a power correction array for the fixture port, that array will be compensated for the fixture loss.  Warning: enabling power compensation can result in an increase in test port power and consequently, increased power to the DUT. Use with caution. OFF (0) \- Do not compensate for loss in source power through the fixture.  
[extrap] |  (Boolean) Optional argument. ON (1) -Applies a simple extrapolation when the S2P file has a narrower frequency range than the Cal Set. The values for the first and last data points are extended in either direction to cover the frequency range of the Cal Set. OFF (0) \- Extrapolation is NOT performed (default setting).  
Examples |  CSET:FIXT:DEEM "MyCalSet","MyNewCalSet","Fixture.s2p",1,1 cset:fixture:deembed "MyCalSet","MyNewCalSet","Fixture.s2p",1,1,1 'extrapolation is performed if the s2p frequency range is narrower than that of the Cal Set.  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:FIXTure:EMBed <cs1>,<cs2>,<s2p>,<port>, <compPwr>[,extrap]

Applicable Models: All (Write-only) Embeds a fixture (usually a matching
network) into an existing Cal Set based on an S2P file. A new Cal Set is
created with the effects of the matching network included in the correction
data.  When the new Cal Set is applied to a channel, the effects of the
fixture are included in the measurement data. Do NOT enable fixturing. The
effects of the matching network are included when the new Cal Set is selected
and correction is turned ON.  
---  
Parameters |   
<cs1> |  (String) Name of an existing Cal Set which resides on the VNA.  
<cs2> |  (String) Name of new Cal Set which contains updated error terms with fixture embedded.  
<s2p> |  (String) Name of the S2P file which characterizes the fixture / matching network.  
<port> |  (Numeric) Port number to which fixture will be added.  
<compPwr> |  (Boolean) ON (1) \- Increase the source power to compensate for the loss through the fixture. The result is that the specified power level will be correct at the DUT input. Warning: enabling power compensation can result in an increase in test port power and consequently, increased power to the DUT. Use with caution. OFF (0) \- Do not compensate for loss in source power through the matching network.  
[extrap] |  (Boolean) Optional argument. ON (1) -Applies a simple extrapolation when the S2P file has a narrower frequency range than the Cal Set. The values for the first and last data points are extended in either direction to cover the frequency range of the Cal Set. OFF (0) \- Extrapolation is NOT performed (default setting).  
Examples |  CSET:FIXT:EMB "MyCalSet","MyNewCalSet","Fixture.s2p",1,1 cset:fixture:embed "MyCalSet","MyNewCalSet","Fixture.s2p",1,1,1 'extrapolation is performed if the s2p frequency range is narrower than that of the Cal Set.  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:FIXTure:ENR:EMBed <inEnr>,<s2p>,<outEnr>

Applicable Models: All (Write-only) Generate a new ENR file by embedding an
adapter to an existing ENR file.  
---  
Parameters |   
<inEnr> |  (String) Path and filename of original ENR file.  
<s2p> |  (String) Path and filename of the S2P file which characterizes the adapter/fixture network.  
<outEnr> |  (String) Path and filename of new ENR file to output  
Examples |  CSET:FIXT:EMB "D:\Original.enr","D:\adapter.s2p","D:\new.enr"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:FIXTure:REVerse <s2pInput>, <s2pResult>,<char>

Applicable Models: All (Write-only) Reverses the fixture ports of s2p1 to the
new output s2p2. [Learn more](../../S3_Cals/Cal_Plane_Manager.md#Reverse).  
---  
Parameters |   
<s2pInput> |  (String) Path and filename of the original S2P file.  
<s2pResult> |  (String) Path and filename of the resulting S2P file with ports reversed.  
<char> |  (Character) Format. Choose from:

  * REIM - Real, imaginary data pairs
  * LOG - Log magnitude, phase
  * LIN - Linear magnitude, phase

  
Examples |  CSET:FIXT:REV "D:\a.s2p","D:\b.s2p",LOG  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:FIXTure:ZERO<original_sNp>,<result_sNp>,<sparameters>,<complexformat>

Applicable Models: All (Write-only) Creates a new SNP file.  
---  
Parameters |   
<original_s4p> |  (String) Path and filename of the original SNP file.  
<result_s4p> |  (String) Path and filename of the new SNP file.  
<sparameters> |  (String) Comma-separated terms to zero-out.  
<complexformat> |  (Character) Format. Choose from:

  * REIM - Real, imaginary data pairs
  * LOG - Log magnitude, phase
  * LIN - Linear magnitude, phase

  
Examples |  CSET:FIXT:ZERO "D:\originalFile.s4p","D:\newFile.s4p","S11,S21,S33",LOG CSET:FIXT:ZERO D:\original.s2p,D:\new.s2p,S11,REIM  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:FREQuency:BWIDth? <calset>

Applicable Models: All (Read-only) Returns the IF Bandwidth value for the
specified Cal Set  
---  
Parameters |   
<calset> |  (String) Name of the Cal Set item.  
Examples |  CSET:FREQ:BWID? "mycalset"  
Return Type |  double  
Query Syntax |  CSET:FREQuency:BWIDth?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:FREQuency:CONVerter? <calset>,<ConvFreq>,<qualifier>

Applicable Models: All (Read-only) Returns a specified start or stop frequency
for converter/mixer Cal Sets  
---  
Parameters |   
<calset> |  (String) Name of the Cal Set item.  
<convFreq> |  (Enum) INPut, OUTPut, LO1 or LO2  
<qualifier> |  (Enum) STARt or STOP  
Examples |  CSET:FREQ:CONV? "mycalset",LO1,STARt  
Return Type |  double  
Query Syntax |  CSET:FREQuency:CONVerter? <calset>,<ConvFreq>,<qualifier>  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:FREQuency:SEGMent? <calset>,<qualifier>

Applicable Models: All (Read-only) Returns a comma separated list of doubles
with all the start or stop values for the frequency segments  
---  
Parameters |   
<calset> |  (String) Name of the Cal Set item.  
<qualifier> |  (Enum) STARt or STOP  
Examples |  CSET:FREQ:SEGM? "mycalset",STARt  
Return Type |  comma separated list of doubles  
Query Syntax |  CSET:FREQuency:SEGMent? <calset>,<Type>  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:FREQuency:SWEPT? <calset>,<qualifier>

Applicable Models: All (Read-only) Returns either the start or stop swept
frequency for the specified Cal Set  
---  
Parameters |   
<calset> |  (String) Name of the Cal Set item.  
<qualifier> |  (Enum) STARt or STOP  
Examples |  CSET:FREQ:SWEPT? "mycalset",STARt  
Return Type |  double  
Query Syntax |  CSET:FREQuency:SWEPT? <calset>,<Type>  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:ITEM:CATalog? <calset>

Applicable Models: All (Read-only) The Cal Set mainly contains error term data
for measurement correction purposes. But Cal Sets can also contain auxiliary
information used to describe how the Cal Set was constructed. This information
is stored as name value pairs and can be accessed by the item name. The
catalog query returns a list of item names contained in the specific Cal Set
being queried.  
---  
Parameters |   
<calset> |  (String) Name of the Cal Set item.  
Examples |  CSET:ITEM:CAT? "mycalset"  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:ITEM:DATA? <calset>,<itemName>

Applicable Models: All (Read-Write) Returns the VNA Measurement Class or
Channel that created the specific Cal Set item.

### About Cal Set Items

A Cal Set item is a named value. You can list the named values using
CSET:ITEM:CATalog? or SENS:CORR:CSET:ITEM:CATalog? You can query the value of
a specific item by asking for its data: CSET:ITEM:DATA? For example, one of
the items added by the VNA firmware to every Cal Set is named 'Created By'.
The value attached to this item is the name of the VNA Measurement Class or
Channel that created the Cal Set. When an SMC cal is performed, you can query
the Cal Set for the 'Create By' item, and it will return 'Scalar
Mixer/Converter'. The same query on an NFx channel returns 'Noise Figure
Converters'. CSET:ITEM:DATA? "mycalset","Created By"  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<calset> |  (String) Name of the Cal Set item.  
<itemName> |  (String) VNA Measurement Class or Channel that created the Cal Set.  
Examples |  CSET:ITEM:DATA? "mycalset","Created By"  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:PROPerties:CATalog? <calset>

Applicable Models: All (Read-only) Returns a list of property values that can
be queried for the specified Cal Set.  
---  
Parameters |   
<calset> |  (String) Name of the Cal Set item.  
Examples |  CSET:PROP:CAT? "mycalset"  
Return Type |  string of comma separated values, (Example: "Start Freq,Stop Freq,Number of Points,IF Bandwidth,Sweep Type,Sweep Mode,Number of Calibrated Ports,Power Calibration Status,Port Power,Port Attenuation or Gain,Mechanical Switches,VNA Security Level")  
Query Syntax |  CSET:PROPerties:CATalog? <calset>  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:PROPerties:DELay? <calset>

Applicable Models: All (Read-only) Returns the list of port pairs with
computed adapter delays for the specified Cal Set.  
---  
Parameters |   
<calset> |  (String) Name of the Cal Set item.  
Examples |  CSET:PROP:DEL? "mycalset"  
Return Type |  String  
Query Syntax |  CSET:PROPerties:DELay? <calset>  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:PROPerties:DELay:PAIRs? <calset>,<portPair>

Applicable Models: All (Read-only) Returns the computed adapter delay for the
specified port pair for the specified Cal Set.  
---  
Parameters |   
<calset> |  (String) Name of the Cal Set item.  
<portPair> |  (String) Specified port pair.  
Examples |  CSET:PROP:DEL:PAIR? "mycalset","1-3"  
Return Type |  String  
Query Syntax |  CSET:PROPerties:DELay:PAIRs? <calset>,<portPair>  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:PROPerties:PATH:CONFig:CATalog? <calset>

Applicable Models: N522xB, N524xB (Read-only) Returns a list of mechanical
switches for specified Cal Set  
---  
Parameters |   
<calset> |  (String) Name of the Cal Set item.  
Examples |  CSET:PROP:PATH:CONF:CAT? "mycalset"  
Return Type |  String  
Query Syntax |  CSET:PROPerties:PATH:CONFig:CATalog? <calset>  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:PROPerties:POINts? <calset>

Applicable Models: All (Read-only) Returns the number of frequency points  
---  
Parameters |   
<calset> |  (String) Name of the Cal Set item.  
Examples |  CSET:PROP:POIN? "mycalset"  
Return Type |  Integer  
Query Syntax |  CSET:PROPerties:POINts? <calset>  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:PROPerties:PORT:ATTENuation? <calset>, <att>

Applicable Models: All (Read-only) Returns a comma separated list of doubles
holding the power value for every calibrated port. The index of attenuator
algins with the index of port list  Example: CSET:PROP:PORTS:LIST? 'CalSet_2'
returns 1, 3, 5 CSET:PROP:PORTS:ATTEN? 'CalSet_2',SOUR returns 15.00, 10.00,
5.00 Then, 15.00 is for port 1, 10.00 is for port 3 and 5.00 is for port 5  
---  
Parameters |   
<calset> |  (String) Name of the Cal Set item.  
<att> |  (Enum) SOURce or RECeiver  
Examples |  CSET:PROP:PORT:LIST? "mycalset",SOUR  
Return Type |  comma separated list of doubles  
Query Syntax |  CSET:PROPerties:PORT:ATTENuation? <calset>,<att>  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:PROPerties:PORT:CATalog? <calset>

Applicable Models: All (Read-only) Returns a comma separated list of integers
holding the calibrated port numbers - ie 1, 3, 5  
---  
Parameters |   
<calset> |  (String) Name of the Cal Set item.  
Examples |  CSET:PROP:PORT:CAT? "mycalset"  
Return Type |  comma separated list of long (integers)  
Query Syntax |  CSET:PROPerties:PORT:CATalog? <calset>  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:PROPerties:PORT:GAIN? <calset>

Applicable Models: All (Read-only) Returns a comma separated list of strings
holding the gain value for every calibrated port. The index of gain algins
with the index of port list. The possible values for gain are High if
receiver gain was fixed to high, Low if fixed to low, Mixed if gain is
fixed by varies by segment and High and Low if gain is Auto or varies by
source port.  CSET:PROP:PORTS:LIST? 'CalSet_2' returns 1, 3, 5
CSET:PROP:PORTS:GAIN?CalSet_2' returns "High,Low,High and Low" Then, High is
for port 1, Low for port 3 and Auto for port 5  
---  
Parameters |   
<calset> |  (String) Name of the Cal Set item.  
Examples |  CSET:PROP:PORT:LIST? "mycalset"  
Return Type |  comma separated list of strings  
Query Syntax |  CSET:PROPerties:PORT:GAIN? <calset>  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:PROPerties:PORT:POWer? <calset>

Applicable Models: All (Read-only) Returns a comma separated list of doubles
holding the power value for every calibrated port. The index of power vector
algins with the index of port list  Example: CSET:PROP:PORTS:LIST? 'CalSet_2'
returns 1, 3, 5 CSET:PROP:PORTS:POW?CalSet_2' returns 15.00, 10.00, 13.00
Then, 15.00 is for port 1, 10.00 is for port 3 and 13.00 is for port 5  
---  
Parameters |   
<calset> |  (String) Name of the Cal Set item.  
Examples |  CSET:PROP:PORT:POW? "mycalset"  
Return Type |  comma separated list of doubles  
Query Syntax |  CSET:PROPerties:PORT:POW? <calset>  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:PROPerties:SECurity:LEVel? <calset>

Applicable Models: All (Read-only) Returns the security level associated with
the specified Cal Set  
---  
Parameters |   
<calset> |  (String) Name of the Cal Set item.  
Examples |  CSET:PROP:SEC:LEV? "mycalset"  
Return Type |  enum (NONE, LOW, HIGH or EXTR)  
Query Syntax |  CSET:PROPerties:SECurity:LELel? <calset>  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:PROPerties:SWEep:MODE? <calset>

Applicable Models: All (Read-only) Returns the sweep mode for the specified
Cal Set  
---  
Parameters |   
<calset> |  (String) Name of the Cal Set item.  
Examples |  CSET:PROP:SWE:MODE? "mycalset"  
Return Type |  enum (STEP or ANAL)  
Query Syntax |  CSET:PROPerties:SWEep:MODE? <calset>  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:PROPerties:SWEep:TYPE? <calset>

Applicable Models: All (Read-only) Returns the sweep type for the specified
Cal Set  
---  
Parameters |   
<calset> |  (String) Name of the Cal Set item.  
Examples |  CSET:PROP:SWE:TYPE? "mycalset"  
Return Type |  enum (LIN, LOG, POW, CW. SEGM or PHAS)  
Query Syntax |  CSET:PROPerties:SWEep:TYPE? <calset>  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:STANdard:CATalog? <CSET Name>[,<standardFilter>]

Applicable Models: All (Read-only) Returns a list of standard data for the
given Cal Set.  
---  
Parameters |   
<CSET Name> |  (String) Name of Cal Set to query.  
<standardFilter> |  (Optional argument) CSET:ETER:CAT? <CSETName>, <standardFilter> will return only the standard names with the filter string in them. For example, if it is a full 2-port cal, then CSET:STAN:CAT? <CSETName>, SA would return all SA_x(n,n) standard data. (Note that the filter is not case sensitive.)  
Entering CSET:STAN:CAT? <CSETName> "" or CSET:STAN:CAT? <CSETName> will return
all standard data for the given Cal Set.  
Examples |  CSET:STAN:CAT? "CalSet_1" CSET:STAN:CAT? "CalSet_1", "SA"  
Return Type |  Variant  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:STANdard[:DATA] <CSET Name>,<Standard Name>,<data>

Applicable Models: All (Read-Write) Sets and returns the standard data (real,
imaginary pairs) for the given Cal Set and error term name.  
---  
Parameters |   
<CSET Name> |  (String) Name of Cal Set to manipulate.  
<Standard Name> |  (String) Name used to identify standard data term in the Cal Set.  
<data> |  (Block) Standard data - a real/imaginary data pair for each data point.  
Examples |  CSET:STAN "CalSet_1","SA_0(1,1)", 0.237,-1.422, 0.513, 0.895  
CSET:STAN? "CalSet_1","SA_0(1,1)" 'read  
Query Syntax |  CSET:STANdard:DATA? <CSET Name>,<Standard Name>  
Return Type |  Block data  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:STANdard:X:VALues <CSET Name>,<Standard Name>,<freqlist>

Applicable Models: All (Read-Write) Sets and returns the x-axis frequencies
for the given Cal Set and standard data name. This command requires that the
standard data already be in existence either from a calibration session or
having been created with** _CSET:STAN:DATA._** **_T his command requires that
the frequency array length match the existing size of the standard term. For
example, if the standard term is 3 buckets long (3 complex numbers), then the
frequency list must be 3 values long_**** _._**  
---  
Parameters |   
<CSET Name> |  (String) Name of Cal Set to manipulate.  
<ETerm Name> |  (String) Name used to identify a standard data term in the Cal Set.  
<freqlist> |  (Block) X-axis frequencies associated with the standard data.  
Examples |  'Query standard term data from calset named "Calset7"  
CSET:STAN:DATA? "Calset7","SA_0(1,1)" 'If needed, change or upload the data
for the "SA_0(1,1)" standard (example of a three point standard)  
CSET:STAN:DATA
"Calset7","SA_0(1,1)",-3.86251918972E-002,+5.34659661353E-002,+2.90613174438E-002,-2.16645095497E-002,-1.38868670911E-003,+3.30922640860E-002
'Query what the frequency values are for the standard  
CSET:STAN:X:VAL? "Calset7","SA_0(1,1)" 'If needed, change the frequency values
for the standard  
CSET:STAN:X:VAL
"Calset7","SA_0(1,1)",1.00000000000E+007,1.42450000000E+008,2.74900000000E+008  
Query Syntax |  CSET:STANdard:X:VALues? <CSET Name>,<Standard Name>  
Return Type |  Block data  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:TIME? <calset>

Applicable Models: All (Read-only) Returns the (hour, minute, second) that the
specified Cal Set was last saved. The time is returned in local time as setup
in the VNA operating system.

### See Also

[CSET:DATE?](CSET.md#Date) [MMEM:DATE?](Memory.md#Date)
[MMEM:TIME?](Memory.md#Time)  
---  
Parameters |   
<calset> |  Cal Set name.  
Examples |  CSET:TIME? "CalSet_11" 'Returns: +13,+6,+1  
Return Type |  Comma-separated integers.  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## CSET:VALidate? <calset>,<channel>

Applicable Models: All (Read-only) This query compares the stimulus of
"chanNumber" (<channel>) with the stimulus stored in the specified calset.  
---  
Parameters |   
<calset> |  (String) Name of the Cal Set item.  
<channel> |  (Integer) Any existing channel number.  
Examples |  CSET:VALidate? "CalSet_11",2  
Return Type |  Enumeration: EQUal \- Calset stimulus matches the channel stimulus. DELTa \- Calset can be used, but differs in some property that is not related to the xAxis. XAXis \- Calset can be used but will be "interpolated": interpolated data maybe computed or just decimated based on the alignment. REStore \- Calset could be used but requires restoring the calibration stimulus stored in the calset. REJect \- Calset is rejected (calset not recognized or was created by an incompatible channel). POWer \- Only power values are different between calset stimulus and channel stimulus.  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

