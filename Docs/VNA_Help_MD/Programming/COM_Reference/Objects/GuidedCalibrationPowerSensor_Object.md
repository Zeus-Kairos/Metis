# GuidedCalibrationPowerSensor Object

* * *

### Description

Contains the methods and properties to configure multiple power sensors to be
used during a guided power calibration.

Note: These commands are supported ONLY on standard channels.

### Accessing the GuidedCalibrationPowerSensor Object

A GuidedCalibrationPowerSensor object is accessed as an item of the
[GuidedCalibrationPowerSensors
Collection](GuidedCalibrationPowerSensors_Collection.htm).

Option explicit Dim app as AgilentPNA835x.Application Set app =
CreateObject("AgilentPNA835x.Application") Dim CalMgr Set CalMgr =
App.GetCalManager Dim guidedCal Set guidedCal = CalMgr.GuidedCalibration Dim
powerSensors Dim port: port = 1 Set powerSensors =
guidedCal.GuidedCalibrationPowerSensors(port) Dim powerSensor2 Set
powerSensor2 = GuidedCalibrationPowerSensors.Item(2)
powerSensor2.Name="26GHzSensor"  
---  
  
### See Also:

  * [GuidedCalibrationPowerSensors Collection](GuidedCalibrationPowerSensors_Collection.md)

  * See Example Programs

  *     * [Perform a Guided Power Cal using Multiple Power Sensors](../../COM_Example_Programs/Perform_a_Guided_Power_Cal_using_Multiple_Power_Sensors.md)

    * [Create a PMAR Device and Measurement](../../COM_Example_Programs/Create_a_PMAR_Device_and_Measurement.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

### Methods

|

###

|

### Description  
  
---|---|---  
None |  |   
  
### Properties

|

### Interface

[See History](IIFConfiguration_Object.md#history) | 

### Description  
  
[Name](../Properties/Name_PowerSensor_Property.md) |  IGuidedCalibrationPowerSensors |  Sets and returns the name of this power sensor.  
[PowerSensorCalKitType](../Properties/PowerSensorCalKitType_Property.md) |  IGuidedCalibrationPowerSensors |  Set and read the cal kit to be used for calibrating at the reference plane.  
[PowerSensorConnectorType](../Properties/PowerSensorConnectorType_Property.md) |  IGuidedCalibrationPowerSensors |  Sets or returns the connector type of the power sensor  
[StartFrequency](../Properties/Start_Frequency_Property.md) |  IGuidedCalibrationPowerSensors |  Sets or returns the start frequency of the power sensor coverage  
[StopFrequency](../Properties/Stop_Frequency_Property.md) |  IGuidedCalibrationPowerSensors |  Sets or returns the stop frequency of the power sensor coverage  
  
###  IGuidedCalibrationPowerSensors History

Interface |  Introduced with VNA Rev:  
---|---  
IGuidedCalibrationPowerSensors |  9.33  
  
* * *

