# SYSTem:CALibrate:PHASe Commands

* * *

Contains the settings to perform an SMC Phase Reference Calibration.

SYSTem:CALibrate:PHASe [CKIT](SystCalPhase.md#ckit) [CONNector](SystCalPhase.md#connector) [DEEMbed](SystCalPhase.md#deembed) FREQuency: | [STARt](SystCalPhase.md#FreqStart) | [STOP](SystCalPhase.md#FreqStop) GUIDed: | [CHANnel?](SystCalPhase.md#GuidedChan) [PORT](SystCalPhase.md#port) [POWer:ATTenuator](SystCalPhase.md#PowerAtten) [REFerence:](SystCalPhase.md#Reference) | [CATalog?](SystCalPhase.md#RefCat) [RESet](SystCalPhase.md#reset) UNKNown: | [INCLude](SystCalPhase.md#UnkInclude) | [INPut:POWer](SystCalPhase.md#UnkInPower) | LO | [FREQuency](SystCalPhase.md#UnkLoFreq) | [POWer](SystCalPhase.md#UnkLoPower)  
---  
  
Click on a red keyword to view the command details.

Important Notes

  * It is NOT necessary to create an SMC measurement before performing a remote Phase Reference Cal. It is necessary when performed from the user interface.
  * Before A..09.90, port selection was made remotely by selecting connectors and Cal Kits for the ports to be included in the SOLT calibration. With A.09.90, port selection is made explicitly with the commands in this node.

  
---  
  
See Also

  * [Example Program](../GPIB_Example_Programs/Perform_an_SMC_Phase_Ref_Cal.md)

  * [About Phase Reference Cal](../../FreqOffset/Phase_Reference_Calibration.md)

  * [Guided Cal commands](Sense/CorrGuided.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## SYSTem:CALibrate:PHASe:CKIT <string>

Applicable Models: N522xB, N523xB, N524xB (Write-Read) Sets and returns the
Cal Kit that will be used to perform the S-parameter Cal. To read a list of
valid Cal Kits, use
[SENSe:CORR:COLL:GUID:CKIT:CAT?](Sense/CorrGuided.md#gKitCat)  
---  
Parameters |   
<string> | Cal Kit.  
Examples | SYST:CAL:PHAS:CKIT "85052D"  
Query Syntax | SYSTem:CALibrate:PHASe:CKIT?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | " "  
  
* * *

## SYSTem:CALibrate:PHASe:CONNector <string>

Applicable Models: N522xB, N523xB, N524xB (Write-Read) Sets and returns the
connector type and gender of your Cal Kit. To read a list of valid connector
types, use [SENS:CORR:COLL:GUID:CONN:CAT?](Sense/CorrGuided.md#gConnCat)  
---  
Parameters |   
<string> | Connector type.  
Examples | SYST:CAL:PHAS:CONN "APC 3.5 female"  
Query Syntax | SYSTem:CALibrate:PHASe:CONNector?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | " "  
  
* * *

## SYSTem:CALibrate:PHASe:DEEMbed <bool>

Applicable Models: N522xB, N523xB, N524xB (Write-Read) Sets and returns the
state of de-embedding (reversing) the port 2 coupler.  
---  
Parameters |   
<bool> | Port 2 coupler de-embed state. Choose from: ON (or 1) \- Configures the calibration to include additional measurements to de-embed the effects of reversing the coupler. (This is the same as clearing the Omit Coupler checkbox.) OFF (or 0) \- Excludes additional measurements for de-embedding the effects of reversing the coupler.  
Examples | SYST:CAL:PHAS:DEEM 1  
Query Syntax | SYSTem:CALibrate:PHASe:DEEMbed?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON or 1  
  
* * *

## SYSTem:CALibrate:PHASe:FREQuency:STARt <value>

Applicable Models: N522xB, N523xB, N524xB (Write-Read) Sets and returns the
phase reference cal start frequency.  
---  
Parameters |   
<value> | Start frequency. Choose any frequency from 10 MHz to the stop frequency of the VNA.  
Examples | SYST:CAL:PHAS:FREQ:STAR 17.5e6  
Query Syntax | SYSTem:CALibrate:PHASe:FREQuency:STARt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Start frequency of the VNA  
  
* * *

## SYSTem:CALibrate:PHASe:FREQuency:STOP <value>

Applicable Models: N522xB, N523xB, N524xB (Write-Read) Sets and returns the
phase reference cal stop frequency.  
---  
Parameters |   
<value> | Stop frequency. Choose any frequency within the range of the VNA.  
Examples | SYST:CAL:PHAS:FREQ:STOP 26.5e9  
Query Syntax | SYSTem:CALibrate:PHASe:FREQuency:STOP?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Stop frequency of the VNA  
  
* * *

## SYSTem:CALibrate:PHASe:GUIDed:CHANnel?

Applicable Models: N522xB, N523xB, N524xB (Read-only) Reads the channel number
of the Phase Reference Calibration. Use this value as the <ch> argument for
the subsequent [Guided:Cal](Sense/CorrGuided.md) commands.  
---  
Parameters | None  
Examples | chan = SYST:CAL:PHAS:GUID:CHAN?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## SYSTem:CALibrate:PHASe:PORT<n> <bool>

Applicable Models: N522xB, N523xB, N524xB (Write-Read) Sets and returns the
enable state for the specified port.  
---  
Parameters |   
<n> | Port number to enable or disable.  
<bool> | Port enable state. Choose from: ON (or 1) \- Enable port <n> OFF (or 0) \- Disable port <n>  
Examples | SYST:CAL:PHAS:PORT2 1  
Query Syntax | SYSTem:CALibrate:PHASe:PORT<n>?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Ports 1 and 2 are enabled. Ports 3 and 4 (if present) are disabled  
  
* * *

## SYSTem:CALibrate:PHASe:POWer:ATTenuator <value>

Applicable Models: N522xB, N523xB, N524xB (Write-Read) Sets and returns the
Source Attenuator setting for the Phase Reference calibration. Note: This
setting MUST match the source attenuator setting at the mixer input port for
subsequent SMC+Phase measurements.  
---  
Parameters |   
<value> | Attenuation value in dB. Choose a valid value for the VNA model. [See valid settings](../../Support/Configurations.md).  
Examples | SYST:CAL:PHAS:POW:ATT 10  
Query Syntax | SYSTem:CALibrate:PHASe:POWER:ATTenuator?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 dB  
  
* * *

## SYSTem:CALibrate:PHASe:REFerence <string>

Applicable Models: N522xB, N523xB, N524xB (Write-Read) Sets and returns the
Phase Reference ID to be used for the Phase Reference calibration. Use
SYST:CAL:PHAS:REF:CAT? to read the phase references currently connected to the
VNA USB.  
---  
Parameters |   
<string> | Phase reference ID string.  
Examples | SYST:CAL:PHAS:REF "MYPRT0001"  
Query Syntax | SYSTem:CALibrate:PHASe:REFerence?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CALibrate:PHASe:REFerence:CATalog?

Applicable Models: N522xB, N523xB, N524xB (Read-only) Reads the ID strings of
the phase references that are currently connected to the VNA USB.  
---  
Parameters | None  
Examples | pRef = SYST:CAL:PHAS:REF:CAT?  
Return Type | Comma-separated string  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CALibrate:PHASe:RESet

Applicable Models: N522xB, N523xB, N524xB (Write-only) Resets all properties
associated with the Phase Reference Cal to their default values.  
---  
Parameters | None  
Examples | SYST:CAL:ALL:PHAS:RES  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CALibrate:PHASe:UNKNown:INCLude <bool>

Applicable Models: N522xB, N523xB, N524xB (Write-Read) Sets and returns the
state of Unknown Mixer calibration.  
---  
Parameters |   
<bool> | Unknown Mixer cal state. Choose from: ON (or 1) \- Enable Unknown Mixer cal. The start frequency becomes 10 MHz and can NOT be changed. OFF (or 0) \- Disable Unknown Mixer cal.  
Examples | SYST:CAL:PHAS:UNKN:INCL 1  
Query Syntax | SYSTem:CALibrate:PHASe:UNKNown:INCLude?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF or 0  
  
* * *

## SYSTem:CALibrate:PHASe:UNKNown:INPut:POWer <value>

Applicable Models: N522xB, N523xB, N524xB (Write-Read) Sets and returns the
input power level to the unknown mixer.  
---  
Parameters |   
<value> | Input power level in dBm.  
Examples | SYST:CAL:PHAS:UNKN:INP:POW -5  
Query Syntax | SYSTem:CALibrate:PHASe:UNKNown:INPut:POWer?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | -15 dBm  
  
* * *

## SYSTem:CALibrate:PHASe:UNKNown:LO:FREQuency <value>

Applicable Models: N522xB, N523xB, N524xB (Write-Read) Sets and returns the LO
frequency to the unknown mixer.  
---  
Parameters |   
<value> | LO frequency in Hz. Choose a value between 3 GHz and (Max Frequency minus 1GHz). For a 26.5 GHz VNA, the range is 3 GHz to 25.5 GHz. For best results, use the default LO frequency. 3.351Ghz. This frequency produces no spurs from the input/LO frequency. And also the Input frequency will have no band breaks.  
Examples | SYST:CAL:PHAS:UNKN:LO:FREQ 3.351e9  
Query Syntax | SYSTem:CALibrate:PHASe:UNKNown:LO:FREQuency?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 3.351 GHz  
  
* * *

## SYSTem:CALibrate:PHASe:UNKNown:LO:POWer <value>

Applicable Models: N522xB, N523xB, N524xB (Write-Read) Sets and returns the LO
power level to the unknown mixer.  
---  
Parameters |   
<value> | LO power level in dBm.  
Examples | SYST:CAL:PHAS:UNKN:LO:POW 10  
Query Syntax | SYSTem:CALibrate:PHASe:UNKNown:LO:POWer?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 10 dBm  
  
* * *

