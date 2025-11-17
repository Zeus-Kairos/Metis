# GuidedCalibrationPowerSensors Collection

* * *

### Description

Contains the methods and properties to enable and configure multiple power
sensors to be used during a guided calibration.

Note: Guided Power Cal, and "multiple sensors" are allowed ONLY on standard
channels.

### Accessing the GuidedCalibrationPowerSensors Collection

Option explicit Dim app as AgilentPNA835x.Application Set app =
CreateObject("AgilentPNA835x.Application") Dim CalMgr Set CalMgr =
App.GetCalManager Dim guidedCal Set guidedCal = CalMgr.GuidedCalibration Dim
port: port = 1 Dim powerSensors Set powerSensors =
guidedCal.GuidedCalibrationPowerSensors(port) powerSensors = powerSensors.Add
"26GHzPowerSensor"  
---  
  
### See Also:

  * [GuidedCalibrationPowerSensor Object](GuidedCalibrationPowerSensor_Object.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [See Example Program](../../COM_Example_Programs/Perform_a_Guided_Power_Cal_using_Multiple_Power_Sensors.md)

### Methods

|

###

|

### Description  
  
---|---|---  
[Add](../Methods/Add_GuidedPowerSensors_Method.md) |  IGuidedCalibrationPowerSensors |  Add a power sensor by name to the collection.  
[Item](../Methods/Item_Method.md) |  IGuidedCalibrationPowerSensors |  Specify a power sensor by name in the collection.  
[Remove](../Methods/Remove_Method.md) |  IGuidedCalibrationPowerSensors |  Remove a power sensor from the collection.  
  
### Properties

|

### Interface

[See History](IIFConfiguration_Object.md#history) | 

### Description  
  
[Count](../Properties/Count_Property.md) |  IGuidedCalibrationPowerSensors |  Return the number of power sensors in the collection.  
[UseMultipleSensors](../Properties/UseMultipleSensors_Property.md) |  IGuidedCalibrationPowerSensors |  Enable the use of multiple power sensors.  
  
###  IGuidedCalibrationPowerSensors History

Interface |  Introduced with VNA Rev:  
---|---  
IGuidedCalibrationPowerSensors |  9.33  
  
* * *

