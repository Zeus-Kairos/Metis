# Sense:Path:Config Commands

* * *

Controls the path configuration settings.

SENSe:PATH:CONFig | [CATalog?](Path.md#catalog) | [COPY](Path.md#copy) | [DELete](Path.md#delete) | [DTEXt](Path.md#dtext) | ELEMent | [CATalog?](Path.md#elementCat) | [[SELect]](Path.md#elemselect) | [[STATe]](Path.md#state) | [VALue:CATalog](Path.md#value) | [NAME](Path.md#name) | [SELect](Path.md#select) | [STORe](Path.md#store)  
---  
  
Click on a keyword to view the command details.

The 'ELEMent' commands are used for both RF path and IF path configuration.

  * [RF Configuration elements and values](../../RF_PathConfig.md)

  * [IF Configuration elements and values](../../../IFAccess/IF_Path_Configuration.md#elements)

See Also

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Learn about RF Path Configuration](../../../S1_Settings/Path_Configurator.md)

  * [Learn about IF Path Configuration](../../../IFAccess/IF_Path_Configuration.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## SENSe:PATH:CONFig:CATalog?

Applicable Models: N522xB, N523xB, N524xB, M983xA, E5081A (Read-only) Returns
a list of configuration names stored in the VNA.  
---  
Examples | SENS:PATH:CONF:CAT?  
Return Type | Comma-separated list of double-quoted strings  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:PATH:CONFig:COPY <num>

Applicable Models: N522xB, N523xB, N524xB, M983xA, E5081A (Write-only) Copies
the mechanical switch and attenuator settings from the specified channel <num>
to channel <ch>. To avoid potential conflicts, all port couplings in the
calling channel will be turned OFF and all port attenuator settings will be
set to manual before copying the switch or attenuator settings. The two
channels CAN be of different measurement classes. Use
[SYSTem:MACRo:COPY:CHANnel](../System.md#COPY_CHANnel) to copy ALL settings
from one channel to another.  
---  
Parameters |   
<ch> | Channel number to copy mechanical settings to. If unspecified, value is set to 1.  
<num> | Channel number to copy mechanical settings from.  
Examples | 'Copies mechanical settings from chan 2 to chan 1. SENS1:PATH:CONF:COPY 2  
Return Type | Not Applicable  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:PATH:CONFig:DELete <string>

Applicable Models: N522xB, N523xB, N524xB, M983xA, E5081A (Write-only) Deletes
the specified configuration name from the VNA. The factory configurations
cannot be deleted. This is the only method of distinguishing a factory
configuration from a user-named configuration.  
---  
Parameters |   
<string> | Configuration name to be deleted.  
Examples | SENS:PATH:CONF:DEL "MyMixer"  
Return Type | Not Applicable  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe:PATH:CONFig:DTEXt <string>

Applicable Models: N522xB, N523xB, N524xB, M983xA, E5081A (Read-Write) Write
and read descriptive text associated with the configuration. This text is
displayed in the path configuration dialog. Text is generally used to describe
external connections that must be made manually to complete the configuration
setup.  
---  
Parameters |   
<string> | Descriptive text enclosed in quotes. Double quotes are not allowed within the descriptive text.  
Examples | SENS:PATH:CONF:DTEX "Connect J1 jumper on the rear panel."  
Query Syntax | SENSe<ch>:PATH:CONFig:DTEXt?  
Return Type | String  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:PATH:CONFig:ELEMent:CATalog?

Applicable Models: N522xB, N523xB, N524xB, M983xA, E5081A (Read-only) Returns
the names of configurable elements as a comma-delimited list of strings. See a
[list of configurable elements and settings](../../RF_PathConfig.md) for
various VNA models.  
---  
Parameters |   
<ch> | Any existing channel number; if unspecified, value is set to 1.  
Examples | SENS:PATH:CONF:ELEM:CAT? 'returns Combiner, Src1, Src2  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:PATH:CONFig:ELEMent[:STATe] <elem>, <setting> Superseded

Applicable Models: N522xB, N523xB, N524xB, M9485A with M9341B, M937xA with
M9341B, P937xA, M980xA, P50xxA/B, E5080B (Read-Write) Write or read the
setting of a specified element in the current configuration. This command is
used for both RF path and IF path configuration.

  * [RF Configuration elements and values](../../RF_PathConfig.md)
  * [IF Configuration elements and values](../../../IFAccess/IF_Path_Configuration.md#elements) (Includes IF Path, Pulse, and DSP elements)

|  |  |   
---|---|---  
|  |   
|  |  |   
Parameters |   
<ch> | Any existing channel number; if unspecified, value is set to 1.  
<elem> | Name of the element for which a setting is to be made.  
<setting> | Element setting. Use [SENS:PATH:CONF:ELEM:VAL:CAT?](Path.md#value) to return a list of valid settings for the specified element.  
Examples | SENS:PATH:CONF:ELEM "Combiner","Normal"  
Query Syntax | SENSe<ch>:PATH:CONFig:ELEMent? "Combiner" Returns the current state of the Combiner element.  
Return Type | String  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## SENSe<ch>:PATH:CONFig:ELEMent[:SELect] <elem>, <setting>

Applicable Models: N522xB, N523xB, N524xB, M9485A with M9341B, M937xA with
M9341B, P937xA, M98xxA, P50xxA/B, E5080B, E5081A (Read-Write) Write or read
the setting of a specified element in the current configuration. This command
is used for both RF path and IF path configuration.

  * (PNA) [RF Configuration elements and values](../../RF_PathConfig.md)
  * (PNA) [IF Configuration elements and values](../../../IFAccess/IF_Path_Configuration.md#elements) (Includes IF Path, Pulse, and DSP elements)
  * (M983xA) Path Configurator (RF and IF)

The other configuration can be set as below. | Type | Element | Setting  
---|---|---  
Spectrum Analyzer channels | "IFGAIN<recieverNotation>" Ex: IFGAINa1, IFGAINb3 Ex for Multi Port Config: IFGAinb9  | 'Auto', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '26"  
Pulse measurement | "PulseTrigInput" | "Internal", "External" "'PXI_TRIG0" to "PXI_TRIG7" (PXI/USB VNA) "'REAR_TRIG1", "REAR_TRIG2", "REAR_NONE" (PXI/USB VNA except for P937xA)  
"PulseModDrive" | "On" ,"Off'" "Pulse1" to "Pulse4",  'PXI_TRIG0" to "PXI_TRIG7", "RearPanel" (PXI/USB VNA) "REAR_TRIG1", "REAR_TRIG2", "REAR_NONE" (USB VNA except for P937xA)  
"PulseModPort<N>" | "Enable", "Disable"  
"Src1Out1PulseModEnable" "Src2Out1PulseModEnable" | "Enable", "Disable"  
Aux Out 1 Pulse / Aux Out 2 Pulse | "AuxOut1PulseModEnable" "AuxOut2PulseModEnable" | "Enable", "Disable"  
  
Note: For M9341B, this can enable the pulse modulation for AUX Out 1 and 2.

When the 'PulseModDrive', 'PulseModPort<N>', 'Src1Out1PulseModEnable' , or
'Src2Out1PulseModEnable' is selected as <elem>, the
[SENS:SWE:PULSE:DRIV:AUTO](SweepPulse.md#drive) automatically is turned off.  
  
Parameters |   
<ch> | Any existing channel number; if unspecified, value is set to 1.  
<elem> | Name of the element for which a setting is to be made. Use SENS:PATH:CONF:ELEM:CAT? to return a list of valid element.  
<setting> | Element setting. Use [SENS:PATH:CONF:ELEM:VAL:CAT?](Path.md#value) to return a list of valid settings for the specified element.  
Examples | SENS:PATH:CONF:ELEM "Combiner","Normal" SENS:PATH:CONF:ELEM "PulseTriggerInput","External"  
Query Syntax | SENSe<ch>:PATH:CONFig:ELEMent[:STATe]? <elem>  
Return Type | String  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## SENSe<ch>:PATH:CONFig:ELEMent:VALue:CATalog? <element>

Applicable Models: N522xB, N523xB, N524xB, M983xA, E5081A (Read-only) Returns
the list of valid settings that can be used with the specified element. See a
[list of configurable elements and settings](../../RF_PathConfig.md) for
various VNA models.  
---  
Parameters |   
<ch> | Any existing channel number; if unspecified, value is set to 1.  
<element> | String. Element name for which to return valid settings.  
Examples | SENS:PATH:CONF:ELEM:VAL:CAT? "Combiner" 'returns "Normal", "Reversed"  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:PATH:CONFig:NAME?

Applicable Models: N522xB, N523xB, N524xB, M983xA, E5081A (Read-only) Returns
the name of the current configuration only if NO individual element settings
had been changed since selecting or storing a configuration. When element
settings change, the path configuration name is cleared.  
---  
Parameters |   
<ch> | Any existing channel number; if unspecified, value is set to 1.  
Examples | SENS:PATH:CONF:NAME? 'returns "Default"  
Return Type | String  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:PATH:CONFig:SELect <string>

Applicable Models: N522xB, N523xB, N524xB, M983xA, E5081A (Write only) Loads
the named configuration onto the specified channel. Note: Loading a stored
configuration will over-write MANY RF and [IF path
configuration](../../../IFAccess/IF_Path_Configuration.htm) settings. Make
your measurement settings AFTER recalling a stored configuration, NOT before.
Use [SENS:PATH:CONF:CAT?](Path.md#catalog) to return the configuration names
that are stored on the VNA.  
---  
Parameters |   
<ch> | Any existing channel number; if unspecified, value is set to 1.  
<string> | Configuration name. "Default" is the default factory configuration.  
Examples | SENS:PATH:CONF:SEL 'default'  
sense2:path:CONFig:select "MyMixer"  
Query Syntax | Not Applicable  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | "Default"  
  
* * *

## SENSe<ch>:PATH:CONFig:STORe <name>

Applicable Models: N522xB, N523xB, N524xB, M983xA, E5081A (Write only) Saves
the path configuration currently associated with channel <ch> to the specified
configuration name.  
---  
Parameters |   
<ch> | Any existing channel number; if unspecified, value is set to 1.  
<name> | String. Configuration name. Factory configurations can NOT be overwritten. Specifying the name of a pre-defined factory configuration will result in an error.  
Examples | SENS:PATH:CONF:STOR "MyMixer"  
Query Syntax | Not Applicable  
[Default](javascript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

