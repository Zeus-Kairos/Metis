# SYSTem:CONFigure:EDEVice:PMAR Commands

* * *

Configures and makes settings for an external Power Meter as Receiver.

SYSTem:CONFigure:EDEVice:PMAR | [CALibrate](SystConfigExtPMAR.md#Calibrate) | [FLIMit](SystConfigExtPMAR.md#pmarFLimit) | [FMAXimum](SystConfigExtPMAR.md#pmarFMAX) | [FMINimum](SystConfigExtPMAR.md#pmarFmin) | CFACtors | STATe | READing: | [COUNt](SystConfigExtPMAR.md#pmarReadCount) [ ](SystConfigExtPMAR.md#pmarReadNtol)| [NTOLerance](SystConfigExtPMAR.md#pmarReadNtol) | [SENSor](SystConfigExtPMAR.md#pmarSens) | CATalog? | TABLe: | CFAC: | [DATA](SystConfigExtPMAR.md#pmarCFACDate) | [FREQuency](SystConfigExtPMAR.md#pmarCFACFreq) | LOSS: | [DATA](SystConfigExtPMAR.md#pmarLossData) | [FREQuency](SystConfigExtPMAR.md#pmarLossFreq) | [STATe](SystConfigExtPMAR.md#pmarLossState) | [RFACtor](SystConfigExtPMAR.md#pmarRFAC) | UNCertainty | CATalog? | FILE | MODel | PLEVel? | READ? | [ZERO](SystConfigExtPMAR.md#zero)  
---  
  
Click on a keyword to view the command details.

### See Also

  * Learn about: [Configure a Power Meter As Receiver](../../System/Configure_a_Power_Meter_As_Receiver.md)

  * See root [SYST:CONF:EDEV](SystConfigExternalDevice.md) commands

  * Learn about [Configure and External Device](../../System/Configure_an_External_Device.md)

  * [SYST:PREF:ITEM:EDEV:DPOL](System_Preferences.md#PrefEdevDpol) \- Determines whether External Devices remain activated or are de-activated when the VNA is Preset or when a Instrument State is recalled.

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## SYSTem:CONFigure:EDEVice:PMAR:CALibrate <name>

Applicable Models: All (Write-only) Performs a calibration of the power
sensor. Calibration usually involves connecting the power sensor to the
meter's 1 mW reference.

  * Keysight P-Series sensors have an internal reference so you can calibrate them using this command without connecting to the meters reference port.
  * Keysight USB power sensors do not require calibrating.
  * For other sensors, refer to the documentation to determine if it has calibration capability.

This command is always synchronous, so *OPC? is the only way to determine that
the operation is complete. Set an I/O timeout of at least 20 seconds.  
---  
Parameters |   
<name> | String \- Name of the power meter.  
Examples | SYST:CONF:EDEV:PMAR:CAL "myDevice" system:configure:edevice:pmar:calibrate "myDevice"  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CONFigure:EDEVice:PMAR:FLIMit <name>,<value>

Applicable Models: All (Read-Write) Enable or disable the power meter min and
max frequencies.  
---  
Parameters |   
<name> | String \- Name of the power meter.  
<value> | Boolean. State of min and max frequency. Choose from: OFF or 0 \- Min and max frequencies disabled. ON or 1 \- Min and max frequencies enabled.  
Examples | SYST:CONF:EDEV:PMAR:FLIM "myDevice", 0 system:configure:edevice:pmar:flimit "myDevice", ON [See example program](../GPIB_Example_Programs/Configure_a_PMAR_Device.md)  
Query Syntax | SYSTem:CONFigure:EDEVice:PMAR:FLIMit? <name>  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SYSTem:CONFigure:EDEVice:PMAR:FMAXimum <name>,<value>

Applicable Models: All (Read-Write) Set and return the maximum frequency of
the power meter.  
---  
Parameters |   
<name> | String \- Name of the power meter.  
<value> | Numeric \- Max frequency in Hz.  
Examples | SYST:CONF:EDEV:PMAR:FMAX "myDevice", 1e10 system:configure:edevice:pmar:fmaximum "myDevice", 3e9 [See example program](../GPIB_Example_Programs/Configure_a_PMAR_Device.md)  
Query Syntax | SYSTem:CONFigure:EDEVice:PMAR:FMAXimum? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CONFigure:EDEVice:PMAR:FMINimum <name>,<value>

Applicable Models: All (Read-Write) Set and return the minimum frequency of
the power meter.  
---  
Parameters |   
<name> | String \- Name of the power meter.  
<value> | Numeric \- Min frequency in Hz.  
Examples | SYST:CONF:EDEV:PMAR:FMIN "myDevice", 1e10 system:configure:edevice:pmar:fminumum "myDevice", 3e9 [See example program](../GPIB_Example_Programs/Configure_a_PMAR_Device.md)  
Query Syntax | SYSTem:CONFigure:EDEVice:PMAR:FMAXimum? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CONFigure:EDEVice:PMAR:CFACtors:STATe<name> <bool>

Applicable Models: All (Read-Write) Enables/disables use of internal
calibration factors for power sensors with built-in calibration factors and
reads the current state.  
---  
Parameters |   
<name> | String \- Name of the power meter.  
<bool> | Choose from: 0 - OFF \- Disables the use of internal calibration factors. 1 - ON \- Enables the use of internal calibration factors. [Learn about these settings](../../System/Configure_a_Power_Meter_As_Receiver.md#SensorDiag).  
Examples | ' This example script demonstrates the SCPI set/get of the "Use Internal Cal Factors" property ' for an existing PMAR named 'MyPMAR'. Option Explicit dim app Set app = CreateObject("AgilentPNA835x.Application") dim scpi Set scpi = app.ScpiStringParser Dim opcReply opcReply = scpi.Parse("SYST:PRES;*OPC?") opcReply = scpi.Parse("SENS1:SWE:MODE HOLD;*OPC?") scpi.Parse "SENS1:FREQ:CW 1E9" scpi.Parse "SENS1:SWE:TYPE CW" scpi.Parse "SENS1:SWE:POIN 3" ' Activate the PMAR and change the default trace to measure that PMAR connected to port 3 scpi.Parse "SYST:CONF:EDEV:STAT 'MyPMAR', ON" scpi.Parse "CALC1:PAR:SEL 'CH1_S11_1'" scpi.Parse "CALC1:PAR:MOD:EXT 'MyPMAR,3'" scpi.Parse "CALC1:FUNC:TYPE MEAN" ' Disable use of the sensor's internal cal factors, take a sweep and report the Mean scpi.Parse "SYST:CONF:EDEV:PMAR:CFAC:STAT 'MyPMAR', OFF" scpi.Parse "SYST:CONF:EDEV:IOENable 'MyPMAR', ON" opcReply = scpi.Parse("SENS1:SWE:MODE SING;*OPC?") MsgBox "Use Internal Cal Factors = " & scpi.Parse("SYST:CONF:EDEV:PMAR:CFAC:STAT? 'MyPMAR'") & ", Mean measured val = " & scpi.Parse("CALC1:FUNC:EXEC;DATA?") ' Enable use of the sensor's internal cal factors, take another sweep and report the Mean again scpi.Parse "SYST:CONF:EDEV:IOENable 'MyPMAR', OFF" scpi.Parse "SYST:CONF:EDEV:PMAR:CFAC:STAT 'MyPMAR', ON" scpi.Parse "SYST:CONF:EDEV:IOENable 'MyPMAR', ON" opcReply = scpi.Parse("SENS1:SWE:MODE SING;*OPC?") MsgBox "Use Internal Cal Factors = " & scpi.Parse("SYST:CONF:EDEV:PMAR:CFAC:STAT? 'MyPMAR'") & ", Mean measured val = " & scpi.Parse("CALC1:FUNC:EXEC;DATA?")  
Query Syntax | SYSTem:CONFigure:EDEVice:PMAR:CFACtors:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## SYSTem:CONFigure:EDEVice:PMAR:READing:COUNt <name>,<value>

Applicable Models: All (Read-Write) This command, along with
SYST:CONF:EDEV:PMAR:READ:NTOL, allows for settling of the power sensor
READINGS. Set and return the maximum number of power readings that are taken
at each stimulus point to allow for measurement settling. Each reading is
averaged with the previous readings at that stimulus point. When this average
meets the Average:NTOLerance value or this number of readings has been made,
the average is returned as the valid reading.  
---  
Parameters |   
<name> | String \- Name of the power meter.  
<value> | Number of readings. Choose a value between 1 and 1000  
Examples | SYST:CONF:EDEV:PMAR:READ:COUN "myDevice", 20 system:configure:edevice:pmar:reading:count "myDevice", 10 [See example program](../GPIB_Example_Programs/Configure_a_PMAR_Device.md)  
Query Syntax | SYSTem:CONFigure:EDEVice:PMAR:READing:COUNt? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 3  
  
* * *

## SYSTem:CONFigure:EDEVice:PMAR:READing:NTOLerance <name>,<value>

Applicable Models: All (Read-Write) This command, along with
SYST:CONF:EDEV:PMAR:READ:COUN, allows for settling of the power sensor
READINGS. Each power reading is averaged with the previous readings at each
stimulus point. When the average meets this nominal tolerance value, or the
max number of readings has been made, the average is returned as the valid
reading.  
---  
Parameters |   
<name> | String \- Name of the power meter.  
<value> | Power measurement settling tolerance value in dB. Choose any number between 0 and 5.  
Examples | SYST:CONF:EDEV:PMAR:READ:NTOL "myDevice", .5 system:configure:edevice:pmar:reading:ntolerance "myDevice",.01 [See example program](../GPIB_Example_Programs/Configure_a_PMAR_Device.md)  
Query Syntax | SYSTem:CONFigure:EDEVice:PMAR:READing:NTOLerance? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | .05  
  
* * *

## SYSTem:CONFigure:EDEVice:PMAR:SENSor <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the power sensor channel
(1 or 2) to be used. This performs the same function as the Use this sensor
only checkbox.  
---  
Parameters |   
<name> | String \- Name of the power meter.  
<value> | Power Meter channel. 1 \- Channel A 2 \- Channel B  
Examples | SYST:CONF:EDEV:PMAR:SENS "myDevice",2 system:configure:edevice:pmar:sensor "myDevice",1 [See example program](../GPIB_Example_Programs/Configure_a_PMAR_Device.md)  
Query Syntax | SYSTem:CONFigure:EDEVice:PMAR:SENSor? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## SYSTem:CONFigure:EDEVice:PMAR:SENSor:CATalog? <name>

Applicable Models: All (Read-only) Returns the power sensor channel assignment
of the specified power meter.  
---  
Parameters |   
<name> | String \- Name of the power meter.  
Examples | SYST:CONF:EDEV:PMAR:SENS:CAT? "myDevice" system:configure:edevice:pmar:sensor:catalog? "myDevice"  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## SYSTem:CONFigure:EDEVice:PMAR:TABLe:CFAC:DATA <name>,<value>[,value]

Applicable Models: All (Read-Write) Sets and returns the cal factor data for
the power sensor.  
---  
Parameters |   
<name> | String \- Name of the power meter.  
<value>[,value] | Cal factor data in percent. For each frequency used with SYST:CONF:EDEV:PMAR:TABL:CFAC:FREQ, enter a cal factor number between 1 and 100.  
Examples | SYST:CONF:EDEV:PMAR:TABL:CFAC:DATA "myDevice", 98,99,99 system:configure:edevice:pmar:table:cfac:data "myDevice", 97,97,97 [See example program](../GPIB_Example_Programs/Configure_a_PMAR_Device.md)  
Query Syntax | SYSTem:CONFigure:EDEVice:PMAR:TABLe:CFAC:DATA? <name>  
Return Type | Numeric \- one number per table segment.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CONFigure:EDEVice:PMAR:TABLe:CFAC:FREQuency <name>,<value>[,value]

Applicable Models: All (Read-Write) Sets and returns the cal factor
frequencies for the power sensor.  
---  
Parameters |   
<name> | String \- Name of the power meter.  
<value>[,value] | Cal factor frequencies in Hz.  
Examples | SYST:CONF:EDEV:PMAR:TABL:CFAC:FREQ "myDevice", 1e7,1e8,1e9 system:configure:edevice:pmar:table:cfac:frequency "myDevice", 5e7,5e8,5e9 [See example program](../GPIB_Example_Programs/Configure_a_PMAR_Device.md)  
Query Syntax | SYSTem:CONFigure:EDEVice:PMAR:TABLe:CFAC:FREQuency?<name>  
Return Type | Numeric \- one number per table segment.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CONFigure:EDEVice:PMAR:TABLe:LOSS:DATA <name>,<value>[,value]

Applicable Models: All (Read-Write) Sets and returns the power loss data for
the power sensor. Each table can contain up to 9999 segments. Values can also
be loaded using the Characterize Adapter macro.  
---  
Parameters |   
<name> | String \- Name of the power meter.  
<value>[,value] | Loss data in dB. POSITIVE values in dB are interpreted as LOSS. To compensate for gain, use negative values. For each frequency used with SYST:CONF:EDEV:PMAR:TABL:LOSS:FREQ, enter a cal factor number between 1 and 100.  
Examples | SYST:CONF:EDEV:PMAR:TABL:LOSS:DATA "myDevice",.01,.02,.03 system:configure:edevice:pmar:table:loss:data "myDevice", .04,.05,.06 [See example program](../GPIB_Example_Programs/Configure_a_PMAR_Device.md)  
Query Syntax | SYSTem:CONFigure:EDEVice:PMAR:TABLe:CFAC:DATA? <name>  
Return Type | Numeric \- one number per table segment.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CONFigure:EDEVice:PMAR:TABLe:LOSS:FREQuency <name>,<value>[,value]

Applicable Models: All (Read-Write) Sets and returns frequencies for the power
loss data.  
---  
Parameters |   
<name> | String \- Name of the power meter.  
<value>[,value] | Power Loss frequencies in Hz.  
Examples | SYST:CONF:EDEV:PMAR:TABL:LOSS:FREQ "myDevice",1e7,1e8,1e9 system:configure:edevice:pmar:table:loss:frequency "myDevice",5e7,5e8,5e9 [See example program](../GPIB_Example_Programs/Configure_a_PMAR_Device.md)  
Query Syntax | SYSTem:CONFigure:EDEVice:PMAR:TABLe:LOSS:FREQuency? <name>  
Return Type | Numeric \- one number per table segment.  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CONFigure:EDEVice:PMAR:TABLe:LOSS:STATe <name>,<value>

Applicable Models: All (Read-Write) Sets and returns whether to use the power
loss table.  
---  
Parameters |   
<name> | String \- Name of the power meter.  
<value> | Boolean. State of the power loss table. Choose from: OFF or 0 \- Power loss table not used. ON or 1 \- Power loss table used.  
Examples | SYST:CONF:EDEV:PMAR:TABL:LOSS:STAT "myDevice",1 system:configure:edevice:pmar:table:loss:state "myDevice",1 [See example program](../GPIB_Example_Programs/Configure_a_PMAR_Device.md)  
Query Syntax | SYSTem:CONFigure:EDEVice:PMAR:TABLe:LOSS:STATe? <name>  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SYSTem:CONFigure:EDEVice:PMAR:TABLe:RFACtor <name>,<value>

Applicable Models: All (Read-Write) Sets and returns the reference cal factor
for the power sensor. Note: If the sensor connected to the power meter
contains cal factors in EPROM (such as the Keysight E-series power sensors),
those will be the cal factors used. The reference cal factor value associated
with this command, and any cal factors entered into the VNA for that sensor
channel, will not be used.  
---  
Parameters |   
<name> | String \- Name of the power meter.  
<value> | Reference cal factor in percent. Choose any number between 1 and 150.  
Examples | SYST:CONF:EDEV:PMAR:TABL:RFAC "myDevice", 1 system:configure:edevice:pmar:table:rfactor "myDevice", 1 [See example program](../GPIB_Example_Programs/Configure_a_PMAR_Device.md)  
Query Syntax | SYSTem:CONFigure:EDEVice:PMAR:TABLe:RFACtor? <name>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 100  
  
* * *

## SYSTem:CONFigure:EDEVice:PMAR:UNCertainty:CATalog?

Applicable Models: All (requires Option S93015A) (Read-only) Returns a list of
available power meters that have power uncertainty.  
---  
Parameters |   
<name> | String \- Name of the device used as power meter which has uncertainty data available from the external device list.   
Examples | SYST:CONF:EDEV:PMAR:UNC:CAT?  system:configure:edevice:pmar:uncertainty:catalog?   
Return Type | Comma separated string  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CONFigure:EDEVice:PMAR:UNCertainty:FILE <name>,<FilePath>

Applicable Models: All (requires Option S93015A) (Read-Write) Sets and returns
a custom model uncertainty file containing all of the power meter uncertainty
properties. When this command is executed, the model name is automatically set
to "CustomFile".  
---  
Parameters |   
<name> | String \- Name of the device used as the power meter.  
<FilePath> | Full path to the custom file.  
Examples | SYST:CONF:EDEV:PMAR:UNC:FILE "myDevice","C:\U8485A_MY55140018.dat" system:configure:edevice:pmar:uncertainty:file "myDevice","C:\U8485A_MY55140018.dat"  
Query Syntax | SYSTem:CONFigure:EDEVice:PMAR:UNCertainty:FILE? <name>  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CONFigure:EDEVice:PMAR:UNCertainty:MODel <name>,<PwrMtrModel>

Applicable Models: N522xB, N523xB, N524xB (requires Option S93015A) (Read-
Write) Sets and returns the name assigned to a specific power meter model
among those available for uncertainty (see
SYSTem:CONFigure:EDEVice:PMAR:UNC:CAT?).  
---  
Parameters |   
<name> | String \- Name of the device used as the power meter.  
<PwrMtrModel> | String - Specific power meter model.  
Examples | SYST:CONF:EDEV:PMAR:UNC:MOD "myPowerMeter","N8488A" system:configure:edevice:pmar:uncertainty:model "myPowerMeter","N8488A"  
Query Syntax | SYSTem:CONFigure:EDEVice:PMAR:UNCertainty:MODel? <name>  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CONFigure:EDEVice:PMAR:UNCertainty:PLEVel? <name>

Applicable Models: N522xB, N523xB, N524xB (requires Option S93015A) (Read-
only) Returns the power level associated with the best accuracy for a specific
power meter.  Note: This is typically the level where the calfactor was
obtained.  
---  
Parameters |   
<name> | String \- Name of the device used as the power meter.  
Examples | SYST:CONF:EDEV:PMAR:UNC:PLEV? "myDevice" system:configure:edevice:pmar:uncertainty:plevel? "myDevice"  
Return Type | Double (dBm)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CONFigure:EDEVice:PMAR:UNCertainty:READing?
<name>,<frequency>,<power>

Applicable Models: N522xB, N523xB, N524xB (requires Option S93015A) (Read-
only) Returns the power uncertainty associated with the specific power meter
at the specified frequency and power. The returned value is the variance of
the power expressed in [mW]^2.  
---  
Parameters |   
<name> | String \- Name of the device used as the power meter.  
<frequency> | Frequency (Hz).  
<power> | Power (dBm).  
Examples | SYST:CONF:EDEV:PMAR:UNC:READ? "myDevice",10e9,0.0 system:configure:edevice:pmar:uncertainty:read? "myDevice",10e9,0.0  
Return Type | Double (W^2)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:CONFigure:EDEVice:PMAR:ZERO <name>[,SYNC,<value>]

Applicable Models: All (Write-only) Performs a zeroing of the PMAR device.
This command is always synchronous, so *OPC? is the only way to determine that
the operation is complete. Set an I/O timeout of at least 20 seconds. Keysight
P-Series sensors do ONLY Internal zeroing. These, and Keysight USB power
sensors when Internal is selected, do NOT require disconnecting from the
measurement path before zeroing. All other Keysight sensors do ONLY External
zeroing.  
---  
Parameters |   
<name> | String \- Name of the power meter.  
[,SYNC,<value>] | Optional argument for use with power sensors that support both internal and external types of zeroing such as Keysight USB power sensors. Choose from: SYNC,INTernal \- Internal zeroing. Power is automatically removed from the sensor input before zeroing occurs (Default setting). SYNC,EXTernal \- External zeroing. First remove the sensor input, then send this command. External zeroing is recommended for powers below -30 dBm with the U2000-Series sensors (-20 dBm for the H models).  
Examples | SYST:CONF:EDEV:PMAR:ZERO "myDevice" system:configure:edevice:pmar:zero "myDevice",sync,internal  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

