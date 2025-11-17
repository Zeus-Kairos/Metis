# Sense:Correction:Collect:Ckit Commands

* * *

Use to change the definitions of calibration kit standards.

SENSe:CORRection:COLLect:CKIT: | [CATalog?](CorrCollCKIT.md#ckitCat) | [CLISt](CorrCollCKIT.md#ckitClist) | [CLABel](CorrCollCKIT.md#ckitClabel) | CONNector | [ADD](CorrCollCKIT.md#add) | [CATalog?](CorrCollCKIT.md#cat) | [DELete](CorrCollCKIT.md#delete) | [FNAMe](CorrCollCKIT.md#Fname) | [SNAMe](CorrCollCKIT.md#sname) | [DESCription](CorrCollCKIT.md#desc) | [INFormation?](CorrCollCKIT.md#Inf) | [NAME](CorrCollCKIT.md#scccn) | [OLAB](CorrCollCKIT.md#olab) | [OLISt?](CorrCollCKIT.md#olist) | [ORDer](CorrCollCKIT.md#sccco) | [PORT[:SELect]](CorrCollCKIT.md#ckitPortSelect) | [RESet](CorrCollCKIT.md#scccr) | [SELect](CorrCollCKIT.md#scccs) | STANdard | [CO, C1, C2, C3](CorrCollCKIT.md#c0) | [CHARacter](CorrCollCKIT.md#sc) | DATA | LOAD | [DELay](CorrCollCKIT.md#sd) | [FMAXimum](CorrCollCKIT.md#sfx) | [FMINimum](CorrCollCKIT.md#sfn) | [IMPedance](CorrCollCKIT.md#si) | [LO, L1, L2, L3](CorrCollCKIT.md#l0) | [LABel](CorrCollCKIT.md#sl) | [LOSS](CorrCollCKIT.md#sls) | [REMove](CorrCollCKIT.md#delete) | [SDEScription](CorrCollCKIT.md#sdes) | [[SELect]](CorrCollCKIT.md#ss) | [TYPE](CorrCollCKIT.md#st) | [TZReal](CorrCollCKIT.md#TZReal) | [TZImag](CorrCollCKIT.md#TZImag) | TRLoption | [IMPedance](CorrCollCKIT.md#TRLImpedance) | [LRLChar](CorrCollCKIT.md#TRLLRLChar) | [RPLane](CorrCollCKIT.md#TRLRplane)  
---  
  
Click on a keyword to view the command details.

Blue keywords are superseded commands.

Most of these commands act on the currently selected standard from the
currently selected calibration kit.

  * To select a Calibration kit, use [SENS:CORR:COLL:CKIT:SEL](CorrCollCKIT.md#scccs).

  * To select a Calibration standard, use [SENS:CORR:COLL:CKIT:STAN:SEL](CorrCollCKIT.md#ss)

  * See an example program that [CREATES a New Cal Kit](../../GPIB_Example_Programs/Create_New_Cal_Kit_using_SCPI.md)

  * See an example program that [MODIFIES an Existing Cal Kit](../../GPIB_Example_Programs/Modify_a_Calibration_Kit_using_GPIB.md)

  * [Learn about Modifying Cal Kits](../../../S3_Cals/ModifyCalKits.md#calkitmod)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

Note: You should provide data for every definition field - for every standard
in your calibration kit. If a field is not set, the default value may not be
what you expect.

For more information, read [Specifying Calibration Standards and Kits for
Keysight Vector Network Analyzers (Application Note
1287-11](http://literature.cdn.Keysight.com/litweb/pdf/5989-4840EN.pdf))

* * *

## SENSe:CORRection:COLLect:CKIT:CATalog?

Applicable Models: All (Read-only) Returns the names of the first 95
mechanical cal kits in your VNA that can be used for unguided calibrations.  
---  
Examples | SENS:CORR:COLL:CKIT:CAT?  
Return Type | A comma-separated string  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:CLISt <class>, <list_stds>

Applicable Models: All (Write-Read) Assigns the calibration class for the
standard  
---  
Parameters |   
<class> | Specify the calibration classes: SA \- OPEN Standards (standards in the SA class are not always Opens) SB \- SHORT Standards SC \- LOAD Standards THRU \- Thru FWDT \- Forward Trans FWDM \- Forward Match REVT \- Reverse Trans REVM \- Reverse Match TRLT \- TRL Thru TRLR \- TRL Reflection  TRLLm \- TRL Line UTHRu \- Unknown Thru ISOL \- Isolation  
<list_stds> | List of standard IDs (Same as [SENS:CORR:COLL:CKIT:OLIS](CorrCollCKIT.md#olist)). A standard ID can be between 1 and 1000.  
---|---  
Examples | SENS:CORR:COLL:CKIT:CLIST SA,1,2,5  
SENS:CORR:COLL:CKIT:CLIST? SA  
---|---  
Return Type | Numeric; returns standard number of the selected class  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:CLABel <class>, <label>

Applicable Models: All (Write-Read) Defines the label for the standard
classes.  
---  
Parameters |   
<class> | Specify the calibration classes: SA \- OPEN Standards (standards in the SA class are not always Opens) SB \- SHORT Standards SC \- LOAD Standards TRAN \- Thru FWDT \- Forward Trans FWDM \- Forward Match REVT \- Reverse Trans REVM \- Reverse Match TRLT \- TRL Thru TRLR \- TRL Reflection  TRLLm \- TRL Line UTHRu \- Unknown Thru ISOL \- Isolation  
<label> | Label of standard |   
---|---|---  
Examples | SENS:CORR:COLL:CKIT:CLABEL SA,"OPEN"  
SENS:CORR:COLL:CKIT:CLABEL? SA  
---|---  
Return Type | String; returns the label.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:CONNector:ADD
<family>,<start>,<stop>,<z0>,<gender>,<media>,<cutoff>

Applicable Models: All (Write only) Creates a new connector. The connector is
automatically added to the list of available connectors for the currently
selected cal kit. If a connector includes both male and female connectors,
each connector must be added separately.  
---  
Parameters |   
<family> | (String) Name of connector family. Limited to 50 characters.  
<start> | Start frequency  
<stop> | Stop frequency  
<z0> | Characteristic Impedance of the connector in ohms.  
<gender> | Connector gender. Choose from:  
MALE  
FEMALE  
NONE  
<media> | Media of the connector. Choose from: COAX \- coaxial   
WAVE \- waveguide  
<cutoff> | Cutoff frequency of the connector (waveguide only).  
Examples | SENS:CORR:COLL:CKIT:CONN:ADD "PSC 1.8 mm",0 HZ,999.9 GHZ,50,FEMALE,COAX,0.0  
SENS:CORR:COLL:CKIT:CONN:ADD "PSC 1.8 mm",0 HZ,999.9 GHZ,50,MALE,COAX,0.0  
Query Syntax | Not applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:CONNector:CATalog?

Applicable Models: All (Read-only) Returns a comma-separated list of all
connectors defined within the currently selected cal kit. The returned string
includes the connector family name followed by the connector gender, if any.
Kits may include a primary connector family name and additional connector
family names. Connector family names are case sensitive. A connector family
named "PSC 2.4" is different from a connector family named "psc 2.4". Learn
more about [Connector Family
Name](../../../S3_Cals/Connectors_Tab.htm#Connectors).  
---  
Examples | SENS:CORR:COLL:CKIT:CONN:CAT? 'Returned string "Type-N (50) male, Type-N (50) female"  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:CONNector:DELete

Applicable Models: All (Write-only) Deletes the primary connector family name
from the selected kit. The VNA allows multiple connector families for each
kit. If a kit includes multiple connector families, only the first listed
(primary) connector family name is deleted.  Once the connector family is
deleted, the connector may not be assigned to any new or existing standard
within the kit.  The previously defined standards retain their association to
the deleted connector name. To reassign standards to a new connector family
name, use [SENS:CORR:COLL:CKIT:CONN:SNAMe](CorrCollCKIT.md#sname).  
---  
Examples | SENS:CORR:COLL:CKIT:CONN:DEL  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:CONNector:FNAMe <name>

Applicable Models: All (Read-Write) Replaces the primary connector family name
from the selected kit with a new connector family name. The connector family
name is replaced in all standards in the kit that share that name. The VNA
allows multiple connector families for each kit. If a kit includes multiple
connector families, only the first listed (primary) connector family name is
replaced. Use the query form of this command to return the name of the primary
connector family.  
---  
Parameters |   
<name> | New connector family name. Limited to 50 characters.  
Examples | SENS:CORR:COLL:CKIT:CONN:FNAM 'MYPSC35' Sense:correction:collect:ckit:connector:name 'My Type N'  
Query Syntax | SENSe:CORRection:COLLect:CKIT:CONNector:FNAMe?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:CONNector:SNAMe <family>,<gender>,<port>

Applicable Models: All (Read-Write) Assigns a family name to the currently
selected standard from the currently selected kit. Specify each port of a
2-port standard individually. Use the query form of this command to read the
connector family name assigned to the current standard. The name is not
assigned unless the connector family name is previously defined within the
selected kit.  
---  
Parameters |   
<family> | String. Connector family name.  
<gender> | Connector gender. Choose from:  
MALE  
FEMALE  
NONE  
<port> | Number of the connector port to be assigned the connector family name. 2-port standards such as a thru line must be assigned separately. It is not relevant which connector is port 1 or port 2. 1 Specifies a 1-port standard or the first port of a 2-port standard. 2 Specifies the second port of a 2-port standard.  
Examples | SENS:CORR:COLL:CKIT:CONN:SNAMe "Type-N (50)",MALE,1  
Query Syntax | SENSe:CORRection:COLLect:CKIT:CONNector:SNAMe?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:DESCription <string>

Applicable Models: All (Read-Write) Modifies the cal kit description field of
the selected kit. This description appears in the [Edit VNA Cal Kit dialog
box](../../../S3_Cals/ModifyCalKits.htm#modmenu).  
---  
Parameters |   
<string> | Description of the cal kit. Limited to 50 characters.  
Examples | SENS:CORR:COLL:CKIT:DESC "My New CalKit"  
Query Syntax | SENSe:CORRection:COLLect:CKIT:DESCription?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:INFormation? <module>[,char]

Applicable Models: All (Read Only) Reads characterization information from an
ECal module.  
---  
Parameters |   
<module> | Specifies which ECal module to read from. Choose from: ECAL1 .through. ECAL50  
[char] | Optional argument. Specifies which characterization within the ECal module to read information from. If this argument is not used, the default is CHAR0. CHAR1 through CHAR5 are for user characterizations that may have been written to the module by the User Characterization feature on the VNA. Choose from: CHAR0 Factory characterization (data that was stored in the ECal module by Keysight) CHAR1 User characterization #1 CHAR2 User characterization #2 \- through - CHAR12 User characterization #12  
Examples | SENS:CORR:COLL:CKIT:INF? ECAL4  
sense:correction:collect:ckit:information? ecal2,char1  
| Example return string:  
| ModelNumber: 85092-60007, SerialNumber: 01386, ConnectorType: N5FN5F,
PortAConnector: Type N (50) female, PortBConnector: Type N (50) female,
MinFreq: 30000, MaxFreq: 9100000000, NumberOfPoints: 250, Calibrated: July 4
2002  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:NAME <name>

Applicable Models: All (Read-Write) Sets a name for the selected calibration
kit.  
---  
Parameters |   
<name> | Calibration Kit name. Any string name, can include numerics, period, and spaces; any length (although the dialog box display is limited to about 30 characters).  
Examples | SENS:CORR:COLL:CKIT:NAME 'MYAPC35'  
sense:correction:collect:ckit:name 'mytypen'  
Query Syntax | SENSe:CORRection:COLLect:CKIT:NAME?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:OLABel<class> <name> \- Superseded

This command is replaced by SENS:COR:CKIT:CLAB. Applicable Models: All (Read-
Write) Sets the label for the calibration class designated by <class>. The
label is used in the prompts for connecting the calibration standards
associated with that <class>.  
---  
Parameters |   
<class> | Number of the calibration class. Choose a number between: 1 and 18\. The <class> numbers are associated with the following calibration Classes:  
| Class | Description  
---|---|---  
Port 1 |  |   
1 | SA | Reflection standard  
2 | SB | Reflection standard  
3 | SC | Reflection standard  
4 | FWD TRANS | Thru/Delay standard  
Port 2 |  |   
5 | SA | Reflection standard  
6 | SB | Reflection standard  
7 | SC | Reflection standard  
8 | REV TRANS | Thru/Delay standard  
3-port analyzers only  
Port 3 |  |   
9 | S33A | Reflection standard  
10 | S33B | Reflection standard  
11 | S33C | Reflection standard  
12 | S32T | Thru/Delay standard  
13 | S23T | Thru/Delay standard  
14 | S31T | Thru/Delay standard  
15 | S13T | Thru/Delay standard  
TRL Calibrations  
16 | TRL "T" | Thru standard  
17 | TRL "R" | Reflect standard  
18 | TRL "L" | Line standard  
<name> | Label for the calibration class. Must be enclosed in quotes. Any string between 1 and 12 characters long. Cannot begin with a numeric.  
---|---  
Examples | SENS:CORR:COLL:CKIT:OLAB3 'LOADS' sense:correction:collect:ckit:olabel4 'Thru'  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:OLISt[class]? \- Superseded

This command is replaced by [SENS:CORR:CKIT:CLIS](CorrCollCKIT.md#ckitClist).
Applicable Models: All (Read-only) Returns seven values of standards that are
assigned to the specified class. This command ALWAYS applies to the Cal Kit
that is selected (using [SENS:CORR:COLL:CKIT:SEL](CorrCollCKIT.md#scccs))
when this ORDer command is sent.  
---  
Parameters |   
<class> | Number of the calibration class to be queried. The <class> numbers are associated with the following calibration Classes:  
| Class | Description  
---|---|---  
Port 1 |  |   
1 | SA | Reflection standard  
2 | SB | Reflection standard  
3 | SC | Reflection standard  
4 | FWD TRANS | Thru/Delay standard  
Port 2 |  |   
5 | SA | Reflection standard  
6 | SB | Reflection standard  
7 | SC | Reflection standard  
8 | REV TRANS | Thru/Delay standard  
3-port analyzers ONLY (N3381A/2A/3A) 4-port analyzers use S11 and S22 classes
[(see example
program)](../../GPIB_Example_Programs/Perform_an_Unguided_Cal_on_a_4-Port_PNA_using_SCPI.htm)  
Port 3 |  |   
9 | S33A | Reflection standard  
10 | S33B | Reflection standard  
11 | S33C | Reflection standard  
12 | S32T | Thru/Delay standard  
13 | S23T | Thru/Delay standard  
14 | S31T | Thru/Delay standard  
15 | S13T | Thru/Delay standard  
TRL Calibration  
16 | TRL "T" | Thru standard  
17 | TRL "R" | Reflect standard  
18 | TRL "L" | Line standard  
Examples | SENS:CORR:COLL:CKIT:OLIS?  
Always returns 7 standard numbers. Unassigned standards return 0  
---|---  
Return Type | Numeric; returns the <class> number of the selected standard.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:ORDer<class> <std> [,<std>] [,<std>] [,<std>]
[,<std>] [,<std>] [,<std>]- Superseded

This command is replaced by [SENS:CORR:CKIT:CLIS](CorrCollCKIT.md#ckitClist).
Applicable Models: All (Read-Write) Sets a standard number to a calibration
class. This command does NOT set or dictate the order for measuring the
standards. For more information, see Assigning Standards to a Calibration
Class. This command ALWAYS applies to the Cal Kit that is selected (using
[SENS:CORR:COLL:CKIT:SEL](CorrCollCKIT.md#scccs)) when this ORDer command is
sent.  
---  
Parameters |   
<class> | Number of the calibration class that is assigned to <standard>. Choose a number between: 1 and 18\. The <class> numbers are associated with the following calibration Classes:  
| Class | Description | [STAN#](Sense_Correction.md#scca)  
---|---|---|---  
Port 1 |  |  |   
1 | SA | Reflection standard | STAN1  
2 | SB | Reflection standard | STAN2  
3 | SC | Reflection standard | STAN3  
4 | FWD TRANS | Thru/Delay standard | STAN4  
Port 2 |  |  |   
5 | SA | Reflection standard | STAN1  
6 | SB | Reflection standard | STAN2  
7 | SC | Reflection standard | STAN3  
8 | REV TRANS | Thru/Delay standard | STAN4  
3-port analyzers ONLY (N3381A/2A/3A) 4-port analyzers use S11 and S22 classes
[(see example
program)](../../GPIB_Example_Programs/Perform_an_Unguided_Cal_on_a_4-Port_PNA_using_SCPI.htm)  
Port 3 |  |  |   
9 | S33A | Reflection standard | STAN1  
10 | S33B | Reflection standard | STAN2  
11 | S33C | Reflection standard | STAN3  
12 | S32T | Thru/Delay standard | STAN4  
13 | S23T | Thru/Delay standard | STAN4  
14 | S31T | Thru/Delay standard | STAN4  
15 | S13T | Thru/Delay standard | STAN4  
TRL Calibration  
16 | TRL "T" | Thru standard | STAN4  
17 | TRL "R" | Reflect standard | STAN1  
18 | TRL "L" | Line standard | STAN3  
<std> | Standard number to be assigned to the class; Choose a standard between 1 and 30. One standard is mandatory; up to six additional standards are optional.  
---|---  
Examples | 'Assigns standard 3 to S11A class:  
SENS:CORR:COLL:CKIT:ORD1 3 'Assigns standard 2 and 5 to S21T class class:  
sense:correction:collect:ckit:order4 2,5  
Query Syntax | SENSe:CORRection:COLLect:CKIT:ORDer<class>? 'Returns only the first standard assigned to the specified class. To query the remaining standards, use [SENSe:CORRection:COLLect:CKIT:OLIST[1-15]?](CorrCollCKIT.md#olist)  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:COLLect:CKIT:PORT<n>[:SELect] <string>

Applicable Models: All (Read-Write) Sets and returns the name of the Cal Kit
to use for Unguided cal. This command effectively does the same task as
[SENS:CORR:COLL:CKIT](CorrCollCKIT.md#scccs) but specifies the cal kit by
name. Note: During an [Unguided
cal](../../../S3_Cals/Calibration_Wizard.htm#unguided), you can access ONLY
mechanical cal kits #1 through #95. However, there is no limit to the number
of cal kits that can be imported.  
---  
Parameters |   
<cnum> | Currently not used. The unguided cal kit selection is for all ports on all channels.  
<n> | Currently not used. The unguided cal kit selection is for all ports on all channels.  
<string> | Cal Kit name enclosed in quotes. Use [SENS:CORR:COLL:CKIT:CAT?](CorrCollCKIT.md#ckitCat) to read a list of all available Cal Kits in the VNA.  
Examples | SENS:CORR:COLL:CKIT:PORT "85052B"  
sense2:correction:collect:ckit:port:select "85052D"  
Query Syntax | SENSe<cnum>:CORRection:COLLect:CKIT:PORT<n>:SELECT?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Last kit selected  
  
* * *

## SENSe:CORRection:COLLect:CKIT:RESet <num> \- Superseded

Applicable Models: All This command is replaced by
[Sens:Corr:Ckit:Init](CorrCKIT_SCPI.md#initialize). (Write-only) Resets the
selected calibration kit to factory default definition values.  
---  
Parameters |   
<num> | The number of the calibration kit to be reset. Choose any integer between:  
1 and 8  
Examples | SENS:CORR:COLL:CKIT:RESet 1  
sense:correction:collect:ckit:reset 4  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:COLLect:CKIT[:SELect] <num>

Applicable Models: All (Read-Write) Selects (makes active) a calibration kit
for performing an UNGUIDED calibration or for modifying standards. All
subsequent "CKIT" commands that are sent apply to this selected calibration
kit. Select a calibration standard using [SENS:CORR:COLL:CKIT:STAN
<num>](CorrCollCKIT.htm#ss). Kits 1 to approximately kit 37 are factory
installed Cal Kits. Note: During an [Unguided
cal](../../../S3_Cals/Calibration_Wizard.htm#unguided), you can access ONLY
mechanical cal kits #1 through #95. However, there is no limit to the number
of cal kits that can be imported. This command effectively does the same task
as [SENS:CORR:COLL:CKIT:PORT](CorrCollCKIT.md#ckitPortSelect) which specifies
the cal kit by name instead of this command which specifies by number.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<num> | The number of the calibration kit. Choose from: Use [SENSe:CORRection:COLLect:CKIT:RESet](CorrCollCKIT.md#scccr) to restore Cal Kits to default values.  
| Name  
1 | Cal Kit 1  
2 | Cal Kit 2  
3 | Cal Kit 3  
|  ''  
|  ''  
94 | Cal Kit 94  
95 | Cal Kit 95  
99 | ECal module Note: Always check the list of available cal kits using SENSe:CORRection:COLLect:CKIT:CATalog? to ensure that the correct cal kit is selected.  
Examples | SENS:CORR:COLL:CKIT 2  
sense2:correction:collect:ckit:select 7  
Query Syntax | SENSe<cnum>:CORRection:COLLect:CKIT?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Last kit selected  
  
* * *

## SENSe:CORRection:COLLect:CKIT:STANdard:C0 <num>

Applicable Models: All (Read-Write) Sets the C0 value (the first capacitance
value) for the selected standard. For a detailed discussion of this value,
search for App Note 8510-5B at [www.Keysight.com](http://www.Keysight.com).  
---  
Parameters |   
<num> | Value for C0 in femtofarads (1E-15)  
Examples | The following commands set C0=15 femtofarads: SENS:CORR:COLL:CKIT:STAN:C0 15  
sense:correction:collect:ckit:standard:c0 15  
Query Syntax | SENSe:CORRection:COLLect:CKIT:STANdard:C0?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:STANdard:C1 <num>

Applicable Models: All (Read-Write) Sets the C1 value (the second capacitance
value) for the selected standard. For a detailed discussion of this value,
search for App Note 8510-5B at [www.Keysight.com](http://www.Keysight.com).  
---  
Parameters |   
<num> | Value for C1.  
Examples | The following two commands set C1=15: SENS:CORR:COLL:CKIT:STAN:C1 15  
sense:correction:collect:ckit:standard:c1 15  
Query Syntax | SENSe:CORRection:COLLect:CKIT:STANdard:C1?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:STANdard:C2 <num>

Applicable Models: All (Read-Write) Sets the C2 value (the third capacitance
value) for the selected standard. For a detailed discussion of this value,
search for App Note 8510-5B at [www.Keysight.com](http://www.Keysight.com).  
---  
Parameters |   
<num> | Value for C2.  
Examples | The following two commands set C2: SENS:CORR:COLL:CKIT:STAN:C2 15  
sense:correction:collect:ckit:standard:c2 15  
Query Syntax | SENSe:CORRection:COLLect:CKIT:STANdard:C2?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:STANdard:C3 <num>

Applicable Models: All (Read-Write) Sets the C3 value (the fourth capacitance
value) for the selected standard. For a detailed discussion of this value,
search for App Note 8510-5B at [www.Keysight.com](http://www.Keysight.com).  
---  
Parameters |   
<num> | Value for C3.  
Examples | The following two commands set C3 SENS:CORR:COLL:CKIT:STAN:C3 15  
sense:correction:collect:ckit:standard:c3 15  
Query Syntax | SENSe:CORRection:COLLect:CKIT:STANdard:C3?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:STANdard:CHARacter <char>

Applicable Models: All (Read-Write) Sets the media type of the selected
calibration standard.  
---  
Parameters |   
<char> | Media type of the standard. Choose from:  
Coax \- Coaxial Cable  
Wave \- Waveguide  
Examples | SENS:CORR:COLL:CKIT:STAN:CHAR COAX  
sense:correction:collect:ckit:standard:character wave  
Query Syntax | SENSe:CORRection:COLLect:CKIT:STANdard:CHARacter?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Coax  
  
* * *

## SENSe:CORRection:COLLect:CKIT:STANdard:DATA:LOAD <string>

Applicable Models: All (Write-only) Loads response (and optionally accuracy)
data from a file for the selected database standard. Accuracy data is loaded
if the file being loaded contains accuracy data. [Learn
more](../../../S3_Cals/Standards_Tab.htm#Upload_Data_From_File).  
---  
Parameters |   
<string> | Path and filename.  
Examples | SENS:CORR:COLL:CKIT:STAN:DATA:LOAD "c:\users\public\network analyzer\database_file.dat"  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:STANdard:DELay <num>

Applicable Models: All (Read-Write) Sets the electrical delay value for the
selected standard.  
---  
Parameters |   
<num> | Electrical delay in picoseconds  
  
* * *  
  
Examples | The following two commands set delay to 50 picoseconds SENS:CORR:COLL:CKIT:STAN:DEL 50e-12  
sense2:correction:collect:ckit:standard:delay 50ps  
Query Syntax | SENSe:CORRection:COLLect:CKIT:STANdard:DELay?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:STANdard:FMAXimum <num>

Applicable Models: All (Read-Write) Sets the maximum frequency for the
selected standard.  
---  
Parameters |   
<num> | Maximum frequency in Hertz.  
Examples | SENS:CORR:COLL:CKIT:STAN:FMAX 9e9  
sense:correction:collect:ckit:standard:fmaximum 9Ghz  
Query Syntax | SENSe:CORRection:COLLect:CKIT:STANdard:FMAXimum?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:STANdard:FMINimum <num>

Applicable Models: All (Read-Write) Sets the minimum frequency for the
selected standard.  
---  
Parameters |   
<num> | Minimum frequency in Hertz.  
Examples | SENS:CORR:COLL:CKIT:STAN:FMIN 1e3  
sense:correction:collect:ckit:standard:fminimum 1khz  
Query Syntax | SENSe:CORRection:COLLect:CKIT:STANdard:FMINimum?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:STANdard:IMPedance <num>

Applicable Models: All (Read-Write) Sets the characteristic impedance for the
selected standard.  
---  
Parameters |   
<num> | Impedance in Ohms  
Examples | SENS:CORR:COLL:CKIT:STAN:IMP 75  
sense:correction:collect:ckit:standard:impedance 50.3  
Query Syntax | SENSe:CORRection:COLLect:CKIT:STANdard:IMPedance?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 50  
  
* * *

## SENSe:CORRection:COLLect:CKIT:STANdard:L0 <num>

Applicable Models: All (Read-Write) Sets the L0 value (the first inductance
value) for the selected standard. For a detailed discussion of this value,
search for App Note 8510-5B at [www.Keysight.com](http://www.Keysight.com).  
---  
Parameters |   
<num> | Value for L0 in femtohenries (1E-15)  
Examples | The following two commands set L0=15 femtohenries: SENS:CORR:COLL:CKIT:STAN:L0 15  
sense:correction:collect:ckit:standard:l0 15  
Query Syntax | SENSe:CORRection:COLLect:CKIT:STANdard:L0?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:STANdard:L1 <num>

Applicable Models: All (Read-Write) Sets the L1 value (the second inductance
value) for the selected standard. For a detailed discussion of this value,
search for App Note 8510-5B at [www.Keysight.com](http://www.Keysight.com).  
---  
Parameters |   
<num> | Value for L1.  
Examples | The following two commands set L1=15: SENS:CORR:COLL:CKIT:STAN:L1 15  
sense:correction:collect:ckit:standard:l1 15  
Query Syntax | SENSe:CORRection:COLLect:CKIT:STANdard:L1?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:STANdard:L2 <num>

Applicable Models: All (Read-Write) Sets the L2 value (the third inductance
value) for the selected standard. For a detailed discussion of this value,
search for App Note 8510-5B at [www.Keysight.com](http://www.Keysight.com).  
---  
Parameters |   
<num> | Value for L2.  
Examples | The following two commands set L2=15: SENS:CORR:COLL:CKIT:STAN:L2 15  
sense:correction:collect:ckit:standard:l2 15  
Query Syntax | SENSe:CORRection:COLLect:CKIT:STANdard:L2?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:STANdard:L3 <num>

Applicable Models: All (Read-Write) Sets the L3 value (the fourth inductance
value) for the selected standard. For a detailed discussion of this value,
search for App Note 8510-5B at [www.Keysight.com](http://www.Keysight.com).  
---  
Parameters |   
<num> | Value for L3.  
Examples | The following two commands set L3=15: SENS:CORR:COLL:CKIT:STAN:L3 15  
sense:correction:collect:ckit:standard:l3 15  
Query Syntax | SENSe:CORRection:COLLect:CKIT:STANdard:L3?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:STANdard:LABel <name>

Applicable Models: All (Read-Write) Sets the label for the selected standard.
The label is used to prompt the user to connect the specified standard.  
---  
Parameters |   
<name> | Label for the standard; Must be enclosed in quotes. Any string between 1 and 12 characters long. Cannot begin with a numeric.  
Examples | SENS:CORR:COLL:CKIT:STAN:LAB 'OPEN'  
sense:correction:collect:ckit:standard:label 'Short2'  
Query Syntax | SENSe:CORRection:COLLect:CKIT:STANdard:LABel?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:STANdard:LOSS <num>

Applicable Models: All (Read-Write) Sets the insertion loss for the selected
standard.  
---  
Parameters |   
<num> | Insertion loss in Gohms / sec. (GigaOhms per second of electrical delay)  
Examples | SENS:CORR:COLL:CKIT:STAN:LOSS 3.5e9  
sense:correction:collect:ckit:standard:loss 3  
Query Syntax | SENSe:CORRection:COLLect:CKIT:STANdard:LOSS?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:STANdard:REMove

Applicable Models: All (Write only) Deletes the selected standard from the
selected cal kit.  
---  
Examples | SENS:CORR:COLL:CKIT:STAN:REMove  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:STANdard:SDEScription <string>

Applicable Models: All (Read-Write) Modifies the description of the selected
standard of the selected kit. This description appears in the [edit kit dialog
box](../../../S3_Cals/Standards_Tab.htm#EditStandardsDiag).  
---  
Parameters |   
<string> | Description of the standard.  
Examples | SENS:CORR:COLL:CKIT:STAN:SDES "My New Standard"  
Query Syntax | SENSe:CORRection:COLLect:CKIT:STANdard:SDEScription?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:STANdard[:SELECT] <num>

Applicable Models: All (Read-Write) Selects the calibration standard. All
subsequent "CKIT" commands to modify a standard will apply to the selected
standard. Select a calibration kit using
[SENS:CORR:COLL:CKIT:SEL](CorrCollCKIT.md#scccs)  
---  
Parameters |   
<num> | Number of the standard. Choose any number between:  
1 and 1000  
Examples | SENS:CORR:COLL:CKIT:STAN 3  
sense:correction:collect:ckit:standard:select 8  
Query Syntax | SENSe:CORRection:COLLect:CKIT:STANdard[:SELect]?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## SENSe:CORRection:COLLect:CKIT:STANdard:TYPE <char>

Applicable Models: All (Read-Write) Sets the type for the selected standard.  
---  
Parameters |   
<char> | Choose from:  
OPEN  
SHORT  
LOAD  
SLOAD (sliding load) THRU (through) ARBI (arbitrary) DATabased (data-based)  
Examples | SENS:CORR:COLL:CKIT:STAN:TYPE LOAD  
sense:correction:collect:ckit:standard:type short  
Query Syntax | SENSe:CORRection:COLLect:CKIT:STANdard:TYPE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:STANdard:TZReal <num>

Applicable Models: All (Read-Write) Sets the TZReal component value of the
Terminal Impedance for the selected standard. Note: Only applicable when the
Standard Type is set to ARBI  
---  
Parameters |   
<num> | Value for TZReal in Ohms  
  
* * *  
  
Examples | The following commands set TZReal=15 Ohms: SENS:CORR:COLL:CKIT:STAN:TZReal 15  
sense:correction:collect:ckit:standard:TZReal 15  
Query Syntax | SENSe:CORRection:COLLect:CKIT:STANdard:TZReal?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:STANdard:TZImag <num>

Applicable Models: All (Read-Write) Sets the TZImag component value of the
Terminal Impedance for the selected standard. Note: Only applicable when the
Standard Type is set to ARBI  
---  
Parameters |   
<num> | Value for TZImag in Ohms  
Examples | The following two commands set TZImag=15 Ohms: SENS:CORR:COLL:CKIT:STAN:TZImag 15  
sense:correction:collect:ckit:standard:TZImag 15  
Query Syntax | SENSe:CORRection:COLLect:CKIT:STANdard:TZImag?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:CKIT:TRLoption:IMPedance <char>

Applicable Models: All (Read-Write) Sets the reference impedance when using
this TRL cal kit. [Learn more](../../../S3_Cals/TRL_Tab.md#Reference). Before
sending this command, select a cal kit using
[SENS:CORR:COLL:CKIT:SELect](CorrCollCKIT.md#scccs).  
---  
Parameters |   
<char> | Choose from: SYSTem \- The system impedance is used as the reference impedance. During a Guided or Unguided Cal, the Z0 of the Cal standard's connector definition sets the System Z0. Make this selection when the desired test port impedance differs from the impedance of the LINE standard. Also, make this selection when skin effect impedance correction is desired for coax lines. LINE The impedance of the line standard is used as the reference impedance, or center of the Smith Chart. Any reflection from the line standard is assumed to be part of the directivity error.  
Examples | SENS:CORR:COLL:CKIT:TRL:IMP SYST sense:correction:collect:ckit:trloption:impedance line  
Query Syntax | SENSe:CORRection:COLLect:CKIT:TRLoption:IMPedance?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | LINE  
  
* * *

## SENSe:CORRection:COLLect:CKIT:TRLoption:LRLChar <bool>

Applicable Models: All (Read-Write) This setting ONLY applies if an LRL Cal
Kit is being modified AND Testport Reference Plane is set to THRU AND the TRL
Thru class standard and the TRL Line/Match class standard both have the same
values for Offset Z0 and Loss. Otherwise, this setting is ignored. Before
sending this command, select a cal kit using
[SENS:CORR:COLL:CKIT:SELect](CorrCollCKIT.md#scccs).  
---  
Parameters |   
<bool> | Choose from: 1 or ON \- Automatically correct for line loss and dispersion characteristics. 0 or OFF \- Select when anomalies appear during a calibrated measurement which may indicate different loss and impedance values for the Line standards.  
Examples | SENS:CORR:COLL:CKIT:TRL:LRLC 1 sense:correction:collect:ckit:trloption:lrlchar off  
Query Syntax | SENSe:CORRection:COLLect:CKIT:TRLoption:LRLChar?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SENSe:CORRection:COLLect:CKIT:TRLoption:RPLane <char>

Applicable Models: All (Read-Write) Sets the reference impedance when using
this cal kit. [Learn more](../../../S3_Cals/TRL_Tab.md#Reference). Before
sending this command, select a cal kit using
[SENS:CORR:COLL:CKIT:SELect](CorrCollCKIT.md#scccs).  
---  
Parameters |   
<char> | Choose from: THRU The THRU standard definition is used to establish the measurement reference plane. Select if the THRU standard is zero-length or very short. REFLect The REFLECT standard definition is used to establish the position of the measurement reference plane. Select if the THRU standard is not appropriate AND the delay of the REFLECT standard is well defined. Also, select If a flush short is used for the REFLECT standard because a flush short provides a more accurate phase reference than a Thru standard.  
Examples | SENS:CORR:COLL:CKIT:TRL:RPL THRU sense:correction:collect:ckit:trloption:rplane reflect  
Query Syntax | SENSe:CORRection:COLLect:CKIT:TRLoption:RPLane?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | THRU  
  
* * *

