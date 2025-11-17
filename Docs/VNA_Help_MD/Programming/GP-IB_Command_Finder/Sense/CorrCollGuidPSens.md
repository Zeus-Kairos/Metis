# Sense:Correction:Collect:Guided:PSensor Commands

* * *

Configures the power sensors to be used during a SmartCal (Guided) Power
Calibration.

Three of these commands can be used with Applications Channels. [Learn
more](CorrCollGuidPSens.htm#SensorNote).

SENSe:CORRection:COLLect:GUIDed:PSENsor [CKIT](CorrCollGuidPSens.md#PsenCKIT) [CONNector](CorrCollGuidPSens.md#PsensorConn) MULTiple | [ADD](CorrCollGuidPSens.md#MultAdd) | [CKIT](CorrCollGuidPSens.md#MultCKIT) | [CONNector](CorrCollGuidPSens.md#MultConn) | [COUNt?](CorrCollGuidPSens.md#multCount) | IMPort | NAME | [STATe] | FREQuency | [STARt](CorrCollGuidPSens.md#multFreqStart) | [STOP](CorrCollGuidPSens.md#multFreqStop) | [NAME](CorrCollGuidPSens.md#multName) | [REMove](CorrCollGuidPSens.md#multRemove) | [[STATe]](CorrCollGuidPSens.md#multState) POWer | [LEVel](CorrCollGuidPSens.md#PsenPowLevel) [POWTable](CorrCollGuidPSens.md#Powtable) [[STATe]](CorrCollGuidPSens.md#PerformPowerCal)  
---  
  
Click on a keyword to view the command details.

Notes EXCEPT for the following THREE commands, the commands listed on this
page are supported ONLY on standard channels. These can be used with
[Application](../../../Applications/Applications.md) channels. See [NFX
example](../../GPIB_Example_Programs/Create_and_Cal_an_NFX_Measurement.htm).

  * [SENS:CORR:COLL:GUID:PSEN<n>:CKIT](CorrCollGuidPSens.md#PsenCKIT)
  * [SENS:CORR:COLL:GUID:PSEN<n>:CONN](CorrCollGuidPSens.md#PsensorConn)
  * [SENS:CORR:COLL:GUID:PSEN<n>:POW:LEV](CorrCollGuidPSens.md#PsenPowLevel)

When using two sensors with a Dual Power Meter, use
[SOUR:POW:CORR:COLL:<pmChan>SEN:SEL](../SourceCorrection.md#SensorSelect) to
select a power sensor.  
---  
  
### See Also

[SENSe:CORRection:COLLect:GUIDed](CorrGuided.md) commands

[Calibrating the VNA Using
SCPI](../../Learning_about_GPIB/Calibrating_the_Analyzer_Using_SCPI.htm)

[Learn about Measurement
Calibration](../../../S3_Cals/Measurement_Calibration.htm)

[Synchronizing the Analyzer and
Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.htm)

* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:CKIT <kit>, [src]

Applicable Models: All (Read-Write) Specifies the calibration kit to be used
when an adapter is necessary to connect the power sensor to the port <pnum>
during a guided calibration. This command can also be used with [Application
channels](../../../Applications/Applications.htm). See [NFX
example](../../GPIB_Example_Programs/Create_and_Cal_an_NFX_Measurement.htm).
When used with [Guided Power
Cal](../../../S3_Cals/Guided_Power_Calibration.htm), first enable a power cal
using [SENS:CORR:COLL:GUID:PSEN ON](CorrCollGuidPSens.md#PerformPowerCal)

  1. Specify the connector type for the adapter with [SENS:CORR:COLL:GUID:PSEN:CONN](CorrCollGuidPSens.md#PsensorConn)
  2. Query the valid available kits for the connector with [SENS:CORR:COLL:GUID:CKIT:CAT? <conn>](CorrGuided.md#ckitCatConn)
  3. Specify the kit using this command.
  4. Perform a query of this command. If the <kit> parameter was incorrectly entered, an error will be returned.

  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<pnum> |  Source port being calibrated. If unspecified, value is set to 1. For NFX cals, port number must be 1.  
<kit> |  Calibration kit to be used for the specified port. When using an ECal module, include the characterization name in the <kit> string. Use [SENSe:CORR:COLL:GUID:CKIT:CAT?](CorrGuided.md#ckitCatConn) to read the list of characterizations available in the module and in VNA disk memory. If two or more identical ECal modules are connected to the VNA, the serial number must be included to distinguish the ECal modules.  
[src] |  String - (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](../source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../../System/Configure_an_External_Source.md#ExtSourceConfig), [true mode balanced port](../../../Applications/iTMSA.md), or one of the Source outputs on the 2-port VNA-x model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. See [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md)  
Examples |  SENS:CORR:COLL:GUID:PSEN1:CKIT '85055A' 'The following includes a serial number when two or more ECal mods are connected sense:correction:collect:guided:psensor2:ckit '85092-60010 ECal 10685' [See example program](../../GPIB_Example_Programs/Perform_Guided_2-Port_Comprehensive_Cal.md)  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:CKIT?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:CONNector <conn>, [src]

Applicable Models: All (Read-Write) Specifies the connector type for a power sensor when a power calibration is part of the Guided Calibration process. Valid connector names are stored within calibration kits. Some cal kits may include both male and female connectors. Therefore, specifying connector gender may be required. This command can also be used with [Application channels](../../../Applications/Applications.md). See [NFX example](../../GPIB_Example_Programs/Create_and_Cal_an_NFX_Measurement.md). |  Follow these steps to ensure port connectors are specified correctly: When used with [Guided Power Cal](../../../S3_Cals/Guided_Power_Calibration.md), first enable a power cal using [SENS:CORR:COLL:GUID:PSEN ON](CorrCollGuidPSens.md#PerformPowerCal)

  1. Use [SENS:CORR:COLL:GUID:CONN:CAT?](CorrGuided.md#gConnCat) to query available connectors before specifying the port connector.
  2. Set a connector type for each port using this command.
  3. Perform a query of this command. If the connector type was incorrectly entered, an error will be returned.
  4. Specify the cal kit to use for each port with [SENS:CORR:COLL:GUID:PSENsor:CKIT](CorrCollGuidPSens.md#PsenCKIT)

  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<pnum> |  Source port being calibrated. If unspecified, value is set to 1.  
<conn> |  String - Power sensor connector type to connect to the specified VNA port <pnum>. Because the default for this argument is 'Ignored", by specifying a connector type, you imply that you want to calibrate and correct for the effects of the adapter.  
[src] |  String - (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](../source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../../System/Configure_an_External_Source.md#ExtSourceConfig), [true mode balanced port](../../../Applications/iTMSA.md), or one of the Source outputs on the 2-port VNA-x model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. See [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md)  
Examples |  SENS:CORR:COLL:GUID:PSEN1:CONN "3.5 mm (50) male" sense:correction:collect:guided:psensor1:connector "3.5 mm (50) female" [See example program](../../GPIB_Example_Programs/Perform_Guided_2-Port_Comprehensive_Cal.md)  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:CONNector?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  "Ignored"  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:MULTiple:ADD <string>

Applicable Models: All (Write-only) Adds a power sensor to be used during a
Guided Power Calibration. Use when multiple power sensors are to be used to
calibrate the entire frequency span. The Name argument is used to recognize
the sensor in the User Interface. An item number is automatically assigned to
the sensor. Use that number to refer to the sensor. The item number of the
newly-added sensor is always equal to the number returned by
[SENS:CORR:COLL:GUID:PSEN:MULT:COUN?](CorrCollGuidPSens.md#multCount) after
the ADD. Note: The "multiple sensors" commands are supported ONLY on standard
channels. [Learn about using multiple power
sensors](../../../S3_Cals/Guided_Power_Calibration.htm#MultipleSensors)  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<pnum> |  Source port being calibrated. If unspecified, value is set to 1.  
<string> |  Power sensor name to add. The power sensor must be already configured as a PMAR device using this name. [Learn how to remotely configure a PMAR device.](../SystConfigExternalDevice.md)  
Examples |  SENS:CORR:COLL:GUID:PSEN1:MULT:ADD "26GHzPwrSensor" [See example program](../../GPIB_Example_Programs/Perform_a_Guided_Cal_using_Multiple_Power_Sensors.md)  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:MULTiple<id>:CKIT
<string>

Applicable Models: All (Read-Write) Set and read the Cal Kit to be used when
an adapter is necessary to connect the power sensor to the cal plane and you
choose to remove its effects from the measurement. Use this command when
multiple power sensors are to be used to calibrate the entire frequency span.
[Learn about using multiple power
sensors](../../../S3_Cals/Guided_Power_Calibration.htm#MultipleSensors).  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<pnum> |  Source port being calibrated. If unspecified, value is set to 1.  
<id> |  Power sensor item number. This 1-based number is assigned automatically when a power sensor is added using [SENS:CORR:COLL:GUID:PSEN:MULT:ADD](CorrCollGuidPSens.md#MultAdd). Use [SENS:CORR:COLL:GUID:PSEN:MULT:COUN?](CorrCollGuidPSens.md#multCount) to return the number of power sensor items that are configured for use on the channel.  
<string> |  Calibration kit to be used for the specified source port. When using an ECal module, include the characterization name in the <kit> string. Use [SENSe:CORR:COLL:GUID:CKIT:CAT?](CorrGuided.md#ckitCatConn) to read the list of characterizations available in the module and in VNA disk memory. If two or more identical ECal modules are connected to the VNA, the serial number must be included to distinguish the ECal modules.  
Examples |  SENS:CORR:COLL:GUID:PSEN1:MULT2:CKIT '85055A' 'The following includes a serial number when two or more ECal mods are connected. sense:correction:collect:guided:psensor2:multiple1:ckit '85092-60010 ECal 10685' [See example program](../../GPIB_Example_Programs/Perform_a_Guided_Cal_using_Multiple_Power_Sensors.md)  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:MULTiple<id>:CKIT?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:MULTiple<id>:CONNector
<conn>

Applicable Models: All (Read-Write) Set and read the connector type of a power
sensor to be used when an adapter is necessary to connect the power sensor to
the cal plane and you choose to remove its effects from the measurement. Use
this command when multiple power sensors are to be used to calibrate the
entire frequency span. [Learn about using multiple power
sensors](../../../S3_Cals/Guided_Power_Calibration.htm#MultipleSensors)  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<pnum> |  Source port being calibrated. If unspecified, value is set to 1.  
<id> |  Power sensor item number. This 1-based number is assigned automatically when a power sensor is added using [SENS:CORR:COLL:GUID:PSEN:MULT:ADD](CorrCollGuidPSens.md#MultAdd). Use [SENS:CORR:COLL:GUID:PSEN:MULT:COUN?](CorrCollGuidPSens.md#multCount) to return the number of power sensor items that are configured for use on the channel.  
<conn> |  String - Power sensor connector type to connect to the specified source port <pnum>. Because the default for this argument is 'Ignored", by specifying a connector type, you imply that you want to calibrate and correct for the effects of the adapter.  
Examples |  SENS:CORR:COLL:GUID:PSEN1:MULT1:CONN "3.5 mm (50) male" [See example program](../../GPIB_Example_Programs/Perform_a_Guided_Cal_using_Multiple_Power_Sensors.md)  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:MULTiple<id>:CONNector?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  "Ignored"  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:MULTiple:COUNt?

Applicable Models: All (Read-only) Returns the number of configured power
sensors to be used during a Guided Power Calibration. [Learn about using
multiple power
sensors](../../../S3_Cals/Guided_Power_Calibration.htm#MultipleSensors)  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<pnum> |  Source port being calibrated. If unspecified, value is set to 1.  
Examples |  SENS:CORR:COLL:GUID:PSEN1:MULT1:COUN? [See example program](../../GPIB_Example_Programs/Perform_a_Guided_Cal_using_Multiple_Power_Sensors.md)  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

##
SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:MULTiple<id>:FREQuency:STARt
<num>

Applicable Models: All (Read-Write) Set and read the start frequency for the
specified power sensor (port number). Use this command when multiple power
sensors are to be used to calibrate the entire frequency span. [Learn about
using multiple power
sensors](../../../S3_Cals/Guided_Power_Calibration.htm#MultipleSensors)  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<pnum> |  Source port being calibrated. If unspecified, value is set to 1.  
<id> |  Power sensor item number. This 1-based number is assigned automatically when a power sensor is added using [SENS:CORR:COLL:GUID:PSEN:MULT:ADD](CorrCollGuidPSens.md#MultAdd). Use [SENS:CORR:COLL:GUID:PSEN:MULT:COUN?](CorrCollGuidPSens.md#multCount) to return the number of power sensor items that are configured for use on the channel.  
<num> |  Start frequency in Hz. Choose a value between the start frequency and stop frequency of the VNA.  
Examples |  SENS:CORR:COLL:GUID:PSEN1:MULT1:FREQ:STAR 1e9 [See example program](../../GPIB_Example_Programs/Perform_a_Guided_Cal_using_Multiple_Power_Sensors.md)  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:MULTiple<id>:FREQuency:STARt?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Start frequency of the VNA  
  
* * *

##
SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:MULTiple<id>:FREQuency:STOP
<num>

Applicable Models: All (Read-Write) Set and read the stop frequency for the
specified power sensor (port number). Use this command when multiple power
sensors are to be used to calibrate the entire frequency span. [Learn about
using multiple power
sensors](../../../S3_Cals/Guided_Power_Calibration.htm#MultipleSensors)  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<pnum> |  Source port being calibrated. If unspecified, value is set to 1.  
<id> |  Power sensor item number. This 1-based number is assigned automatically when a power sensor is added using [SENS:CORR:COLL:GUID:PSEN:MULT:ADD](CorrCollGuidPSens.md#MultAdd). Use [SENS:CORR:COLL:GUID:PSEN:MULT:COUN?](CorrCollGuidPSens.md#multCount) to return the number of power sensor items that are configured for use on the channel.  
<num> |  Stop frequency in Hz. Choose a value between the start frequency and stop frequency of the VNA.  
Examples |  SENS:CORR:COLL:GUID:PSEN1:MULT1:FREQ:STOP 2e9 [See example program](../../GPIB_Example_Programs/Perform_a_Guided_Cal_using_Multiple_Power_Sensors.md)  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:MULTiple<id>:FREQuency:STOP?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Stop frequency of the VNA  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:MULTiple<id>:IMPort:NAME
<string>

Applicable Models: All (Read-Write) Controls the calset name.  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<pnum> |  Source port being calibrated. If unspecified, value is set to 1.  
<id> |  Power sensor item number. This 1-based number is assigned automatically when a power sensor is added using SENS:CORR:COLL:GUID:PSEN:MULT:ADD. Use SENS:CORR:COLL:GUID:PSEN:MULT:COUN? to return the number of power sensor items that are configured for use on the channel.  
<string> |  Calset name.  
Examples |  SENS:CORR:COLL:GUID:PSEN1:MULT1:IMP:NAME "calset1"  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:MULTiple<id>:IMPort:NAME?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |   
  
* * *

##
SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:MULTiple<id>:IMPort[:STATe]
<bool>

Applicable Models: All (Read-Write) Controls the import flag of the power
sensor. Must be set before setting the calset name with
SENSe:CORRection:COLLect:GUIDed:PSENsor:MULTiple:IMPort:NAME.  Will return
'false' until the calset name is set with
SENSe:CORRection:COLLect:GUIDed:PSENsor:MULTiple:IMPort:NAME. **NOTE:** When
the import flag is set to true, the command
SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:MULTiple<id>:NAME returns an
empty string.  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<pnum> |  Source port being calibrated. If unspecified, value is set to 1.  
<id> |  Power sensor item number. This 1-based number is assigned automatically when a power sensor is added using SENS:CORR:COLL:GUID:PSEN:MULT:ADD. Use SENS:CORR:COLL:GUID:PSEN:MULT:COUN? to return the number of power sensor items that are configured for use on the channel.  
<bool> |  Boolean ON (or 1) Enable the import flag OFF (or 0) Disable the import flag  
Examples |  SENS:CORR:COLL:GUID:PSEN1:MULT1:IMP:STAT 1  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:MULTiple<id>:IMPort:STATe?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:MULTiple<id>:NAME
<string>

Applicable Models: All (Read-Write) Set and read the name of the power sensor.
[Learn about using multiple power
sensors](../../../S3_Cals/Guided_Power_Calibration.htm#MultipleSensors).  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<pnum> |  Source port being calibrated. If unspecified, value is set to 1.  
<id> |  Power sensor item number. This 1-based number is assigned automatically when a power sensor is added using [SENS:CORR:COLL:GUID:PSEN:MULT:ADD](CorrCollGuidPSens.md#MultAdd). Use [SENS:CORR:COLL:GUID:PSEN:MULT:COUN?](CorrCollGuidPSens.md#multCount) to return the number of power sensor items that are configured for use on the channel.  
<string> |  Sensor name. The power sensor must be already configured as a PMAR device using this name. [Learn how to remotely configure a PMAR device.](../SystConfigExternalDevice.md)  
Examples |  SENS:CORR:COLL:GUID:PSEN1:MULT1:NAME "26GHzPwrSensor" [See example program](../../GPIB_Example_Programs/Perform_a_Guided_Cal_using_Multiple_Power_Sensors.md)  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:MULTiple<id>:NAME?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |   
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:MULTiple<id>:REMove

Applicable Models: All (Write-only) Deletes a power sensor from the sensors to
be used during a Guided Power Calibration.  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<pnum> |  Source port being calibrated. If unspecified, value is set to 1.  
<id> |  Power sensor item number to remove. Use [SENS:CORR:COLL:GUID:PSEN:MULT:COUN?](CorrCollGuidPSens.md#multCount) to return the number of power sensor items that are configured for use on the channel.  
Examples |  SENS:CORR:COLL:GUID:PSEN1:MULT1:REM [See example program](../../GPIB_Example_Programs/Perform_a_Guided_Cal_using_Multiple_Power_Sensors.md)  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:MULTiple[:STATe] <value>

Applicable Models: All (Read-Write) Enables the use of multiple power sensors
to calibrate the entire frequency span of the channel. [Learn about using
multiple power
sensors](../../../S3_Cals/Guided_Power_Calibration.htm#MultipleSensors).  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<pnum> |  Source port being calibrated. If unspecified, value is set to 1. ONLY one port may be calibrated with a Guided Power Cal.  
<value> |  Boolean ON (or 1) Use multiple power sensors. OFF (or 0) Do NOT use multiple power sensors.  
Examples |  SENS:CORR:COLL:GUID:PSEN1:MULT 0 sense:correction:collect:guided:psensor2:multiple:state ON [See example program](../../GPIB_Example_Programs/Perform_a_Guided_Cal_using_Multiple_Power_Sensors.md)  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:MULTiple[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF (0)  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:POWer:LEVel <value>,
[src]

Applicable Models: All (Read-Write) Specifies the power level at which to
perform a power calibration during a guided calibration. This command can also
be used with [Application channels](../../../Applications/Applications.md).
See [NFX
example](../../GPIB_Example_Programs/Create_and_Cal_an_NFX_Measurement.htm).
When used with [Guided Power
Cal](../../../S3_Cals/Guided_Power_Calibration.htm), first enable a power cal
using [SENS:CORR:COLL:GUID:PSEN ON](CorrCollGuidPSens.md#PerformPowerCal).  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<pnum> |  Source port being calibrated. If unspecified, value is set to 1. For NFX cals, port number must be 1.  
<value> |  Power level in dBm at which to perform the power calibration. [Learn more.](../../../Applications/Noise_Cal.md#CalPowerLevel)  
[src] |  String - (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](../source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../../System/Configure_an_External_Source.md#ExtSourceConfig), [true mode balanced port](../../../Applications/iTMSA.md), or one of the Source outputs on the 2-port VNA-x model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. See [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md)  
Examples |  SENS:CORR:COLL:GUID:PSEN1:POW:LEV 0 sense:correction:collect:guided:psensor2:power:level -5 Setting calibration power for Gain Compression Converters (GCX) SENS:CORR:COLL:GUID:PSEN1:POW:LEV -21 'Sets the cal power over the input frequencies where port 1 is the input of the mixer SENS:CORR:COLL:GUID:PSEN2:POW:LEV -6 'Sets the cal power over the output frequencies where port 2 is the output of the mixer [See example program](../../GPIB_Example_Programs/Perform_Guided_2-Port_Comprehensive_Cal.md)  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:POWer:LEVel?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:POWTable <file>, [src]

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Loads a file that
defines a power table to be used during a SMC Guided Power Cal or Cal All
Channels on a mmWave system. This feature is available because power sensors
are NOT typically available at mmWave frequencies. [Learn
more](../../../IFAccess/External_Test_Head_Configuration.htm#SMCPowerProcess).  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<pnum> |  Source port being calibrated. If unspecified, value is set to 1. For NFX cals, port number must be 1.  
<file> |  (String) Full path and filename of a *.prn file that defines the power table. An error is returned if the file is not found.  
[src] |  String - (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](../source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../../System/Configure_an_External_Source.md#ExtSourceConfig), [true mode balanced port](../../../Applications/iTMSA.md), or one of the Source outputs on the 2-port VNA-x model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. See [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md)  
Examples |  SENS:CORR:COLL:GUID:PSEN1:POWT "C:/powertable1.prn" sense:correction:collect:guided:psensor2:powtable "C:/powertable2.prn"  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>:POWTable?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>[:STATe] <value>, [src]

Applicable Models: All (Read-Write) Enables [Guided Power
Cal](../../../S3_Cals/Guided_Power_Calibration.htm) and sets the source port
to be calibrated.  
---  
Parameters |   
<ch> |  Channel being calibrated, depending on the [CHAN:MODE](CorrGuided.md#ChanMode) setting. If unspecified, value is set to 1.  
<pnum> |  Source port being calibrated. If unspecified, value is set to 1. ONLY one port may be calibrated with a Guided Power Cal.  
<value> |  Boolean ON (or 1) Perform Power Cal. OFF (or 0) Do NOT perform Power Cal.  
[src] |  String - (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](../source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../../System/Configure_an_External_Source.md#ExtSourceConfig), [true mode balanced port](../../../Applications/iTMSA.md), or one of the Source outputs on the 2-port VNA-x model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority. See [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md)  
Examples |  SENS:CORR:COLL:GUID:PSEN1 0 sense:correction:collect:guided:psensor2:state ON [See example program](../../GPIB_Example_Programs/Perform_Guided_2-Port_Comprehensive_Cal.md)  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:PSENsor<pnum>[:STATe]?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF (0)  
  
* * *

