# SYSTem:CONFigure:EDEVice:DC Commands

* * *

Configures external SMU, DC Meter, and DC Source properties.

SYST:CONF:EDEVice:DC | COMMand | EXIT | INIT | LIMit | POINt | SET | SWEep | ABORt | AFTer | BEFore | [CORRection](SystConfigExtDC.md#CorrectionState) | [DPOint](SystConfigExtDC.md#DwellPoint) | [DSWeep](SystConfigExtDC.md#DwellSweep) | LIMit | CURRent | VOLTage | MAX | [:STATe] | VALue | MIN | [:STATe] | VALue | [OFFSet](SystConfigExtDC.md#offset) | QUERy | ERRor | ID | [SCALe](SystConfigExtDC.md#scale) | [TYPE](SystConfigExtDC.md#TYPE)  
---  
  
Click on a red keyword to view the command details.

### See Also

  * All [SYST:CONF:EDEV](SystConfigExternalDevice.md) commands

  * [SOURce:DC](SourceDC.md) commands (make DC sweep settings)

  * Learn about: [Configure an External DC Device](../../System/Configure_a_DC_Device.md)

  * Learn about [Configure an External Device](../../System/Configure_an_External_Device.md)

  * [SYST:PREF:ITEM:EDEV:DPOL](System_Preferences.md#PrefEdevDpol) \- Determines whether External Devices remain activated or are de-activated when the VNA is Preset or when a Instrument State is recalled.

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## SYSTem:CONFigure:EDEVice:DC:COMMand:EXIT <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the Disable I/O command
for an external DC Source and an external DC Meter.  
---  
Parameters |   
<name> | String - Name of the device.  
<value> | String - The SCPI command used to disable the DC Source and DC Meter.  
Examples | SYST:CONF:EDEV:DC:COMM:EXIT "myDCDevice","OUTP OFF" system:configure:edevice:dc:command:exit "myDCDevice","OUTP OFF"  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:COMMand:EXIT? <name>  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | " " Empty String  
  
* * *

## SYSTem:CONFigure:EDEVice:DC:COMMand:INIT <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the Enable I/O command
for an external DC Source and an external DC Meter.  
---  
Parameters |   
<name> | String - Name of the device.  
<value> | String - The SCPI command used to enable the DC Source and DC Meter.  
Examples | SYST:CONF:EDEV:DC:COMM:INIT "myDCDevice","OUTP ON" system:configure:edevice:dc:command:init "myDCDevice","OUTP ON"  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:COMMand:INIT? <name>  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | " " Empty String  
  
* * *

## SYSTem:CONFigure:EDEVice:DC:COMMand:LIMit <name>, <cmd>

Applicable Models: All (Read-Write) Sets and returns a user-defined command
string that is used to set the DC limit of the external DC source. The actual
limit value is set using either the SYST:CONF:EDEV:DC:LIM:VOLT (voltage) or
SYST:CONF:EDEV:DC:LIM:CURR (current). The limit command is sent to the
external DC source at the beginning of a sweep for each channel. The firmware
automatically selects the current or voltage limit value depending on the
external DC source type.  
---  
Parameters |   
<name> | String - Name of the device.  
<cmd> | String - User-defined command name: Include {%f} in the command string which will be substituted by the actual limit value.  
Examples | SYST:CONF:EDEV:DC:COMM:LIM "myDCDevice","Limit Command {%f}" system:configure:edevice:dc:command:limit "myDCDevice","Limit Command {%f}"  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:COMMand:LIMit? <name>  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CONFigure:EDEVice:DC:COMMand:POINt:SET <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the Point Read Commands
for an external DC Meter or Point Set Commands for an external DC Source.  
---  
Parameters |   
<name> | String - Name of the device.  
<value> | String - For DC Source, sets the Point Set Commands. Use {%f} to specify a double value and {%d} to specify an integer. For DC Meter, sets the Point Read Commands (for example, meas:volt?).  
Examples | SYST:CONF:EDEV:DC:COMM:POIN:SET "myDCDevice","sour1:volt {%f}" system:configure:edevice:dc:command:point:set "myDCDevice","meas:volt?"  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:COMMand:POINt:SET? <name>  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | " " Empty String  
  
* * *

## SYSTem:CONFigure:EDEVice:DC:COMMand:SWEep:ABORt <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the Abort Sweep command
for an external DC Source and an external DC Meter.  
---  
Parameters |   
<name> | String - Name of the device.  
<value> | String - The SCPI command used to abort or reset the DC Source or DC Meter.  
Examples | SYST:CONF:EDEV:DC:COMM:SWE:ABOR "myDCDevice","ABORt" system:configure:edevice:dc:command:sweep:abort "myDCDevice","ABORt"  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:COMMand:SWEep:ABORt? <name>  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | " " Empty String  
  
* * *

## SYSTem:CONFigure:EDEVice:DC:COMMand:SWEep:AFTer <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the After Sweep command
for an external DC Source and an external DC Meter.  
---  
Parameters |   
<name> | String - Name of the device.  
<value> | String - The SCPI command to be sent at the end of a sweep.  
Examples | SYST:CONF:EDEV:DC:COMM:SWE:AFT "myDCDevice","OUTP OFF" system:configure:edevice:dc:command:sweep:after "myDCDevice","OUTP OFF"  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:COMMand:SWEep:AFTer? <name>  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | " " Empty String  
  
* * *

## SYSTem:CONFigure:EDEVice:DC:COMMand:SWEep:BEFore <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the Before Sweep command
for an external DC Source and an external DC Meter.  
---  
Parameters |   
<name> | String - Name of the device.  
<value> | String - The SCPI command to be sent at the beginning of a sweep.  
Examples | SYST:CONF:EDEV:DC:COMM:SWE:BEF "myDCDevice","OUTP ON" system:configure:edevice:dc:command:sweep:before "myDCDevice","OUTP ON"  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:COMMand:SWEep:BEFore? <name>  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | " " Empty String  
  
* * *

## SYSTem:CONFigure:EDEVice:DC:CORRection <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the correction ON/OFF
state for a DC Meter and a DC Source.  
---  
Parameters |   
<name> | String - Name of the device.  
<value> | Correction ON/OFF state. Choose from: ON or 1 \- Turn Correction ON OFF or 0 \- Turn Correction OFF  
Examples | SYST:CONF:EDEV:DC:CORR "myDCDevice",1 system:configure:edevice:dc:correction "myDCDevice",OFF  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:CORRection? <name>  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SYSTem:CONFigure:EDEVice:DC:DPOint <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the "Dwell Before/After
Point" value for an external DC Device which can be configured as either a DC
Meter or a DC Source.  
---  
Parameters |   
<name> | String - Name of the device.  
<value> | For DC Meter, the dwell time (in seconds) before making a data point measurement. For DC Source, the dwell time (in seconds) after making a data point setting.  
Examples | SYST:CONF:EDEV:DC:DPO "myDCDevice",10e-3 system:configure:edevice:dc:dpoint "myDCDevice",.01  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:DPOint? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 3 milliseconds  
  
* * *

## SYSTem:CONFigure:EDEVice:DC:DSWeep <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the "Dwell Before Sweep"
value for an external DC Device which can be configured as either a DC Meter
or a DC Source.  
---  
Parameters |   
<name> | String - Name of the device.  
<value> | The dwell time (in seconds) before making a new sweep.  
Examples | SYST:CONF:EDEV:DC:DSW "myDCDevice",10e-3 system:configure:edevice:dc:dsweep "myDCDevice",.01  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:DSWeep? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1 millisecond  
  
* * *

## SYSTem:CONFigure:EDEVice:DC:LIMit:CURRent <name>, <value>

Applicable Models: All (Read-Write) Sets and returns the maximum output
current value of the external DC Source. This command supports Keysight B2900A
and N6700 series devices only.  
---  
Parameters |   
<name> | String - Name of the device.  
<value> | Current limit value.  
Examples | SYST:CONF:EDEV:DC:LIM:CURR "myDCDevice",4 system:configure:edevice:dc:limit:current "myDCDevice",1.25  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:LIMit:CURRent? <name>  
Return Type | Double  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## SYSTem:CONFigure:EDEVice:DC:LIMit:VOLTage <name>, <value>

Applicable Models: All (Read-Write) Sets and returns the maximum output
voltage value of the external DC Source. This command supports Keysight B2900A
and N6700 series devices only.  
---  
Parameters |   
<name> | String - Name of the device.  
<value> | Voltage limit value.  
Examples | SYST:CONF:EDEV:DC:LIM:VOLT "myDCDevice",4 system:configure:edevice:dc:limit:voltage "myDCDevice",1.25  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:LIMit:VOLTage? <name>  
Return Type | Double  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## SYSTem:CONFigure:EDEVice:DC:MAX[:STATe] <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the "Define Max As"
ON/OFF state for an external DC Source.  
---  
Parameters |   
<name> | String - Name of the device.  
<value> | "Define Max As" ON/OFF state. Choose from: ON or 1 \- Turn "Define Max As" ON OFF or 0 \- Turn "Define Max As" OFF  
Examples | SYST:CONF:EDEV:DC:MAX "myDCDevice",1 system:configure:edevice:dc:max:state "myDCDevice",OFF  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:MAX:STATe? <name>  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## SYSTem:CONFigure:EDEVice:DC:MAX:VALue <name>, <value>

Applicable Models: All (Read-Write) Sets and returns the "Define Max As" value
for an external DC Source.  
---  
Parameters |   
<name> | String - Name of the device.  
<value> | Maximum value for the external DC Source (in volts).  
Examples | SYST:CONF:EDEV:DC:MAX:VAL "myDCDevice",10 system:configure:edevice:dc:max:value "myDCDevice",10  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:MAX:VALue? <name>  
Return Type | Double  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 10  
  
* * *

## SYSTem:CONFigure:EDEVice:DC:MIN[:STATe] <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the "Define Min As"
ON/OFF state for an external DC Source.  
---  
Parameters |   
<name> | String - Name of the device.  
<value> | "Define Min As" ON/OFF state. Choose from: ON or 1 \- Turn "Define Min As" ON OFF or 0 \- Turn "Define Min As" OFF  
Examples | SYST:CONF:EDEV:DC:MIN "myDCDevice",1 system:configure:edevice:dc:min:state "myDCDevice",OFF  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:MIN:STATe? <name>  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## SYSTem:CONFigure:EDEVice:DC:MIN:VALue <name>, <value>

Applicable Models: All (Read-Write) Sets and returns the "Define Min As" value
for an external DC Source.  
---  
Parameters |   
<name> | String - Name of the device.  
<value> | Minimum value for the external DC Source (in volts).  
Examples | SYST:CONF:EDEV:DC:MIN:VAL "myDCDevice",-10 system:configure:edevice:dc:min:value "myDCDevice",-10  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:MIN:VALue? <name>  
Return Type | Double  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | -10  
  
* * *

## SYSTem:CONFigure:EDEVice:DC:OFFSet <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the offset correction
value for an external DC Device which can be configured as either a DC Meter
or a DC Source.  
---  
Parameters |   
<name> | String - Name of the device.  
<value> | DC offset value. The VNA will display readings from a DC Meter as: Display = (Meas'd value - Offset) * Scale The VNA will adjust the output from a DC Source as: Output = (Set value - Offset) * Scale  
Examples | SYST:CONF:EDEV:DC:OFFS "myDCDevice",4 system:configure:edevice:dc:offset "myDCDevice",1.25  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:OFFSet? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## SYSTem:CONFigure:EDEVice:DC:QUERy:ERRor <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the Error Query command
for an external DC Source and an external DC Meter.  
---  
Parameters |   
<name> | String - Name of the device.  
<value> | String - The SCPI command for returning DC Source and DC Meter errors.  
Examples | SYST:CONF:EDEV:DC:QUER:ERR "myDCDevice","SYST:ERR?" system:configure:edevice:dc:query:error "myDCDevice","SYST:ERR?"  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:QUERy:ERRor? <name>  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | "SYST:ERR?"  
  
* * *

## SYSTem:CONFigure:EDEVice:DC:QUERy:ID <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the ID Query command for
an external DC Source and an external DC Meter.  
---  
Parameters |   
<name> | String - Name of the device.  
<value> | String - The SCPI command for returning DC Source and DC Meter ID string.  
Examples | SYST:CONF:EDEV:DC:QUER:ID "myDCDevice","*IDN?" system:configure:edevice:dc:query:error "myDCDevice","*IDN?"  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:QUERy:ID? <name>  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | "*IDN?"  
  
* * *

## SYSTem:CONFigure:EDEVice:DC:SCALe <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the scale correction
value for an external DC Device which can be configured as either a DC Meter
or a DC Source.  
---  
Parameters |   
<name> | String - Name of the device.  
<value> | DC Scale value. The VNA will display readings from a DC Meter as: Display = (Meas'd value - Offset) * Scale The VNA will adjust the output from a DC Source as: Output = (Set value - Offset) * Scale  
Examples | SYST:CONF:EDEV:DC:SCAL "myDCDevice",1.2 system:configure:edevice:dc:scale "myDCDevice",.5  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:SCALe? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## SYSTem:CONFigure:EDEVice:DC:TYPE <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the DC Type for an
external DC Device which can be configured as either a DC Meter or a DC
Source. This setting is used as the units for display on the VNA X-axis.  
---  
Parameters |   
<name> | String - Name of the device.  
<value> | DC type. Choose from: "dBm", "A", "V", "W", "K", "F", "C"  
Examples | SYST:CONF:EDEV:DC:TYPE "myDCDevice","A" system:configure:edevice:dc:type "myDCDevice","w"  
Query Syntax | SYSTem:CONFigure:EDEVice:DC:TYPE? <name>  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | "V"  
  
* * *

* * *

