# SYSTem:CONFigure:EDEVice:PULSe Commands

* * *

Configures and makes settings for an external Keysight 81110A Pulse Generator.

SYST:CONF:EDEVice:PULSe | [CHAN](SystConfigExtPulseGen.md#chan) | [HAMP](SystConfigExtPulseGen.md#hamp) | [LAMP](SystConfigExtPulseGen.md#lamp) | [LIMP](SystConfigExtPulseGen.md#limp) | [PMODe](SystConfigExtPulseGen.md#Mmode) | [SIMP](SystConfigExtPulseGen.md#simp)  
---  
  
Click on a keyword to view the command details.

### See Also

  * Root [SYST:CONF:EDEV](SystConfigExternalDevice.md) commands

  * All [Integrated Pulse App commands](Sense/Pulse.md)

  * Learn about: [Configure an External Pulse Generator](../../System/Configure_an_External_Pulse_Generator.md)

  * Learn about [Configure and External Device](../../System/Configure_an_External_Device.md)

  * [SYST:PREF:ITEM:EDEV:DPOL](System_Preferences.md#PrefEdevDpol) \- Determines whether External Devices remain activated or are de-activated when the VNA is Preset or when a Instrument State is recalled.

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## SYSTem:CONFigure:EDEVice:PULSe:CHAN <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the output channel of the
pulse generator.  
---  
Parameters |   
<name> | String - Name of the external pulse generator.  
<value> | Pulse Generator output port. Choose from 1 or 2.  
Examples | SYST:CONF:EDEV:PULS:CHAN "81110",1 system:configure:edevice:pulse:chan "myPG",2  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:PULSe:CHAN? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## SYSTem:CONFigure:EDEVice:PULSe:HAMP <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the High amplitude
(voltage) of the pulse generator.  
---  
Parameters |   
<name> | String - Name of the external pulse generator.  
<value> | Pulse Generator high amplitude voltage.  
Examples | SYST:CONF:EDEV:PULS:HAMP "81110",3 system:configure:edevice:pulse:HAMP "myPG",4  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:PULSe:HAMP? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 5  
  
* * *

## SYSTem:CONFigure:EDEVice:PULSe:LAMP <name>,<value>

Applicable Models: All (Read-Write) Pulse Generator low amplitude voltage.  
---  
Parameters |   
<name> | String - Name of the external pulse generator.  
<value> | Pulse Generator low amplitude voltage.  
Examples | SYST:CONF:EDEV:PULS:LAMP "81110",.2 system:configure:edevice:pulse:lamp "myPG",1  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:PULSe:LAMP? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## SYSTem:CONFigure:EDEVice:PULSe:LIMP <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the load impedance of the
pulse generator.  
---  
Parameters |   
<name> | String - Name of the external pulse generator.  
<value> | Pulse generator load impedance.  
Examples | SYST:CONF:EDEV:PULS:LIMP "81110",52 system:configure:edevice:pulse:limp "myPG",49  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:PULSe:LIMP? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 50  
  
* * *

## SYSTem:CONFigure:EDEVice:PULSe:PMODe <name>,<bool>

Applicable Models: All (Read-Write) Sets and returns the primary (On/Off)
setting of the external pulse generator. The ON setting allows the external
pulse generator to set the primary clock frequency for the other pulse
generators.  
---  
Parameters |   
<name> | String - Name of the external pulse generator.  
<bool> | Primary setting. Choose from: ON or 1 \- Use the external pulse generator becomes the primary clock frequency. OFF or 0 \- Use the internal pulse generator as the primary clock frequency.  
Examples | SYST:CONF:EDEV:PULS:PMOD "81110",OFF system:configure:edevice:pulse:pmode "myPG",1  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:PULSe:PMODe? <name>  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF or 0  
  
* * *

## SYSTem:CONFigure:EDEVice:PULSe:SIMP <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the source impedance of
the pulse generator.  
---  
Parameters |   
<name> | String - Name of the external pulse generator.  
<value> | Pulse generator source impedance.  
Examples | SYST:CONF:EDEV:PULS:SIMP "81110",52 system:configure:edevice:pulse:simp "myPG",49  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:PULSe:SIMP? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 50  
  
* * *

* * *

