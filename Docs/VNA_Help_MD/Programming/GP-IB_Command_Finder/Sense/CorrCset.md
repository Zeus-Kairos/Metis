# Sense:Correction:Cset Commands

* * *

Performs actions on calibration sets.

## SENSe:CORRection:CSET

[ACTivate](CorrCset.md#activate) [CATalog?](CorrCset.md#catalog) [COPY](CorrCset.md#copy) [CREate](CorrCset.md#create) | DEFault | LEAKage [DATA](CorrCset.md#data) [DEACtivate](CorrCset.md#DEACtivate) [DELete](CorrCset.md#delete) [DESCription](CorrCset.md#desc) ETERm | [CATalog?](CorrCset.md#etermCAT) | [[DATA]](CorrCset.md#eterm) [FLATten](CorrCset.md#Flatten) GENerate | RECeiver [GUID](CorrCset.md#guid) ITEM | CAT? | [:DATA]? [NAME](CorrCset.md#name) [SAVE](CorrCset.md#sccsv) [[SELect]](CorrCset.md#sccse) [STANdard[:DATA]](CorrCset.md#standard) | [CATalog?](CorrCset.md#Cat) [STIMulus?](CorrCset.md#Stimulus) TSET | [ALLPorts?](CorrCset.md#AllPorts) | [TYPE?](CorrCset.md#TsetType) TYPE | [CATalog?](CorrCset.md#TypeCat)  
---  
  
Click on a keyword to view the command details.

Blue keywords are superseded commands. [Learn
more](../../Replacement_Commands.htm).

### See Also

  * [Creating Cal Sets](../../Learning_about_GPIB/Calibrating_the_Analyzer_Using_SCPI.md#CreateCalSet)

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Learn about Cal Sets](../../../S3_Cals/Cal_Sets.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

* * *

## SENSe<cnum>:CORRection:CSET:ACTivate <string>, <bool>

Applicable Models: All This command replaces
[SENS:CORR:CSET:GUID](CorrCset.md#guid) (Read-Write) Selects and applies a
Cal Set to the specified channel. Use
[SENS:CORR:CSET:CAT?](CorrCset.md#catalog) to list the Cal Sets.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<string> |  Cal Set to make active. Specify the Cal Set by GUID or Name. Use [SENS:CORR:CSET:CAT?](CorrCset.md#catalog) to list the available Cal Sets in either format.  
<bool> |  Should the Cal Set stimulus values be applied to the channel. Choose from: ON (1) Apply the Cal Set stimulus values to the channel. OFF (0) Do NOT apply the Cal Set stimulus values. If the Cal Set stimulus values do not match the channel stimulus values, then the following will occur:

  * If interpolation is ON, then interpolation will be attempted. This may fail if the channel frequency is outside the range of the Cal Set.
  * If interpolation is OFF, the selection will be abandoned and an error is returned:

  
Examples |  SENS:CORR:CSET:ACT "My2Port",1 sense:correction:cset:activate? name  
'returns  
"My2Port"  
Query Syntax |  SENSe<cnum>:CORRection:CSET:ACTivate? [GUID|NAME] Returns the name of the Cal Set that is applied to the specified channel. Choose from GUID or NAME to specify which string is returned. If unspecified, the GUID of the Cal Set is returned. If no Cal Set is applied to the specified channel, then "No Calset Selected" is returned.  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe:CORRection:CSET:CATalog? [char] - Superseded

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA This command is
replaced by [CSET:CAT?](../CSET.md#CAT) (Read-only) Returns a list of Cal
Sets.  
---  
Parameters |   
<char> |  Optional argument. The list is returned in one of the following formats. Both return comma-separated string lists. GUID Cal Sets are listed by GUID (Default if unspecified). NAME Cal Sets are listed by Name  
Examples |  SENS:CORR:CSET:CAT? 'Returns:  
{FD6F863E-9719-11d5-8D6C-00108334AE96},{1B03B2CE-971A-11d5-8D6C-00108334AE96}
sense2:correction:cset:catalog? name  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:CSET:COPY <string>

Applicable Models: All (Write-only) Creates a new Cal Set and copies the
current Cal Set data into it. Use this command to manipulate data on a Cal Set
without corrupting the original cal data.  
---  
Parameters |   
<cnum> |  Channel number using the Cal Set to be copied. If unspecified, value is set to 1  
<string> |  Name of the new Cal Set.  
Examples |  SENS2:CORR:CSET:COPY 'My2Port'  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:CSET:CREate [name]

Applicable Models: All (Write-only) Creates an empty Cal Set and attaches it
to the specified channel. This command is ONLY necessary before remotely
filling the Cal Set with error term data. (For Advanced Users). A Cal Set is
automatically created, applied to the channel, and saved at the completion of
a guided cal according to the preference setting
[SENS:CORR:PREF:CSET:SAVE.](Sense_Correction.md#CsetSave)  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
[name] |  Optional argument. Name of the Cal Set. Spaces or punctuation are NOT allowed. If unspecified, a unique name is chosen in the form "Calset_N" where N is a unique number.  
Examples |  SENS:CORR:CSET:CRE 'My2Port'  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:CSET:CREate:DEFault [<csetname>], [<correctiontype>]

Applicable Models: All (Write-only) Creates a unity Cal Set useful for
debugging or to quickly test a prototype of automation software.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
[<csetname>] |  Optional argument. Name of the Cal Set. Spaces or punctuation are NOT allowed. If unspecified, a unique name is chosen in the form "Calset_N" where N is a unique number.  
[<correctiontype>] |  Optional argument. Specifies the correction type to use as the default. In general, Full **N** P(X,Y,Z, ) where N is the number of ports covered in the calset, and X,Y,Z are a port list. "Full 2P(1,2)"

  * 2 port S-parameter correction including Port 1 and Port 2

"Full 3P(2,3,4)"

  * 3 port S-parameter correction including Port 2, Port 3, and Port 4

"Full 2P+(1,2)"

  * 2 port S-parameter correction with power correction including Port 1 and Port 2

"Full 1P(3)"

  * 1 port S-parameter correction on Port 3

"ResponseTracking(a1)"

  * Response tracking term for the a1 receiver

  
Examples |  'This example applies 2-port error correction as if the system were perfect.  
'All error terms will be 1 or 0.  
SENS:CORR:CSET:CRE:DEF 'My2Port', 'Full 2P(1,2)'  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:CSET:CREate:LEAKage <csetname>, <portgroup>

Applicable Models: All (Write-only) Creates an ideal leaky calset  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<csetname> |  Name of the Cal Set.   
<portgroup> |  Strng list. (same as SENS:CORR:COLL:LEAK:INIT)  
List of the ports involved, grouped in leaky sets of ports, enclosed in square
brackets.  
Ports in the same group are separated by , while groups are separated by
;. Example: [1,2] > 2 ports, single group: leakage will be among the two
ports.  
Example: [1,2; 3,4] > 4 ports, 2 leaky groups [1,2] and [3,4]: leakage will be
among [1,2] and among [3,4] but not between 1 and 3 because those ports belong
to different groups.  
Example: [1,2, 3,4] > 4 ports, single group: leakage among all 4 ports  
Examples |  SENS:CORR:CSET:CRE:LEAK 'MyCalSet', '[1,2]'  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:CSET:DATA <eterm, portA, portB,>[<rec>,] <block>

Applicable Models: All (Read-Write) Read or Write a specific error term
from/to the Cal Set currently attached to the specified channel. (For Advanced
Users). The command can be used only for the error terms listed. See
[SENS:CORR:CSET:ETERM](CorrCset.md#eterm) to get and put error term data
using a string argument for all error terms.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<eterm, portA, portB> |  Error Term, Port pair of the specified error term. Although not all error terms use two port numbers, two are required by the VNA in all cases. Each port number must be between 1 and the number of ports on the VNA. EDIR - directivity portA: the port at which directivity is measured. portB: Not used, but must be a valid VNA port number.  
|  ESRM \- source match portA: the port at which source match is measured.
portB: Not used, but must be a valid VNA port number.  
|  ERFT \- reflection tracking portA: the port at which reflection tracking is
measured. portB: Not used, but must be a valid VNA port number.  
|  ELDM \- load match portA: the port at which load match is measured. portB:
the source port. Load match is measured with a cable connected between the
measured port (portA) and the source port (portB). The cal system requires
that the complete matrix of loadmatch arrays be filled. In most cases you can
measure loadmatch once at a port, driven by any other port. Then use that data
for all variations of the receive port. (The exception is the 3-port VNA
models, which requires the loadmatch-measured port to be driven by every other
port.) For example: Measure the loadmatch at port2 while driving port1. Then
upload this same data to the following arrays: ELDM,2,1,<data> ELDM,2,3,<data>
ELDM,2,4,<data>  
|  ETRT \- transmission tracking portA: the receive port portB: the source
port for this measurement  
|  EXTLK \- crosstalk portA: the receive port portB: the source port for this
measurement  
|  ERSPT \- response tracking. portA: Not used, but must be a valid VNA port
number. portB: Not used, but must be a valid VNA port number.  
|  ERSPI \- response isolation. portA: Not used, but must be a valid VNA port
number. portB: Not used, but must be a valid VNA port number.  
<rec> |  <string> \- Specify the VNA receiver for which the Eterm applies. Required ONLY when Eterm is response tracking (ERSPT) or response isolation (ERSPI). [Logical receiver notation](../../../S1_Settings/Measurement_Parameters.md#RecNotation) is allowed.  
|  A full 4-port calibration requires the following terms be uploaded: |  |  |  PORT B  
---|---|---  
|  |  1 |  2 |  3 |  4  
P O R T A |  1 |  EDIR,1,1 ERFT,1,1 ESRM,1,1 |  ELDM,1,2 ETRT,1,2 EXTLK,1,2 |  ELDM,1,3 ETRT,1,3 EXTLK,1,3 |  ELDM,1,4 ETRT,1,4 EXTLK,1,4  
2 |  ELDM,2,1 ETRT,2,1 EXTLK,2,1 |  EDIR,2,2 ERFT,2,2 ESRM,2,2 |  ELDM,2,3 ETRT,2,3 EXTLK,2,3 |  ELDM,2,4 ETRT,2,4 EXTLK,2,4  
3 |  ELDM,3,1 ETRT,3,1 EXTLK,3,1 |  ELDM,3,2 ETRT,3,2 EXTLK,3,2 |  EDIR,3,3 ERFT,3,3 ESRM,3,3 |  ELDM,3,4 ETRT,3,4 EXTLK,3,4  
4 |  ELDM,4,1 ETRT,4,1 EXTLK,4,1 |  ELDM,4,2 ETRT,4,2 EXTLK,4,2 |  ELDM,4,3 ETRT,4,3 EXTLK,4,3 |  EDIR,4,4 ERFT,4,4 ESRM,4,4  
  
Reflection terms

Transmission terms  
  
<block> |  (Block). Error term data. A Real / Imaginary data pair for each data point. Format is set using [FORM:DATA](../Format_SCPI.md#fd) command. For REAL binary formats, refer to [Getting Data from the Analyzer using SCPI](../../Learning_about_GPIB/Getting_Data_from_the_Analyzer.md)  
Example |  'Set the directivity term with a cal set using 5 points SENS1:CORR:CSET:DATA EDIR, 1, 1, +6.12569600000E-002,-7.27163800000E-003,-3.63812000000E-003,+1.33521800000E-002,-4.36775100000E-003,+1.87792400000E-002,-4.09239100000E-003,+4.24291200000E-002,-2.03784900000E-002,+3.21425100000E-002"  
Query Syntax |  SENSe<cnum>:CORRection:CSET:DATA? <eterm,portA, portB>,<rec>  
Query Examples |  'Read the response isolation eterms for the port 1 reference receiver  sens:corr:cset:data? ERSPI,1,1,R1 'Same receiver using logical receiver notation sens:corr:cset:data? ERSPI,1,1,a1  
Return Type |  Block data  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:CSET:DEACtivate

Applicable Models: All (Write-only) Unselects a Cal Set from the specified
channel.  
---  
Parameters |   
<cnum> |  Channel number to have Cal Set unselected.  
Examples |  SENS:CORR:CSET:DEAC sense2:correction:cset:deactivate  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe:CORRection:CSET:DELete <string> \- Superseded

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA This command is
replaced by [CSET:DEL](../CSET.md#delete). (Write-only)Deletes a Cal Set from
the set of available Cal Sets. This method immediately updates the Cal Set
file on the hard drive. If the Cal Set is currently being used by a channel or
does not exist, this request will be denied and an error is returned.  
---  
Parameters |   
<string> |  Cal Set to be deleted. Specify the Cal Set by GUID or Name. Use [SENS:CORR:CSET:CAT?](CorrCset.md#catalog) to list the available Cal Sets in either format.  
Examples |  SENS:CORR:CSET:DEL '{2B893E7A-971A-11d5-8D6C-00108334AE96}'  
sense2:correction:cset:delete 'MyCalSet'  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:CSET:DESCription <string>

Applicable Models: All (Read-Write) Sets or returns the descriptive string
assigned to the selected Cal Set. Change this string so that you can easily
identify each Cal Set. Apply and select the Cal Set using
[SENS:CORR:CSET:ACT](CorrCset.md#activate).  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<string> |  The descriptive string associated with the currently-selected Cal Set  
Examples |  SENS:CORR:CSET:DESC 'MyCalSet'  
sense2:correction:cset:description 'thisCalSet'  
Query Syntax |  SENSe<cnum>:CORRection:CSET:DESCription?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:CSET:ETERm[:DATA] <string>,<data>

Applicable Models: All (Read-Write) Sets or returns error term data for all
VNA measurements. This command modifies a calset that is currently in use by
the channel. To see the effects of this modification you need to save the
calset and turn correction off and then on again. The commands are as follows:
SENS:CORR:CSET:SAVE SENS:CORR:STATe OFF SENS:CORR:STATe ON  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<string> |  (String) Error term to read or write. The error term is specified using the EXACT case-sensitive string displayed in the [Cal Set Viewer](../../../S3_Cals/Errors.md#Monitoring) utility. See [SENS:CORR:CSET:DATA](CorrCset.md#data) for a description of port numbers.  
<data> |  (Block) Error term data. A Real / Imaginary data pair for each data point. Format is set using [FORM:DATA](../Format_SCPI.md#fd) command. For REAL binary formats, refer to [Getting Data from the Analyzer using SCPI](../../Learning_about_GPIB/Getting_Data_from_the_Analyzer.md)  
Examples |  SENS:CORR:CSET:ETERM "Directivity(1,1)", 0.237,-1.422, 0.513, 0.895 ' set directivity(source error term for 2 points  
SENS:CORR:CSET:ETERM? "Directivity(1,1)" 'read  
Query Syntax |  SENSe<cnum>:CORRection:CSET:ETERm[:DATA]? <string>  
Return Type |  Block data  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:CSET:ETERm:CATalog?

Applicable Models: All (Read-only) Returns a list of error term names found in
the current Cal Set that is applied to the specified channel.  
---  
Parameters |   
Examples |  SENS:CORR:CSET:ETER:CAT? 'For a 1-port cal, returns "Directivity(1,1),ReflectionTracking(1,1),SourceMatch(1,1)"  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:CSET:FLATten <string>

Applicable Models: All (Write-only) When a Cal Set that was produced by a
calibration has been interpolated or otherwise modified (for example, by
Fixturing operations) this command saves the modified Cal Set to the VNA hard
drive so that it can be reused. There is no User Interface equivalent for this
command.  Background When a Cal Set is selected for use by a channel, the
channel reads the Cal Set from disk (primary Cal Set). If the channel aligns
perfectly with the Cal Set, the primary Cal Set is used directly. In this
case, the active Cal Set is the primary Cal Set. When processing occurs on the
error terms due to interpolation or modification due to the use of fixturing,
the channel will generate a temporary "memory-resident" Cal Set. In this case,
the active Cal Set is the memory-resident Cal Set. This FLATten command allows
you to save the active Cal Set to disk. Depending on the measurement
conditions, this flattening of the Cal Set can improve performance, especially
if the Cal Set is applied often (using multiple recall states) or used by many
channels. Flattening a version of the Cal Set for each channel can avoid the
interpolation or the fixturing processing that would otherwise occur when the
Cal Set is selected or the instrument state is recalled.  You will have to
manage the application of such a Cal Set as the VNA itself will have no way to
determine what processing had been done once the flatten command is used. For
example, if fixture de-embedding occurred prior to the flatten command, that
Cal Set should then be applied WITHOUT fixturing on, because fixturing is
already embedded in that Cal Set. It is your responsibility to apply the Cal
Set properly. If you want to repeatedly de-embed multiple networks (i.e.
concatenate multiple 2-port de-embedding files) you can use the flatten
command to create a new primary Cal Set after each de-embed, and sequentially
add additional de-embed networks.  
---  
Parameters |   
<cnum> |  Channel number on which the modified Cal Set resides. If unspecified, value is set to 1  
<string> |  Name of the new Cal Set. Spaces or punctuation NOT allowed.  
Examples |  SENS:CORR:CSET:FLAT "MyCalSet"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:CSET:GENerate:RECeiver <receiverName>

Applicable Models: All Models This command converts the selected Cal Set from
an S-parameter Cal Set to an S-parameter+Power Cal Set. This command requires
a Cal Set to be selected. There are 2 modes for using this command: **Mode
1:** The <receiverName> is optional. If not specified, then
ResponseTracking(a1) is set to 1, and the rest of ResponseTracking() terms are
computed to be consistent with the S-parameter calibration terms. **Mode 2:**
Use this pattern when there is already a receiver calibration for one of the
receivers. In that case, this command can be used to transfer the receiver
calibration to the other receivers. If <receiverName> is specified, it must be
either 'a1','a2','a3', etc or 'b1','b2','b3'. The ResponseTracking term for
this receiver must already be added to the Cal Set, or else this command will
generate an error. This command will then compute the ResponseTracking() terms
for all of the other receivers in a manner consistent with the S-parameter
calibration terms.  
---  
Parameters |   
<cnum> |  Channel number on which the modified Cal Set resides. If unspecified, value is set to 1.  
<receiverName> |  Name of the receiver ('a1', 'a2', 'a3', etc., or 'b1', 'b2', 'b3', etc.)  
Examples |  SENS:CORR:CSET:GEN:REC 'a1'  
Query Syntax |  SENSe<cnum>:CORRection:CSET:GENerate:RECeiver?  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:CSET:GUID <string> Superseded

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA This command is
replaced by [SENS:CORR:CSET:ACTivate](CorrCset.md#activate). (Read-Write)
Selects the Cal Set identified by the string parameter (GUID) and applies it
to the specified channel.

  * A Cal Set cannot be selected for a channel which is not ON.
  * If the stimulus settings of the selected Cal Set differ from those of the selected channel, the instrument will automatically change the channel's settings to match the Cal Set.

  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<string> |  GUID of the desired Cal Set. The curly brackets and hyphens must be included.  
Examples |  SENS:CORR:CSET:GUID '{2B893E7A-971A-11d5-8D6C-00108334AE96}'  
sense2:correction:cset:guid '{2B893E7A-971A-11d5-8D6C-00108334AE96}'  
Query Syntax |  SENSe<cnum>:CORRection:CSET:GUID? Returns the GUID of the currently-selected Cal Set for the specified channel.  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:CSET:ITEM:CATalog?

Applicable Models: All (Read-only) Returns the names of the items n the Cal
Set.  
---  
Parameters |   
Examples |  SENS:CORR:CSET:ITEM:CAT? **" Created By,Firmware Revision,Model Number,Serial Number"** 'Example returned item names.  
Return Type |  String If no Cal Set is applied on the current channel, the following error message is displayed: +163, "Requested Cal Set was not found in Cal Set Storage."  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:CSET:ITEM[:DATA]? <itemName>

Applicable Models: All (Read-only) Read the value of the Cal Set item. The Cal
Set item is added by the VNA firmware to every Cal Set.

### About Cal Set Items

A Cal Set item is a named value. You can list the named values using
CSET:ITEM:CATalog? or SENS:CORR:CSET:ITEM:CATalog? You can query the value of
a specific item by asking for its data: CSET:ITEM:DATA? For example, one of
the items added by the VNA firmware to every Cal Set is named 'Created By'.
The value attached to this item is the name of the VNA Measurement Class or
Channel that created the Cal Set. When an SMC cal is performed, you can query
the Cal Set for the 'Created By' item, and it will return 'Scalar
Mixer/Converter'. The same query on an NFx channel returns 'Noise Figure
Converters'.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<itemName> |  (String) Item added by the VNA firmware to the currently loaded Cal Set.  
Examples |  SENS:CORR:CSET:ITEM? "Model Number" "N5242B" 'Example returned Model Number value.  
Return Type |  String If no Cal Set is applied on the current channel, the following error message is displayed: +163, "Requested Cal Set was not found in Cal Set Storage."  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:CSET:NAME <string>

Applicable Models: All (Read-Write) Sets or queries the name of the Cal Set
currently applied to the specified channel.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<string> |  Name of the Cal Set. Spaces or punctuation NOT allowed.  
Examples |  SENS:CORR:CSET:NAME 'MyCalSet'  
sense2:correction:cset:name 'thisCalSet'  
Query Syntax |  SENSe<cnum>:CORRection:CSET:NAME?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:CSET:SAVE [<char>]

Applicable Models: All This command is NOT necessary after completion of a
calibration. A Cal Set is automatically created, applied to the channel, and
saved at the completion of a guided cal according to the preference setting
[SENS:CORR:PREF:CSET:SAVE](Sense_Correction.md#CsetSave). (Read Write) Saves
the channel's Cal Set to the VNA hard drive. For example, use this command
after writing data to a Cal Set using [SENS:CORR:CSET:DATA](CorrCset.md#data)
(For Advanced Users). The file name is saved as "CSETx.cst" where x is the
user number assigned to <char>, and .cst specifies a Cal Set and instrument
state. This is not the same syntax as a file saved through the default choices
from the front panel, which is "at00x.cst". For more information on the file
naming syntax, see the [MMEMory](../Memory.md) subsystem. Learn more about
[Instrument/Cal States.](../../../S5_Output/SaveRecall.md#FileTypes)  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
[<char>] |  Optional argument. Choose from: USER01 USER02... and so forth, until... USER10 If <char> is NOT specified, changes that may have been made are saved to the cal set and NOT to the *cst file.  
Examples |  SENS:CORR:CSET:SAVE USER03  
sense2:correction:cset:save user09 'save changes to only the cal set
SENS:CORR:CSET:SAVE  
Query Syntax |  SENSe<cnum>:CORRection:CSET:SAVE? Queries the last correction set saved.  
Return Type |  Charact er  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SENSe<cnum>:CORRection:CSET[:SELect] <char> Superseded

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA This command is
replaced by [MMEM:LOAD](../Memory.md#recall) (Read-Write) Recalls a *.cst
file from memory. The file name is "CSETx.cst" where x is the user number
assigned to <char>. Learn more about [.cst
files](../../../S5_Output/SaveRecall.htm#FileTypes) For more information on
the file naming syntax, see the [MMEMory](../Memory.md) subsystem. Note: This
command does NOT select a Cal Set for a channel. To select a Cal Set, use
[SENS:CORR:CSET:ACTivate](CorrCset.md#activate)  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<char> |  Choose from:  
DEF \- Presets the analyzer USER01 \- Restores User01 calibration data USER02
- Restores User02 calibration data through... USER10 - Restores User10
calibration data  
Examples |  SENS:CORR:CSET DEF  
sense2:correction:cset:select user02  
Query Syntax |  SENSe<cnum>:CORRection:CSET[:SELect]?  
Return Type |  Charact er  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  DEF  
  
* * *

## SENSe<cnum>:CORRection:CSET:STANdard[:DATA] <string>,<data>

Applicable Models: All (Read-Write) Sets or returns standard data. Standard
data is available for Unguided Cals ONLY.  Note: The Standards data
container in the calset is intended for internal use only. External access is
provided for use in diagnosing calibration problems. Users should not form any
expectations as to the presence of the data or the naming conventions used.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<string> |  (String) Cal standard to read or write. The standard is specified using the EXACT case-sensitive string displayed in the [Cal Set Viewer](../../../S3_Cals/Errors.md#Monitoring) utility. See [SENS:CORR:CSET:DATA](CorrCset.md#data) for a description of port numbers.  
<data> |  (Block). Acquisition data. A Real / Imaginary data pair for each data point. Format is set using [FORM:DATA](../Format_SCPI.md#fd) command. For REAL binary formats, refer to [Getting Data from the Analyzer using SCPI](../../Learning_about_GPIB/Getting_Data_from_the_Analyzer.md)  
Examples |  SENS:CORR:CSET:STAN 'S11C(1,1), 0.237,-1.422, 0.513, 0.895 ' Set acquisition data for two points. SENS:CORR:CSET:STAN:DATA? "S11C(1,1)" 'Read data  
Query Syntax |  SENSe<cnum>:CORRection:CSET:STANdard[:DATA]? (string)  
Return Type |  Block data  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe:CORRection:CSET:STANDard:CATalog?

Applicable Models: All (Read-only) Returns a list of available standard name
found in the current Cal Set that is applied to the specific channel.  
---  
Parameters |   
Examples |  SENS:CORR:CSET:STAN:CAT?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:CSET:STIMulus? [num]

Applicable Models: All (Read-only) Returns the source or response stimulus
values for the Cal Set that is currently used by channel <ch>. Values are
returned in the format specified by [FORM:DATA](../Format_SCPI.md#fd) (Block
or ASCII).  
---  
Parameters |   
<ch> |  Channel number to query Cal Set stimulus values. If unspecified, value is set to 1  
[num] |  Optional argument. Range of frequencies to return. These values would be different when FOM (Opt S93080A) is enabled. 0 \- returns source frequencies. Default setting if not specified. 1 \- returns response frequencies. 2 \- returns primary frequencies.  
Examples |  SENS:CORR:CSET:STIM? sense:correction:cset:stimulus 1  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe:CORRection:CSET:TSET:ALLPorts? <cset>

Applicable Models: All (Read-only) Reads the port mapping used for the
specified Cal Set. The returned values are the physical ports. The POSITION of
the returned values corresponds to the logical ports. For example, with an
N44xx test set, if the returned string is "PNA 1,TS 2,PNA 2, TS 4" this means:

  * VNA 1 is assigned to logical port 1
  * TS 2 is assigned to logical port 2
  * VNA 2 is assigned to logical port 3
  * TS 4 is assigned to logical port 4

  
---  
Parameters |   
<cset> |  (String) Name or GUID of the Cal Set. Use [SENS:CORR:CSET:CAT?](CorrCset.md#catalog) to read the list of available Cal Set names or GUIDs.  
Examples |  SENS:CORR:CSET:TSET:ALLP? "MyCalSet"  
sens:correction:cset:tset:allports? "{2B893E7A-971A-11d5-8D6C-00108334AE96}"  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe:CORRection:CSET:TSET:TYPE? <cset>

Applicable Models: All (Read-only) Reads the test set type (model) used for
the specified Cal Set.  
---  
Parameters |   
<cset> |  (String) Name or GUID of the Cal Set. Use [SENS:CORR:CSET:CAT?](CorrCset.md#catalog) to read the list of available Cal Set names or GUIDs.  
Examples |  SENS:CORR:CSET:TSET:TYPE? "MyCalSet" 'returns "N44xx" sens:correction:cset:tset:type? "{2B893E7A-971A-11d5-8D6C-00108334AE96}"  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:CSET:TYPE:CATalog? [format]

Applicable Models: All (Read-only) Query the Cal Types available in the
selected Cal Set. The output is a comma separated list of Guids or a Cal Type
names. [Learn more about applying Cal Types using
SCPI.](../../Learning_about_GPIB/Calibrating_the_Analyzer_Using_SCPI.htm#Applying)
Use
[CALC:MEAS:CORR:TYPE](../Calculate/MeasureCorrection.md#CALCulate:MEASure:CORRection:TYPE)
to apply a Cal Type.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
[format] |  (Optional) Format of the output of cal types. choose from: NAME \- (default) returns a list of cal type string names. GUID - returns a list of cal type GUIDs  
Examples |  SENS:CORR:CSET:TYPE:CAT? NAME SENS2:CORRection:CSET:TYPE:CAT?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

