# SENSe:MIXer:SEGMent Commands

* * *

Configures Mixer Segments.

SENSe:MIXer:SEGMent [ADD](MixerSegment.md#Add) [BWIDth](MixerSegment.md#bwid) [CALCulate](MixerSegment.md#calculate) COUNt? [DELete](MixerSegment.md#delete) | [ALL](MixerSegment.md#DeleteAll) [IF:FREQ:SIDeband](MixerSegment.md#IF_SIDE) INPut:FREQ: | [FIXed](MixerSegment.md#InputFixed) | [MODE](MixerSegment.md#InputMode) | [STARt](MixerSegment.md#INPut_START) | [STOP](MixerSegment.md#inputStopFreq) [INPut:POWer](MixerSegment.md#InputPower) LO:FREQ: | [FIXed](MixerSegment.md#LOFixFreq) | [ILTI](MixerSegment.md#loILTI) | [MODE](MixerSegment.md#LOFreqMode) | [STARt](MixerSegment.md#LOStart) | [STOP](MixerSegment.md#LoStop) [LO:POWer](MixerSegment.md#LOPower) OUTPut:FREQ: | [FIXed](MixerSegment.md#OutputFixed) | [MODE](MixerSegment.md#OutputFreqMode) | [SIDeband](MixerSegment.md#OutputSideband) | [STARt](MixerSegment.md#OutputFreqStart) | [STOP](MixerSegment.md#OutputFreqStop) [OUTPut:POWer](MixerSegment.md#OutputPower) [POINts](MixerSegment.md#Points) [STATe](MixerSegment.md#State)  
---  
  
Click on a red keyword to view the command details.

See Also

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Learn about the Frequency Converter Application](../../../FreqOffset/FCA_Use.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

### Scratch vs Applied Mixer Properties

Each mixer configuration has two sets of properties:

  1. Scratch mixer contains the properties that have been set, but NOT YET applied. Send the [SENSe<ch>:MIXer:APPLy](MIXerSCPI.md#apply) command to copy these properties to the Applied mixer.
  2. Applied mixer contains the properties that makeup the current mixer configuration.

Power settings are immediately applied to both the Scratch and Applied mixer.
A successful [Calculate](MIXerSCPI.md#calc) also perform an Apply. Note:
Queries always return the Applied mixer properties. Therefore, first send
[SENSe<ch>:MIXer:APPLy](MIXerSCPI.md#apply) before querying new settings.  
---  
  
* * *

## SENSe<ch>:MIXer:SEGMent<n>:ADD <value>

Applicable Models: All (Write only) Adds the specified number of segments to
the scratch mixer beginning at the last segment position. All segments are
added with default settings.  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
<n> |  Position at which to add segments. Valid range is between 1 and the current segment count +1. Using count +1 adds segments to the end of the segment table. Use [SENS:MIX:SEGM:COUN?](MixerSegment.md#count) to read the current count in the Applied Mixer.  
<value> |  Optional argument. Number of segments to add. If unspecified, 1 segment is added.  
Examples |  SENS:MIX:SEGM1:ADD 3 'Adds 3 segments beginning at position 1. For a preset state, this results in a total of 4 segments.  
Query Syntax |  Not Applicable  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:MIXer:SEGMent<n>:BWIDth <value>

Applicable Models: All (Read/Write) Sets and returns the IF Bandwidth for the
sweep segment.  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
<n> |  Existing segment for which IF Bandwidth is to be set. Use [SENS:MIX:SEGM:COUN?](MixerSegment.md#count) to read the current count in the Applied Mixer.  
<value> |  IF Bandwidth in Hz. The list of valid IF Bandwidths is different depending on the VNA model. [(Click to see the lists.)](../../../S2_Opt/Trce_Noise.md#IFDiag) If an invalid number is specified, the analyzer will round up to the closest valid number. This parameter supports MIN and MAX as arguments. [Learn more.](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min)  
Examples |  SENS:MIX:SEGM1:BWID 1e3  
Query Syntax |  SENSe<ch>:MIXer:SEGMent<n>:BWIDth? Send [Apply](MIXerSCPI.md#apply) before sending this query. [Learn more](MixerSegment.md#Scratch).  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  10 kHz  
  
* * *

## SENSe<ch>:MIXer:SEGMent<n>:CALCulate <char>

Applicable Models: All (Write only) Calculates the Input, IF, or Output
frequencies of the mixer setup and updates the channel settings.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<n> |  Existing segment to calculate. Use [SENS:MIX:SEGM:COUN?](MixerSegment.md#count) to read the current count in the Applied Mixer.  
<char> |  Mixer port to be calculated. Choose from: |  <char> |  1st or only stage requires: |  In addition, 2nd stage requires:  
---|---|---  
INPut | 

  * Output Start and Stop frequencies
  * LO frequency
  * Output sideband (High or Low)

|

  * IF Start and Stop frequencies
  * 2nd LO frequency
  * IF sideband (High or Low)

  
BOTH |  NA | 

  * IF Start and Stop frequencies
  * Both LO frequencies

  
OUTPut | 

  * Input Start and Stop frequencies
  * LO frequency
  * Output sideband (High or Low)

|

  * IF Start and Stop frequencies
  * 2nd LO frequency
  * IF sideband (High or Low)

  
LO_1 | 

  * Input Start and Stop frequencies
  * Output frequency
  * Output sideband (High or Low)

|

  * IF Start and Stop frequencies
  * 2nd LO frequency
  * IF sideband (High or Low)

  
LO_2 |  NA | 

  * Input Start and stop frequencies
  * 1st LO start and stop frequencies
  * Output frequency
  * IF sideband(High or Low
  * Output sideband(High or Low)

  
Examples |  SENS:MIX:SEGM2:CALC Output  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:MIXer:SEGMent:COUNt?

Applicable Models: All (Read-only) Returns the number of segments on the
[Applied mixer](MixerSegment.md#Scratch).  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
Examples |  SENS:MIX:SEGM:COUN?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
![](../../../assets/images/Programming/Tp.gif)

* * *

## SENSe<ch>:MIXer:SEGMent<n>:DELete <value>

Applicable Models: All (Write only) Removes the specified number of segments
from the [scratch
mixer](../../COM_Reference/Objects/Converter_Object.htm#Scratch) starting at
the index position.  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
<n> |  Position at which to start removing segments. Valid index range is between 1 and the current segment count. Use [SENS:MIX:SEGM:COUN?](MixerSegment.md#count) to read the current count in the Applied Mixer.  
<value> |  Optional argument. Number of segments to remove. If unspecified, 1 segment is removed.  
Examples |  SENS:MIX:SEGM1:DEL 5 'Removes 5 segments beginning at the first position.  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:MIXer:SEGMent:DELete:ALL

Applicable Models: All (Write only) Removes all segments from the [scratch
mixer](../../COM_Reference/Objects/Converter_Object.htm#Scratch).  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
Examples |  SENS:MIX:SEGM:DEL:ALL  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:MIXer:SEGMent<n>:DWELI

Applicable Models: All (Read-Write) Sets or returns the Input sweep mode of
the segment.  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
<n> |  Existing segment for which Input frequency mode is to be set. Use SENS:MIX:SEGM:COUN? to read the current count in the Applied Mixer.  
Examples |  SENS:MIX:SEGM2:DWELI  
Query Syntax |  SENSe<ch>:MIXer:SEGMent<n>:DWELI? Send [Apply](MIXerSCPI.md#apply) before sending this query. Learn more.  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Swept  
  
* * *

## SENSe<ch>:MIXer:SEGMent<n>:IF:FREQuency:SIDeband <char>

Applicable Models: All (Read-Write) When [two LO stages are
used](MIXerSCPI.htm#Stage), sets or returns whether to select the sum or
difference for the IF1 product. (Input + or - LO1 = IF1)

  * This setting corresponds to the ![](../../../assets/images/mixerMinus.gif) buttons on LO1 on the [Mixer Setup](../../../Applications/MixerConverter_Setup.md#MixerSetupTab) dialog.
  * This setting is ignored when [ONE LO stage](MIXerSCPI.md#Stage) is selected.
  * Also set [SENS:MIX:OUTP:FREQ:SID](MIXerSCPI.md#OUTput_SIDE) to LOW or HIGH to set the output frequency of the mixer.

  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
<n> |  Existing segment for which IF Sideband is to be set. Use [SENS:MIX:SEGM:COUN?](MixerSegment.md#count) to read the current count in the Applied Mixer.  
<char> |  Sideband value. Choose from LOW \- Difference (-) HIGH \- Sum (+)  
Examples |  SENS:MIX:SEGM2:IF:FREQ:SID LOW  
Query Syntax |  SENSe<ch>:MIXer:SEGMent<n>:IF:FREQuency:SIDeband? Send [Apply](MIXerSCPI.md#apply) before sending this query. [Learn more](MixerSegment.md#Scratch).  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  LOW  
  
* * *

## SENSe<ch>:MIXer:SEGMent<n>:INPut:FREQuency:FIXed <value>

Applicable Models: All (Read-Write) Sets or returns the Input fixed frequency
of the segment. Also, set [SENS:MIX:SEGM:INP:FREQ:MODE
FIXED](MixerSegment.htm#InputMode).  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
<n> |  Existing segment for which input fixed frequency is to be set. Use [SENS:MIX:SEGM:COUN?](MixerSegment.md#count) to read the current count in the Applied Mixer.  
<value> |  Input fixed frequency. Choose a value between the start and stop frequency of the VNA.  
Examples |  SENSe2:MIXer:SEGMent2:INPut:FREQ:FIX 1e9  
Query Syntax |  SENSe<ch>:MIXer:SEGMent<n>:INPut:FREQuency:FIXed? Send [Apply](MIXerSCPI.md#apply) before sending this query. [Learn more](MixerSegment.md#Scratch).  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Start frequency of the VNA.  
  
* * *

## SENSe<ch>:MIXer:SEGMent<n>:INPut:FREQuency:MODE <char>

Applicable Models: All (Read-Write) Sets or returns the Input sweep mode of
the segment.  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
<n> |  Existing segment for which Input frequency mode is to be set. Use [SENS:MIX:SEGM:COUN?](MixerSegment.md#count) to read the current count in the Applied Mixer.  
<char> |  Input sweep mode. Choose either FIXED or SWEPT  
Examples |  SENS:MIX:SEGM2:INP:FREQ:MODE FIXED  
Query Syntax |  SENSe<ch>:MIXer:SEGMent<n>:INPut:FREQuency:MODE? Send [Apply](MIXerSCPI.md#apply) before sending this query. [Learn more](MixerSegment.md#Scratch).  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Swept  
  
* * *

## SENSe<ch>:MIXer:SEGMent<n>:INPut:FREQuency:STARt <value>

Applicable Models: All (Read-Write) Sets or returns the Input start frequency
value of the segment. Also, set [SENS:MIX:SEGM:FREQ:MODE
SWEPT](MixerSegment.htm#InputMode).  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
<n> |  Existing segment for which Input start frequency is to be set. Use [SENS:MIX:SEGM:COUN?](MixerSegment.md#count) to read the current count in the Applied Mixer.  
<value> |  Input Start frequency. Choose a value between the start and stop frequency of the VNA.  
Examples |  SENSe2:MIXer:SEGMent2:INPut:FREQ:STARt 1000000000  
Query Syntax |  SENSe<ch>:MIXer:SEGMent<n>:INPut:FREQuency:STARt? Send [Apply](MIXerSCPI.md#apply) before sending this query. [Learn more](MixerSegment.md#Scratch).  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Start frequency of the VNA.  
  
* * *

## SENSe<ch>:MIXer:SEGMent<n>:INPut:FREQuency:STOP <value>

Applicable Models: All (Read-Write) Sets or returns the Input stop frequency
value of the segment.  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
<n> |  Existing segment for which Input stop frequency is to be set. Use [SENS:MIX:SEGM:COUN?](MixerSegment.md#count) to read the current count in the Applied Mixer.  
<value> |  Input Stop frequency. Choose a value between the start and stop frequency of the VNA.  
Examples |  SENSe2:MIXer:SEGMent2:INPut:FREQ:STOP 1000000000  
Query Syntax |  SENSe<ch>:MIXer:SEGMent<n>:INPut:FREQuency:STOP? Send [Apply](MIXerSCPI.md#apply) before sending this query. [Learn more](MixerSegment.md#Scratch).  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Stop frequency of the VNA.  
  
* * *

## SENSe<ch>:MIXer:SEGMent<n>:INPut:POWer <value>

Applicable Models: All (Read-Write) Sets or returns the Input power value of
the segment.  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
<n> |  Existing segment for which Input power is to be set. Use [SENS:MIX:SEGM:COUN?](MixerSegment.md#count) to read the current count in the Applied Mixer.  
<value> |  Input power level in dBm. Choose a value within the power range of the VNA.  
Examples |  SENSe2:MIXer:SEGMent2:INPut:POWer 0  
Query Syntax |  SENSe<ch>:MIXer:SEGMent<n>:INPut:POWer? Send [Apply](MIXerSCPI.md#apply) before sending this query. [Learn more](MixerSegment.md#Scratch).  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  -15 dBm  
  
* * *

## SENSe<ch>:MIXer:SEGMent<n>:LO<x>:FREQuency:FIXed <value>

Applicable Models: All (Read-Write) Sets or returns the LO1 and LO2 fixed
frequency value of the segment.  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
<n> |  Existing segment for which the LO1 and LO2 fixed frequency value is to be set. Use [SENS:MIX:SEGM:COUN?](MixerSegment.md#count) to read the current count in the Applied Mixer.  
<x> |  LO stage number for which the fixed frequency is to be set. Choose 1 or 2. Set number of stages for the mixer using [SENSe<ch>:MIXer:STAGe](MIXerSCPI.md#Stage).  
<value> |  The LO1 and LO2 fixed frequency value in Hz. Choose a value within the frequency range of the source.  
Examples |  SENSe2:MIXer:SEGMent2:LO1:FREQ:FIX 1e9  
Query Syntax |  SENSe<ch>:MIXer:SEGMent<n>:LO<x>:FREQuency:FIXed? Send [Apply](MIXerSCPI.md#apply) before sending this query. [Learn more](MixerSegment.md#Scratch).  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0 Hz  
  
* * *

## SENSe<ch>:MIXer:SEGMent<n>:LO<x>:FREQuency:ILTI <bool>

Applicable Models: All (Read-Write) Specifies whether to use the Input
frequency that is greater than the LO or less than the LO. To learn more, see
the [mixer
setup](../../../Applications/MixerConverter_Setup.htm#MixerSetupTab) dialog
box help.  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
<n> |  Existing segment for which the LO1 and LO2 fixed frequency value is to be set. Use [SENS:MIX:SEGM:COUN?](MixerSegment.md#count) to read the current count in the Applied Mixer.  
<x> |  LO stage number for which ILT is to be set. Choose 1 or 2. Set number of stages for the mixer using [SENSe<ch>:MIXer:STAGe](MIXerSCPI.md#Stage).  
<bool> |  ON (1) \- Use the Input that is Greater than the specified LO. OFF (0) \- Use the Input that is Less than the specified LO.  
Examples |  SENSe2:MIXer:SEGMent2:LO1:FREQ:ILTI 1  
Query Syntax |  SENSe<ch>:MIXer:SEGMent<n>:LO<x>:FREQuency:ILTI? Send [Apply](MIXerSCPI.md#apply) before sending this query. [Learn more](MixerSegment.md#Scratch).  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## SENSe<ch>:MIXer:SEGMent<n>:LO<x>:FREQuency:MODE <char>

Applicable Models: All (Read-Write) Sets or returns the LO1 or LO2 sweep mode
of the segment.  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
<n> |  Existing segment for which LO frequency mode is to be set. Use [SENS:MIX:SEGM:COUN?](MixerSegment.md#count) to read the current count in the Applied Mixer.  
<x> |  LO stage number for which ILT is to be set. Choose 1 or 2. Set number of stages for the mixer using [SENSe<ch>:MIXer:STAGe](MIXerSCPI.md#Stage).  
<char> |  LO sweep mode. Choose either FIXED or SWEPT  
Examples |  SENS:MIX:SEGM2:LO1:FREQ:MODE FIXED  
Query Syntax |  SENSe<ch>:MIXer:SEGMent<n>:LO<n>:FREQuency:MODE? Send [Apply](MIXerSCPI.md#apply) before sending this query. [Learn more](MixerSegment.md#Scratch).  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Fixed  
  
* * *

## SENSe<ch>:MIXer:SEGMent<n>:LO<x>:FREQuency:STARt <value>

Applicable Models: All (Read-Write) Sets or returns the LO start frequency
value of the segment.  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
<n> |  Existing segment for which LO start frequency is to be set. Use [SENS:MIX:SEGM:COUN?](MixerSegment.md#count) to read the current count in the Applied Mixer.  
<x> |  LO stage number. Choose 1 or 2. Set number of stages for the mixer using [SENSe<ch>:MIXer:STAGe](MIXerSCPI.md#Stage).  
<value> |  LO Start frequency. Choose a value between the start and stop frequency of the VNA.  
Examples |  SENSe2:MIXer:SEGMent2:LO1:FREQ:STARt 1000000000  
Query Syntax |  SENSe<ch>:MIXer:SEGMent<n>:LO<x>:FREQuency:STARt? Send [Apply](MIXerSCPI.md#apply) before sending this query. [Learn more](MixerSegment.md#Scratch).  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Start frequency of the VNA.  
  
* * *

## SENSe<ch>:MIXer:SEGMent<n>:LO<x>:FREQuency:STOP <value>

Applicable Models: All (Read-Write) Sets or returns the LO stop frequency
value of the segment.  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
<n> |  Existing segment for which LO stop frequency is to be set. Use [SENS:MIX:SEGM:COUN?](MixerSegment.md#count) to read the current count in the Applied Mixer.  
<x> |  LO stage number. Choose 1 or 2. Set number of stages for the mixer using [SENSe<ch>:MIXer:STAGe](MIXerSCPI.md#Stage).  
<value> |  LO Stop frequency. Choose a value between the start and stop frequency of the VNA.  
Examples |  SENSe2:MIXer:SEGMent2:LO<x>:FREQ:STOP 1000000000  
Query Syntax |  SENSe<ch>:MIXer:SEGMent<n>:LO<x>:FREQuency:STOP? Send [Apply](MIXerSCPI.md#apply) before sending this query. [Learn more](MixerSegment.md#Scratch).  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Stop frequency of the VNA.  
  
* * *

## SENSe<ch>:MIXer:SEGMent<n>:LO<x>:POWer <value>

Applicable Models: All (Read-Write) Sets or returns the LO power of the
segment.  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
<n> |  Existing segment for which LO power is to be set. Use [SENS:MIX:SEGM:COUN?](MixerSegment.md#count) to read the current count in the Applied Mixer.  
<x> |  LO stage number. Choose 1 or 2. Set number of stages for the mixer using [SENSe<ch>:MIXer:STAGe](MIXerSCPI.md#Stage).  
<value> |  LO power level in dBm. Choose a value within the power range of the VNA.  
Examples |  SENSe2:MIXer:SEGMent2:INPut:POWer 0  
Query Syntax |  SENSe<ch>:MIXer:SEGMent<n>:INPut:POWer? Send [Apply](MIXerSCPI.md#apply) before sending this query. [Learn more](MixerSegment.md#Scratch).  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  -10 dBm  
  
* * *

## SENSe<ch>:MIXer:SEGMent<n>:OUTPut:FREQuency:FIXed <value>

Applicable Models: All (Read-Write) Sets or returns the Output fixed frequency
of the segment. Also, set [SENS:MIX:SEGM:INP:FREQ:MODE
FIXED](MixerSegment.htm#InputMode).  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
<n> |  Existing segment for which Output fixed frequency is to be set. Use [SENS:MIX:SEGM:COUN?](MixerSegment.md#count) to read the current count in the Applied Mixer.  
<value> |  Output fixed frequency. Choose a value between the start and stop frequency of the VNA.  
Examples |  SENSe2:MIXer:SEGMent2:OUTP:FREQ:FIX 1e9  
Query Syntax |  SENSe<ch>:MIXer:SEGMent<n>:OUTPut:FREQuency:FIXed? Send [Apply](MIXerSCPI.md#apply) before sending this query. [Learn more](MixerSegment.md#Scratch).  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Start frequency of the VNA.  
  
* * *

## SENSe<ch>:MIXer:SEGMent<n>:OUTPut:FREQuency:MODE <char>

Applicable Models: All (Read-Write) Sets or returns the Output sweep mode of
the segment.  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
<n> |  Existing segment for which Output frequency mode is to be set. Use [SENS:MIX:SEGM:COUN?](MixerSegment.md#count) to read the current count in the Applied Mixer.  
<char> |  Output sweep mode. Choose either FIXED or SWEPT  
Examples |  SENS:MIX:SEGM2:OUTP:FREQ:MODE FIXED  
Query Syntax |  SENSe<ch>:MIXer:SEGMent<n>:OUTPut:FREQuency:MODE? Send [Apply](MIXerSCPI.md#apply) before sending this query. [Learn more](MixerSegment.md#Scratch).  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Swept  
  
* * *

## SENSe<ch>:MIXer:SEGMent<n>:OUTPut:FREQuency:SIDeband <char>

Applicable Models: All (Read-Write) When [two LO stages are
used](MIXerSCPI.htm#Stage), sets or returns whether to select the sum or
difference for the Output product. Use for both 1 or 2 stage mixers.

  * This setting corresponds to the ![](../../../assets/images/mixerMinus.gif) buttons on the Output on the [Mixer Frequency](../../../Applications/MixerConverter_Setup.md#MixerFreqTab) dialog.
  * Also set [SENS:MIX:IF:FREQ:SID](MixerSegment.md#IF_SIDE) to LOW or HIGH to determine the IF frequency for 2-stage mixers.

  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
<n> |  Existing segment for which Output Sideband is to be set. Use [SENS:MIX:SEGM:COUN?](MixerSegment.md#count) to read the current count in the Applied Mixer.  
<char> |  Sideband value. Choose from LOW \- Difference (-) HIGH \- Sum (+)  
Examples |  SENS:MIX:SEGM2:OUTP:FREQ:SID LOW  
Query Syntax |  SENSe<ch>:MIXer:SEGMent<n>:OUTPut:FREQuency:SIDeband? Send [Apply](MIXerSCPI.md#apply) before sending this query. [Learn more](MixerSegment.md#Scratch).  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  LOW  
  
* * *

## SENSe<ch>:MIXer:SEGMent<n>:OUTPut:FREQuency:STARt <value>

Applicable Models: All (Read-Write) Sets or returns the Output start frequency
value of the segment. Also, set [SENS:MIX:SEGM:FREQ:MODE
SWEPT](MixerSegment.htm#InputMode).  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
<n> |  Existing segment for which Output start frequency is to be set. Use [SENS:MIX:SEGM:COUN?](MixerSegment.md#count) to read the current count in the Applied Mixer.  
<value> |  Output Start frequency. Choose a value between the start and stop frequency of the VNA.  
Examples |  SENSe2:MIXer:SEGMent2:OUTPut:FREQ:STARt 1000000000  
Query Syntax |  SENSe<ch>:MIXer:SEGMent<n>:OUTPut:FREQuency:STARt? Send [Apply](MIXerSCPI.md#apply) before sending this query. [Learn more](MixerSegment.md#Scratch).  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Start frequency of the VNA.  
  
* * *

## SENSe<ch>:MIXer:SEGMent<n>:OUTPut:FREQuency:STOP <value>

Applicable Models: All (Read-Write) Sets or returns the Output stop frequency
value of the segment.  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
<n> |  Existing segment for which Output stop frequency is to be set. Use [SENS:MIX:SEGM:COUN?](MixerSegment.md#count) to read the current count in the Applied Mixer.  
<value> |  Output Stop frequency. Choose a value between the start and stop frequency of the VNA.  
Examples |  SENSe2:MIXer:SEGMent2:OUTPut:FREQ:STOP 1000000000  
Query Syntax |  SENSe<ch>:MIXer:SEGMent<n>:OUTPut:FREQuency:STOP? Send [Apply](MIXerSCPI.md#apply) before sending this query. [Learn more](MixerSegment.md#Scratch).  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Stop frequency of the VNA.  
  
* * *

## SENSe<ch>:MIXer:SEGMent<n>:OUTPut:POWer <value>

Applicable Models: All (Read-Write) Sets or returns the Output power value of
the segment.  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
<n> |  Existing segment for which Output power is to be set. Use [SENS:MIX:SEGM:COUN?](MixerSegment.md#count) to read the current count in the Applied Mixer.  
<value> |  Output power level in dBm. Choose a value within the power range of the VNA.  
Examples |  SENSe2:MIXer:SEGMent2:OUTPut:POWer 0  
Query Syntax |  SENSe<ch>:MIXer:SEGMent<n>:OUTPut:POWer? Send [Apply](MIXerSCPI.md#apply) before sending this query. [Learn more](MixerSegment.md#Scratch).  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  -10 dBm  
  
* * *

## SENSe<ch>:MIXer:SEGMent<n>:POINts <value>

Applicable Models: All (Read/Write) Sets and returns the number of data points
for the sweep segment.  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
<n> |  Existing segment for which number of points is to be set. Use [SENS:MIX:SEGM:COUN?](MixerSegment.md#count) to read the current count in the Applied Mixer.  
<value> |  Number of data points. Choose any number between 1 and the [VNA maximum number of points.](../../../S1_Settings/DPoints.md#PointsDiag) This parameter supports MIN and MAX as arguments. [Learn more.](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min)  
Examples |  SENS:MIX:SEGM1:POIN 3  
Query Syntax |  SENSe<ch>:MIXer:SEGMent<n>:POINts? Send [Apply](MIXerSCPI.md#apply) before sending this query. [Learn more](MixerSegment.md#Scratch).  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  21  
  
* * *

## SENSe<ch>:MIXer:SEGMent<n>:STATe <bool>

Applicable Models: All (Read/Write) Sets and returns the ON/OFF state for the
segment.  
---  
Parameters |   
<ch> |  Channel number of the mixer measurement. If unspecified, value is set to 1.  
<n> |  Existing segment to be set ON or OFF. Use [SENS:MIX:SEGM:COUN?](MixerSegment.md#count) to read the current count in the Applied Mixer.  
<bool> |  Segment state. Choose from: ON (or 1) - Turns the segment ON. OFF (or 0) - Turns the segment OFF  
Examples |  SENS:MIX:SEGM1:STATe 1  
Query Syntax |  SENSe<ch>:MIXer:SEGMent<n>:STATe? Send [Apply](MIXerSCPI.md#apply) before sending this query. [Learn more](MixerSegment.md#Scratch).  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

* * *

