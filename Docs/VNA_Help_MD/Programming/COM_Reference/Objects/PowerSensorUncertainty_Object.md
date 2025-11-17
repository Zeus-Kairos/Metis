# PowerSensorUncertainty Object

* * *

Description

The PowerSensorUncertainty object allows you to set up power uncertainty on a
power meter.

### Accessing the PowrSensorUncertainty Object

You can obtain a handle to a PowerSensorUncertainty object through the
PowerSensor object.

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim PwrSensUncert As PowerSensorUncertainty  
Set PwrSensUncert = app.PowerSensor.PowerSensorUncertainty  
---  
  
### See Also

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Interface

|

### Description  
  
---|---|---  
None |  |   
  
### Properties

|

### Interface

|

### Description  
  
[PowerForBestAccuracy](../Properties/PowerForBestAccuracy_Property.md) | IPowerSensorUncertainty | Returns the power level for best accuracy.  
[PowerMtrReadingUncertainty](../Properties/PowerMtrReadingUncertainty_Property.md) | IPowerSensorUncertainty | Returns the power meter reading uncertainty.  
[UncertaintyFile](../Properties/UncertaintyFile_Property.md) | IPowerSensorUncertainty | Sets and returns a custom model uncertainty file containing all of the power meter uncertainty properties.  
[UncertaintyModel](../Properties/UncertaintyModel_Property.md) | IPowerSensorUncertainty | Sets and returns the name assigned to a specific power meter model among those available for uncertainty.  
[UncertaintyModelCatalog](../Properties/UncertaintyModelCatalog_Property.md) | IPowerSensorUncertainty | Returns a list of available power meters that have power uncertainty.  
  
###  IPowerSensor History

Interface | Introduced with VNA Rev:  
---|---  
IPowerSensorUncertainty | 13.50  
|

