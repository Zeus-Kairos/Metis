# Sense:Correction:Collect:Leak Commands

* * *

Performs Leakage calibration

SENSe:CORRection:COLLect:LEAKage ABORt COMPute COUNt INITiate OPTion | RECiprocity | DELay | DATA | FILE | [:VALue] | [P](CorrCollGuidVMC.md#NetworkFilename)ORT | TYPE PORTs RESTore SAVE | CSET | FIXture STANDard | DEFinition | DATA | CATalog | CLEar | LOAD | SAVE | SHOW | [:VALue] | FILE | MEASure | ACQuire | DATA | CATalog | CLEar | LOAD | SAVE | SHOW | [:VALue] | FILE STORe VERify  
---  
  
Click on a red keyword to view the command details.

See Also

  * [Leakage Calibration](../../../S3_Cals/Leakage_Calibration.md)

* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:ABORt

Applicable Models: All with Leakage Cal Application (S9x008B) (Write Only)
Destroys the leaky capability. Data not saved will be lost  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
Examples |  SENS:CORR:COLL:LEAK:ABOR  
Query Syntax |  N/A  
Return Type |  N/A  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  NONE  
  
* * *

## SENSe :CORRection:COLLect:LEAKage:COMPute

Applicable Models: All with Leakage Cal Application (S9x008B) (Write Only)
computes the leaky coefficients (compute only: it does not store them)  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
Examples |  SENS:CORR:COLL:LEAK:COMP  
Query Syntax |  N/A  
Return Type |  N/A  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  NONE  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:COUNt <NoC>

Applicable Models: All with Leakage Cal Application (S9x008B) (Read-Write)
Sets or queries the number of cal stds  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1..  
<NoC> |  Number of Cal Standard  
Examples |  SENS:CORR:COLL:LEAK:COUNt 3  
Query Syntax |  :SENSe<ch>:CORRection:COLLect:LEAKage:COUNt?  
Return Type |  Integr  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0  
  
* * *

## SENSe :CORRection:COLLect:LEAKage:INITiate <portGroup>

Applicable Models: All with Leakage Cal Application (S9x008B) (Write Only)
create the leaky capability for the current channel. Must be called as first
command always. If the current channel has a calset applied, that calset will
be used as first-tier calset and the leaky calibration will be of type TWOTier
(see :OPT:TYPE?), otherwise the calibration will be ONETier.  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<portGroup> |  Strng list.   
List of the ports involved, grouped in leaky sets of ports, enclosed in square
brackets.  
Ports in the same group are separated by , while groups are separated by
;. Example: [1,2] > 2 ports, single group: leakage will be among the two
ports.  
Example: [1,2; 3,4] > 4 ports, 2 leaky groups [1,2] and [3,4]: leakage will be
among [1,2] and among [3,4] but not between 1 and 3 because those ports belong
to different groups.  
Example: [1,2, 3,4] > 4 ports, single group: leakage among all 4 ports  
Examples |  SENS:CORR:COLL:LEAK:COMP  
Query Syntax |  N/A  
Return Type |  N/A  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  NONE  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:OPTion:RECiprocity:DELay:DATA
<blockData>

Applicable Models: All with Leakage Cal Application (S9x008B) (Write Only)
Specify the data (complex-valued array having the same points as the
calibration stimulus) to be used as delay value  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<blockDatag> |  Complex-valued array having the same points as the calibration stimulus.  
Examples |  SENSe2:CORRection:COLLect:LEAKage:OPTion:RECiprocity:DELay:DATA array()  
Query Syntax |  N/A  
Return Type |  N/A  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:OPTion:RECiprocity:DELay:FILE
<fileName>, <port_i>, <port_j>

Applicable Models: All with Leakage Cal Application (S9x008B) (Write Only)
specifies to use SnP file data as delay value;  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<blockDatag> |  Complex-valued array having the same points as the calibration stimulus.  
<port_i> |  Specify which Sij parameter to use  
<port_j> |  Specify which Sij parameter to use  
Examples |  SENSe2:CORRection:COLLect:LEAKage:OPTion:RECiprocity:DELay:FILE 'C:\temp\delay.s2p', 1, 2  
Query Syntax |  N/A  
Return Type |  N/A  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:OPTion:RECiprocity:DELay:[:VALue]
<delay>

Applicable Models: All with Leakage Cal Application (S9x008B) (Write Only)
sets the delay value in seconds  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<delay> |  Sets the delay value in seconds   
Examples |  SENSe2:CORRection:COLLect:LEAKage:OPTion:RECiprocity:DELay:VALue 0.02  
Query Syntax |  N/A  
Return Type |  N/A  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:OPTion:RECiprocity:PORT <port>

Applicable Models: All with Leakage Cal Application (S9x008B) (Read-Write)
specifies the port that uses the delay settings  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<port> |  Set the port number  
Examples |  SENSe2:CORRection:COLLect:LEAKage:OPTion:RECiprocity:DELay:PORT 1  
Query Syntax |  :SENSe<ch>:CORRection:COLLect:LEAKage:OPTion:RECiprocity:PORT?  
Return Type |  Integer  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:OPTion:TYPE

Applicable Models: All with Leakage Cal Application (S9x008B) (Read Only)
Returns the calibration type, One Tier or Two Tier.  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
Examples |  :SENSe2:CORRection:COLLect:LEAKage:OPTion:TYPE?  
Query Syntax |  :SENSe<ch>:CORRection:COLLect:LEAKage:OPTion:TYPE?  
Return Type |  String (ONETier/TWOTier)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ONETier  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:PORTs

Applicable Models: All with Leakage Cal Application (S9x008B) (Read Only)
Returns the port list and leaky groups  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
Examples |  :SENSe2:CORRection:COLLect:LEAKage:PORTs?  
Query Syntax |  :SENSe<ch>:CORRection:COLLect:LEAKage:PORTs?  
Return Type |  Strng list.   
List of the ports involved, grouped in leaky sets of ports, enclosed in square
brackets.  
Ports in the same group are separated by , while groups are separated by
;. Example: [1,2] > 2 ports, single group: leakage will be among the two
ports.  
Example: [1,2; 3,4] > 4 ports, 2 leaky groups [1,2] and [3,4]: leakage will be
among [1,2] and among [3,4] but not between 1 and 3 because those ports belong
to different groups.  
Example: [1,2, 3,4] > 4 ports, single group: leakage among all 4 ports  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:RESTore <fileName>

Applicable Models: All with Leakage Cal Application (S9x008B) (Write Only)
Resumes data from file  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<fileName> |  file name with .lcg extention.  
Examples |  SENSe2:CORRection:COLLect:LEAKage:RESTore "C:\temp\Mydata.lcg"  
Query Syntax |  N/A  
Return Type |  N/A  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

##

## SENSe<ch>:CORRection:COLLect:LEAKage:SAVE:CSET <fileName>

Applicable Models: All with Leakage Cal Application (S9x008B) (Write Only)
Saves to CalSet from file  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<fileName> |  file name of CalSet  
Examples |  SENSe2:CORRection:COLLect:LEAKage:SAVE:CSET "C:\temp\Mydata.cst"  
Query Syntax |  N/A  
Return Type |  N/A  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:SAVE:FIXture <fileName>

Applicable Models: All with Leakage Cal Application (S9x008B) (Write Only)
Saves to SnP file the leaky box S-parameters. This should be used only for
TWOTIER calibrations.  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<fileName> |  file name of SnP file  
Examples |  SENSe2:CORRection:COLLect:LEAKage:SAVE:CSET "C:\temp\Myfile.s2p"  
Query Syntax |  N/A  
Return Type |  N/A  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:STANdard<std>:DEFinition:DATA:CATalog

Applicable Models: All with Leakage Cal Application (S9x008B) (Read Only) List
the available parameters for the selected standard.  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<std> |  The standard number starts from 1 to the value of :SENSe:CORRection:COLLect:LEAKage:COUNt  
Examples |  SENSe2:CORRection:COLLect:LEAKage:STANdard1:DEFinition:DATA:CATalog?  
Query Syntax |  SENSe<cnum>:CORRection:COLLect:LEAKage:STANdard<std>:DEFinition:DATA:CATalog  
Return Type |  String Example: S1_1, S1_2, S2_1, S2_2  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:STANdard<std>:DEFinition:DATA:CLEar

Applicable Models: All with Leakage Cal Application (S9x008B) (Write Only)
Clears and zeros all definition data for the selected standard  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<std> |  The standard number starts from 1 to the value of :SENSe:CORRection:COLLect:LEAKage:COUNt  
Examples |  SENSe2:CORRection:COLLect:LEAKage:STANdard1:DEFinition:DATA:CLEar  
Query Syntax |  N/A  
Return Type |  N/A  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:STANdard<std>:DEFinition:DATA:LOAD
<fileName>

Applicable Models: All with Leakage Cal Application (S9x008B) (Write Only)
Load the binary data file for the selected standard.  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<std> |  The standard number starts from 1 to the value of :SENSe:CORRection:COLLect:LEAKage:COUNt  
<fileName> |  file name of binary data  
Examples |  SENSe2:CORRection:COLLect:LEAKage:STANdard1:DEFinition:DATA:LOAD "C:\temp\mydata.dat"  
Query Syntax |  N/A  
Return Type |  N/A  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:STANdard<std>:DEFinition:DATA:SAVE
<fileName>

Applicable Models: All with Leakage Cal Application (S9x008B) (Write Only)
Save the binary data file for the selected standard.  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<std> |  The standard number starts from 1 to the value of :SENSe:CORRection:COLLect:LEAKage:COUNt  
<fileName> |  file name of binary data  
Examples |  SENSe2:CORRection:COLLect:LEAKage:STANdard1:DEFinition:DATA:SAVE "C:\temp\mydata.dat"  
Query Syntax |  N/A  
Return Type |  N/A  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:STANdard<std>:DEFinition:DATA:SHOW

Applicable Models: All with Leakage Cal Application (S9x008B) (Write Only)
Displays the definition data in the acquisition channel  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<std> |  The standard number starts from 1 to the value of :SENSe:CORRection:COLLect:LEAKage:COUNt  
Examples |  SENSe2:CORRection:COLLect:LEAKage:STANdard1:DEFinition:DATA:SHOW  
Query Syntax |  N/A  
Return Type |  N/A  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:STANdard<std>:DEFinition:DATA[:VALue]
<param>, <blockdata>

Applicable Models: All with Leakage Cal Application (S9x008B) (Read-Write)
Sets/gets the definition data for the selected parameter (uses block data as
real/imag stream)  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<std> |  The standard number starts from 1 to the value of :SENSe:CORRection:COLLect:LEAKage:COUNt  
<param> |   
<blockdata> |   
Examples |  SENSe2:CORRection:COLLect:LEAKage:STANdard1:DEFinition:DATA:SHOW  
Query Syntax |  SENSe<ch>:CORRection:COLLect:LEAKage:STANdard<std>:DEFinition:DATA[:VALue]?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:STANdard<std>:DEFinition:FILE
<fileName>

Applicable Models: All with Leakage Cal Application (S9x008B) (Write Only)
Load the measurements from SnP file  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<std> |  The standard number starts from 1 to the value of :SENSe:CORRection:COLLect:LEAKage:COUNt  
<fileName> |   
Examples |  SENSe2:CORRection:COLLect:LEAKage:STANdard1:DEFinition:FIlE "c:\temp\Mydata.s2p"  
Query Syntax |  N/A  
Return Type |  N/A  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:STANdard<std>:MEASure:ACQuire <enum>

Applicable Models: All with Leakage Cal Application (S9x008B) (Read-Write)
Make the VNA acquire all measurement data for the selected standard. trigger
is synchronous.  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<std> |  The standard number starts from 1 to the value of :SENSe:CORRection:COLLect:LEAKage:COUNt  
<enum> |  SYNChronous ASYNchronous  
Examples |  SENSe2:CORRection:COLLect:LEAKage:STANdard1:MEASure ASYNchronous  
Query Syntax |  SENSe<ch>:CORRection:COLLect:LEAKage:STANdard<std>:MEASurement:ACQuire?  
Return Type |  String.SYNChronous or ASYNchronous  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  SYNChronous  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:STANdard<std>:MEASure:DATA:CATalog

Applicable Models: All with Leakage Cal Application (S9x008B) (Read Only) List
the available parameters for the selected standard.  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<std> |  The standard number starts from 1 to the value of :SENSe:CORRection:COLLect:LEAKage:COUNt  
Examples |  SENSe2:CORRection:COLLect:LEAKage:STANdard1:MEASure:DATA:CATalog?  
Query Syntax |  SENSe<cnum>:CORRection:COLLect:LEAKage:STANdard<std>:MEASure:DATA:CATalog  
Return Type |  String Example: S1_1, S1_2, S2_1, S2_2  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:STANdard<std>:MEASure:DATA:CLEar

Applicable Models: All with Leakage Cal Application (S9x008B) (Write Only)
Clears and zeros all measurement data for the selected standard  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<std> |  The standard number starts from 1 to the value of :SENSe:CORRection:COLLect:LEAKage:COUNt  
Examples |  SENSe2:CORRection:COLLect:LEAKage:STANdard1:MEASure:DATA:CLEar  
Query Syntax |  N/A  
Return Type |  N/A  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:STANdard<std>:MEASure:DATA:LOAD
<fileName>

Applicable Models: All with Leakage Cal Application (S9x008B) (Write Only)
Load the binary data file for the selected standard.  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<std> |  The standard number starts from 1 to the value of :SENSe:CORRection:COLLect:LEAKage:COUNt  
<fileName> |  file name of binary data  
Examples |  SENSe2:CORRection:COLLect:LEAKage:STANdard1:MEASure:DATA:LOAD "C:\temp\mydata.dat"  
Query Syntax |  N/A  
Return Type |  N/A  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:STANdard<std>:MEASure:DATA:SAVE
<fileName>

Applicable Models: All with Leakage Cal Application (S9x008B) (Write Only)
Save the binary data file for the selected standard.  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<std> |  The standard number starts from 1 to the value of :SENSe:CORRection:COLLect:LEAKage:COUNt  
<fileName> |  file name of binary data  
Examples |  SENSe2:CORRection:COLLect:LEAKage:STANdard1:MEASure:DATA:SAVE "C:\temp\mydata.dat"  
Query Syntax |  N/A  
Return Type |  N/A  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:STANdard<std>:MEASure:DATA:SHOW

Applicable Models: All with Leakage Cal Application (S9x008B) (Write Only)
Displays the measurement data in the acquisition channel  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<std> |  The standard number starts from 1 to the value of :SENSe:CORRection:COLLect:LEAKage:COUNt  
Examples |  SENSe2:CORRection:COLLect:LEAKage:STANdard1:MEASure:DATA:SHOW  
Query Syntax |  N/A  
Return Type |  N/A  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:STANdard<std>:MEASure:DATA[:VALue]
<param>, <blockdata>

Applicable Models: All with Leakage Cal Application (S9x008B) (Read-Write)
Sets/gets the measurement data for the selected parameter (uses block data as
real/imag stream)  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<std> |  The standard number starts from 1 to the value of :SENSe:CORRection:COLLect:LEAKage:COUNt  
<param> |   
<blockdata> |   
Examples |  SENSe2:CORRection:COLLect:LEAKage:STANdard1:MEASure:DATA:SHOW  
Query Syntax |  SENSe<ch>:CORRection:COLLect:LEAKage:STANdard<std>:MEASure:DATA[:VALue]?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:STANdard<std>:MEASure:FILE <fileName>

Applicable Models: All with Leakage Cal Application (S9x008B) (Write Only)
Load the measurements from SnP file  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<std> |  The standard number starts from 1 to the value of :SENSe:CORRection:COLLect:LEAKage:COUNt  
<fileName> |   
Examples |  SENSe2:CORRection:COLLect:LEAKage:STANdard1:MEASure:FIlE "c:\temp\Mydata.s2p"  
Query Syntax |  N/A  
Return Type |  N/A  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:STORe <fileName>

Applicable Models: All with Leakage Cal Application (S9x008B) (Write Only)
Save all data currently acquired, including calibration settings, to file
(binary file); this is used for cal resume/refresh  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<std> |  The standard number starts from 1 to the value of :SENSe:CORRection:COLLect:LEAKage:COUNt  
<fileName> |   
Examples |  SENSe2:CORRection:COLLect:LEAKage:STANdard1:STORe "c:\temp\Mydata.lcg"  
Query Syntax |  N/A  
Return Type |  N/A  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

## SENSe<ch>:CORRection:COLLect:LEAKage:VERify

Applicable Models: All with Leakage Cal Application (S9x008B) (Read Only)
Perform verification on the std list to assess whether those standards are
enough. +1 is returned if success, 0 if failure  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<std> |  The standard number starts from 1 to the value of :SENSe:CORRection:COLLect:LEAKage:COUNt  
<fileName> |   
Examples |  SENSe2:CORRection:COLLect:LEAKage:VERify?  
Query Syntax |  :SENSe<ch>:CORRection:COLLect:LEAKage:VERify?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  N/A  
  
* * *

