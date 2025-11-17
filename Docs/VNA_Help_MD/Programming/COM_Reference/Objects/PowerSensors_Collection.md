# PowerSensors Collection

* * *

Description

A collection object that provides a mechanism for iterating through the
PowerSensor objects which are connected to the power meter. Each time this
collection object is accessed, the power meter is queried to determine how
many sensors are connected to it. The collection size and order of objects is
then adjusted accordingly before the requested method or property operation is
performed. The power meter is specified by using the
[PowerMeterGPIBAddress](../Properties/PowerMeterGPIBAddress_Property.md)
property of the [SourcePowerCalibrator](SourcePowerCalibrator_Object.md)
object.

### Accessing the PowerSensors Collection

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim PwrSensors As PowerSensors  
Set PwrSensors = app.SourcePowerCalibrator.PowerSensors

### See Also:

  * [PowerSensor Object](PowerSensor_Object.md)

  * [Collections in the Analyzer](../../Learning_about_COM/Collections_in_the_Analyzer.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Description  
  
---|---  
[Item](../Methods/Item_Method.md) |  Use to get a handle to a PowerSensor object in the collection.  
  
### Properties

|

### Description  
  
[Count](../Properties/Count_Property.md) |  Returns the number of objects in the collection.  
[Parent](../Properties/Parent_Property.md) |  Returns a handle to the Parent object ([SourcePowerCalibrator](SourcePowerCalibrator_Object.md)) of this collection.  
  
* * *

