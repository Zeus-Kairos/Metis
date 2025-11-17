# IndependentPowerCalibration Object

* * *

### Description

Contains the methods and properties used to perform an independent power
calibration.

### Accessing the IndependentPowerCalibration object

For standard S-parameter channels:

Dim app as AgilentPNA835x.Application  
Dim CalMgr  
Set CalMgr = App.GetCalManager  
Dim CalAll  
Set CalAll = CalMgr.CalibrateAllChannels  
  
Dim IndependentPwrCal  
Set IndependentPwrCal = CalAll.IndependentPowerCalibration

To calibrate an [Application](../../../Applications/Applications.md) channel,
see [CreateCustomCalEx](../Methods/CreateCustomCalEx_Method.md) Method.

### See Also:

  * [PNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The PNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

###

|

### Description  
  
---|---|---  
[Item](../Methods/Item_\(IndependentPowerCalibrationPort\)_Method.md) | IIndependentPowerCalibration | Use to get a handle to a IndependentPowerCalibrationPort object.  
  
### Properties

|

### Interface

[See History](IIFConfiguration_Object.md#history) | 

### Description  
  
[ValidPorts](../Properties/ValidPorts.md) | IIndependentPowerCalibration | Queries available ports for independent power calibration.  
  
###  IIndependentPowerCalibration History

Interface | Introduced with PNA Rev:  
---|---  
IIndependentPowerCalibration | 10.60  
  
* * *

