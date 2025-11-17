# SOURce:DC commands

* * *

Controls the internal and external DC sources.

SOURce:DC: | [CATalog?](SourceDC.md#CATalog) | CURRent | CLAMp | [NEGative](SourceDC.md#currclamneg) | [POSitive](SourceDC.md#currclampos) | [RANGe](SourceDC.md#currrang) | [DATA](SourceDC.md#data) | [ENABle](SourceDC.md#Enable) | LIMit | MAXimum | MINimum | [LOCK:OUTPut:RELay:CLOSed](SourceDC.md#lock) | PROTection | [CATalog?](SourceDC.md#protcat) | [ENABle](SourceDC.md#protenab) | [LEVel](SourceDC.md#protlev) | [RESet](SourceDC.md#protres) | [SEQuencing[:STATe]](SourceDC.md#seq) | [STIMe](SourceDC.md#seqstim) | [STARt](SourceDC.md#start) | [STATe](SourceDC.md#state) | [STOP](SourceDC.md#stop) | [TYPE](SourceDC.md#type) | VOLTage | CALibrate | [DATE](SourceDC.md#voltcaldate) | [EXECute](SourceDC.md#voltcalexec) | [TIME](SourceDC.md#voltcaltime) | [BANDwidth](SourceDC.md#voltband) | [CLAMp](SourceDC.md#voltclamp) | [RANGE](SourceDC.md#voltrang)  
---  
  
Click on a keyword to view the command details.

Note: The VNA internal DC sources are named "AO1" and "AO2" using CAPITAL O
(NOT zero - 0)

See Also

  * [Learn about DC Source control](../../S1_Settings/DC_Control.md)

  * [Configure an Ext DC Device](SystConfigExtDC.md) (SCPI commands)

  * [Example Programs](../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

  * [Remotely Specifying a Source Port](../Remotely_Specifying_a_Source_Port.md)

* * *

## SOURce<ch>:DC:CATalog?

Applicable Models: N524xB, E5080B, E5081A, All PXIe/USB VNAs (Read-only)
Returns the names of the configured and active DC sources for the specified
channel. Use [SYST:CONF:EDEV:CAT?](SystConfigExternalDevice.md#cat) to read a
list of all configured external devices, including inactive devices.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
Examples | SOUR:DC:CAT? 'Returns the following... "AO1,AO2,MyDCSupply" 'AO1 and AO2 are PNA-X internal DC Sources  
Return Type | String, Names are separated by commas.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SOURce<ch>:DC:CURRent:CLAMp:NEGative <name>,<num>

Applicable Models: All PXIe VNAs (Read-Write) Sets and returns the negative
current limit (in Amps) when output regulation is in voltage priority mode.
This command is available for PXI SMU only. This is the same function with
"IKtM911xOutputChannelCurrent Interface section, NegativeLimit property of
the M911x driver.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<name> | String. DC Source Name. The name and port must EXACTLY match those in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl).  
<num> | Negative current limit value in Amps  
Examples | SOUR2:DC:CURR:CLAM:NEG "SMU1",-2  
Query Syntax | SOURce<ch>:DC:VOLTage:CLAMp:NEGative? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | -3.06  
  
* * *

## SOURce<ch>:DC:CURRent:CLAMp:POSitve <name>,<num>

Applicable Models: All PXIe VNAs (Read-Write) Sets and returns the positive
current limit (in Amps) when output regulation is in voltage priority mode.
This command is available for PXI SMU only. This is the same function with
"IKtM911xOutputChannelCurrent Interface section, PositiveLimit property of
the M911x driver.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<name> | String. DC Source Name. The name and port must EXACTLY match those in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl). "SMU* represents the SMU DC Meter name. * is the SMU module number.  
<num> | Positive current limit value in Amps  
Examples | SOUR2:DC:CURR:CLAM:POS "SMU1",2  
Query Syntax | SOURce<ch>:DC:VOLTage:CLAMp:POSitive? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 3.06  
  
* * *

## SOURce<ch>:DC:CURRent:RANGe <name>,<num>

Applicable Models: All PXIe VNAs (Read-Write) Sets and returns a current
output range in Amps. This command is available for both PXI SMU and
Digital/Analog I/O M9341B. For PXI SMU, this is the same function with
IKtM911xOutputChannelCurrent.Range Property section of the M911x driver.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1 [M9341B] If different setting is set between channels, the channel which is not same as active channel will be blocked to avoid wearing out an internal mechanical relay. SENSe:SWEep:BLOCked? can detect the blocked status.  
<name> | String. DC Source Name. The name and port must EXACTLY match those in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl). [SMU] "SMU* represents the SMU DC Meter name. * is the SMU module number. [M9341B] "AO1" or" AO2"  
<num> | [SMU] Current range in Amps (0.01 or3)  [M9341B] Current range in Amps. The range is 0.5 to 0.05, but Analog Out2 cant be set to 0.5. If an invalid number is specified, the analyzer will round up to the closest valid number. AO1 (Mode1: 0.5, Mode2: 0.05) AO2 (Mode1: 0.1, Mode2: 0.05)  
Examples | SOUR2:DC:CURR:RANG "SMU1",1m  
Query Syntax | SOURce<ch>:DC:CURRent:RANGe? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | (SMU) 3, (M9341B) 0.05  
  
* * *

## SOURce<ch>:DC:DATA <name[,port]>,<data>

Applicable Models: N524xB, E5080B, E5081A, All PXIe/USB VNAs (Read-Write) Sets
and returns the DC stimulus values per point to be sent from the specified DC
source. This setting overrides the Start and Stop DC settings for the channel.
Only the values that are set with this command can be read by this command.
The read command does NOT read the values that are set using the Start and
Stop settings.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<name[,port]> | String. The name and port must EXACTLY match those in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl). name \- DC Source Name. See [note for specifying internal DC Sources](SourceDC.md#Note). [port] \- Optional. VNA port for DC Source data. This is equivalent to the <per port> setting in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl). If unspecified, data is applied to ALL ports. Important: When you specify a port for this command, it must also be included for ALL DC Source commands that have this optional [port] specifier.  
<data> | The stimulus value array to be set. The size of the array should be equal to the sweep point number.  
Examples | 'Set 3 data points on the channel scpi.Execute "SENS:SWE:POIN 3" 'Enable DC Source output scpi.Execute "SOUR:DC:ENAB ON" 'Set AO1 state to be always ON (no port value) scpi.Execute "SOUR:DC:STATe 'AO1',ON" 'Set DC value for each data point scpi.Execute "SOUR:DC:DATA 'AO1',1,5,1" 'Read data back data = scpi.Execute ("SOUR:DC:DATA? 'AO1'") msgbox data  
Query Syntax | SOURce<ch>:DC:DATA? <name[,port]>  
Return Type | Comma-separated values  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SOURce<ch>:DC:ENABle <bool>

Applicable Models: N524xB, E5080B, E5081A, All PXIe/USB VNAs (Read-Write) Sets
and returns the ON / Off state of all configured DC sources for the specified
channel. This setting is the same as the checkbox at the top of the [DC Source
Control dialog](../../S1_Settings/DC_Control.htm). Individual DC sources must
ALSO be enabled using [SOUR:DC:STATe](SourceDC.md#state). Use
[SYST:CONF:EDEV:CAT?](SystConfigExternalDevice.md#cat) to read a list of all
configured external devices. Use [SOUR:DC:CAT?](SourceDC.md#names) to read a
list of ACTIVE configured DC source names  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<bool> | ON / Off state. Choose from: ON or 1 \- All DC sources enabled. OFF or 0 \- All DC sources disabled.  
Examples | SOUR:DC:ENAB 0  
Query Syntax | SOURce<ch>:DC:ENABle?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## SOURce<ch>:DC:LIMit:MAXimum <name>,<num>

Applicable Models: All (Read-Write) Sets and returns the Max DC limit value
for a DC source.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<name> | String. DC Source Name. See note for specifying internal DC Sources. The name must EXACTLY match those in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl).  
<num> | Max DC limit value. Choose a value within the range of the DC source.  
Examples | SOUR2:DC:LIM:MAX "myDCSource",10 source:dc:limit:maximum "myDCSource",10  
Query Syntax | SOURce<ch>:DC:LIMit:MAXimum? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 10  
  
* * *

## SOURce<ch>:DC:LIMit:MINimum <name>,<num>

Applicable Models: All (Read-Write) Sets and returns the Min DC limit value
for a DC source.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<name> | String. DC Source Name. See note for specifying internal DC Sources. The name must EXACTLY match those in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl).  
<num> | Min DC limit value. Choose a value within the range of the DC source.  
Examples | SOUR2:DC:LIM:MIN "myDCSource",-10 source:dc:limit:minimum "myDCSource",-10  
Query Syntax | SOURce<ch>:DC:LIMit:MINimum? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | -10  
  
* * *

## SOURce<ch>:DC:LOCK:OUTPut:RELay:CLOSed <name>, <bool>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the locked-down
state of the output relays on SMU units with output relays. When
enabled/locked, the output relays remain closed. When disabled, the output
relays open and close as the output toggles on and off. This command is
available for PXI SMU only. This is the same function with
IKtM911xOutputChannelRelay Interface section, LockEnabled property of the
M911x driver.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<name> | String. DC Source Name. The name must EXACTLY match those in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl).  
<bool> | ON / Off state. Choose from: ON or 1 \- The output relays remain closed OFF or 0 \- The output relays open and close as the output toggles on and off.  
Examples | SOUR:DC:LOCK:OUTP:REL:CLOS 0  
Query Syntax | SOURce<ch>:DC:LOCK:OUTPut:RELay:CLOSed? <name>  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## SOURce<ch>:DC:PROTection:CATalog?

Applicable Models: All PXIe VNAs, E5080B, E5081A (Read-only) Returns the
module list or name of DC source in which protection function is activated due
to over current or voltage. This command is available for both PXI SMU and
Digital/Analog I/O M9341B and E5080B.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
Examples | SOUR:DC:PROT:CAT?  
Query Syntax | SOURce<ch>:DC:PROTection:CATalog?  
Return Type | String, Names are separated by commas. "NONE is returned if no modules are detected.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SOURce<ch>:DC:PROTection:ENABle <name>, <bool>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the DC output
protection state. This command is available for PXI SMU only.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<name> | String. DC Source Name. The name must EXACTLY match those in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl).  
<bool> | ON / Off state. Choose from: ON or 1 \- Enable the protection OFF or 0 \- Disable the protection.  
Examples | SOUR:DC:PROT:ENAB "SMU1", 0  
Query Syntax | SOURce<ch>:DC:PROTection:ENABle? <name>  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## SOURce<ch>:DC:PROTection:LEVel <name>, <num>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the protection
voltage level for the DC output. This command is available for PXI SMU only.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<name> | String. DC Source Name. The name must EXACTLY match those in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl).  
<bool> | Protection voltage level in Volts  
Examples | SOUR:DC:PROT:LEV "SMU1", 10  
Query Syntax | SOURce<ch>:DC:PROTection:LEVel? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 14.4  
  
* * *

## SOURce<ch>:DC:PROTection:RESet <name>

Applicable Models: All PXIe VNAs, E5080B, E5081A (Write Only) Resets the
instrument's output protection circuit after a protection condition occurs. If
successful, the output will return to the output enabled state. Remove the
fault condition that caused the protection trip before resetting the
protection circuit in order to prevent the protection from tripping again.
This command is available for both PXI SMU and Digital/Analog I/O M9341B and
E5080B.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<name> | String. DC Source Name. The name must EXACTLY match those in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl). [SMU] "SMU* represents the SMU DC Meter name. * is the SMU module number. [M9341B] "AO1" or "AO2" [E5080B] "AO1" or "AO2" or both  
Examples | SOUR:DC:PROT:RES "SMU1"  
Query Syntax | Not Applicable  
Return Type | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SOURce<ch>:DC:NAMes?

Applicable Models: N524xB, E5080B, E5081A, All PXIe/USB VNAs (Read-only) Reads
the DC source names  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
Examples | SOUR:DC:NAM?  
Query Syntax | SOURce<ch>:DC:NAMes?  
Return Type |   
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SOURce<ch>:DC:SEQuencing[:STATe] <bool>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the DC output
sequencing state. This command is valid for SMU sources only. Other DC
sources, such as AO1, AO2, do not have the sequencing control. This
command is available for PXI SMU only.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<name> | String. DC Source Name. The name must EXACTLY match those in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl).  
<bool> | ON / Off state. Choose from: ON or 1 OFF or 0  
Examples | SOUR:DC:SEQ 1  
Query Syntax | SOURce<ch>:DC:SEQuencing[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## SOURce<ch>:DC:SEQuencing:STIMe <num>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the DC output
sequencing settling time. This command is available for PXI SMU only. Other DC
sources, such as AO1, AO2, do not have the sequencing control.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1.  
<name> | String. DC Source Name. The name must EXACTLY match those in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl).  
<bool> | Source settling time in second.  
Examples | SOUR:DC:SEQ:STIM 1  
Query Syntax | SOURce<ch>:DC:SEQuencing:STIMe?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## SOURce<ch>:DC:STARt <name[,port]>,<num>

Applicable Models: N524xB, E5080B, E5081A, All PXIe/USB VNAs (Read-Write) Sets
and returns start DC value for the specified DC source.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<name[,port]> | String. The name and port must EXACTLY match those in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl). name \- DC Source Name. See [note for specifying internal DC Sources](SourceDC.md#Note). [port] \- Optional. VNA port for DC Source start value. This is equivalent to the <per port> setting in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl). If unspecified, DC Start value is applied for ALL ports. Important: When you specify a port for this command, it must also be included for ALL DC Source commands that have this optional [port] specifier.  
<num> | Start value. Choose a value within the range of the DC source.  
Examples | SOUR2:DC:STARt "myDCSource",3 source:dc:start "AO1,Port 1",1  
Query Syntax | SOURce<ch>:DC:START? <name[,port]>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | .5  
  
* * *

## SOURce<ch>:DC:STATe <name[,port]>,<bool>

Applicable Models: N524xB, E5080B, E5081A, All PXIe/USB VNAs (Read-Write) Sets
and returns the ON / Off state of the specified DC source and port. Use
[SYST:CONF:EDEV:CAT?](SystConfigExternalDevice.md#cat) to read a list of all
configured external devices. Use [SOUR:DC:CAT?](SourceDC.md#names) to read a
list of ACTIVE configured DC source names  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<name[,port]> | String. The name and port must EXACTLY match those in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl). name \- DC Source Name. See [note for specifying internal DC Sources](SourceDC.md#Note). [port] \- Optional. VNA port for DC Source state. This is equivalent to the <per port> setting in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl). If unspecified, DC is ALWAYS ON or OFF for ALL ports. Important:When you specify a port for this command, it must also be included for ALL DC Source commands that have this optional [port] specifier.  
<bool> | ON / Off state. Choose from: ON or 1 \- DC source/port enabled. OFF or 0 \- DC source/port disabled.  
Examples | 'Set AO1 to always ON source:dc:state "AO1",1 'Set MyDCSource to ON when RF source Port 1 is ON SOUR:DC:STAT "MyDCSource,Port 1",ON 'Read state for MyDCSource,Port 1 SOUR:DC:STAT? "MyDCSource,Port 1"  
Query Syntax | SOURce<ch>:DC:STATe? <name[,port]>  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 \- OFF  
  
* * *

## SOURce<ch>:DC:STOP <name[,port]>,<num>

Applicable Models: N524xB, E5080B, E5081A, All PXIe/USB VNAs (Read-Write) Sets
and returns stop DC value for the specified DC source.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<name[,port]> | String. The name and port must EXACTLY match those in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl). name \- DC Source Name. See [note for specifying internal DC Sources](SourceDC.md#Note). [port] \- Optional. VNA port for DC Stop value. This is equivalent to the <per port> setting in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl). If unspecified, DC Stop is applied for ALL ports. Important: When you specify a port for this command, it must also be included for ALL DC Source commands that have this optional [port] specifier.  
<num> | Stop value. Choose a value within the range of the DC source.  
Examples | SOUR2:DC:STOP "myDCSource", 3  
Query Syntax | SOURce<ch>:DC:STOP?<name[,port]>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## SOURce<ch>:DC:TYPE <name>,<char>

Applicable Models: All PXIe VNAs (Read-Write) Sets and returns the output
regulation mode. This command is available for PXI SMU only. This is the same
function with IKtM911xOutputChannel Interface section, PriorityMode
property of the M911x driver.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<name> | String. DC Source Name. The name and port must EXACTLY match those in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl).  
<char> | Source control type. VOLTage \- voltage priority CURRent \- current priority  
Examples | SOUR2:DC:TYPE "SMU1",VOLT  
Query Syntax | SOURce<ch>:DC:TYPE? <name>  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | VOLTage  
  
* * *

## SOURce<ch>:DC:VOLTage:CALIBrate:DATE <name>

Applicable Models: All PXIe VNAs (Read only) Returns the date of execution
output voltage calibration. This command is available for M9341B only.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<name> | String. DC Source Name. The name and port must EXACTLY match those in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl) AO1 or AO2 or both.  
Examples | SOUR2:DC:VOLT:CALB:DATE? "AO1,AO2"  
Query Syntax | SOURce<ch>:DC:VOLTage:CALIbrate:DATE? <name>  
Return Type | String. Comma separated numbers representing year, month and day.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SOURce<ch>:DC:VOLTage:CALIBrate:EXECute <name>

Applicable Models: All PXIe VNAs (Write only) Execute the output voltage
calibration for both AO1 and AO2. The calibration is finished within 1 second,
so this is not an overlapped command. This command is available for M9341B
only.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<name> | String. DC Source Name. The name and port must EXACTLY match those in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl) AO1 or AO2 or both. Even either "AO1" or "AO2" is selected, both ports are calibrated at the same time.  
Examples | SOUR2:DC:VOLT:CALB:EXEC "AO1,AO2"  
Query Syntax | Not Applicable  
Return Type | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SOURce<ch>:DC:VOLTage:CALIBrate:TIME <name>

Applicable Models: All PXIe VNAs (Read only) Returns the time of execution
output voltage calibration. If the calibration is not executed, [SCPI: 1111]:
Calibration data is missing." is returned. This command is available for
M9341B only.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<name> | String. DC Source Name. The name and port must EXACTLY match those in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl) AO1 or AO2 or both.  
Examples | SOUR2:DC:VOLT:CALB:TIME? "AO1,AO2"  
Query Syntax | SOURce<ch>:DC:VOLTage:CALIbrate:TIME? <name>  
Return Type | String. Comma separated numbers representing hours, minutes and seconds.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SOURce<ch>:DC:VOLTage:BANDwidth <name>,<string>

Applicable Models: All PXIe VNAs (Read-Write) Sets and returns a voltage
bandwidth to optimize the output response time with capacitive loads. This
command is available for PXI SMU only. This is the same function with
IKtM911xOutputChannelVoltage.Bandwidth Property section of the M911x driver.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<name> | String. DC Source Name. The name and port must EXACTLY match those in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl). "SMU* represents the SMU DC Meter name. * is the SMU module number.  
<string> | Source control type. "LOW", " HIGH1", "HIGH2", or " HIGH3"  
Examples | SOUR2:DC:VOLT:BAND "SMU1","LOW"  
Query Syntax | SOURce<ch>:DC:VOLTage:BANDwidth? <name>  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | "LOW"  
  
* * *

## SOURce<ch>:DC:VOLTage:CLAMp <name>,<num>

Applicable Models: All PXIe VNAs (Read-Write) Sets and returns the positive
voltage limit in Volts when output regulation is in current priority mode.
This command is available for PXI SMU only. This is the same function with
IKtM911xOutputChannelVoltage Interface section, Limit property of the
M911x driver.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<name> | String. DC Source Name. The name and port must EXACTLY match those in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl). "SMU* represents the SMU DC Meter name. * is the SMU module number.  
<num> | Limit value in Volts  
Examples | SOUR2:DC:VOLT:CLAM "SMU1",5  
Query Syntax | SOURce<ch>:DC:VOLTage:CLAMp? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 6.12  
  
* * *

## SOURce<ch>:DC:VOLTage:RANGe <name>,<num>

Applicable Models: All PXIe VNAs (Read-Write) Sets and returns a voltage
output range in Volts. This command is available for both PXI SMU only. This
is the same function with IKtM911xOutputChannelVoltage.Range Property
section of the M911x driver.  
---  
Parameters |   
<ch> | Any existing channel number. If unspecified, value is set to 1  
<name> | String. DC Source Name. The name and port must EXACTLY match those in the [DC Source Control dialog](../../S1_Settings/DC_Control.md#DCControl). "SMU* represents the SMU DC Meter name. * is the SMU module number.  
<num> |  Voltage range (6 or 13)  
Examples | SOUR2:DC:VOLT:RANG "SMU1",13  
Query Syntax | SOURce<ch>:DC:VOLTage:RANGe? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  6  
  
* * *

