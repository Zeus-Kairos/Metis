# Sense:Correction:Collect:Guided:VMC Commands

* * *

Performs a VMC calibration on a frequency converting device.

Note: These commands replace the
[SENSe:CORRectionCOLLect:Session:VMC](CorrCollSessVMC.md) commands. These
commands allow the entire VMC cal to be performed from the Guided cal
interface.

SENSe:CORRection:COLLect:GUIDed:VMC FSIMulator | NETWork | [FILename](CorrCollGuidVMC.md#NetworkFilename) | [MODE](CorrCollGuidVMC.md#NetworkMode) [LO:PCAL[:STATe]](CorrCollGuidVMC.md#LOPwrCal) MIXer | CHARacterize | CAL | [FILename](CorrCollGuidVMC.md#filename) | [OPTion](CorrCollGuidVMC.md#MIX_CHAR_CAL_OPT) | [REVerse](CorrCollGuidVMC.md#Reverse) | ECAL | [PORTmap](CorrCollGuidVMC.md#MIX_ECAL_PortMAP) [OPERation](CorrCollGuidVMC.md#VMC_OPERation)  
---  
  
Click on a red keyword to view the command details.

See Also

  * [All GUIDED Cal commands](CorrGuided.md)

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Learn about VMC Calibration](../../../FreqOffset/VMC_Measurements.md#VMCcalOverview)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:VMC:FSIMulator:NETWork<x>:MODE <char>

Applicable Models: All with VMC Options (S9x083A/B) (Read-Write) Allows you to
embed (add) or de-embed (remove) circuit network effects on the input and
output of your mixer measurement. [Learn
more.](../../../FreqOffset/VMC_Measurements.htm#Waveguide)  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<x> |  Apply network to input or output of mixer. Choose from: 1 - Input of mixer 2 - Output of mixer  
<char> |  Choose from: NONE \- Do nothing with effects of S2P file. EMBed \- Add effects of S2P file from the measurement results. DEEMbed \- Remove effects of S2P file from the measurement results.  
Examples |  SENS:CORR:COLL:GUID:VMC:FSIM:NETW1:MODE EMB  
Query Syntax |  SENS<ch>:CORRection:COLLect:GUIDed:VMC:FSIMulator:NETWork<x>:MODE?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  NONE  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:VMC:FSIMulator:NETWork<x>:FILename
<string>

Applicable Models: All with VMC Options (S9x083A/B) (Read-Write) Specifies the
S2P filename to embed or de-embed on the input or output of your mixer
measurement. [Learn more.](../../../FreqOffset/VMC_Measurements.md#Waveguide)  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1..  
<x> |  Apply network to input or output of mixer. Choose from: 1 - Input of mixer 2 - Output of mixer  
<string> |  Filename of the S2P used for embedding or de-embedding. Use the full path name, file name, and .S2P suffix, enclosed in quotes.  
Examples |  SENS:CORR:COLL:GUID:VMC:FSIM:NETW1:FIL "D:\WaveguideAdapt.S2P"  
Query Syntax |  SENS<ch>:CORRection:COLLect:GUIDed:VMC:FSIMulator:NETWork<x>:FILename?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:VMC:LO<n>:PCAL[:STATe] <bool>

Applicable Models: All with VMC Options (S9x083A/B) (Read-Write) Sets and
returns whether or not the LO power cal step is included in the cal steps when
a VMC cal is performed. [Learn
more.](../../../Applications/Gain_Compression_for_Converters.htm#GCXCal)  
---  
Parameters |   
<cnum> |  Any existing channel number; if unspecified, value is set to 1.  
<n> |  LO Stage. Choose 1.  
<bool> |  LO Power Cal state. Choose from: O or OFF \- Skips over the LO Power Cal when calibrating. 1 or ON \- Includes a step for LO Power Cal when calibrating  
Examples |  SENS:CORR:COLL:GUID:VMC:LO1:PCAL 0  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:VMC:LO<n>:PCAL[:STATe]  
Return Type |  Boolean  
Default |  OFF or 0  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:VMC:MIXer:CHARacterize:CAL:FILename
<string>

Applicable Models: All with VMC Options (S9x083A/B) (Read-Write) Specifies the
.S2P filename used for mixer characterization. Use the
[VMC:MIXer:CHARacterize:CAL:OPTion](CorrCollGuidVMC.md#MIX_CHAR_CAL_OPT)
command to load the file for mixer characterization. Once loaded, use this
command to query the current filename or set a new filename.  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<string> |  Filename of the S2P used for mixer characterization. Use the full path name, file name, and .S2P suffix, enclosed in quotes.  
Examples |  SENS2:CORR:COLL:GUID:VMC:MIXer:CHAR:CAL:FIL "D:\MyMixer.S2P"  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:VMC:MIXer:CHARacterize:CAL:FILename ?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  D:\default.s2p  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:VMC:MIXer:CHARacterize:CAL:OPTion
<char>

Applicable Models: All with VMC Options (S9x083A/B) (Read-Write) Sets the
mixer characterization method to CKIT (ECal or Mechanical) or load a
previously-performed mixer characterization (*.s2p) file. [Learn about the
requirements of the characterization mixer
file](../../../FreqOffset/VMC_Measurements.htm#Select_cal_procedure).  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<char> |  Choose from:

  * CKIT \- Use an ECal or Mechanical Cal Kit for the mixer characterization. Use [SENS:CORR:COLL:GUID:CKIT:PORT](CorrGuided.md#gKit) to specify the cal kit. For the output of the calibration mixer, specify port 3. If port 3 is already used for the output of the DUT mixer, then specify port 4.
  * FILE, <filename> - Retrieve a mixer characterization file. Also specify the filename of the S2P used for mixer characterization. Use the full path name, file name, and .S2P suffix. Use the [VMC:CHARacterize:CAL:FILename](CorrCollGuidVMC.md#filename) command to query the filename.

  
Examples |  SENS:CORR:COLL:GUID:VMC:MIX:CHAR:CAL:OPT CKIT 'or SENS:CORR:COLL:GUID:VMC:MIX:CHAR:CAL:OPT FILE,'D:\Mixer001.s2p'  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:VMC:MIXer:CHARacterize:CAL:OPTion?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  CKIT  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:VMC:MIXer:CHARacterize:CAL:REVerse
<bool>

Applicable Models: All with VMC Options (S9x083A/B) (Read-Write) Specifies the
direction in which to characterize the calibration mixer. [Learn more about
the calibration
mixer.](../../../FreqOffset/VMC_Measurements.htm#Measurement_direction)  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<bool> |  OFF (0) \- Characterize the calibration mixer in the SAME direction as that specified in the mixer setup. ON (1) \- Characterize the calibration mixer in the REVERSE direction as that specified in the mixer setup.  
Examples |  SENS:CORR:COLL:GUID:VMC:MIX:CHAR:CAL:REV 1  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:VMC:MIXer:CHARacterize:CAL:REVerse?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:VMC:MIXer:ECAL:PORTmap <mod>, <string>

Applicable Models: All with VMC Options (S9x083A/B) (Read-Write) Sets the port
mapping for the mixer characterization with ECal. This command is required if
[SENS:CORR:COLL:GUID:VMC:MIX:CHAR:CAL:OPT
ECAL](CorrCollGuidVMC.htm#MIX_CHAR_CAL_OPT) is specified.  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<mod> |  1 \- Electronic Calibration Module  
<string> |  Choose from: "A1" \- ECAL module port A is connected to VNA port 1 "B1" \- ECAL module port B is connected to VNA port 1  
Examples |  SENS2:CORR:COLL:GUID:VMC:MIXer:ECAL:PORTmap 1,"A1"  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:VMC:MIXer:ECAL:PORTmap <mod>?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  "A1"  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:VMC:OPERation <string>

Applicable Models: All with VMC Options (S9x083A/B) (Read-Write) Perform
either full VMC calibration or mixer characterization only.  
---  
Parameters |   
<ch> |  Channel number to be calibrated. If unspecified, value is set to 1.  
<char> |  'CAL' \- full calibration and mixer characterization 'CHAR' \- mixer characterization only (no reference mixer required) - Saves an .S2P file with the filename specified in [SENS<ch>:CORR:COLL:GUID:VMC:CHARacterize:CAL:FILename <filename>](CorrCollGuidVMC.md#filename) . If none is specified, a filename is automatically generated and can be queried using the filename command.  
Examples |  SENS:CORR:COLL:GUID:VMC:OPER 'CAL'  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:VMC:OPERation?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  "CAL"  
  
* * *

