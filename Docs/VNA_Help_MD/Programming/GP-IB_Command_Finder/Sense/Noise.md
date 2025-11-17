# SENSe:NOISe Commands

* * *

Controls the Noise Figure / NFX configuration and calibration.

SENSe:NOISe: AMPLifier <string> | CATalog? [AVERage](Noise.md#Average) <num> | [STATe](Noise.md#avgState) <bool> [BWIDth](Noise.md#bwid) <num> [CALibration:](Noise.md#CalMethod) | [METHod](Noise.md#CalMethod) <string> | [RMEThod](Noise.md#RMethod) <string> CONTrol | HANDler | PIN | FUNCtion ENR | [FILename](Noise.md#ENRFilename) <string> [EXDC:NAME](Noise.md#ExdcId) [GAIN](Noise.md#gain) <num> | CTCheck [IMPedance:COUNt](Noise.md#ImpCount) <num> [NARRowband[:STATe]](Noise.md#Narrowband) <bool> [PMAP](Noise.md#pmapSet) <in>,<out> | [INPut?](Noise.md#PortIN) | [OUTPut?](Noise.md#PortOutput) [PULL[:STATe]](Noise.md#Pull) <bool> [RECeiver](Noise.md#Receiver) <char> [SNP?](Noise.md#snp) <string> | [SAVE](Noise.md#snpSave) <string> SOURce: | [CKIT](Noise.md#sourceCKIT) <string> | [CONNector](Noise.md#sourceConn) <string> SWEep | MACRo | FILe | RNPath | RSPath | SNPath | SSPath | STATe | TIMe? TEMPerature | [AMBient](Noise.md#TempAmb) <num> | AUTO | SOURce | AUTO | [:VALue] TUNer: | FILE:NAME <string> | FILE[:STATe] | [ID](Noise.md#tunerID) <string> | [INPut](Noise.md#TunerInput) <string> | [ORIent[:STATe]](Noise.md#tunerOrient) | [OUTPut](Noise.md#tunerOutput) <string> USBSource: | CATalog? | ENR | SAVE | [:SELect]  | TEMPerature?  
---  
  
Click on a keyword to view the command details.

### Other Noise Figure SCPI commands

The calibration commands listed in this topic are supplemental to the [Guided
Cal commands](CorrGuided.htm).

  * [CALCulate:MEASure:DEFine](../Calculate/Measure.md#CALCulate:MEASure:DEFine) \- creates a noise figure measurement.

  * [CONTrol:NOISe:SOURce](../Control.md#NoiseSourceState) or [OUTPut:MANual:NOISe[:STATe]](../Output.md#NoiseState) \- turns the Noise Source ON and OFF.

  * [MMEMory:LOAD:ENR](../Memory.md#recall) and [MMEM:STORe:ENR](../Memory.md#save) \- load and save ENR files.

  * [SENSe:PATH:CONF:ELEMent[:STATe]](Path.md) \- sets the port 1 and port 2 noise switches.

  * [SENS:CORR:ENR:CAL:](Sense_Correction.md)\- manage ENR data - usually not necessary.

  * [SYST:PREF:ITEM:SWIT:DEF](../System_Preferences.md#Switch) \- Sets the default setting of the Noise Tuner switch

  * [SENS:CORR:NOISe](Sense_Correction.md#NoiseENRDeemb) commands - noise calibration

  * [SENS:CORR:Guided](CorrGuided.md) commands - performs most of noise cal.

See Also

  * Examples:
  *     * [Create and Cal a Noise Figure Measurement](../../GPIB_Example_Programs/Create_and_Cal_a_Noise_Figure_Measurement.md)

    * [Create and Cal an NFX Measurement](../../GPIB_Example_Programs/Create_and_Cal_an_NFX_Measurement.md)

  * [Learn about Noise Figure Application](../../../Applications/Noise_Figure.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## SENSe<ch>:NOISe::AMPLifier:[:SELect] <string>

Applicable Models: All with Noise Figure Option (S9x029A/B, Licensed Feature)
(Read-Write) Selects and queries the connected U7229x series USB Low Noise
Amplifier, identified by its device ID. Once a noise amplifier is selected,
the network analyzer will immediately begin sending commands to the device to
switch the state to Gain and Thru automatically before each noise and
S-Parameter sweep, respectively. To unselect the device, use an empty string
as the parameter.  Note: A sweep delay of 500 milliseconds is recommended to
allow ample time for the LNA switch state to settle in between noise and
S-Parameter sweeps. Set the sweep delay before selecting an amplifier using
SENSe:SWEep:DWELl:SDELay.  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<string> |  "ModelNumber SerialNumber"  
Examples |  SENS:NOIS:AMPL "U7229M MY12345678" sense2:noise: amplifier:select ""  
Query Syntax |  SENSe:NOISe:AMPL?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SENSe<ch>:NOISe::AMPLifier:CATalog?

Applicable Models: All with Noise Figure Option (S9x029A/B, Licensed Feature)
(Read-only) Returns a comma separated list of connected U7229x series USB Low
Noise Amplifiers, identified by their device ID: "ModelNumber SerialNumber".  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
Examples |  SENS:NOIS:AMPL:CAT? sense:noise: amplifier:catalog?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SENSe<ch>:NOISe:AVERage[:COUNt] <num>

Applicable Models: All with with Noise Figure Option (S9x029A/B, 028, 029)
(Read-Write) Set and read the averaging factor for the noise receiver. [Learn
more](../../../Applications/Noise_Figure.htm#NoiseSettingDiag)  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<num> |  Averaging value. Choose any number from 1 to 16000.  
Examples |  SENS:NOIS:AVER 20 sense:noise:average:count 10  
Query Syntax |  SENSe:NOISe:AVERage[:COUNt]?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1  
  
* * *

## SENSe<ch>:NOISe:AVERage:STATe <bool>

Applicable Models: VNAs with Noise Figure Option (S9x029A/B, 028, 029) (Read-
Write) Turns noise averaging ON and OFF.  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<bool> |  Averaging state. Choose from 0 - Noise averaging OFF 1 - Noise averaging ON  
Examples |  SENS:NOIS:AVER:STAT 0 sense:noise:average:state 1  
Query Syntax |  SENSe:NOISe:AVERage:STATe?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  O - OFF  
  
* * *

## SENSe<ch>:NOISe:BWIDth[:RESolution] <num>

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Read-
Write) Set and read the bandwidth of the noise receiver. [Learn
more](../../../Applications/Noise_Figure.htm#NoiseSettingDiag)  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<num> |  Bandwidth value. Choose from: For [Sens:Noise:Receiver](Noise.md#Receiver) = NOISe (Opt 029) choose from: 800 KHz, 2 MHz, 4 MHz, 8 MHz, or 24 MHz or the numerical equivalent, such as 8e6 and so forth. For [Sens:Noise:Receiver](Noise.md#Receiver) = NORMal (Opt 028) choose from: 720 kHz or 1.2 MHz If the value does not match one of these, it is rounded up to the next valid bandwidth value.  
Examples |  SENS:NOIS:BWID 2e6 sense:noise:bwidth:resolution 8mhz  
Query Syntax |  SENSe:NOISe:BWIDth[:RESolution]?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  4 MHz for Noise Receiver 1.2 MHz for Normal Receiver  
  
* * *

## SENSe<ch>:NOISe:CALibration:METHod <string>

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Read-
Write) Set and read the method for performing a calibration on a noise
channel.  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<string> |  Calibration method. NOT case-sensitive. Choose from:

  * "VectorFull" or "Vector"
  * "SParameter" (Not available for NFX measurements)
  * "ScalarFull" or "Scalar"

  
Examples |  SENS:NOIS:CAL:METH "Vector" sense:noise:calibration:method "SParameter"  
Query Syntax |  SENSe:NOISe:CALibration:METHod?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  "VectorFull"  
  
* * *

## SENSe<ch>:NOISe:CALibration:RMEThod <string>

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Read-
Write) Set and read the method used to characterize the noise receivers.
[Learn more.](../../../Applications/Noise_Cal.md#Overview)  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<string> |  Receiver characterization method. NOT case-sensitive. Choose from:

  * "NoiseSource - Use a noise source. This selection is NOT allowed when a standard VNA receiver is used as the noise receiver ([SENS:NOIS:REC NORM](Noise.md#Receiver)).
  * PowerMeter - Use a power meter. NOTE: This selection is NOT allowed when the [Noise Bandwidth](Noise.md#bwid) is 8 MHz or 24 MHz.

  
Examples |  SENS:NOIS:CAL:RMET "PowerMeter" sense:noise:calibration:rmethod "noisesource"  
Query Syntax |  SENSe:NOISe:CALibration:RMEThod?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  "NoiseSource"  
  
* * *

## SENSe<ch>:NOISe:CONTrol:HANDler:PIN<xy>:FUNCtion <func>

Applicable Models: PNA and PNA-X only with Noise Figure Option (S9x029A/B,
028, 029) (Read-Write) Set and Read the function for the specified port in
Material Handler I/O interface. Only Port C may be used for this functionality
(Pins 22, 23, 24, 25). Note: User may want to add sweep delay to allow for the
RF switch time to properly change from one position to another. 0.5s is a good
margin value for a TTL relay. This can be done with the
[SENse:SWEep:DWELl:SDELay](https://na.support.keysight.com/vna/help/latest/Programming/GP-
IB_Command_Finder/Sense/Sweep_SCPI.htm#SweepDelay) command  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<xy> |  Pin number.  
<func> |  One of six functions. Choose from: |  Function name |  Description |  Assignable  
Pin Number  
---|---|---  
"LOW" |  Sets the pin low. |  22-25  
"HIGH" |  Sets the pin high. |  22-25  
"NF_SOURCE" |  Noise Figure source switch control for input port. This function sets the pin low for S-parameter measurements and high for NF measurements. |  22-25  
"NF_SOURCE_INVERTED" |  Noise Figure source switch control for input port. This function sets the pin high for S-parameter measurements and low for NF measurements. |  22-25  
"NF_RECEIVER" |  Noise Figure receiver switch control for output port. This function sets the pin low for S-parameter measurements and high for NF measurements. |  22-25  
"NF_RECEIVER_INVERTED" |  Noise Figure receiver switch control for output port. This function sets the pin high for S-parameter measurements and low for NF measurements. |  22-25  
  
Examples |  SENSe:NOISe:CONTrol:HANDler:PIN23:FUNCtion "NF_RECEIVER" sens:nois:cont:hand:pin22:func?  
Query Syntax |  SENSe<ch>:NOISe:CONTrol:HANDler:PIN<xy>:FUNCtion?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  "LOW"  
  
* * *

## SENSe<ch>:NOISe:ENR:FILename <string>

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Read-
Write) Set and read the path and name of the ENR file associated with the
noise source.  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<string> |  Full path, filename, and extension of the ENR file.  
Examples |  SENS:NOIS:ENR:FIL "c:\Program Files(x86)\Keysight\Network Analyzer\Documents\ENR\346C.enr" sense:noise:enr:filename "c:\Program Files(x86)\Keysight\Network Analyzer\Documents\ENR\346C.enr"  
Query Syntax |  SENSe:NOISe:ENR:FILename?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SENSe<ch>:NOISe:ENR <INTernal | FILE >

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Read-
Write) Specifies whether to use the ENR file stored internally on the USB
sensor or to use specified .enr file (located on the VNA).  Note: 1) If FILE
is used, the .enr file should be specified using SENSe<ch>:NOISe:ENR:FILename
<string> 2) If INT is used, then "SENSe:NOISe:ENR:FILename? returns
Internal  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<INTernal | FILE> |  Choose from: INTernal = use internal file on the USB FILE = use separate .enr file.  
Examples |  SENS:NOIS:ENR INT sense:noise:enr file  
Query Syntax |  SENSe:NOISe:ENR?  
Return Type |  Characters  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SENSe<ch>:NOISe:EXDC:NAME <string>

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029), except
PNA and PNA-X (Read-Write) Set and read the external DC source name in order
to control the noise source.  
---  
Parameters |   
<ch> |  Noise Figure channel number but this number is ignored for this command.  
<string> |  DC source name. The DC source should be defined in the external device dialog in advance.  
Examples |  Add DC-biased Noise Source named "NoiseSource1". Open NF channel before sending following commands. SYSTem:CONFigure:EDEVice:ADD "NoiseSource1" SYSTem:CONFigure:EDEVice:DTYPE "NoiseSource1","DC Source" SYSTem:CONFigure:EDEVice:DRIVer "NoiseSource1", "DC Source" SYSTem:CONFigure:EDEVice:IOConfig "NoiseSource1", "GPIB0::23::INSTR" SYSTem:CONFigure:EDEVice:LOAD "NoiseSourceSettings.xml", "NoiseSource1" SENSe:NOISe:EXDC:NAME "NoiseSource1" NOTE: NoiseSourceSettings.xml has setting information about waiting time and SCPI commands to DC Source. Create this xml file before sending SCPI commands.  
Query Syntax |  SENSe:NOISe:EXDC:NAME?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ""  
  
* * *

## SENSe<ch>:NOISe:GAIN <num>

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Read-
Write) Set and read the amount of gain for the noise receiver. This setting is
NOT used when [Sens:Noise:Receiver](Noise.md#Receiver) = NORMal (Opt 028)  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<num> |  Gain value. Choose from:

  * 0 \- Low gain;select if the gain of your DUT is relatively high (>35 dB)
  * 15 \- Medium gain; select if the gain of your DUT is about average (20 dB to 45 dB)
  * 30 \- High gain;.select if the gain of your DUT is relatively low (<30 dB)

[Learn more about Noise Receiver Gain
setting](../../../Applications/Noise_Figure.htm#NoiseSettingDiag). If the
value does not match one of these, it is rounded up to the next legal value.  
Examples |  SENS:NOIS:GAIN 15 sense:noise:gain 0  
Query Syntax |  SENSe:NOISe:GAIN?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  30  
  
* * *

## SENSe<ch>:NOISe:GAIN:CTCheck <bool>

Applicable Models: N524xA/B with Noise Figure Option (S9x029A/B) (Read-Write)
Turns ON and OFF the check for noise receiver compression.  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<bool> |  Threshold checking state. Choose from 0 - Noise threshold checking OFF 1 - Noise threshold checking ON  
Examples |  SENS:NOIS:GAIN:CTC 0 sense:noise:gain:ctcheck 1  
Query Syntax |  SENSe:NOISe:GAIN:CTCheck?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  O - OFF  
  
* * *

## SENSe<ch>:NOISe:IMPedance:COUNt <num>

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Read-
Write) Sets the number of impedance states to use during calibrated
measurements.  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<num> |  Number of impedance states to use. Choose between 4 and the maximum number allowed by the noise tuner device. The more states that are used, the more accurate, and slower, the measurement. If the specified number exceeds the capability of the device, the measurement will use the maximum number of states the device allows.   
Examples |  SENS:NOIS:IMP:COUN 5 sense:noise:impedance:count 7  
Query Syntax |  SENSe:NOISe:IMPedance:COUNt?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  4  
  
* * *

## SENSe<ch>:NOISe:NARRowband[:STATe] <bool>

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Excepts
M9485A, M980xA, P50xxA) (Read-Write) Turns narrowband noise figure
compensation ON and OFF  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<bool> |  Compensation state. Choose from 0 or OFF - Narrowband noise compensation OFF 1 or ON - Narrowband noise compensation ON  
Examples |  SENS:NOIS:NARR 0 sense:noise:narrowband:state 1  
Query Syntax |  SENSe:NOISe:NARRowband[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  O - OFF  
  
* * *

## SENSe<ch>:NOISe:PMAP <in>,<out>

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Write-
only) Set the DUT-to-VNA port mapping for Noise Figure. Port mapping is
allowed without restriction when the standard PNA receiver is used
(SENSe:NOISe:RECeiver is set to NORMal). When the low-noise receiver is
selected (SENSe:NOISe:RECeiver is set to NOISe) the following restrictions
apply:

  * If the low-noise receiver is selected, the DUT output port must be port 2.
  * On high-frequency PNAs that have an internal tuner on port 1, the input port must be port 1 if the internal tuner is selected as the noise tuner. Conversely, if the input port is something other than 1, the internal tuner cannot be selected.
  * For PNAs that have a maximum frequency of 26.5 GHz or less, any port can be selected as the DUT input port.
  * If a vector calibration is desired, the tuner must be connected to the selected input port.

Use the SENSe:NOISe:PMAP:INPut? and SENSe:NOISe:PMAP:OUTPut? commands to read
the DUT input and output ports.  
---  
Parameters |   
<ch> |  Any existing NF or NFX channel. If unspecified, value is set to 1.  
<in> |  VNA port which is connected to the DUT input.  
<out> |  VNA port which is connected to the DUT output.  
Examples |  SENS:NOIS:PMAP 1,2 sense:noise:pmap 2,1 [See example program](../../GPIB_Example_Programs/Setup_Noise_Figure_Port_Mapping.md)  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1,2  
  
* * *

## SENSe<ch>:NOISe:PMAP:INPut?

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Read-
only) Read the VNA port number to be connected to the DUT Input.  Use
[SENS:NOISe:PMap](Noise.md#pmapSet) to set the port mapping.  
---  
Parameters |   
<ch> |  Any existing NF or NFX channel. If unspecified, value is set to 1.  
Examples |  SENS:NOIS:PMAP:INP? sense:noise:pmap:input?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1  
  
* * *

## SENSe<ch>:NOISe:PMAP:OUTPut?

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Read-
only) Read the VNA port number to be connected to the DUT Output.  
---  
Parameters |   
<ch> |  Any existing NF or NFX channel. If unspecified, value is set to 1.  
Examples |  SENS:NOIS:PMAP:OUTP? sense:noise:pmap:output?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  2  
  
* * *

## SENSe<ch>:NOISe:PULL[:STATe] <bool>

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Read-
Write) Enables and disables the use of source pull technique to compute S22.
[Learn
more.](../../../Applications/Noise_Figure_on_Converters.htm#SourcePulling)  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<bool> |  Source pull technique state. Choose from: OFF or 0 \- Disable use of source pull technique. ON or 1 \- Enable use of source pull technique.  
Examples |  SENS:NOIS:PULL 0 sense2:noise:pull:state ON  
Query Syntax |  SENSe:NOISe:PULL[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0 - OFF  
  
* * *

## SENSe<ch>:NOISe:RECeiver <char>

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Excepts
M9485A, M98xxA, P50xxA/B, E5080B, E5081A). Use of MM Head reserved for
Broadband configurations only with N5290A and N5291A testsets. (Read-Write)
Sets and returns the noise receiver to use for noise measurements.  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<char> |  Noise receiver. Choose from: NORMal The standard VNA receiver. (Opt 028 and Opt 029) NOISe The low-noise receivers. (Opt 029 only) MMHead TBroadband Millimeter head. (Opt 029 with Broadband N5290A or N5291A configuration only). If selecting the MMHead, this command should be sent before other configuration commands, as it will reset the configuration for proper measurements.  
Examples |  SENS:NOIS:REC NORM sense2:noise:receiver noise  
Query Syntax |  SENSe:NOISe:RECeiver?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  NOISe  
  
* * *

## SENSe<ch>:NOISe:SNP? [string]

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Except
M9485A) (Read-Only) Returns S-parameter and noise parameter data for vector
noise figure measurements.  Noise parameters are NOT valid for NFX or Scalar
noise figure measurements. Learn more about [noise
parameters](../../../Applications/Noise_Figure.htm#NoisePowerParams).  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
[string] |  Optional parameter. Choose "NoiseParameter" - Noise parameter data. If unspecified, only S-parameter data is saved.  
Examples |  SENS:NOIS:SNP? sense2:noise:snp? "NoiseParameter"  
Return Type |  Comma-separated values Data is returned in this order: 1\. <all frequencies | point number> 2\. <real S11> <imag S11> <real S21> <imag S21> <real S12> <imag S12> <real S22> <imag S22> Then if noise parameters are specified: 3\. <NFMin dB> <mag GammaOpt> <phase GammaOpt> <Rn/Z0> The data display format depends on [MMEM:STOR:TRAC:FORM:SNP](../Memory.md#snp)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:NOISe:SNP:SAVE <filename>, [data]

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Write-
only) Saves the S-parameters and vector noise parameters to an S2P file. For
NFX channels, mixer setup information is included as comments at the beginning
of the file.  Learn more about [noise
parameters](../../../Applications/Noise_Figure.htm#NoisePowerParams).  The
format of the snp data is set with
[MMEM:STOR:TRAC:FORM:SNP](../Memory.md#snp).  The following is sample data
for two data points from a Noise Figure measurement: ! Keysight
Technologies,N5242A,USxxxxxxx,A.09.85 ! pnan-nn Thu Nov 01 12:26:27 2012 # HZ
S MA R 50 !freq (Hz) S11M S11A S21M S21A S12M S12A S22M S22A 2000000000
9.038147e-001 6.241193e+001 5.855965e+000 -6.116778e+001 2.232653e-002
-1.475392e+002 5.275644e-001 1.750775e+002 8000000000 6.951366e-001
-1.458202e+002 5.307699e+000 -7.055212e+001 7.838612e-002 -1.460951e+002
3.986142e-001 -2.226317e+001 ! Noise Parameters !freq (Hz) NFMin(dB)
Rho_opt(Mag) Rho_opt(deg) Rn/Z0 2000000000 1.251697e+000 2.172018e-001
-8.765875e+001 1.806663e-001 8000000000 1.583849e+000 2.015185e-001
1.029875e+002 1.320403e-001  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<filename> |  Path (optional), filename and suffix of location to store SNP data. If path is not specified, the current path is used.  
[data] |  String. Optional parameter. Choose "NoiseParameter" - Noise parameter data. If unspecified, only S-parameter data is saved.  
Examples |  SENS:NOIS:SNP:SAVE "MySparams.s2p" sense2:noise:snp:save "C:\Program Files(x86)\Keysight\Network Analyzer\Documents\MyNoiseParams.s2p", "NoiseParameter"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:NOISe:SOURce:CKIT <string>

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Read-
Write) Set and read the Cal Kit that will be used for the Noise Source
adapter.  An adapter is always necessary to connect a 346C Noise Source to the
VNA port 2. Select a Cal Kit that is the same type and gender as the noise
source connector. If the Noise Source mates directly to VNA port 2, then set
this type to "None".  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<string> |  Cal Kit. Case sensitive. To read possible cal kit strings for the adapter:

  * Change the port connector type to that of the noise source using: [SENS:CORR:COLL:GUID:CONN:PORT<n>](CorrGuided.md#gConSelect)
  * Then read the possible cal kit strings for that port using: [SENS:CORR:COLL:GUID:CKIT:PORT<n>:CAT?](CorrGuided.md#gKitCat)

  
Examples |  SENS:NOIS:SOUR:CKIT "N4691-60004 ECal" sense:noise:source:ckit "  
Query Syntax |  SENSe:NOISe:SOURce:CKIT?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SENSe<ch>:NOISe:SOURce:CONNector <string>

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Read-
Write) Set and read the Noise Source connector type and gender. The Keysight
346C has an "APC 3.5 male" connector.  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<string> |  Noise source connector type and gender. Case sensitive. Use [SENS:CORR:COLL:GUID:CONN:CAT?](CorrGuided.md#gConnCat) to read possible connector strings.  
Examples |  SENS:NOIS:SOUR:CONN "APC 3.5 male" sense:noise:source:connector "APC 3.5 female"  
Query Syntax |  SENSe:NOISe:SOURce:CONNector?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SENSe<ch>:NOISe:SWEep:MACRo:FILE:RNPath <string1>,<string2>

Applicable Models: All with Noise Figure Option (S9x029A/B, Licensed Feature)
(Read-Write) Sets the macro and arguments to be called for each receiver-side
noise path type sweep.  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<string1> |  Full path to the macro.exe.  
<string2> |  Arguments  
Examples |  SENS:NOIS:SWE:MACR:FILE:RNP "C:\path\to\mymacro.exe,"argument" sense:noise:sweep:macro:file:rnpath "C:\path\to\mymacro.exe,"argument"  
Query Syntax |  SENSe:NOISe:SWEep:MACRo:FILe:RNPath?  
Return Type |  string  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:NOISe:SWEep:MACRo:FILE:RSPath <string1>,<string2>

Applicable Models: All with Noise Figure Option (S9x029A/B, Licensed Feature)
(Read-Write) Sets the macro and arguments to be called for each receiver-side
S-paramenter type sweep.  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<string1> |  Full path to the macro.exe.  
<string2> |  Arguments  
Examples |  SENS:NOIS:SWE:MACR:FILE:RSP "C:\path\to\mymacro.exe,"argument" sense:noise:sweep:macro:file:rspath "C:\path\to\mymacro.exe,"argument"  
Query Syntax |  SENSe:NOISe:SWEep:MACRo:FILe:RSPath?  
Return Type |  string  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:NOISe:SWEep:MACRo:FILE:SNPath <string1>,<string2>

Applicable Models: All with Noise Figure Option (S9x029A/B, Licensed Feature)
(Read-Write) Sets the macro and arguments to be called for each source-side
noise path type sweep.  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<string1> |  Full path to the macro.exe.  
<string2> |  Arguments  
Examples |  SENS:NOIS:SWE:MACR:FILE:SNP "C:\path\to\mymacro.exe,"argument" sense:noise:sweep:macro:file:snpath "C:\path\to\mymacro.exe,"argument"  
Query Syntax |  SENSe:NOISe:SWEep:MACRo:FILe:SNPath?  
Return Type |  string  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:NOISe:SWEep:MACRo:FILE:SSPath <string1>,<string2>

Applicable Models: All with Noise Figure Option (S9x029A/B, Licensed Feature)
(Read-Write) Sets the macro and arguments to be called for each source-side
S-parameter path type sweep.  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<string1> |  Full path to the macro.exe.  
<string2> |  Arguments  
Examples |  SENS:NOIS:SWE:MACR:FILE:SSP "C:\path\to\mymacro.exe,"argument" sense:noise:sweep:macro:file:sspath "C:\path\to\mymacro.exe,"argument"  
Query Syntax |  SENSe:NOISe:SWEep:MACRo:FILE:SSPath?  
Return Type |  string  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:NOISe:SWEep:MACRo:STATe <bool>

Applicable Models: All with Noise Figure Option (S9x029A/B, Licensed Feature)
(Read-Write) Enables or disables the use of macros during noise figure sweep.  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<bool> |  Choose from 0 or OFF \- Disable the macro feature 1 or ON \- Enable the macro feature  
Examples |  SENS:NOIS:SWE:MACR:STAT ON sense:noise:sweep:macro:state 1  
Query Syntax |  SENSe:NOISe:SWEep:MACRo:STATe?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0 -OFF  
  
* * *

## SENSe<ch>:NOISe:SWEep:TIMe?

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Read-
only) Returns the APPROXIMATE time the channel will take to make one noise
receiver sweep given the current setup. This, along with the sweep time for a
standard receiver measurement and the following calculations, can tell you how
long a single sweep would take so that you can set an appropriate "timeout"
in your program.  To calculate the total sweep time: Noise Figure on
amplifiers (Vector Correction ON):

  * 2*SSwpTime + X*NoiseReceiverSweepTime
  * Where X = the number of noise receiver impedance state sweeps. (Default is 4).

Noise Figure on converters (NFX) correction on - increased number of sweeps
due to extra mixer sweeps and source pulling:

  * 4*SSwpTime + X*NoiseReceiverSweepTime (without source pulling)
  * 8*SSwpTime + X*NoiseReceiverSweepTime (with source pulling)
  * Where X = the number of noise receiver impedance state sweeps. (Default is 4).

Note: The number of sweeps to perform a noise measurement is annotated at the
bottom of the Noise Figure screen.  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
Examples |  SENS:NOIS:SWE:TIM? sense:noise:sweep:time?  
Return Type |  Double  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SENSe<ch>:NOISe:TEMPerature:AMBient <num>

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Read-
Write) Sets the temperature at which the current noise measurement is
occurring. [Learn
more](../../../Applications/Noise_Figure.htm#NoiseSettingDiag)  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<num> |  Ambient temperature in Kelvin.  
Examples |  SENS:NOIS:TEMP:AMB 292 sense:noise:temperature 289  
Query Syntax |  SENSe:NOISe:TEMPerature:AMBient?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  295  
  
* * *

## SENSe<ch>:NOISe:TEMPerature:AMBient:AUTO <bool>

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Read-
Write) If ON, will use 302K as the ambient temperature when vector correction
is applied and the tuner is an ECal or internal tuner. If OFF, will use the
specified ambient temperature.  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<bool> |  Choose from: OFF or 0 \- Use the specified ambient temperature. ON or 1 \- Use 302K as the ambient temperature when vector correction is applied and the tuner is an ECal or internal tuner.  
Examples |  SENS:NOIS:TEMP:AMB:AUTO 0 sense2:noise:temperature:ambient:auto on  
Query Syntax |  SENSe:NOISe:TEMPerature:AMBient:AUTO?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1 - ON  
  
* * *

## SENSe<ch>:NOISe:TEMPerature:SOURce:AUTO <bool>

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Read-
Write) If ON, will use 302K as the source temperature when vector correction
is applied and the tuner is an ECal or internal tuner. If OFF, will use the
specified source temperature.  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<bool> |  Choose from: OFF or 0 \- Use the specified source temperature. ON or 1 \- Use 302K as the source temperature when vector correction is applied and the tuner is an ECal or internal tuner.  
Examples |  SENS:NOIS:TEMP:SOUR:AUTO 0 sense2:noise:temperature:source:auto on  
Query Syntax |  SENSe:NOISe:TEMPerature:SOURce:AUTO?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1 - ON  
  
* * *

## SENSe<ch>:NOISe:TEMPerature:SOURce[:VALue] <num>

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Read-
Write) Sets the temperature at which the current noise measurement is
occurring. [Learn
more](../../../Applications/Noise_Figure.htm#Source_Temperature)  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<num> |  Source temperature in Kelvin.  
Examples |  SENS:NOIS:TEMP:SOUR 292 sense:noise:temperature:source 289  
Query Syntax |  SENSe:NOISe:TEMPerature:SOURce[:VALue]?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  297  
  
* * *

## SENSe<ch>:NOISe:TUNer:FILE:NAME <string>

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Except
M9485A) (Read-Write) Set and read a custom noise tuner file to be used instead
of the one generated automatically based on the state. This is considered an
"expert user" feature and is therefore the responsibility of the user to
provide a calibration file that yields proper results. Specify the full path
of the file. If the full path is not specified, the noise tuner file must be
stored in the C:\Users\Public\Documents\Network Analyzer directory. To enable
the custom noise tuner file, the SENSe:NOISe:TUNer:FILE:STATE must be set to
ON.  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<string> |  Noise tuner file name.  
Examples |  SENS:NOIS:TUN:FILE:NAME "MyNoiseFile.tm" sense:noise:tuner:file:name "MyNoiseFile.tm"  
Query Syntax |  SENSe:NOISe:TUNer:FILE:NAME?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SENSe<ch>:NOISe:TUNer:FILE[:STATe] <bool>

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Except
M9485A) (Read-Write) Sets the state of the custom noise tuner file specified
using the SENSe:NOISe:TUNer:FILE:NAME command.  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<bool> |  Custom noise tuner file state. Choose from: OFF or 0 \- Disable custom noise tuner file ON or 1 \- Enable custom noise tuner file  
Examples |  SENS:NOIS:TUN:FILE 1 sense2:noise:tuner:file:state ON  
Query Syntax |  SENSe:NOISe:TUNer:FILE[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0 - OFF  
  
* * *

## SENSe<ch>:NOISe:TUNer:ID <string>

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Except
M9485A) (Read-Write) Set and read the identity of the noise tuner. This is an
ECal model and serial number string. To read the identities of the connected
ECal modules, use [SENSe:CORRection:CKIT:ECAL:LIST?](CorrCKIT_SCPI.md#List)
and [SENSe:CORRection:CKIT:ECAL<mod>:INFormation?](CorrCKIT_SCPI.md#ECALInf)  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<string> |  ECal model and serial number string. The ECal module must be connected when this command is sent.  
Examples |  SENS:NOIS:TUN:ID "N4691-60004 ECal 02822" sense:noise:tuner:id ""N4691-60004 ECal 02822"  
Query Syntax |  SENSe:NOISe:TUNer:ID?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SENSe<ch>:NOISe:TUNer:INPut <string>

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Except
M9485A) (Read-Write) Sets and reads the port of the ECal noise tuner that is
connected to the VNA SOURCE OUT.  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<string> |  ECal port identifier. Case sensitive.  
Examples |  SENS:NOIS:TUN:INP "B" sense:noise:tuner:input "A"  
Query Syntax |  SENSe:NOISe:TUNer:INPut?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  "B"  
  
* * *

## SENSe<ch>:NOISe:TUNer:ORIent[:STATe] <bool>

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Except
M9485A) (Read-Write) Sets the state of auto orientation for a noise tuner
during Noise Figure for NFX.  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<bool> |  Auto-orientation state. Choose from: OFF or 0 \- Disable Auto-orientation ON or 1 \- Enable Auto-orientation  
Examples |  SENS:NOIS:TUN:ORI 0 sense2:noise:tuner:orient:state ON  
Query Syntax |  SENSe:NOISe:TUNer:ORIent[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1 - ON  
  
* * *

## SENSe<ch>:NOISe:TUNer:OUTPut <string>

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Except
M9485A) (Read-Write) Sets and reads the port of the ECal noise tuner that is
connected to the CPLR THRU.  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
<string> |  ECal port identifier. Case sensitive.  
Examples |  SENS:NOIS:TUN:OUTP "B" sense:noise:tuner:output "A"  
Query Syntax |  SENSe:NOISe:TUNer:OUTput?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  "A"  
  
## SENSe<ch>:NOISe:USBSource:CATalog?

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Read
only) Returns a comma separated list of connected USB Noise Sources,
identified by their usbNsSrcID: ModelNumber Serialnumber.  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
Examples |  SENS:NOIS:USBS:CAT? sense:noise:usbsource:catalog?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SENSe<ch>:NOISe:USBSource:ENR:SAVE " usbNsSrcID ","filename"

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Write
only) This writes the ENR file stored in USB Noise Sensor to the filename
specified by filename  Notee: When a full path is not given, the .enr file
will be written to the default folder. Change the default folder name using[
MMemory:CDIRectory](../Memory.htm#chgdir).  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
Examples |  SENS:NOIS:ENR:SAVE U1831C MY12345678,C:\myUSBSensor.enr sense:noise:enr:save U1231C MY12345678, my.enr  
Query Syntax |  None  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SENSe<ch>:NOISe:USBSource[:SELect] usbNsSrcID

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Read-
Write) Sets and queries the USB noise source to use for calibration,
identified by their usbNsSrcID: ModelNumber Serialnumber.  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
Examples |  SENS:NOIS:USBS:SEL U1831C MY12345678 sense:noise:usbsource:select U1831C MY12345678  
Query Syntax |  SENSe:NOISe:USBSource?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SENSe<ch>:NOISe:USBSource:TEMPerature? "usbNsSrcID"

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Read only) Returns sensor reported temperature in Kelvin as reported by the USB noise Source.  |  Note: This can be used to help determine what temperature to use for the noise source temperature during calibration. Learn more about [ConfigureNSDiag](../../../Applications/Noise_Cal.md#ConfigureNSDiag).  The commands to set the noise source connector temperature for calibration remotely are:  Smart Cal: SENSe<cnum>:CORRection:TCOLd:USER:VALue<num> Cal All: SYSTem:CALibrate:ALL[1-250]:MCLass:PROPerty:VALue[:STATe] Noise Source Temperature,<value>  
---  
Parameters |   
<ch> |  Noise Figure channel number. If unspecified, value is set to 1.  
Examples |  SENS:NOIS:USBS:TEMP? U1831C MY12345678 sense:noise:usbsource:select U1831C MY12345678  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

