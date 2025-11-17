# Sense:Mixer Commands

* * *

Performs Mixer setup and configuration.

SENSe:MIXer: [APPLy](MIXerSCPI.md#apply) [AVOidspurs](MIXerSCPI.md#avoid) [CALCulate](MIXerSCPI.md#calc) [DISCard](MIXerSCPI.md#discard) [ELO - More Commands](MixrEmbedLO.md) IF:FREQ: | [SIDeband](MIXerSCPI.md#IF_SIDE) | [STARt](MIXerSCPI.md#IF_START) | [STOP](MIXerSCPI.md#IF_STOP) INPut:FREQ: | [DENominator](MIXerSCPI.md#INPut_DEN) | [FIXed](MIXerSCPI.md#INPut_FIX) | [MODE](MIXerSCPI.md#InputMode) | [NUMerator](MIXerSCPI.md#INPut_NUM) | [STARt](MIXerSCPI.md#INPut_START) | [STOP](MIXerSCPI.md#INPut_STOP) [INPut:POWer](MIXerSCPI.md#INPut_POWer) | STARt | STOP | [USENominal](MIXerSCPI.md#UseNominal) LO:FREQ: | [DENominator](MIXerSCPI.md#LO_DEN) | [FIXed](MIXerSCPI.md#LO_FIX) | [ILTI](MIXerSCPI.md#ilti) | [MODE](MIXerSCPI.md#LoMode) | [NUMerator](MIXerSCPI.md#LO_NUM) | [STARt](MIXerSCPI.md#LO_Start) | [STOP](MIXerSCPI.md#LO_stop) [LO:NAME](MIXerSCPI.md#name) [LO:POWer](MIXerSCPI.md#LO_POWer) | [STARt](MIXerSCPI.md#LOPowerStart) | [STOP](MIXerSCPI.md#LOPowerStop) [LOAD](MIXerSCPI.md#Load) [NORMalize:POINt](MIXerSCPI.md#Normalize) OUTPut:FREQ: | [FIXed](MIXerSCPI.md#Out_Fix) | [MODE](MIXerSCPI.md#OutputMode) | [SIDeband](MIXerSCPI.md#OUTput_SIDE) | [STARt](MIXerSCPI.md#OUTput_START) | [STOP](MIXerSCPI.md#OUTput_STOP) PHASe | [[:STATe]](MIXerSCPI.md#Phase) | ABSolute | [:STATe] [PMAP](MIXerSCPI.md#pmap) | [INPut](MIXerSCPI.md#PmapInput) | [OUTPut](MIXerSCPI.md#pmapOutput) [RECalculate](MIXerSCPI.md#Recalc) [REVerse](MIXerSCPI.md#Reverse) ROLE | [CATalog?](MIXerSCPI.md#RoleCat) | [DEVice](MIXerSCPI.md#RoleDevice) [SAVE](MIXerSCPI.md#Save) [SEGMent More Commands](MixerSegment.md) [STAGe](MIXerSCPI.md#Stage) (number of LOs) [XAXis](MIXerSCPI.md#X)  
---  
  
Click on a keyword to view the command details.

See Also

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Learn about the Frequency Converter Application](../../../FreqOffset/FCA_Use.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

Note: If you are changing several mixer configuration settings, you can make
all the changes first and then issue the [Calculate](MIXerSCPI.md#calc) and
[Apply](MIXerSCPI.md#apply) commands as you would do from the user interface.

* * *

## SENSe<ch>:MIXer:APPLy

Applicable Models: All (Write only) Applies the mixer setup settings and turns
the channel ON. (Performs the same function as the Apply button on the [mixer
setup dialog
box](../../../Applications/MixerConverter_Setup.htm#Mixer_setup_help)).  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
Examples | SENS:MIX:APPL  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:AVOidspurs <bool>

Applicable Models: N522xB, N523xB, N524xB (Read Write) Sets and returns the
state of the avoid spurs feature. [Learn more about avoid
spurs.](../../../FreqOffset/FCA_Use.htm#Avoid)  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<bool> | Avoid spurs state. Choose from 0 - Avoid spurs OFF 1 - Avoid spurs ON  
Examples | SENS:MIX:AVO sense2:mixer:avoidspurs 1  
Query Syntax | SENSe<ch>:MIXer:AVOidspurs?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 (OFF)  
  
* * *

## SENSe<ch>:MIXer:CALCulate <char>

Applicable Models: All (Write only) Calculates the Input, IF, or Output
frequencies of the mixer setup and updates the channel settings. Note: The
target mode must be swept. This command does not allow calculation of fixed
values.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<char> | Mixer port to be calculated. Choose from: | <char> | 1st or only stage requires: | In addition, 2nd stage requires:  
---|---|---  
INPut | 

  * Output Start/Stop/Fixed frequencies
  * LO Start/Stop/Fixed frequencies
  * Output sideband (High or Low)

|

  * IF Start/Stop/Fixed frequencies
  * 2nd Start/Stop/Fixed frequencies
  * IF sideband (High or Low)

  
BOTH | NA | 

  * IF Start/Stop/Fixed frequencies
  * Both Start/Stop/Fixed frequencies

  
OUTPut | 

  * Input Start/Stop/Fixed frequencies
  * LO Start/Stop/Fixed frequencies
  * Output sideband (High or Low)

|

  * IF Start/Stop/Fixed frequencies
  * 2nd Start/Stop/Fixed frequencies
  * IF sideband (High or Low)

  
LO_1 | 

  * Input Start/Stop/Fixed frequencies
  * Output Start/Stop/Fixed frequencies
  * Output sideband (High or Low)

|

  * IF Start/Stop/Fixed frequencies
  * 2nd Start/Stop/Fixed frequencies
  * IF sideband (High or Low)

  
LO_2 | NA | 

  * Input Start/Stop/Fixed frequencies
  * 1st LO Start/Stop/Fixed frequencies
  * Output Start/Stop/Fixed frequencies
  * IF sideband(High or Low
  * Output sideband(High or Low)

  
Examples | SENS:MIX:CALC Output  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:DISCard

Applicable Models: All (Write only) Cancels changes that have been made to the
Converter setup and reverts to the previously-saved setup. Same as the Cancel
button on the [mixer setup dialog
box](../../../Applications/MixerConverter_Setup.htm#Mixer_setup_help).  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
Examples | SENS:MIX:DISC  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:IF:FREQuency:SIDeband <char>

Applicable Models: All (Read-Write) When [two LO stages are
used](MIXerSCPI.htm#Stage), sets or returns whether to select the sum or
difference for the IF1 product. (Input + or - LO1 = IF1)

  * This setting corresponds to the ![](../../../assets/images/mixerMinus.gif) buttons on LO1 on the [Mixer setup dialog](../../../Applications/MixerConverter_Setup.md#Mixer_setup_help)
  * This setting is ignored when [ONE LO stage](MIXerSCPI.md#Stage) is selected.
  * Also set [SENS:MIX:OUTP:FREQ:SID](MIXerSCPI.md#OUTput_SIDE) to LOW or HIGH to determine the output frequency of the mixer.

[See Note](MIXerSCPI.md#Note)  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<char> | Sideband value. Choose from LOW \- Difference (-) HIGH \- Sum (+)  
Examples | SENS:MIX:IF:FREQ:SID LOW  
SENSe2:MIXer:IF:FREQ:SIDeband HIGH  
Query Syntax | SENSe<ch>:MIXer:IF:FREQuency:SIDeband?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | LOW  
  
* * *

## SENSe<ch>:MIXer:IF:FREQuency:STARt <num>

Applicable Models: All (Read-Write) Sets or returns the IF start frequency
value of the mixer. [See Note](MIXerSCPI.md#Note)  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<num> | IF Start Frequency value  
Examples | SENS:MIX:IF:FREQ:STAR 1e9  
SENSe2:MIXer:IF:FREQ:STARt 1000000000  
Query Syntax | SENSe<ch>:MIXer:IF:FREQuency:STARt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:IF:FREQuency:STOP <num>

Applicable Models: All (Read-Write) Sets or returns the stop frequency value
of the mixer IF frequency. [See Note](MIXerSCPI.md#Note)  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<num> | IF Stop Frequency value  
Examples | SENS:MIX:IF:FREQ:STOP 2e9  
SENSe2:MIXer:IF:FREQ:STOP 2000000000  
Query Syntax | SENSe<ch>:MIXer:IF:FREQuency:STOP?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:INPut:FREQuency:DENominator <value>

Applicable Models: All (Read-Write) Sets or returns the denominator value of
the Input Fractional Multiplier. [See Note](MIXerSCPI.md#Note)  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<value> | Input denominator value.  
Examples | SENS:MIX:INP:FREQ:DEN 5  
SENS2:MIXer:INPut:FREQ:DENominator 4  
Query Syntax | SENSe<ch>:MIXer:INPut:FREQuency:DENominator?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:INPut:FREQuency:FIXed<value>

Applicable Models: All (Read-Write) Sets or returns the fixed frequency of the
input. [See Note](MIXerSCPI.md#Note)  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<value> | Input frequency.  
Examples | SENSe:MIXer:INPut:FREQ:FIXed 1e9  
SENSe2:MIXer:INPut:FREQ:FIXed 1000000000  
Query Syntax | SENSe<ch>:MIXer:INPut:FREQuency:FIXed?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:INPut:FREQuency:MODE <char>

Applicable Models: All (Read-Write) Sets or returns the Input sweep mode.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<char> | Input sweep mode. Choose either FIXED or SWEPT  
Examples | SENS:MIX:INP:FREQ:MODE FIXED  
SENSe2:MIXer:INP:FREQ:MODE swept  
Query Syntax | SENSe<ch>:MIXer:INPut:FREQuency:MODE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Fixed  
  
* * *

## SENSe<ch>:MIXer:INPut:FREQuency:NUMerator <value>

Applicable Models: All (Read-Write) Sets or returns the numerator value of the
Input Fractional Multiplier. [See Note](MIXerSCPI.md#Note)  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<value> | Input numerator value.  
Examples | SENS:MIX:INP:FREQ:NUM 3  
SENSe2:MIXer:INPut:FREQ:NUMerator 1  
Query Syntax | SENSe<ch>:MIXer:INPut:FREQ:NUMerator?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:INPut:FREQuency:STARt <value>

Applicable Models: All (Read-Write) Sets or returns the Input start frequency
value of the mixer. [See Note](MIXerSCPI.md#Note)  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<value> | Input Start frequency  
Examples | SENS:MIX:INP:FREQ:STAR 1e9  
SENSe2:MIXer:INPut:FREQ:STARt 1000000000  
Query Syntax | SENSe<ch>:MIXer:INPut:FREQuency:STARt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:INPut:FREQuency:STOP <value>

Applicable Models: All (Read-Write) Sets or returns the Input stop frequency
value of the mixer. [See Note](MIXerSCPI.md#Note)  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<value> | Input stop frequency  
Examples | SENS:MIX:INP:FREQ:STOP 2e9  
SENSe2:MIXer:INPut:FREQ:STOP 2000000000  
Query Syntax | SENSe<ch>:MIXer:INPut:FREQuency:STOP?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:INPut:POWer <value>

Applicable Models: All (Read-Write) Sets or returns the value of the Input
Power.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<value> | Input power in dBm.  
Examples | SENS:MIX:INP:POW 9  
SENSe2:MIXer:INPut:POWer 5  
Query Syntax | SENSe<ch>:MIXer:INPut:POWer?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:INPut:POWer:STARt <value>

Applicable Models: All

(Read-Write) Sets the input start power for a power sweep in a mixer channel
like SMC. The value is only used when the sweep type is power sweep.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<value> | Input power value in units of dBm.  
Examples | SENS:MIX:INP:POW STAR 6  
SENSe2:MIXer:INPut:POWer:STARt 5  
Query Syntax | SENSe<ch>:MIXer:INPut:POWer:STARt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:INPut:POWer:STOP <value>

Applicable Models: All

(Read-Write) Sets the input stop power for a power sweep in a mixer channel .
The value is only used when the sweep type is power sweep.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<value> | Input power value in units of dBm.  
Examples | SENS:MIX:INP:POW STOP 9  
SENSe2:MIXer:INPut:POWer:STOP 5  
Query Syntax | SENSe<ch>:MIXer:INPut:POWer:STOP?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:INPut:POWer:USENominal <bool>

Applicable Models: All (Read-Write) Toggles the Use Nominal Incident Power
setting ON and OFF. This setting is ONLY to be used with SMC measurements.
[Learn more about Nominal Incident
Power.](../../../FreqOffset/SMC_Measurements.htm#UseNominal)  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<value> | (boolean) \- Nominal Incident Power State. Choose from: ON (1) - Turn nominal incident power ON OFF (0) - Turn nominal incident power OFF  
Examples | SENS:MIX:INP:POW:USEN 1  
SENSe2:MIXer:INPut:POWer:USENominal OFF  
Query Syntax | SENSe<ch>:MIXer:INPut:POWer:USENominal?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SENSe<ch>:MIXer:LO<n>:FREQuency:DENominator <value>

Applicable Models: All (Read-Write) Sets or returns the denominator value of
the LO Fractional Multiplier. [See Note](MIXerSCPI.md#Note)  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | LO stage number. Choose 1 or 2.  
<value> | LO denominator.  
Examples | SENS:MIX:LO:FREQ:DEN 5  
SENSe2:MIXer:LO2:FREQ:DENominator 4  
Query Syntax | SENSe<ch>:MIXer:LO<n>:FREQuency:DENominator?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## SENSe<ch>:MIXer:LO<n>:FREQuency:FIXed <value>

Applicable Models: All (Read-Write) Sets or returns the fixed frequency of the
specified mixer LO. [See Note](MIXerSCPI.md#Note)  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | LO stage number. Choose 1 or 2  
<value> | LO frequency.  
Examples | SENS:MIX:LO:FREQ:FIX 1e9  
SENSe2:MIXer:LO2:FREQ:FIXed 1000000000  
Query Syntax | SENSe<ch>:MIXer:LO<n>:FREQuency:FIXed?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:LO<n>:FREQuency:ILTI <bool>

Applicable Models: All (Read-Write) Specifies whether to use the Input
frequency that is greater than the LO or less than the LO. To learn more, see
the [mixer setup](../../../Applications/MixerConverter_Setup.md#ILTI) dialog
box help.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | LO stage number. Choose 1 or 2  
<bool> | ON (1) \- Use the Input that is Greater than the specified LO. OFF (0) \- Use the Input that is Less than the specified LO.  
Examples | SENS:MIX:LO1:FREQ:ILTI 1  
sense2:mixer:lo2:frequency:ilti ON  
Query Syntax | SENSe<ch>:MIXer:LO<n>:FREQuency:ILTI?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## SENSe<ch>:MIXer:LO<n>:FREQuency:MODE <char>

Applicable Models: All (Read-Write) Sets or returns the LO sweep mode.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | LO stage number. Choose 1 or 2  
<char> | LO sweep mode. Choose either FIXED or SWEPT  
Examples | SENS:MIX:LO:FREQ:MODE FIXED  
SENSe2:MIXer:LO2:FREQ:MODE swept  
Query Syntax | SENSe<ch>:MIXer:LO<n>:FREQuency:MODE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Fixed  
  
* * *

## SENSe<ch>:MIXer:LO<n>:FREQuency:NUMerator <value>

Applicable Models: All (Read-Write) Sets or returns the numerator value of the
LO Fractional Multiplier. [See Note](MIXerSCPI.md#Note)  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | LO stage number. Choose 1 or 2  
<value> | LO Numerator.  
Examples | SENS:MIX:LO:FREQ:NUM 5  
SENSe2:MIXer:LO2:FREQ:NUMerator 4  
Query Syntax | SENSe<ch>:MIXer:LO<n>:FREQuency:NUMerator?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:LO<n>:FREQuency:STARt <value>

Applicable Models: All (Read-Write) Sets or returns the LO start frequency
value. [See Note](MIXerSCPI.md#Note)  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | LO stage number. Choose 1 or 2  
<value> | LO Start Frequency in Hertz.  
Examples | SENS:MIX:LO:FREQ:STAR 5E9  
Query Syntax | SENSe<ch>:MIXer:LO<n>:FREQuency:STARt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:LO<n>:FREQuency:STOP <value>

Applicable Models: All (Read-Write) Sets or returns the LO stop frequency
value. [See Note](MIXerSCPI.md#Note)  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | LO stage number. Choose 1 or 2  
<value> | LO Stop Frequency in Hertz.  
Examples | SENS:MIX:LO:FREQ:STOP 5E9  
Query Syntax | SENSe<ch>:MIXer:LO<n>:FREQuency:STOP?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:LO<n>:NAME <value>

Applicable Models: All (Read-Write) Sets or returns the name of the VNA
internal source or external source to use as the LO in a converter
measurement. Important Note: This setting is immediately send to the channel
configuration. First set and apply mixer frequency settings, then send this
command. Otherwise, 'invalid setting' errors may occur. See [Remotely
Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.htm).  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | LO stage number. Choose 1 or 2.  
<value> | (string) \- LO Source name. Use [Source:CAT?](../source.md#Cat) to return a list of valid source ports. An external source must be configured and selected to be valid. [Learn more about external source configuration.](../../../System/Configure_an_External_Device.md)  
Examples | SENS:MIX:LO:NAME "MySource"  
Query Syntax | SENSe<ch>:MIXer:LO<n>:NAME?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | "Not Controlled"  
  
* * *

## SENSe<ch>:MIXer:LO<n>:POWer <value>

Applicable Models: All (Read-Write) Sets or returns the LO Power fixed value.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | LO stage. Choose 1 or 2  
<value> | LO Power in dBm  
Examples | SENS:MIX:LO:POW 9  
Query Syntax | SENSe<ch>:MIXer:LO<n>:POWer?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:LO<n>:POWer:STARt <value>

Applicable Models: All (Read-Write) For an LO power sweep, sets or returns the
LO power start value.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | LO stage. Choose 1  
<value> | LO start power in dBm  
Examples | SENS:MIX:LO1:POW:STAR -10  
Query Syntax | SENSe<ch>:MIXer:LO1:POWer:STARt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | \- 20 dBm  
  
* * *

## SENSe<ch>:MIXer:LO<n>:POWer:STOP <value>

Applicable Models: All (Read-Write) For an LO power sweep, sets or returns the
LO power stop value.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | LO stage. Choose 1  
<value> | LO stop power in dBm  
Examples | SENS:MIX:LO1:POW:STOP 10  
Query Syntax | SENSe<ch>:MIXer:LO1:POWer:STOP?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | -10 dBm  
  
* * *

## SENSe<ch>:MIXer:LOAD <name>

Applicable Models: All (Write-only) Loads a previously-configured mixer
attributes file (.mxr)  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<name> | Path and file name (including .mxr extension) to load.  
Examples | SENSe:MIXer:LOAD "C:\Program Files(x86)\Keysight\Network Analyzer\Documents\Mixer\MyMixer.mxr"  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:NORMalize:POINt <value>

Applicable Models: All (Read-Write) Sets or returns the data point for
normalizing the phase measurement. [Learn
more.](../../../FreqOffset/SMC_plus_Phase.htm)  
---  
Parameters |   
<ch> | Channel number of the SMC measurement. If unspecified, value is set to 1.  
<value> | Normalization data point. Choose a data point number between 1 and the max number of data points in the sweep that has the least amount of expected noise.  
Examples | SENS:MIX:NORM:POIN 101 sense2:mixer:normalize:point 50  
Query Syntax | SENSe<ch>:MIXer:NORMalize:POINt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Middle point in the sweep  
  
* * *

## SENSe<ch>:MIXer:OUTPut:FREQuency:FIXed <value>

Applicable Models: All (Read-Write) Sets or returns the output fixed frequency
of the mixer. [See Note](MIXerSCPI.md#Note)  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<value> | Output fixed frequency in Hertz.  
Examples | SENS:MIX:OUTP:FREQ:FIX 5e9  
Query Syntax | SENSe<ch>:MIXer:OUTPut:FREQuency:FIXed?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:OUTPut:FREQuency:MODE <char>

Applicable Models: All (Read-Write) Sets or returns the Output sweep mode.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<char> | Output sweep mode. Choose either FIXED or SWEPT  
Examples | SENS:MIX:OUTP:FREQ:MODE FIXED  
SENSe2:MIXer:OUTput:FREQuency:MODE swept  
Query Syntax | SENSe<ch>:MIXer:OUTPut:FREQuency:MODE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Fixed  
  
* * *

## SENSe<ch>:MIXer:OUTPut:FREQuency:SIDeband <value>

Applicable Models: All (Read-Write) Specify whether to select the sum (High)
or difference (Low) products.

  * When one LO is used: Input + or - LO1 = Output frequency
  * When two LOs are used: IF1 + or - LO2 = Output frequency

Use [SENS:MIX:IF:FREQ:SID](MIXerSCPI.md#IF_SIDE) when two LOs are used to
determine the IF1 frequency. Use [Sens:Mixer:Stage](MIXerSCPI.md#Stage) to
set 1 or 2 LOs [See Note](MIXerSCPI.md#Note)  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<value> | Sideband value. Choose from LOW \- Low or Difference (-) HIGH \- High or Sum (+)  
Examples | SENS:MIX:OUTP:FREQ:SID LOW  
SENSe2:MIXer:OUTPut:FREQ:SIDeband HIGH  
Query Syntax | SENSe<ch>:MIXer:OUTPut:FREQuency:SIDeband?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | LOW  
  
* * *

## SENSe<ch>:MIXer:OUTPut:FREQuency:STARt <value>

Applicable Models: All (Read-Write) Sets or returns the Output start frequency
of the mixer. [See Note](MIXerSCPI.md#Note)  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<value> | Output start frequency  
Examples | SENS:MIX:OUTP:FREQ:STAR 1e9  
SENSe2:MIXer:OUTPut:FREQ:STARt 1000000000  
Query Syntax | SENSe<ch>:MIXer:OUTPut:FREQuency:STARt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:OUTPut:FREQuency:STOP <value>

Applicable Models: All (Read-Write) Sets or returns the Output stop frequency
of the mixer. [See Note](MIXerSCPI.md#Note)  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<value> | Output stop frequency  
Examples | SENS:MIX:OUTP:FREQ:STOP 1e9  
SENSe2:MIXer:OUTPut:FREQ:STOP 1000000000  
Query Syntax | SENSe<ch>:MIXer:OUTPut:FREQuency:STOP?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:PHASe[:STATe] <bool>

Applicable Models: N522xB, N523xB, N524xB (Read Write) Sets and returns the
state of SMC Phase measurements and calibrations. [Learn
more.](../../../FreqOffset/SMC_plus_Phase.htm) In the User Interface, there
are two "enable phase" checkboxes: in the [Phase Settings
dialog](../../../FreqOffset/SMC_plus_Phase.htm) and in the [Calibration
Wizard](../../../FreqOffset/SMC_Measurements.htm#CalWizard). Checking one
enables both. This single command also enables both.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<bool> | Include Phase measurement state. Choose from ON or 1 - Include phase in SMC measurements OFF or 0 - Do NOT include phase in SMC measurements  
Examples | SENS:MIX:PHAS 1 sense2:mixer:phase:state off  
Query Syntax | SENSe<ch>:MIXer:PHASe[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 (OFF)  
  
* * *

## SENSe<ch>:MIXer:PHASe:ABSolute[:STATe] <bool>

Applicable Models: N522xB, N523xB, N524xB (Read Write) Sets and returns the
state of SMC Phase measurements to use absolute phase. LO1 must be set to an
internal source to enable this feature. [Learn
more.](../../../FreqOffset/SMC_plus_Phase.htm#HowEnableSMCPhase)  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<bool> | Absolute Phase measurement state. Choose from ON or 1 - Enable absolute phase in SMC measurements OFF or 0 - Disable absolute phase in SMC measurements  
Examples | SENS:MIX:PHAS:ABS 1 sense2:mixer:phase:absolute:state off  
Query Syntax | SENSe<ch>:MIXer:PHASe:ABSolute[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 (OFF)  
  
* * *

## SENSe<ch>:MIXer:PMAP <in>,<out>

Applicable Models: All (Write-only) Sets the VNA to DUT port map for FCA
measurements. Use SENS:MIX:PMAP:INP? and SENS:MIX:PMAP:OUTP? to read these
values. Learn about [selectable FCA DUT
ports.](../../../FreqOffset/FCA_Use.htm#dutPorts) Changing the ports may limit
your ability to use an internal second source. If a selected port is shared by
one of the sources, then that source will not be available as an LO source.
[Learn more about Internal second
sources](../../../S0_Start/Internal_Second_Source.htm).  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<in> | VNA port to connect to the DUT input.

  * For SMC, choose any unused VNA port.
  * For VMC, set to 1.

  
<out> | VNA port to connect to the DUT output. Choose any unused port for SMC and VMC.  
Examples | SENS:MIX:PMAP 2,1  
sense2:mixer:pmap 4,2  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1,2  
  
![](../../../assets/images/Programming/Tp.gif)

* * *

## SENSe<ch>:MIXer:PMAP:INPut?

Applicable Models: All (Read-only) Returns the VNA port that is mapped to the
DUT input. Use [SENS:MIX:PMAP](MIXerSCPI.md#pmap) to set this value. Learn
about [selectable FCA DUT ports.](../../../FreqOffset/FCA_Use.md#dutPorts)  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
Examples | SENS:MIX:PMAP:INP?  
sense2:mixer:pmap:input?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
![](../../../assets/images/Programming/Tp.gif)

* * *

## SENSe<ch>:MIXer:PMAP:OUTPut?

Applicable Models: All (Read-only) Returns the VNA port that is mapped to the
DUT output. Use [SENS:MIX:PMAP](MIXerSCPI.md#pmap) to set this value. Learn
about [selectable FCA DUT ports.](../../../FreqOffset/FCA_Use.md#dutPorts)  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
Examples | SENS:MIX:PMAP:OUTP?  
sense2:mixer:pmap:output?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 2  
  
![](../../../assets/images/Programming/Tp.gif)

* * *

## SENSe<ch>:MIXer:RECalculate

Applicable Models: All (Write only) Repeats the last calculation that was
performed, including all ON (state) segments in segment table.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
Examples | SENS:MIX:REC  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:REVerse <bool>

Applicable Models: All (Read-Write) Sets whether to include SC12 sweeps during
measurements.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<bool> | (Boolean) Choose from: ON (1) \- Include the SC12 (reverse) sweep. OFF (0) \- Do NOT Include the SC12 (reverse) sweep.  
Examples | SENS:MIX:REV 1  
sense2:mixer:reverse ON  
Query Syntax | SENSe<ch>:MIXer:REVerse?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON (1)  
  
![](../../../assets/images/Programming/Tp.gif)

* * *

## SENSe<ch>:MIXer:ROLE:CATalog? \- Superseded

Applicable Models: All (Read-only) This command is replaced with
[SENSe:ROLE:CATalog](Role.md#catalog) which can be used by all channels.
Returns a list of valid roles for the IMD Converter application.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
Examples | SENS:MIX:ROLE:CAT?  
sense2:mixer:role:catalog?  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
![](../../../assets/images/Programming/Tp.gif)

* * *

## SENSe<ch>:MIXer:ROLE:DEVice <role>,<source> Superseded

Applicable Models: All (Read-Write) This command is replaced with
[SENSe:ROLE:DEVice](Role.md#Device) which can be used by all channels.
Assigns a configured external source to the specified role for the converter
application.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<role> | (String) Role to which the external source is assigned. Choose from: For IMDX and IMSX, choose from: "RF2" "LO1" "LO2" For all other converter applications, choose from: "LO1" "LO2"  
<source> | String) Source name from [Source Configuration dialog](../../../System/Configure_an_External_Device.md#ext_source_config).  
Examples | SENS:MIX:ROLE:DEV "LO1","LO1Name"  
sense2:mixer:role:device "LO1","LO1Name"  
Query Syntax | SENSe<ch>:MIXer:ROLE:DEVice? <source>  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
![](../../../assets/images/Programming/Tp.gif)

* * *

## SENSe<ch>:MIXer:SAVE <name>

Applicable Models: All (Write-only) Saves the settings for the mixer/converter
test setup to a mixer attributes file.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<name> | Path and file name (including .mxrx extension) to save.  
Examples | SENSe:MIXer:SAVE "C:\Program Files(x86)\Keysight\Network Analyzer\Documents\Mixer\MyMixer.mxr"  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:MIXer:STAGe <n>

Applicable Models: All (Read-Write) Number of IF stages (LOs) used in the
mixer. [See Note](MIXerSCPI.md#Note)  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<n> | Number of stages. Choose either 1 or 2  
Examples | SENSe1:MIXer:LO1:FREQ:NUMerator 6  
SENSe1:BWID 1000  
SENSe1:MIXer:SEGMent1:ADD 165  
'New segments will reset stage to single stage mode. Therefore, always add
dual stage setting after adding segments  
SENSe1:MIXer:STAGE 2  
Query Syntax | SENSe<ch>:MIXer:STAGe?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## SENSe<ch>:MIXer:XAXis <char>

Applicable Models: All (Read-Write) Sets or returns the swept frequency range
to display on the X-axis for the IMDx or NFx channel. For FCA and GCX
measurements, use
[CALC:MEAS:MIXer:XAXis](../Calculate/MeasureX.md#CALCulate:MEASure:X:AXiS)  
---  
Parameters |   
<ch> | Channel number of the IMDx or NFx Converter measurement. If unspecified, value is set to 1.  
<char> | Frequency range to display on the X-Axis. NOT case-sensitive. Choose from:

  * INPUT \- Input frequency range
  * LO_1 \- LO frequency range
  * LO_2 \- LO 2 frequency range
  * OUTPUT \- Output frequency range

If the specified frequency range is not swept, the default swept range is
used.  
Examples | SENSe:MIXer:XAXis INPUT sense2:mixer:xaxis LO_1  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Search is made in the following order until a swept range is found:

  1. OUTPUT
  2. INPUT (If the OUTPUT is fixed)
  3. Number of Points (If ALL ranges are fixed)

  
  
* * *

