# SYSTem:CONFigure:EDEVice Commands

* * *

Configures and makes settings for an external device.

SYSTem:CONFigure:EDEVice: | [ADD](SystConfigExternalDevice.md#Add) | [CAT?](SystConfigExternalDevice.md#cat) | CHANnel | BASE? | COUNt? | NAME? | NUMBer? | STATe | SYNC | [DRIVer](SystConfigExternalDevice.md#Driver) | [DTYPe](SystConfigExternalDevice.md#DTYPe) | [EXISts?](SystConfigExternalDevice.md#EdevExists) | [IOConfig](SystConfigExternalDevice.md#ioconf) | [IOENable](SystConfigExternalDevice.md#IOEnable) | [LOAD](SystConfigExternalDevice.md#load) | RCLock | VNA | STATe | [REMove](SystConfigExternalDevice.md#Remove) | [SAVE](SystConfigExternalDevice.md#save) | SMU | CHANnel | STATe | [STATe](SystConfigExternalDevice.md#State) | [TOUT](SystConfigExternalDevice.md#Tout) | [DC More commands](SystConfigExtDC.md) | [PMAR More commands](SystConfigExtPMAR.md) | [PULSe More commands](SystConfigExtPulseGen.md) | SOURce: | [DPPoint](SystConfigExternalDevice.md#ESourceDPP) | HYBRid | INPut | FREQuency:CARRier | FREQency:MULTiplier | NAME | POWer:LIMit | PULSe:ENABle | LO | FREQuency:MULTiplier | NAME | POWer | PULSe:ENABle | LOCK:STATe | OUTPut | FREQuency:MAX | FREQuency:MIN | GAIN | MIXer:SIDeband | TYPE | MODulation | CONTrol | :STATe | [TMODe](SystConfigExternalDevice.md#ESourceTMODE) | [TPORt](SystConfigExternalDevice.md#ESourceTport)  
---  
  
Click on a red keyword to view the command details.

See Also

  * Learn about: [Configure an External Source](../../System/Configure_an_External_Device.md)

  * Learn about: [Configure a PMAR Device](../../System/Configure_a_Power_Meter_As_Receiver.md)

  * Example: [Configure an External Source](../GPIB_Example_Programs/Configure_an_External_Source.md)

  * Example: [Configure a PMAR Device](../GPIB_Example_Programs/Configure_a_PMAR_Device.md)

  * [SYST:PREF:ITEM:EDEV:DPOL](System_Preferences.md#PrefEdevDpol) \- Determines whether external devices remain activated or are de-activated when the VNA is Preset or when a Instrument State is recalled.

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## SYSTem:CONFigure:EDEVice:ADD <name>

Applicable Models: All (Write-only) Adds an external device to the list of
configured devices. This is the same as pressing New on the [Select an
external
device](../../System/Configure_an_External_Device.htm#SelectExtSource) dialog.
Upon creation, all settings on the new device are set to the defaults. The
device is not active until set using
[SYST:CONF:EDEV:STAT](SystConfigExternalDevice.md#State)  
---  
Parameters |   
<name> |  String - Model and type of the external device. To see a list of configured external devices, use [SYST:CONF:EDEV:CAT?](SystConfigExternalDevice.md#cat)  
Examples |  SYST:CONF:EDEV:ADD "myDevice" system:configure:edevice:add "myDevice"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:CONFigure:EDEVice:CAT?

Applicable Models: All (Read-only) Returns a list of names of all configured
devices. These are devices that appear in the [external
devices](../../System/Configure_an_External_Device.htm) dialog.  Use
[SENS:FOM:CAT?](Sense/FOM.md#cat) to report all active devices. Use
[Source:CAT?](source.md#Cat) to report all active sources.  
---  
Parameters |  None  
Example |  SYST:CONF:EDEV:CAT? system:configure:edevice:cat  
Return Type |  String of comma-separated devices. "Device0:Driver0, Device1:Driver1"  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SYSTem:CONFigure:EDEVice:CHANnel<cnum>:BASE? <decoratedName>

Applicable Models: All (Read-only) Returns the base name from the decorated
name. For example, "N5186A Ch 3" returns N5186A. See also, the [Enable
Output](../../System/Configure_an_External_Source.htm#Enable_Output) feature
of the External Source Device dialog.  
---  
Parameters |   
<cnum> |  Channel number of the external device. Ignored for this query.  
<decoratedName> |  String  
Example |  SYST:CONF:EDEV:CHAN:BASE? "myDevice"  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SYSTem:CONFigure:EDEVice:CHANnel<cnum>:COUNt? <deviceName>

Applicable Models: All (Read-only) This returns the total number of channels
possible. Currently, this is always 4. See also, the [Enable
Output](../../System/Configure_an_External_Source.htm#Enable_Output) feature
of the External Source Device dialog.  
---  
Parameters |   
<cnum> |  Channel number of the external device. Ignored for this query.  
<deviceName> |  String  
Example |  SYST:CONF:EDEV:CHAN:COUNt? "myDevice"  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SYSTem:CONFigure:EDEVice:CHANnel<cnum>:NAME? <deviceName>

Applicable Models: All (Read-only) Returns the decorated name of the device
for a particular channel. For example, SYST:CONF:EDEV:CHAN3:NAME? "N5186A"
returns N5186A Ch 3. See also, the [Enable
Output](../../System/Configure_an_External_Source.htm#Enable_Output) feature
of the External Source Device dialog.  
---  
Parameters |   
<cnum> |  Channel number of the external device.  
<deviceName> |  String  
Example |  SYST:CONF:EDEV:CHAN:NAME? "myDevice"  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SYSTem:CONFigure:EDEVice:CHANnel<cnum>:NUMBer? <decoratedName>

Applicable Models: All (Read-only) Returns the channel number from the
decorated name. For example: "N5186A Ch 3" returns 3. See also, the [Enable
Output](../../System/Configure_an_External_Source.htm#Enable_Output) feature
of the External Source Device dialog.  
---  
Parameters |   
<cnum> |  Channel number of the external device. Ignored for this query.  
<decoratedName> |  String  
Example |  SYST:CONF:EDEV:CHAN:NUMBer? "myDevice"  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Numeric  
  
* * *

## SYSTem:CONFigure:EDEVice:CHANnel<cnum>[:STATe] <deviceName>,<value>

Applicable Models: All (Read-only) Turns on or off channels on a particular
external source. See also, the [Enable
Output](../../System/Configure_an_External_Source.htm#Enable_Output) feature
of the External Source Device dialog.  
---  
Parameters |   
<cnum> |  Channel number of the external device.  
<deviceName> |  String  
<value> |  Boolean - Choose from: OFF or 0 \- Device communication disabled ON or 1 \- Device communication enabled  
Example |  SYST:CONF:EDEV:CHAN3 "myDevice",1  
Query Syntax |  SYSTem:CONFigure:EDEVice:CHANnel:STATe? <myDevice>  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SYSTem:CONFigure:EDEVice:CHANnel:SYNC <deviceName>,<value>

Applicable Models: All (Read-only) Turns on or off channel phase
synchronization on an external source supporting this feature. See also, the
[Enable Output](../../System/Configure_an_External_Source.md#Enable_Output)
feature of the External Source Device dialog.  
---  
Parameters |   
<deviceName> |  String  
<value> |  Boolean - Choose from: OFF or 0 \- Channel synchronization disabled ON or 1 \- Channel synchronization enabled  
Example |  SYST:CONF:EDEV:CHAN:SYNC "myDevice",1  
Query Syntax |  SYSTem:CONFigure:EDEVice:CHANnel:SYNC? <myDevice>  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SYSTem:CONFigure:EDEVice:DRIVer <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the external device
driver (model).  
---  
Parameters |   
<name> |  String - Name of the device.  
<value> |  String - External device driver (model). Choose from the following: "AGPM" for all power meters. "AGPULSEGEN" for supported pulse generators. "DCSource" for all supported DC Sources "DCMeter" for all supported DC Meters [See a list of supported external source drivers.](../../System/Configure_an_External_Device.md#Supported)  
Examples |  SYST:CONF:EDEV:DRIV "myDevice","AGPM" system:configure:edevice:driver "myDevice","AGESG"  
Query Syntax |  SYSTem:CONFigure:EDEVice:DRIVer? <name>  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  "AGGeneric"  
  
* * *

## SYSTem:CONFigure:EDEVice:DTYPe <name>,<type>

Applicable Models: All (Read-Write) Sets and returns the Device Type for the
external device.  
---  
Parameters |   
<name> |  String - Name of the device to modify.  
<type> |  String - Device type - not case sensitive. Choose from: "None" "Source" \- external source "Power Meter" \- power meter "DC Meter" \- DC voltmeter "DC Source" \- DC power supply "Pulse Generator" \- external pulse generator "SMU" \- Source Measure Unit  
Examples |  SYST:CONF:EDEV:DTYP "myDevice","Power Meter" system:configure:edevice:dtype "myDevice","Source"  
Query Syntax |  SYSTem:CONFigure:EDEVice:DTYPe? <name>  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Source  
  
* * *

## SYSTem:CONFigure:EDEVice:EXISts? <string>

Applicable Models: All (Read-only) Returns whether the named device is present
on the bus for which it is configured.  
---  
Parameters |   
<string> |  Name of the external device.  
Example |  SYST:CONF:EDEV:EXIS? "MyPowerMeter"  
Return Type |  Boolean

  * 0 \- The device is not in the collection or the device fails to respond and times out when communication is attempted.
  * 1 \- The device responds when communication is attempted.

  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SYSTem:CONFigure:EDEVice:IOConfig <name>,<value>

Applicable Models: All (Read-Write) Sets and return the configuration path for
the specified external device.  
---  
Parameters |   
<name> |  String - Name of the device.  
<value> |  String - Configuration path. Any valid VISA resource shown in the IO Configuration field of the [external devices dialog](../../System/Configure_an_External_Device.md#ext_source_config), enclosed in quotes. Use the [SYST:COMM:VISA:RDEV:FIND?](SystCommunicate.md#VISA_FIND) command to return IO devices that the visa subsystem can identify. This command will return addresses for devices found on GPIB, USB, or LAN.  
Examples |  SYST:CONF:EDEV:IOC "myDevice","GPIB0::13::INSTR" SYST:CONF:EDEV:IOC "myDevice","TCPIP0::141.121.148.119::inst0::INSTR" system:configure:edevice:ioconfig "myDevice","USB0::10893::19457::MZ00703073::0::INSTR"  
Query Syntax |  SYSTem:CONFigure:EDEVice:IOConfig? <name>  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  "" Empty String  
  
* * *

## SYSTem:CONFigure:EDEVice:IOENable <name>,<value>

Applicable Models: All (Read-Write) Enable or disable communication with an
external device.  When disabled (OFF), the VNA will NOT attempt to connect to
the external device regardless of the instrument state command
([SYST:CONF:EDEV:STATe](SystConfigExternalDevice.md#State)). Therefore, no
errors will be produced if the device is not connected. This command is useful
for debugging and testing states when the external device is not connected.
This command is unnecessary in ordinary operation (when the device is
connected).  
---  
Parameters |   
<name> |  String - Name of the device.  
<value> |  Boolean - Choose from: OFF or 0 \- Device communication disabled ON or 1 \- Device communication enabled  
Examples |  SYST:CONF:EDEV:IOEN "myDevice", ON system:configure:edevice:ioenable "myDevice", 0  
Query Syntax |  SYSTem:CONFigure:EDEVice:IOENable? <name>  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON  
  
* * *

## SYSTem:CONFigure:EDEVice:LOAD <file>,<name>

Applicable Models: All (Write-only) Recalls an external device configuration
file from the VNA hard drive.  Currently, only DC Supply and DC Meter
configuration files are supported. See more [DC Device
commands](SystConfigExtDC.htm). Use
[SYST:CONF:EDEV:SAVE](SystConfigExternalDevice.md#save) to save a
configuration file.  
---  
Parameters |   
<file> |  String - Filename of the external device configuration file.

  1. If <file> is not a full path, it is assumed to be a relative path based at "D:\Drivers".
  2. The file specified using <file> cannot be the same file as "D:\Drivers\<name>.xml".

  
<name> |  String - Name of the external device. Currently, only DC Supply and DC Meter configuration files are supported.  
Examples |  SYST:CONF:EDEV:LOAD "D:\Drivers\MyConfigFile.xml","MyDevice"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:CONFigure:EDEVice:RCLock:VNA:STATe <name>,<state>

Applicable Models: All (Read-Write) Set and return if VNA is Reference Clock
Provider for the specified external device.  
---  
Parameters |   
<name> |  String - Name of the device.   
<state> |  Boolean - Choose from: **OFF or 0** \- VNA is NOT Reference Clock Provider **ON or****1** \- VNA is Reference Clock Provider  
Examples |  SYST:CONF:EDEV:RCL:VNA:STAT "myDevice",1 system:configure:edevice:rclock:vna:state "myDevice",0  
Query Syntax |  SYSTem:CONFigure:EDEVice:RCLock:VNA:STATe? <name>  
Retrun Type  |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0  
  
* * *

## SYSTem:CONFigure:EDEVice:REMove <name>

Applicable Models: All (Write-only) Removes the specified device from the list
of configured devices. If the device is a Source and both Active and I/O
Enabled is checked (ON), then the RF power state is set to OFF. [Learn
more.](../../System/Configure_an_External_Device.htm#ExtDevConfig)  
---  
Parameters |   
<name> |  String - Name of the device. Not case sensitive. Use [SYST:CONF:EDEV:CAT?](SystConfigExternalDevice.md#cat) to return a list of configured devices.  
Examples |  SYST:CONF:EDEV:REM "myDevice" system:configure:edevice:remove "myDevice"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:CONFigure:EDEVice:SAVE <file>,<name>

Applicable Models: All (Write-only) Saves an external device configuration
file to the VNA hard drive.  Currently, only DC Supply and DC Meter
configuration files are supported. See more [DC Device
commands](SystConfigExtDC.htm). Use
[SYST:CONF:EDEV:LOAD](SystConfigExternalDevice.md#load) to recall a
configuration file.  
---  
Parameters |   
<file> |  String - Filename of the external device configuration file.  
<name> |  String - Name of the external device. Currently, only DC Supply and DC Meter configuration files are supported.  
Examples |  SYST:CONF:EDEV:SAVE "myDevice.xml","MyDCSupply"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SYSTem:CONFigure:EDEVice:SMU:CHANnel[1-4]:STATe <name>,<state>

Applicable Models: All (Read-Write) Set and return the state of activation of
the SMU device channel. Learn more about [configuring an external
SMU](../../System/Configure_an_External_SMU.htm#SetupTab).  When
[SYST:CONF:EDEV:IOEN](SystConfigExternalDevice.md#IOEnable) = ON, and this
command is set to ON, the VNA will attempt communication with the external
device. Send this command AFTER sending other external device settings
(especially [SYST:CONF:EDEV:DTYP](SystConfigExternalDevice.md#DTYPe)) to
avoid communicating with the device before it has been fully configured. See
Also: [SYST:PREF:ITEM:EDEV:DPOL](System_Preferences.md#PrefEdevDpol) \-
Determines whether external devices remain activated or are de-activated when
the VNA is Preset or when a Instrument State is recalled.  
---  
Parameters |   
<name> |  String - Name of the SMU device.  
<state> |  Boolean - Choose from: OFF or 0 \- SMU Device channel is NOT activated ON or 1 \- SMU Device channel is activated.  
Examples |  SYST:CONF:EDEV:SMU:CHAN2:STAT "myDevice", ON system:configure:edevice:smu:channel2:state "myDevice", 0  
Query Syntax |  SYSTem:CONFigure:EDEVice:SMU:CHANnel[1-4]:STATe? <name>  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SYSTem:CONFigure:EDEVice:STATe <name>,<state>

Applicable Models: All (Read-Write) Set and return the state of activation of
the device. When [SYST:CONF:EDEV:IOEN](SystConfigExternalDevice.md#IOEnable)
= ON, and this command is set to ON, the VNA will attempt communication with
the external device.  Send this command AFTER sending other external device
settings (especially
[SYST:CONF:EDEV:DTYP](SystConfigExternalDevice.md#DTYPe)) to avoid
communicating with the device before it has been fully configured. See Also:
[SYST:PREF:ITEM:EDEV:DPOL](System_Preferences.md#PrefEdevDpol) \- Determines
whether external devices remain activated or are de-activated when the VNA is
Preset or when a Instrument State is recalled.  
---  
Parameters |   
<name> |  String - Name of the device.  
<state> |  Boolean - Choose from: OFF or 0 \- Device is NOT activated ON or 1 \- Device is activated.  
Examples |  SYST:CONF:EDEV:STAT "myDevice", ON system:configure:edevice:state "myDevice", 0  
Query Syntax |  SYSTem:CONFigure:EDEVice:STATe? <name>  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF - When configured using the front panel user interface, the device is ON (activated) by default.  
  
* * *

## SYSTem:CONFigure:EDEVice:TOUT <name>,<value>

Applicable Models: All (Read-Write) Set and return the time out value for the
specified external device. This is the time allowed for communication with the
device before an error is generated.  
---  
Parameters |   
<name> |  String - Name of the device.  
<value> |  Time out value in seconds.  
Examples |  SYST:CONF:EDEV:TOUT "myDevice",2 system:configure:edevice:tout "myDevice",5  
Query Syntax |  SYSTem:CONFigure:EDEVice:TOUT? <name>  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  20  
  
* * *

## SYSTem:CONFigure:EDEVice:SOURce:DPPoint <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the amount of time the
VNA should wait after for an external source to settle before making a
measurement at each data point. This setting applies to all channels that use
this external source.  
---  
Parameters |   
<name> |  String - Name of the device.  
<value> |  Dwell time in seconds.  
Examples |  SYST:CONF:EDEV:SOUR:DPP "myDevice",2 system:configure:edevice:source:dppoint "myDevice",.1  
Query Syntax |  SYSTem:CONFigure:EDEVice:SOURce:DPP? <name>  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  3.114 e-3  
  
* * *

## SYSTem:CONFigure:EDEVice:SOURce:HYBRid:INPut:FREQuency:CARRier
<name>,<value>

Applicable Models: All (Read-Write) For an SSB Mixer, the center of the input
modulated signal is offset from DC by the carrier frequency.  The Hybrid
Source will adjust the LO Source to set the frequency of the output. In some
cases, the Input Carrier frequency must be adjusted by a slight amount so that
the input mixed with the LO results in the desired output. This entry is
labeled as being "Nominal" because the value may be changed by the Hybrid
Source.  
---  
Parameters |   
<name> |  String - Name of the device.  
<value> |  Carrier in Hz. Range is 0 to 10 GHz.  
Examples |  SYST:CONF:EDEV:SOUR:HYBRid:INPut:FREQuency:CARRier "myDevice",1e9  
Query Syntax |  SYSTem:CONFigure:EDEVice:SOURce:HYBRid:INPut:FREQuency:CARRier? <name>  
Return Type |  Numeric  
Default |  0 Hz  
  
* * *

## SYSTem:CONFigure:EDEVice:SOURce:HYBRid:INPut:FREQuency:MULTiplier
<name>,<value>

Applicable Models: All (Read-Write) If there is a multiplier placed between
the Input Source and the SSB mixer, then use this command to specify the
multiplication factor.  
---  
Parameters |   
<name> |  String - Name of the device.  
<value> |  Muliplier. Range is 1 to 999.  
Examples |  SYST:CONF:EDEV:SOUR:HYBR:INP:FREQ:MULT "myDevice",10  
Query Syntax |  SYSTem:CONFigure:EDEVice:SOURce:HYBRid:INPut:FREQuency:MULTiplier? <name>  
Return Type |  Numeric  
Default |  1  
  
* * *

## SYSTem:CONFigure:EDEVice:SOURce:HYBRid:INPut:NAME <name>,<value>

Applicable Models: All (Read-Write) Select external or internal sources for
the input source.  
---  
Parameters |   
<name> |  String - Name of the device.  
<value> |  String - Name of the input source.  
Examples |  SYST:CONF:EDEV:SOUR:HYBR:INP:NAME "myDevice","Port1"  
Query Syntax |  SYSTem:CONFigure:EDEVice:SOURce:HYBRid:INPut:NAME? <name>  
Return Type |  String  
Default |  None  
  
* * *

## SYSTem:CONFigure:EDEVice:SOURce:HYBRid:INPut:POWer:LIMit <name>,<value>

Applicable Models: All (Read-Write) This is the maximum power setting allowed
for the Input Source.  The system will adjust the output power of the Hybrid
Source by changing the power level of the Input Source and correcting for the
Nominal Gain. This limit ensures that the Input Source is not set to a power
level that will damage the SSB mixer.  
---  
Parameters |   
<name> |  String - Name of the device.  
<value> |  Power Limit in dBm. Range is -200 to 100.  
Examples |  SYST:CONF:EDEV:SOUR:HYBR:INP:POW:LIM "myDevice",10  
Query Syntax |  SYSTem:CONFigure:EDEVice:SOURce:HYBRid:INPut:POWer:LIMit? <name>  
Return Type |  Numeric  
Default |  0  
  
* * *

## SYSTem:CONFigure:EDEVice:SOURce:HYBRid:INPut:PULSe:ENABle <device>,<state>

Applicable Models: All (Read-Write) Enables pulse on the Input Source.  The
hybrid source can be pulsed either by pulsing the Input Source or by pulsing
the LO Source. The user can choose which source is pulsed when the hybrid
source is pulsed. See also, SCPI command description for enabling pulse on LO
Source.  
---  
Parameters |   
<device> |  String - Name of the device.  
<state> |  Boolean - Choose from: OFF or 0 \- Pulse is NOT activated ON or 1 \- Pulse is activated.  
Examples |  SYST:CONF:EDEV:SOUR:HYBR:INP:PULS:ENAB "myDevice",1  
Query Syntax |  SYSTem:CONFigure:EDEVice:SOURce:HYBRid:INPut:PULSe:ENABle? <device>  
Return Type |  Numeric  
Default |  0  
  
* * *

## SYSTem:CONFigure:EDEVice:SOURce:HYBRid:LO:FREQuency:MULTiplier
<name>,<value>

Applicable Models: All (Read-Write) If there is a multiplier placed between
the LO Source and the SSB mixer, then use this command to specify the
multiplication factor.  
---  
Parameters |   
<name> |  String - Name of the device.  
<value> |  Muliplier. Range is 1 to 999.  
Examples |  SYST:CONF:EDEV:SOUR:HYBR:LO:FREQ:MULT "myDevice",10  
Query Syntax |  SYSTem:CONFigure:EDEVice:SOURce:HYBRid:LO:FREQuency:MULTiplier? <name>  
Return Type |  Numeric  
Default |  1  
  
* * *

## SYSTem:CONFigure:EDEVice:SOURce:HYBRid:LO:NAME <name>,<value>

Applicable Models: All (Read-Write) Select external or internal sources for
the LO source.  
---  
Parameters |   
<name> |  String - Name of the device.  
<value> |  String - Name of the LO source.  
Examples |  SYST:CONF:EDEV:SOUR:HYBR:LO:NAME "myDevice","Port1"  
Query Syntax |  SYSTem:CONFigure:EDEVice:SOURce:HYBRid:LO:NAME? <name>  
Return Type |  String  
Default |  None  
  
* * *

## SYSTem:CONFigure:EDEVice:SOURce:HYBRid:LO:POWer <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the amount of time the
VNA should wait after for an external source to settle before making a
measurement at each data point. This setting applies to all channels that use
this external source.  
---  
Parameters |   
<name> |  String - Name of the device.  
<value> |  LO Power in dBm. Range is -200 to 100.  
Examples |  SYST:CONF:EDEV:SOUR:HYBR:LO:POW "myDevice",10  
Query Syntax |  SYSTem:CONFigure:EDEVice:SOURce:HYBRid:LO:POWer? <name>  
Return Type |  Numeric  
Default |  0  
  
* * *

## SYSTem:CONFigure:EDEVice:SOURce:HYBRid:LO:PULSe:ENABle <device>,<state>

Applicable Models: All (Read-Write) Enables pulse on the LO Source.  The
hybrid source can be pulsed either by pulsing the Input Source or by pulsing
the LO Source. The user can choose which source is pulsed when the hybrid
source is pulsed. See also, SCPI command description for enabling pulse on
Input Source.  
---  
Parameters |   
<device> |  String - Name of the device.  
<state> |  Boolean - Choose from: OFF or 0 \- Pulse is NOT activated ON or 1 \- Pulse is activated.  
Examples |  SYST:CONF:EDEV:SOUR:HYBR:LO:PULS:ENAB "myDevice",1  
Query Syntax |  SYSTem:CONFigure:EDEVice:SOURce:HYBRid:LO:PULSe:ENABle? <device>  
Return Type |  Numeric  
Default |  0  
  
* * *

## SYSTem:CONFigure:EDEVice:SOURce:HYBRid:LOCK:STATe <device>,<state>

Applicable Models: All (Read-Write) This locks out sources that are used by
the hybrid source from the GUI. By default this is checked.  
---  
Parameters |   
<device> |  String - Name of the device.  
<state> |  Boolean - Choose from: OFF or 0 \- Lock is NOT activated ON or 1 \- Lock is activated.  
Examples |  SYST:CONF:EDEV:SOUR:HYBR:LOCK:STAT "myDevice",0  
Query Syntax |  SYSTem:CONFigure:EDEVice:SOURce:HYBRid:LOCK:STAT? <device>  
Return Type |  Numeric  
Default |  1  
  
* * *

## SYSTem:CONFigure:EDEVice:SOURce:HYBRid:OUTPut:FREQuency:MAX
<device>,<value>

Applicable Models: All (Read-Write) Sets the maximum output frequency limit of
the mixer.  
---  
Parameters |   
<device> |  String - Name of the device.  
<value> |  Maximum frequency limit for the mixer in Hz. Range is 0 to 1000 GHz.  
Examples |  SYST:CONF:EDEV:SOUR:HYBR:OUTP:FREQ:MAX "myDevice",10e9  
Query Syntax |  SYSTem:CONFigure:EDEVice:SOURce:HYBRid:OUTP:FREQ:MAX? <device>  
Return Type |  Numeric  
Default |  1000 GHz  
  
* * *

## SYSTem:CONFigure:EDEVice:SOURce:HYBRid:OUTPut:FREQuency:MIN
<device>,<value>

Applicable Models: All (Read-Write) Sets the minimum output frequency limit of
the mixer.  
---  
Parameters |   
<device> |  String - Name of the device.  
<value> |  Minimum frequency limit for the mixer in Hz. Range is 0 to 1000 GHz.  
Examples |  SYST:CONF:EDEV:SOUR:HYBR:OUTP:FREQ:MIN "myDevice",10e6  
Query Syntax |  SYSTem:CONFigure:EDEVice:SOURce:HYBRid:OUTP:FREQ:MIN? <device>  
Return Type |  Numeric  
Default |  0 Hz  
  
* * *

## SYSTem:CONFigure:EDEVice:SOURce:HYBRid:OUTPut:GAIN <device>,<value>

Applicable Models: All (Read-Write) This is the nominal gain of the SSB mixer
system. The nominal gain value is used to set the input source power in order
to get the desired output source power. The user may choose to add an
amplifier to the hybrid source to get more output power.  Note that if the
input multiplier is set to some value other than 1, then the concept of
amplification not very clear. In this case, we will assume that the gain
represents the gain from the input power limit value to the resulting output
power.  
---  
Parameters |   
<device> |  String - Name of the device.  
<value> |  Gain in dB. Range is -200 to 100  
Examples |  SYST:CONF:EDEV:SOUR:HYBR:OUTP:GAIN "myDevice",10  
Query Syntax |  SYSTem:CONFigure:EDEVice:SOURce:HYBRid:OUTPut:GAIN? <device>  
Return Type |  Numeric  
Default |  0 dB  
  
* * *

## SYSTem:CONFigure:EDEVice:SOURce:HYBRid:OUTPut:MIXer:SIDeband
<device>,<value>

Applicable Models: All (Read-Write) Specify whether to select the sum (High)
or difference (Low) products. Input + or - LO = Output frequency  
---  
Parameters |   
<device> |  String - Name of the device.  
<value> |  Sideband value. Choose from LOW \- Low or Difference (-) HIGH \- High or Sum (+)  
Examples |  SYST:CONF:EDEV:SOUR:HYBR:OUTP:MIX:SID "myDevice",HIGH  
Query Syntax |  SYSTem:CONFigure:EDEVice:SOURce:HYBRid:OUTP:MIX:SID? <device>  
Return Type |  Character  
Default |  LOW  
  
* * *

## SYSTem:CONFigure:EDEVice:SOURce:HYBRid:TYPE <name>,<value>

Applicable Models: All (Read-Write) Currently provides two selections: SSB
Mixer (default) and Multiplier. The External Device dialog changes appearance
and available settings according to the Hybrid Type you select.  
---  
Parameters |   
<name> |  String - Name of the device.  
<value> |  String - Name of the Hybrid Type.  
Examples |  SYST:CONF:EDEV:SOUR:HYBR:TYPE "myDevice","Multiplier"  
Query Syntax |  SYSTem:CONFigure:EDEVice:SOURce:HYBRid:TYPE? <name>  
Return Type |  String  
Default |  SSB Mixer  
  
* * *

## SYSTem:CONFigure:EDEVice:SOURce:MODulation:CONTrol:STATe <name>,<state>

Applicable Models: All (Read-Write) Sets and reads the state of the modulation
control. Modulation control must be ON to control the modulation of an
external source.  
---  
Parameters |   
<name> |  String - Name of the device.  
<state> |  ON (or 1) Enable control of external modulation. OFF (or 0) Disable control of external modulation. [Learn about these settings](../../System/Configure_an_External_Source.md) and about [adding an external source](../../System/Configure_an_External_Device.md).  
Examples |  SYST:CONF:EDEV:SOUR:MOD:CONT:STAT "qasmxg",1 system:configure:edevice:source:modulation:control:state "qasmxg",OFF  
Query Syntax |  SYSTem:CONFigure:EDEVice:SOURce:MODulation:CONTrol:STATe? "qasmxg"  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF  
  
* * *

## SYSTem:CONFigure:EDEVice:SOURce:TMODe <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the trigger mode for an
external source. [Learn
more.](../../System/Configure_an_External_Device.htm#ext_source_config)  
---  
Parameters |   
<name> |  String - Name of the device.  
<value> |  Trigger Mode. Choose from: CW \- Software CW mode HW \- Hardware list mode  
Examples |  SYST:CONF:EDEV:SOUR:TMOD "myDevice",CW system:configure:edevice:source:tmode "myDevice",hw  
Query Syntax |  SYSTem:CONFigure:EDEVice:SOURce:TMODe? "myDevice"  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Depends on Source and VNA Model  
  
* * *

## SYSTem:CONFigure:EDEVice:SOURce:TPORt <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the VNA port through
which an external source is to be triggered.  
---  
Parameters |   
<name> |  String - Name of the device.  
<value> |  Trigger Port. Choose from aux1 or aux2  
Examples |  system:configure:edevice:source:tport "myDevice",aux1  
Query Syntax |  SYSTem:CONFigure:EDEVice:SOURce:TPORt? <name>  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  aux1  
  
* * *

