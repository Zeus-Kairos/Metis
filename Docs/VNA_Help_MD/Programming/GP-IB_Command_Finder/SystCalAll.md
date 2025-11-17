# SYSTem:CALibrate:ALL Commands

* * *

Contains the settings to configure a "Cal All" Calibration.

Use the [Guided Cal](Sense/CorrGuided.md) interface to perform the
calibration.

SYSTem:CALibrate:ALL: CHANnel: | [PORTs[:SELect]](SystCalAll.md#PortsSelect) CSET: | [CATalog?](SystCalAll.md#csetCat) [ | PREFix](SystCalAll.md#csetPrefix) GUIDed: | CHANnel:LIST? | [CHANnel[:VALue]?](SystCalAll.md#GuideChan) | [PORTs?](SystCalAll.md#GuidedPorts) [IFBW](SystCalAll.md#ifbw) INDependent: | SOURce: | CALibration: | CATalog? | RANGe: | ADD | CLEar | COUNt | PONts | STARt | STOP MCLass: | PROPerty: | [NAME:CATalog?](SystCalAll.md#PropNameCat) | VALue: | [CATalog?](SystCalAll.md#PropValueCat) | [[STATe]](SystCalAll.md#PropValueSelect) PATH: | CONFigure: | ELEMent PORT<n>: | [RECeiver:ATTen](SystCalAll.md#RecAtten) | SOURce:POWer: | [ATTen](SystCalAll.md#SourceAtten) | [OFFSet](SystCalAll.md#SourceOffset) | [[VALue]](SystCalAll.md#SourcePower) [RESet](SystCalAll.md#Reset) [SELect](SystCalAll.md#ChanSelect)  
---  
  
Click on a red keyword to view the command details.

See Also

  * [About Calibrate All Channels](../../S3_Cals/Calibrate_All_Channels.md)

  * [Example Programs](../GPIB_Example_Programs/Perform_a_CalAllChannels_Calibration.md)

  * [Guided Cal commands](Sense/CorrGuided.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## SYSTem:CALibrate:ALL[1-500]:CHANnel<ch>:PORTs[:SELect] <value>

Applicable Models: All (Write-Read) For each channel to be calibrated, sets
and returns the ports to be calibrated. Specify port numbers ONLY for standard
channels.  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
<ch> |  Channel number to be calibrated.  
<value> |  Ports to be calibrated for the specified channel. Select any of the native VNA ports (1,2,3,4).  
Examples |  SYST:CAL:ALL:CHAN2:PORT 1,2,3  
Query Syntax |  SYSTem:CALibrate:ALL:CHANnel<ch>:PORTs[:SELect]?  
Return Type |  Comma-separated port numbers.  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1,2  
  
* * *

## SYSTem:CALibrate:ALL[1-500]:CSET:CATalog?

Applicable Models: All (Read-only) Returns the User Cal Set or cal register
names that were produced by the cal all session.  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
Examples |  SYST:CAL:ALL:CSET:CATalog? 'returns this format: "MyCalAll_STD_001, MyCalAll_SMC_002" [See example program](../GPIB_Example_Programs/Perform_a_CalAllChannels_Calibration.md)  
Return Type |  String of comma-separated Cal Set or cal register names  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:CALibrate:ALL[1-500]:CSET:PREFix<value>

Applicable Models: All (Write-Read) Sets and returns the prefix to be used
when saving User Cal Sets that result from the Cal All session. The Meas Class
and channel number are appended to this prefix for each calibrated channel.
Use [SYST:CAL:ALL:CSET:CATalog?](SystCalAll.md#csetCat) to read the saved cal
set names.

  * [SENS:CORR:COLL:GUID:SAVE:CSET](Sense/CorrGuided.md#SaveCSET) can also be used to set the Cal Set prefix.
  * If a Cal Set prefix is NOT set using either command, the cal data for each channel will be saved only to cal registers. [Learn about cal registers](../../S3_Cals/Cal_Sets.md#Registers).

  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
<value> |  (String) User Cal Set prefix.  
Examples |  SYST:CAL:ALL:CSET:PREFix "MyCalAll"  
Query Syntax |  SYSTem:CALibrate:ALL:CSET:PREFix?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  " " (Empty string)  
  
* * *

## SYSTem:CALibrate:ALL[1-500]:GUIDed:CHANnel:LIST?

Applicable Models: All (Read-only) Returns all cal all guided calibration
channels.  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
Examples |  chan = SYST:CAL:ALL:GUID:CHAN:LIST?  
Return Type |  Numeric of comma-separated channel numbers  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SYSTem:CALibrate:ALL[1-500]:GUIDed:CHANnel[:VALue]?

Applicable Models: All (Read-only) Returns the primary guided calibration
channel number if more than one channel exists; otherwise, this command
returns the one value. Use this value as the <ch> argument for the subsequent
[Guided:Cal](Sense/CorrGuided.md) commands.  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
Examples |  chan = SYST:CAL:ALL:GUID:CHAN:VAL?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SYSTem:CALibrate:ALL[1-500]:GUIDed:PORTs?

Applicable Models: All (Read-only) Returns the ports to be calibrated during
the Cal All Channels calibration. Specify connectors and cal kits for these
ports using the [Guided:Cal](Sense/CorrGuided.md) commands.  Specify the
ports to be calibrated for each channel using
[SYST:CAL:ALL:CHAN<ch>:PORT](SystCalAll.md#PortsSelect).  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
Examples |  ports = SYST:CAL:ALL:GUID:PORT?  
Return Type |  Comma-separated list of port numbers  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SYSTem:CALibrate:ALL[1-500]:IFBW <value>

Applicable Models: All (Write-Read) Sets and returns the IFBW for a Cal All
calibration. [Learn more about this
setting](../../S3_Cals/Calibrate_All_Channels.htm#ifbw).  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
<value> |  IF Bandwidth in Hz. The list of valid IF Bandwidths is different depending on the VNA model. [See the list of valid settings](../../S2_Opt/Trce_Noise.md#Variable_IF_Bandwidth). If an invalid number is specified, the VNA will round up to the closest valid setting. This command supports MIN and MAX as arguments. [Learn more](../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min).  
Examples |  SYST:CAL:ALL:IFBW 10e3  
Query Syntax |  SYSTem:CALibrate:ALL:IFBW?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1 kHz  
  
* * *

## SYSTem:CALibrate:ALL[1-500]:INDependent:SOURce:CALibration:CATalog?

Applicable Models: All (Read-only) Returns available ports for independent
power calibration.  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
Examples |  SYST:CAL:ALL:IND:SOUR:CAL:CAT?  
Return Type |  String  
Default |  Not applicable  
  
* * *

## SYSTem:CALibrate:ALL[1-500]:INDependent:SOURce<n>:CALibration:RANGe:ADD

Applicable Models: All (Write-only) This command adds a power cal range for a
specific port <n>. Note that external sources are valid and specifying a
source port is the same as other remote commands. By default this will create
a range with the preset start/stop frequency and 201 points. The maximum
number of ranges that can be added is 100 (same as the maximum number of
segments).  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
<n> |  Port number  
Examples |  SYST:CAL:ALL:IND:SOUR3:CAL:RANG:ADD  
Default |  Not applicable  
  
* * *

## SYSTem:CALibrate:ALL[1-500]:INDependent:SOURce<n>:CALibration:RANGe:CLEar

Applicable Models: All (Write-only) This command resets all ranges for the
given source port <n>.  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
<n> |  Port number  
Examples |  SYST:CAL:ALL:IND:SOUR3:CAL:RANG:CLE  
Default |  Not applicable  
  
* * *

## SYSTem:CALibrate:ALL[1-500]:INDependent:SOURce<n>:CALibration:RANGe:COUNt?

Applicable Models: All (Read-only) This command queries how many ranges are
included in the calibration for source port <n>.  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
<n> |  Port number  
Examples |  SYST:CAL:ALL:IND:SOUR3:CAL:RANG:COUN?  
Return Type |  Numeric  
Default |  Not applicable  
  
* * *

##
SYSTem:CALibrate:ALL[1-500]:INDependent:SOURce<n>:CALibration:RANGe<m>:POINts
<value>

Applicable Models: All (Write-Read) This command sets and gets the number of
points for range <m> for source port<n>.  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
<n> |  Port number  
<m> |  Range number  
<value> |  Number of points  
Examples |  SYST:CAL:ALL:IND:SOUR3:CAL:RANG1:POIN 7  
Query Syntax |  SYSTem:CALibrate:ALL:INDependent:SOURce<n>:CALibrate:RANGe<m>:POINts?  
Return Type |  Numeric  
Default |  201  
  
* * *

##
SYSTem:CALibrate:ALL[1-500]:INDependent:SOURce<n>:CALibration:RANGe<m>:STARt
<value>

Applicable Models: All (Write-Read) This command sets and gets the start
frequency for range <m> for source port<n>.  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
<n> |  Port number  
<m> |  Range number  
<value> |  Start frequency for range <m>  
Examples |  SYST:CAL:ALL:IND:SOUR3:CAL:RANG1:STAR 20e9  
Query Syntax |  SYSTem:CALibrate:ALL:INDependent:SOURce<n>:CALibrate:RANGe<m>:STARt?  
Return Type |  Numeric  
Default |  Not applicable  
  
* * *

## SYSTem:CALibrate:ALL[1-500]:INDependent:SOURce<n>:CALibration:RANGe<m>:STOP
<value>

Applicable Models: All (Write-Read) This command sets and gets the stop
frequency for range <m> for source port<n>.  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
<n> |  Port number  
<m> |  Range number  
<value> |  Stop frequency for range <m>  
Examples |  SYST:CAL:ALL:IND:SOUR3:CAL:RANG1:STOP 21e9  
Query Syntax |  SYSTem:CALibrate:ALL:INDependent:SOURce<n>:CALibrate:RANGe<m>:STOP?  
Return Type |  Numeric  
Default |  Not applicable  
  
* * *

## SYSTem:CAL:ALL[1-500]:MCLass:PROPerty:NAME:CATalog? [mclass]

Applicable Models: All (Read-only) Returns the unique, settable properties for
the current cal all session.  [See a list of valid properties and values for
each measurement
class](../../S3_Cals/Calibrate_All_Channels.htm#propertiesDiag).  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
[mclass] |  Optional argument. String name of the measurement class for which properties are to be returned. [See a list of valid measurement class Application names](Calculate/Custom.md#CustDef). The measurement class must be included in the current Cal All calibration.  
Examples |  SYST:CAL:ALL:MCL:PROP:NAME:CAT? 'with NFX app, returns: "Noise Cal Method,Noise Tuner,AutoOrient Tuner,Tuner In,Tuner Out,Receiver Characterization Method,ENR File,Noise Source Connector,Noise Source CalKit"  
Return Type |  String of comma-separated properties.  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SYSTem:CAL:ALL[1-500]:MCLass:PROPerty:VALue:CATalog? <prop>

Applicable Models: All (Read-only) Returns the valid property values for a
specific property name.  [See a list of valid properties and values for each
measurement class](../../S3_Cals/Calibrate_All_Channels.htm#propertiesDiag).  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
<prop> |  (String) Property name for which valid values are to be returned.  
Examples |  SYST:CAL:ALL:MCL:PROP:VAL:CAT? "Noise Cal Method" 'with NFX app, returns: "Scalar,Vector"  
Return Type |  String of comma-separated values  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SYSTem:CALibrate:ALL[1-500]:MCLass:PROPerty:VALue[:STATe] <prop>,<value>

Applicable Models: All (Write-Read) Sets and returns the property value for a
specific property name.  [See a list of valid properties and values for each
measurement class](../../S3_Cals/Calibrate_All_Channels.htm#propertiesDiag).  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
<prop> |  (String) Property name for which value is to be set or returned.  
<value> |  Property value. To read a list of valid values, use [SYST:CAL:ALL:MCL:PROP:VAL:CAT?](SystCalAll.md#PropValueCat)  
Examples |  Example 1:  
SYST:CAL:ALL:MCL:PROP:VAL "Noise Cal Method","Noise:Scalar" Example 2:  
SYST:CAL:ALL:MCL:PROP:VAL "Enable Extra Power Cals","Port 1 Src2,Port3"
Example 3:  
SYST:CAL:ALL:MCL:PROP:VAL "Port 1 Src2 Cal Power","-20"  
Query Syntax |  SYSTem:CALibrate:ALL:MCLass:PROPerty:VALue[:STATe]? <prop>  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Varies with the property name.  
  
* * *

## SYSTem:CALibrate:ALL[1-500]:PATH:CONFigure:ELEMent[:STATe]
<element>,<setting>

Applicable Models: N522xB, N523xB, N524xB, M983xA (Write-Read) Sets and
returns the Path Configuration settings for a Cal All calibration.  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
<element> |  (String) Path configuration element to be set. [See a list of configurable RF Path elements and settings.](../RF_PathConfig.md)  
<setting> |  (String) Path configuration element setting.  
Examples |  SYST:CAL:ALL:PATH:CONFigure:ELEMent "Port1NoiseTuner","Internal"  
Query Syntax |  SYSTem:CALibrate:ALL:PATH:CONFigure:ELEMent[:STATe]? <element>  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:CALibrate:ALL[1-500]:PORT<n>:RECeiver:ATTen<value>[,src]

Applicable Models: All (Write-Read) Sets and returns the Receiver Attenuator
setting for a Cal All calibration.  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
<n> |  Receiver port number.  
<value> |  Attenuation value in dB for a Cal All calibration. Choose a valid value for the VNA model. [See valid settings](../../Support/Configurations.md).  
[src] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an external source, [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples |  SYST:CAL:ALL:PORT2:REC:ATT 10  
Query Syntax |  SYSTem:CALibrate:ALL:PORT<n>:RECeiver:ATTen?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0  
  
* * *

## SYSTem:CALibrate:ALL[1-500]:PORT<n>:RECeiver:ATTen:REFerence<num>

Applicable Models: N522xB, N523xB, N524xB, M9485A

(Write-Read) Sets and returns the reference attenuator setting for a Cal All
calibration.  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
<n> |  Receiver port number.  
<num> |  Attenuation value in dB for a Cal All calibration. 0dB or 35dB. If a number other than these is entered, the analyzer will select the next lower valid value. For example, if 19dB is entered, then 0dB attenuation will be selected.  
Examples |  SYST:CAL:ALL:PORT2:REC:ATT:REF 0  
Query Syntax |  SYSTem:CALibrate:ALL:PORT<n>:RECeiver:ATTen:REFerence?  
Return Type |  Numeric. If querying for the standard (M9376A) port, the return value is 0  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  35  
  
* * *

## SYSTem:CALibrate:ALL[1-500]:PORT<n>:RECeiver:ATTen:TEST<num>

Applicable Models: N522xB, N523xB, N524xB, M9485A

(Write-Read) Sets and returns the test attenuator setting for a Cal All
calibration.  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
<n> |  Receiver port number.  
<num> |  Attenuation value in dB for a Cal All calibration. 0dB or 35dB. If a number other than these is entered, the analyzer will select the next lower valid value. For example, if 19dB is entered, then 0dB attenuation will be selected.  
Examples |  SYST:CAL:ALL:PORT2:REC:ATT:TEST 0  
Query Syntax |  SYSTem:CALibrate:ALL:PORT<n>:RECeiver:ATTen:TEST?  
Return Type |  Numeric. If querying for the standard (M9376A) port, the return value is 0.  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  35  
  
* * *

## SYSTem:CALibrate:ALL[1-500]:PORT<n>:SOURce:POWer:ATTen<value>[,src]

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Write-Read) Sets
and returns the Source Attenuator setting for the Cal All calibration.  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
<n> |  Source port number.  
<value> |  Attenuation value in dB for the Cal All calibration. Choose a valid value for the VNA model. [See valid settings](../../Support/Configurations.md).  
[src] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an external source, [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples |  SYST:CAL:ALL:PORT2:SOUR:POW:ATT 10  
Query Syntax |  SYSTem:CALibrate:ALL:PORT<n>:SOURce:POWer:ATTen?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0  
  
* * *

## SYSTem:CALibrate:ALL[1-500]:PORT<n>:SOURce:POWer:OFFSet <value>[,src]

Applicable Models: All (Write-Read) Sets and returns the power offset value
for a Cal All calibration.  Power Offset provides a method of compensating
port power for added attenuation or amplification in the source path. The
result is that power at the specified port reflects the added components.  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
<n> |  Source port number.  
<value> |  Power offset value in dB for a Cal All calibration.

  * For amplification, use positive offset.
  * For attenuation, use negative offset.

  
[src] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an external source, [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples |  SYST:CAL:ALL:PORT2:SOUR:POW:OFFS 10  
Query Syntax |  SYSTem:CALibrate:ALL:PORT<n>:SOURce:POWer:OFFSet?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0  
  
* * *

## SYSTem:CALibrate:ALL[1-500]:PORT<n>:SOURce:POWer[:VALue] <value>[,src]

Applicable Models: All (Write-Read) Sets and returns the power level at which
a Cal All calibration is to be performed.  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
<n> |  Source port number.  
<value> |  Power level at which the calibration is to be performed.  
[src] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an external source, [true mode balanced port](../../Applications/iTMSA.md), or one of the Source outputs on the 2-port PNA-X model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples |  SYST:CAL:ALL:PORT2:SOUR:POW 0  
Query Syntax |  SYSTem:CALibrate:ALL:PORT<n>:SOURce:POWer[:VALue]?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Preset power of the VNA model. [See the data sheet for the power level for each model](../../Specs/ManualChoice.md).  
  
* * *

## SYSTem:CALibrate:ALL[1-500]:RESet

Applicable Models: All (Write-only) Resets all properties associated with the
Cal All session to their default values.  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
Examples |  SYST:CAL:ALL:RES  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:CALibrate:ALL[1-500]:SELect <value>

Applicable Models: All (Write-Read) Sets and returns the list of channels to
be calibrated during the Cal All session.  
---  
Parameters |   
[1-500] |  Calibration number. The default is 1.  
<value> |  Channel numbers to be calibrated. These channels must already exist.  
Examples |  SYST:CAL:ALL:SEL 1,2,3  
Query Syntax |  SYSTem:CALibrate:ALL:SELect?  
Return Type |  Comma-separated channel numbers.  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Existing channels  
  
* * *

* * *

