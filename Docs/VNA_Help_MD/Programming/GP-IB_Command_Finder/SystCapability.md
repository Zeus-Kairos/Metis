# SYSTem:CAPability Commands

* * *

Reads various capabilities of the analyzer.

SYSTem:CAPability: ALC:POWer: | [MAXimum[:LEVel]?](SystCapability.md#ALC:POWer:MAX) | [MINimum[:LEVel]?](SystCapability.md#ALCPOWerMIN) [CHANnels:MAXimum[:COUNt]?](SystCapability.md#ChanMAX) DELay | TRIGger | MAX? | MIN? [FOM:EXISts?](SystCapability.md#FomEXISts) FREQuency | [MAXimum?](SystCapability.md#FreqMax) | [MINimum?](SystCapability.md#FreqMin) HARDware: | ATTenuator:RECeiver: | [EXISts?](SystCapability.md#hardAttRecExist) | [MAXimum?](SystCapability.md#hardAttRecMax) | [STEP[:SIZE]?](SystCapability.md#hardAttRecStep) | ATTenuator:SOURce: | [MAXimum?](SystCapability.md#hardAttSourMax) | [STEP[:SIZE]?](SystCapability.md#hardAttSourStep) | DC:RECeiver | INTernal:CATalog? | INTernal:COUNt? | DC:SOURce | INTernal:CATalog? | INTernal:COUNt? | IF | MAXimum? | MINimum? | LFEXtension | EXISts? | [MODule](SystCapHardModule.md) | PORTs: | [CATalog?](SystCapability.md#hardPortsCat) | [COUNt?](SystCapability.md#hardPortsCount) | INTernal | [CATalog?](SystCapability.md#hardPortIntCat) | [COUNt?](SystCapability.md#hardPortIntCount) | [PNUMber?](SystCapability.md#hardPortPnum) | SOURce | [CATalog?](SystCapability.md#hardPortSourCat) | [COUNt?](SystCapability.md#hardPortSourCount) | INTernal | [CATalog?](SystCapability.md#hardPortSourIntCat) | [COUNt?](SystCapability.md#hardPortSourIntCount) | POWer | DISCrete | FREQuency | LIST | MAXimum? | LIST? | MINimum? | LIST? | PATH | CONFig | ELEMent | CATalog? | [:STATe] | VALue | CATalog? | PORT | RANGe | FREQuency | STARt | STOP | MAXimum? | MINimum? | RESet | TYPE | [RBSWitch:EXISts?](SystCapability.md#hardRBSwitch) | RECeiver: | GAIN | COUPling | CONTrol? | INTernal | [COUNt?](SystCapability.md#hardRecCount) | [DACCess?](SystCapability.md#RecDaccess) | [SOURce:COUNt?](SystCapability.md#hardSrcCount) [IFBW:CATalog?](SystCapability.md#ifbwCat) IFBW | MAXimum? | MINimum? LICenses: | CATalog? | FEATure | CATalog? | ENABle? NBW: | [NOISe:CATalog?](SystCapability.md#nbwNoise) | [STD:CATalog?](SystCapability.md#nbwStd) POINts: | [MAXimum?](SystCapability.md#pointsMax) | [MINimum?](SystCapability.md#pointsMin) PRESet:FREQuency: | [MAXimum?](SystCapability.md#presFreqMax) | [MINimum?](SystCapability.md#presFreqMin) [RBW:IMS:CATalog?](SystCapability.md#rbwIMS) [RBW:SA:CATalog?](SystCapability.md#rbwSaCat) SUPPort | DWELl? | RIFBw? WINDows | [MAXimum[:COUNt]?](SystCapability.md#windMax) | [TRACes:MAXimum[:COUNt]?](SystCapability.md#windTracesMax)  
---  
  
Click on a red keyword to view the command details.

## SYSTem:CAPability:HARDware:POWer Commands

These commands provide access to data sheet specified and typical, max and min
power levels (in dBm). Max power refers to the maximum leveled source power at
the specified port. Min power is calculated by subtracting the power sweep
range from the max leveled power. This information is stored by frequency band
in a power specification file. These commands provide access to the files
contents and provide an interface to configure the port number and RF signal
path of interest.

Power data is available as either the most restrictive value across a range of
frequencies (when SYST:CAP:HARD:POW:RANG:MAX and SYST:CAP:HARD:POW:RANG:MIN
are used) or for discrete CW frequencies (when SYST:CAP:HARD:POW:DISC:MAX and
SYST:CAP:HARD:POW:DISC:MIN are used).

No measurement of instrument-specific dynamic range is performed; all power
levels are equivalent to power data published in device data sheets. Power
levels are valid only for measurement configurations where the front panel
jumpers are in their standard positions, as originally shipped. Internal
source attenuation and any calibrated external path loss/gain due to cables,
fixtures, switches or booster amplifiers are not included in the reported
min/max leveled power values. It remains the users responsibility to
transform the reported factory power range data to a value corresponding to
the specific calibration plane of their setups.

The power range data files contain both specified min/max leveled power values
and the corresponding typical values. Some paths, that are not part of the
specifications of the instrument may only have typical data. Only the
Specified power range data is guaranteed for an instrument with an up-to-
date calibration certificate.

## Setting Up Power Range

The following describes the command sequence for setting up power range to
query the right information.

Setup Power Range to correct path and path settings:

  1. Set to the port that you would like to query leveled output power  
SYST:CAP:HARD:POW:PORT <portNum>

  2. Find path elements available for the port specified (Optional)  
SYST:CAP:HARD:POW:PATH:CONF:ELEM:CAT?

  3. Find settings for a path element name given by the above command (Optional)  
SYST:CAP:HARD:POW:PATH:CONF:ELEM:VAL:CAT? <PathElementName>

  4. Specify the path element and the value to query power data from  
SYST:CAP:HARD:POW:PATH:CONF:ELEM:STAT <PatheElementName> ,
<PathElementSetting>

Query power limits for the port using a specific path and path settings:

Discrete frequencies: (CW)

  1. Input discrete frequencies of interest  
SYST:CAP:HARD:POW:DISC:FREQ:LIST <freqList>

  2. Query maximum power limit of each frequency in the list  
SYST:CAP:HARD:POW:DISC:MAX:LIST?

  3. Query minimum power limit of each frequency in the list  
SYST:CAP:HARD:POW:DISC:MIN:LIST?

  4. Query most restrictive maximum of all frequencies in the list  
SYST:CAP:HARD:POW:DISC:MAX?

  5. Query most restrictive minimum of all frequencies in the list  
SYST:CAP:HARD:POW:DISC:MIN?

Frequency range: (Freq sweep)

  1. Input start frequency  
SYST:CAP:HARD:POW:RANG:FREQ:STAR <startFreq>

  2. Input stop frequency  
SYST:CAP:HARD:POW:RANG:FREQ:STOP <stopFreq>

  3. Query the most restrictive maximum within the specified range  
SYST:CAP:HARD:POW:RANG:MAX?

  4. Query the most restrictive minimum within the specified range  
SYST:CAP:HARD:POW:RANG:MIN?

See Also

  * [Example Programs](../GPIB_Example_Programs/Perform_a_CalAllChannels_Calibration.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## SYSTem:CAPability:DELay:TRIGger:MAX?

Applicable Models: All (Read-only) Returns the maximum trigger delay of the
analyzer.  
---  
Parameters | None  
Examples | SYST:CAP:DEL:TRIG:MAX?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:DELay:TRIGger:MIN?

Applicable Models: All (Read-only) Returns the minimum trigger delay of the
analyzer.  
---  
Parameters | None  
Examples | SYST:CAP:DEL:TRIG:MIN?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:ALC:POWer:MAXimum[:LEVel]?

Applicable Models: All (Read-only) Returns the maximum leveled source power
setting in dB. [Learn more about leveled source
power](../../S1_Settings/Power_Level.htm#Leveling).  
---  
Parameters | None  
Examples | SYST:CAP:ALC:POW:MAX?   
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:ALC:POWer:MINimum[:LEVel]?

Applicable Models: All (Read-only) Returns the minimum leveled source power
setting in dB with 0 dB attenuation. [Learn more about leveled source
power](../../S1_Settings/Power_Level.htm#Leveling).  
---  
Parameters | None  
Examples | SYST:CAP:ALC:POW:MIN?   
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:CHANnels:MAXimum[:COUNt]?

Applicable Models: All (Read-only) Returns the maximum possible number of
channels. [Learn more about
Channels](../../S0_Start/Traces_Channels_and_Windows.htm#channel).  
---  
Parameters | None  
Examples | SYST:CAP:CHAN:MAX?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:FOM:EXISts?

Applicable Models: All (Read-only) Returns whether or not the analyzer has FOM
installed. [Learn more](../../FreqOffset/Frequency_Offset_Mode.md).  
---  
Parameters | None  
Examples | SYST:CAP:FOM:EXIS?  
Return Type | Boolean 1 - Yes, FOM is installed. 0 - No, FOM is NOT installed.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:FREQuency:MAXimum?

Applicable Models: All (Read-only) Returns the maximum frequency of the
analyzer, including any over-sweep. Over-sweep frequencies can be set but are
not specified.  
---  
Parameters | None  
Examples | SYST:CAP:FREQ:MAX?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:FREQuency:MINimum?

Applicable Models: All (Read-only) Returns the minimum frequency of the
analyzer, including any under-sweep. Under-sweep frequencies can be set but
are not specified.  
---  
Parameters | None  
Examples | SYST:CAP:FREQ:MIN?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:ATTenuator:RECeiver:EXISts? <portNum>

Applicable Models: All (Read-only) Returns whether or not there is a receiver
attenuator on the specified port.  
---  
Parameters |   
<portNum> | Port number. Choose from the number of test ports on the analyzer.  
Examples | SYST:CAP:HARD:ATT:REC:EXIS? 2  
Return Type | Boolean 1 - Yes, the test port has a receiver attenuator. 0 - No, the test port does NOT have a receiver attenuator.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:ATTenuator:RECeiver:MAXimum? <portNum>

Applicable Models: All (Read-only) Returns the maximum amount of receiver
attenuation on the specified port. See
[SYST:CAP:HARD:ATT:REC:EXIS?](SystCapability.md#hardAttRecExist) to check if
there is a receiver attenuator on the specified port.  
---  
Parameters |   
<portNum> | Port number. Choose from the number of test ports on the analyzer.  
Examples | SYST:CAP:HARD:ATT:REC:MAX? 2  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:ATTenuator:RECeiver:STEP[:SIZE]? <portNum>

Applicable Models: All (Read-only) Returns the step size of the receiver
attenuator on the specified port. See
[SYST:CAP:HARD:ATT:REC:EXIS?](SystCapability.md#hardAttRecExist) to check if
there is a receiver attenuator on the specified port.  
---  
Parameters |   
<portNum> | Port number. Choose from the number of test ports on the analyzer.  
Examples | SYST:CAP:HARD:ATT:REC:STEP? 2  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:ATTenuator:SOURce:MAXimum? <portNum>

Applicable Models: All (Read-only) Returns the maximum amount of source
attenuation on the specified port.  
---  
Parameters |   
<portNum> | Port number. Choose from the number of test ports on the analyzer.  
Examples | SYST:CAP:HARD:ATT:SOUR:MAX? 2  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:ATTenuator:SOURce:STEP[:SIZE]? <portNum>

Applicable Models: All (Read-only) Returns the step size of the source
attenuator on the specified port.  
---  
Parameters |   
<portNum> | Port number. Choose from the number of test ports on the analyzer.  
Examples | SYST:CAP:HARD:ATT:SOUR:STEP? 2  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:DC:RECeiver:INTernal:CATalog?

Applicable Models: All (Read-only) Returns a list of names of the internal DC
receivers.  
---  
Parameters | None  
Examples | SYST:CAP:HARD:DC:REC:INT:CAT?  
Return Type | String of internal DC receivers separated by commas. For example, "AI1,AI2,AIG,AOS1,AOS2"  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:DC:RECeiver:INTernal:COUNt?

Applicable Models: All (Read-only) Returns the number of internal DC receivers
in the analyzer.  
---  
Parameters | None  
Examples | SYST:CAP:HARD:DC:REC:INT:COUN?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:DC:SOURce:INTernal:CATalog?

Applicable Models: All (Read-only) Returns a list of names of the internal DC
sources.  
---  
Parameters | None  
Examples | SYST:CAP:HARD:DC:SOUR:INT:CAT?  
Return Type | String of internal DC sources separated by commas. For example, "AO1,AO2"  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:DC:SOURce:INTernal:COUNt?

Applicable Models: All (Read-only) Returns the number of internal DC sources
in the analyzer.  
---  
Parameters | None  
Examples | SYST:CAP:HARD:DC:SOUR:INT:COUN?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:IF:MAXimum?

Applicable Models: N522xB, N523xB, N524xB (Read-only) Returns the maximum IF
frequency the instrument supports.  
---  
Parameters | None  
Examples | SYST:CAP:HARD:IF:MAX?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:IF:MINimum?

Applicable Models: All (Read-only) Returns the minimum IF frequency the
instrument supports.  
---  
Parameters | None  
Examples | SYST:CAP:HARD:IF:MIN?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:LFEXtension:EXISts?

Applicable Models: All (Read-only) Returns whether or not the VNA has the low
frequency extension (LFE) installed. [Learn
more](../../IFAccess/Low_Frequency_Extension/Overview.htm).  
---  
Parameters | None  
Examples | SYST:CAP:HARD:LFEX:EXISts?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:PORTs:CATalog?

Applicable Models: All (Read-only) Returns a list of test port names including
external testset ports.  
---  
Parameters | None  
Examples | SYST:CAP:HARD:PORT:CAT?  
Return Type | String of port names separated by commas. For example, "Port 1,Port 2,Port 3,Port 4".  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:PORTs:COUNt?

Applicable Models: All (Read-only) Returns the number of test ports including
external testset ports.  
---  
Parameters | None  
Examples | SYST:CAP:HARD:PORT:COUN?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:PORTs:INTernal:CATalog?

Applicable Models: All (Read-only) Returns a list of internal test port names.  
---  
Parameters | None  
Examples | SYST:CAP:HARD:PORT:INT:CAT?  
Return Type | String of port names separated by commas. For example, "Port 1,Port 2,Port 3,Port 4".  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:PORTs:INTernal:COUNt?

Applicable Models: All (Read-only) Returns the number of internal test ports.  
---  
Parameters | None  
Examples | SYST:CAP:HARD:PORT:INT:COUN?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:PORTs:PNUMber? <portName>

Applicable Models: All (Read-only) Returns the port number associated with the
specified port name.  
---  
Parameters | None  
<portName> | String. Port name. Use [SYST:CAP:HARD:PORT:CAT?](SystCapability.md#hardPortSourCat) to return a list of valid port names.  
Examples | SYST:CAP:HARD:PORT:PNUM? "Port 1"  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:PORTs:SOURce:CATalog?

Applicable Models: All (Read-only) Returns a list of source port names,
including any configured external sources.  
---  
Parameters | None  
Examples | SYST:CAP:HARD:PORT:SOUR:CAT?  
Return Type | String of source port names separated by commas. For example, "Port 1,Port 2,Port 3,Port 4, Port 1 Src 2,Source3".  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:PORTs:SOURce:COUNt?

Applicable Models: All (Read-only) Returns the number of source ports,
including any configured external sources.  
---  
Parameters | None  
Examples | SYST:CAP:HARD:PORT:SOUR:COUN?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:PORTs:SOURce:INTernal:CATalog?

Applicable Models: All (Read-only) Returns a list of internal source port
names.  
---  
Parameters | None  
Examples | SYST:CAP:HARD:PORT:SOUR:INT:CAT?  
Return Type | String of internal source port names separated by commas. For example, "Port 1,Port 2,Port 3,Port 4, Port 1 Src 2,Source3"  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:PORTs:SOURce:INTernal:COUNt?

Applicable Models: All (Read-only) Returns the number of internal source
ports.  
---  
Parameters | None  
Examples | SYST:CAP:HARD:PORT:SOUR:INT:COUN?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:POWer:DISCrete:FREQuency:LIST <freqList>

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Sets or returns the
list of discrete frequencies corresponding to the powers returned by the
discrete min and max power list functions.  
---  
Parameters |   
<freqList> | List of frequencies for which power is returned.  
Examples | SYST:CAP:HARD:POW:DISC:FREQ:LIST 1e9,2e9,3e9,4e9 system:capability:hardware:power:discrete:frequency:list 10e6,100e6,1e9,10e9  
Query Syntax | SYSTem:CAPability:HARDware:POWer:DISCrete:FREQuency:LIST?  
Return Type | Array  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:POWer:DISCrete:MAXimum?

Applicable Models: N522xB, N523xB, N524xB (Read-only) Returns a single max
leveled power value (in dBm) indicating the most restrictive maximum for all
discrete maximum powers (the minimum of all max leveled powers).  
---  
Parameters | None  
Examples | SYST:CAP:HARD:POW:DISC:MAX? System:capability:hardware:power:discrete:maximum?  
Return Type | Double  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:POWer:DISCrete:MAXimum:LIST?

Applicable Models: N522xB, N523xB, N524xB (Read-only) Returns an array of max
leveled power values (in dBm), where each element corresponds to the maximum
leveled power possible for CW stimulus at the corresponding frequency set by
the SYSTem:CAPability:HARDware:POWer:DISCrete:FREQuency:LIST command.  
---  
Parameters | None  
Examples | SYST:CAP:HARD:POW:DISC:MAX:LIST? system:capability:hardware:power:discrete:maximum:list?  
Return Type | Array  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:POWer:DISCrete:MINimum?

Applicable Models: N522xB, N523xB, N524xB (Read-only) Returns a single minimum
power value (in dBm) indicating the most restrictive minimum for all discrete
minimum powers (the maximum of all minimum powers).  
---  
Parameters | None  
Examples | SYST:CAP:HARD:POW:DISC:MIN? system:capability:hardware:power:discrete:minimum?  
Return Type | Double  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:POWer:DISCrete:MINimum:LIST?

Applicable Models: N522xB, N523xB, N524xB (Read-only) Returns an array of
minimum power values (in dBm), where each element corresponds to the minimum
power possible for CW stimulus at the corresponding frequency set by the
SYSTem:CAPability:HARDware:POWer:DISCrete:FREQuency:LIST command.  
---  
Parameters | None  
Examples | SYST:CAP:HARD:POW:DISC:MIN:LIST? System:capability:hardware:power:discrete:minimum:list?  
Return Type | Array  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:POWer:PATH:CONFig:ELEMent:CATalog?

Applicable Models: N522xB, N523xB, N524xB (Read-only) Returns a string with
the names of all valid RF path configuration elements.  
---  
Parameters | None  
Examples | SYST:CAP:HARD:POW:PATH:CONF:ELEM:CAT? syst:capability:hardware:power:path:conf:element:catalog?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:POWer:PATH:CONFig:ELEMent[:STATe]
<element>,<setting>

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Returns the name of the
value for the given path element name or sets the value of a path element.  
---  
Parameters |   
<element> | String \- Choose from all path elements listed with SYST:CAP:HARD:POW:PATH:CONF:ELEM:CAT?.  
<setting> | String \- Choose from all element settings listed with SYST:CAP:HARD:POW:PATH:CONF:ELEM:VAL:CAT?.  
Examples | SYST:CAP:HARD:POW:PATH:CONF:ELEM Src1Out1LowBand,HiPwr SYST:CAP:HARD:POW:PATH:CONF:ELEM:STAT Port1Bypass,Thru  
Query Syntax | SYSTem:CAPability:HARDware:POWer:PATH:CONFig:ELEMent:STATe? Src2Out1LowBand Returns the setting for the specified element.  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:POWer:PATH:CONFig:ELEMent:VALue:CATalog?
<PathElementName>

Applicable Models: N522xB, N523xB, N524xB (Read-only) Returns all valid values
for the given path configuration element.  
---  
Parameters |   
<PathElementName> | (String) Chose from all path elements (see PATH:CONF:ELEM:CAT?)  
Examples | SYST:CAP:HARD:POW:PATH:CONF:ELEM:VAL:CAT? syst:capability:hardware:power:path:conf:element:value:catalog?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:POWer:PORT <portNum>

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Sets and reads the port
number for power range data. When two sources are available in combiner mode,
refer to the portNum selections below.  
---  
Parameters |   
<portNum> | Port number. Choose from: 1 - Port 1. 2 - Port 2. 3 - Port 3 (4-port instrument) or Src2-Out1 (2-port instrument with option 224). 4 - Port 4 (4-port instrument) or Src2-Out2 (2-port instrument with option 423). 5 - Src2Out1LowBand (2-port with option 224 or 4-port with option 423). 6 \- Source 3  
Examples | SYST:CAP:HARD:POW:PORT 1   
Query Syntax | SYSTem:CAPability:HARDware:POWer:PORT?  
Return Type | Integer  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:POWer:RANGe:FREQuency:STARt <num>

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Sets or returns the
lower bound of the frequency range used for range based power min and max.  
---  
Parameters |   
<num> | Start frequency. Choose a number within the frequency limits of the analyzer. Units are Hz.  
Examples | SYST:CAP:HARD:POW:RANG:FREQ:STAR 1e9 system:capability:hardware:power:range:frequency:start 1e9  
Query Syntax | SYSTem:CAPability:HARDware:POWer:RANGe:FREQuency:STARt?  
Return Type | Double  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:POWer:RANGe:FREQuency:STOP <num>

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Sets or returns the
upper bound of the frequency range used for range based power min and max.  
---  
Parameters |   
<num> | Stop frequency. Choose a number within the frequency limits of the analyzer. Units are Hz.  
Examples | SYST:CAP:HARD:POW:RANG:FREQ:STOP 2e9  
Query Syntax | SYST:CAP:HARD:POW:RANG:FREQ:STOP?  
Return Type | Double  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:POWer:RANGe:MAXimum?

Applicable Models: N522xB, N523xB, N524xB (Read-only) Returns the minimum of
all max leveled power values (in dBm) from range start frequency to stop
frequency (inclusive).  
---  
Parameters | None  
Examples | SYST:CAP:HARD:POW:RANG:MAX?  
Return Type | Double  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:POWer:RANGe:MINimum?

Applicable Models: N522xB, N523xB, N524xB (Read-only) The maximum of all min
power values (in dBm) from range start frequency to stop frequency
(inclusive).  
---  
Parameters |   
Examples | SYST:CAP:HARD:POW:RANG:MIN?  
Return Type | Double  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:POWer:RESet

Applicable Models: N522xB, N523xB, N524xB (Write-only) Resets all power range
properties to default values, as if the instrument had been preset. Power
range type is set to SPECified, port number is set to 1 with all path
configuration elements in their default states.  
---  
Parameters | None  
Examples | SYST:CAP:HARD:POW:RES system:capability:hardware:power:reset  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:POWer:TYPE <enum>

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Sets and reads the type
of power range data (specified or typical) to be returned.  
---  
Parameters |   
<enum> | Choose from: SPECified \- Warranted performance. TYPical \- Typical performance.  
Examples | SYST:CAP:HARD:POW:TYPE SPEC system:capability:hardware:power:type typical  
Query Syntax | SYSTem:CAPability:HARDware:POWer:TYPE?  
Return Type | Enumeration  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | SPECified  
  
* * *

## SYSTem:CAPability:HARDware:RBSWitch:EXISts? <portNum>

Applicable Models: All (Read-only) Returns whether or not the specified port
number has a reference bypass switch.  
---  
Parameters |   
<portNum> | Port number. Choose from the number of test ports on the analyzer.  
Examples | SYST:CAP:HARD:RBSW:EXIS? 2  
Return Type | Boolean 1 - Yes, the test port has a reference bypass switch. 0 - No, the test port does NOT have a reference bypass switch.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:RECeiver:GAIN:COUPling:CONTrol? <port>

Applicable Models: M983xA (Read-only) Returns whether or not the gain coupling
can be changed.  
---  
Parameters |   
<port> | Port number.  
Examples | SYST:CAP:HARD:REC:GAIN:COUP:CONT? 1  
Return Type | Boolean (0 =NOT changeable , 1 = Changeable)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:RECeiver:INTernal:COUNt?

Applicable Models: All (Read-only) Returns the number of receivers in the
analyzer.  
---  
Parameters | None  
Examples | SYST:CAP:HARD:REC:INT:COUN?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:RECeiver:DACCess?

Applicable Models: All (Read-only) Returns whether or not the analyzer has
direct receiver access (front-panel jumpers).  
---  
Parameters | None  
<bool> | Choose from: 1 \- Yes, the analyzer has direct receiver access. 0 \- No, the analyzer does NOT have direct receiver access.  
Examples | SYST:CAP:HARD:REC:DACC?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:HARDware:SOURce:COUNt?

Applicable Models: All (Read-only) Returns the number of sources in the
analyzer.  
---  
Parameters | None  
Examples | SYST:CAP:HARD:SOUR:COUN?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:IFBW:CATalog?

Applicable Models: All (Read-only) Returns the list of supported IFBW values.  
---  
Parameters | None  
Examples | SYST:CAP:IFBW:CAT?  
Return Type | Variant array of string values  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:IFBW:MAXimum?

Applicable Models: All (Read-only) Returns the maximum IFBW for the standard
IF filter.  
---  
Parameters | None  
Examples | SYST:CAP:IFBW:MAX?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:IFBW:MINimum?

Applicable Models: All (Read-only) Returns the minimum IFBW for the standard
IF filter.  
---  
Parameters | None  
Examples | SYST:CAP:IFBW:MIN?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:LICenses:CATalog? <selection>

Applicable Models: All (Read-only) Returns the list of licenses. [See a list
of common licenses](../../Support/Configurations.htm#options).  
---  
Parameters |   
<selection> | Choose from: VALID \- Return a list of licenses which have enabled VNA features. For PXI/USB VNA, only software licenses are returned. For PNA/ENA, all options including hardware are returned. ALL \- Return a list of all installed licenses/options in the Keysight License Manager including the ones not related to the VNA software. IGNORED \- Return a list of VNA software licenses which are either invalid or ignored. This can occur when a transportable license is transported to an instrument that does not support the license feature. In addition, this can occur when multiple licenses for the same base feature are installed and only the least restrictive license is used (the more restrictive licenses are ignored). For example, when transporting multiple Spectrum Analyzer licenses to the same instrument, the license with the greatest frequency range is used and the other licenses are ignored. Note: Licenses not related to the VNA software but installed on the instrument are not reported as ignored when using IGNORED.  
Examples | SYST:CAP:LIC:CAT? ALL N5242B-423,N5242B-020,N5242B-021,N5242B-022,S93029A/B-1FP  
Return Type | Variant array of string values  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:LICenses:FEATure:CATalog?

Applicable Models: All (Read-only) Returns the list of licensed features. [See
a list of licensed
features](../../Support/Software_Support.htm#List_of_Licensed_Features).  
---  
Parameters | None  
Example | SYST:CAP:LIC:FEAT:CAT?  "Gain Compression Phase,AFR Config and 2X Thru for N Port,Mixer CSV Format,Support for U1832X and U1833X Noise Sources,TD Transform Window,SA IQ Data Output,Modulation Distortion IQ Data Output,L8990M Switch Matrix,Drift Cal,"  
Return Type | Variant array of string values  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:LICenses:FEATure:ENABle? <feature name>

Applicable Models: All (Read-only) Returns a "1" if the specified feature is
enabled and a "0" if the specified feature is disabled. [See a list of
licensed
features](../../Support/Software_Support.htm#List_of_Licensed_Features).  
---  
Parameters |   
<feature name> | Licensed feature name. Use SYSTem:CAPability:LICenses:FEATure:CATalog? to return a list of licensed feature names.  
Example | SYST:CAP:LIC:FEAT:ENAB? "Gain Compression Phase" 1  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:NBW:NOISe:CATalog?

Applicable Models: All (Read-only) Returns the list of supported Noise
Bandwidth values when using a noise receiver (option 029). [Learn more about
Opt. 029](../../Applications/Noise_Figure.htm#OptionsExplained).  
---  
Parameters | None  
Examples | SYST:CAP:NBW:NOIS:CAT?  
Return Type | Variant array of string values  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:NBW:STD:CATalog?

Applicable Models: All (Read-only) Returns the list of supported Noise
Bandwidth values when using the NA receiver for noise measurements (option
028). [Learn more about Opt
028](../../Applications/Noise_Figure.htm#OptionsExplained).  
---  
Parameters | None  
Examples | SYST:CAP:NBW:STD:CAT?  
Return Type | Variant array of string values  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:POINts:MAXimum?

Applicable Models: All (Read-only) Returns the maximum number of points.  
---  
Parameters | None  
Examples | SYST:CAP:POIN:MAX?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:POINts:MINimum?

Applicable Models: All (Read-only) Returns the minimum number of points.  
---  
Parameters | None  
Examples | SYST:CAP:POIN:MIN?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:PRESet:FREQuency:MAXimum?

Applicable Models: All (Read-only) Returns the maximum specified frequency of
the analyzer. Does not include any over-sweep. See also:
[SYST:CAP:FREQ:MAX?](SystCapability.md#FreqMax)  
---  
Parameters | None  
Examples | SYST:CAP:PRES:FREQ:MAX?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:PRESet:FREQuency:MINimum?

Applicable Models: All (Read-only) Returns the minimum specified frequency of
the analyzer. Does not include any under-sweep. See also:
[SYST:CAP:FREQ:MIN?](SystCapability.md#FreqMin)  
---  
Parameters | None  
Examples | SYST:CAP:PRES:FREQ:MIN?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:RBW:IMS:CATalog?

Applicable Models: All (Read-only) Returns the list of supported Resolution BW
values for the IMSpectrum channel. [Learn more about
IMSpectrum](../../Applications/Swept_IMD_and_IM_Spectrum_Concepts.htm#HowIMSpectrum).  
---  
Parameters | None  
Examples | SYST:CAP:RBW:IMS:CAT?  
Return Type | Variant array of string values  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:RBW:SA:CATalog?

Applicable Models: All with Spectrum Analysis Options (S9x09xxA/B, S9x090A/B)
(Read-only) Returns the list of supported Resolution BW values for the SA
channel. [Learn more about the SA
application.](../../Applications/Spectrum_Analyzer.htm)  
---  
Parameters | None  
Examples | SYST:CAP:RBW:SA:CAT?  
Return Type | Variant array of string values  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:SUPPort:DWELl? <ifBandwidth>

Applicable Models: VNAs with S93070xA/B or S95070A/B (Read-only) Returns
whether a given IF Bandwidth value supports dwell time (dwell time between
each sweep point). Dwell time can be used for all IF Bandwidth values.  
---  
Parameters |   
<ifBandwidth> | IF Bandwidth value.  
Examples | SYST:CAP:SUPP:DWEL? 1E3  
Return Type | Boolean 0 = False 1 = True  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:SUPPort:RIFBw?

Applicable Models: VNAs with S93070xA/B or S95070A/B (Read-only) Returns
whether the VNA supports the [Reduce IF BW at Low
Frequencies](../../S2_Opt/Trce_Noise.htm#ReduceIFBW) feature. The noise floor
increases at low frequencies. By reducing the IFBW automatically, the noise
floor is kept constant. Otherwise, measurements get nosier at low frequencies.
When a constant bandwidth is required (for pulse measurement for instance),
then the [Reduce IF BW at Low
Frequencies](../../S2_Opt/Trce_Noise.htm#ReduceIFBW) is turned off.  
---  
Parameters | None  
Examples | SYST:CAP:SUPP:RIFB?  
Return Type | Boolean 0 = False 1 = True  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:WINDows:MAXimum[:COUNt]?

Applicable Models: All (Read-only) Returns the maximum number of windows.
[Learn more](../../S0_Start/Traces_Channels_and_Windows.md).  
---  
Parameters | None  
Examples | SYST:CAP:WIND:MAX?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CAPability:WINDows:TRACes:MAXimum[:COUNt]?

Applicable Models: All (Read-only) Returns the maximum number of traces per
window. [Learn more](../../S0_Start/Traces_Channels_and_Windows.md).  
---  
Parameters | None  
Examples | SYST:CAP:WIND:TRAC:MAX?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

