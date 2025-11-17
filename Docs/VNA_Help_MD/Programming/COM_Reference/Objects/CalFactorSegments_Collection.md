# CalFactorSegments Collection

* * *

Description

A collection object that provides a mechanism for iterating through the
segments of a power sensor cal factor table. The Cal Factor table can contain
up to 100 segments.

### Accessing the CalFactorSegments collection

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim calFact As CalFactorSegments  
Set calFact = app.SourcePowerCalibrator.PowerSensors(1).CalFactorSegments

### See Also:

  * [PowerSensorCalFactorSegment Object](PowerSensorCalFactorSegment_Object.md)

  * [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)

  * [Collections in the Analyzer](../../Learning_about_COM/Collections_in_the_Analyzer.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Description  
  
---|---  
[Add](../Methods/Add_PowerSensorCalFactorSegment_Method.md) |  Adds a PowerSensorCalFactorSegment object to the collection  
[Item](../Methods/Item_Method.md) |  Use to get a handle to a PowerSensorCalFactorSegment object in the collection.  
[Remove](../Methods/Remove_Method.md) |  Removes an object from the collection.  
  
### Properties

|

### Description  
  
[Count](../Properties/Count_Property.md) |  Returns the number of objects in the collection.  
[Parent](../Properties/Parent_Property.md) |  Returns a handle to the Parent object ([PowerSensor](PowerSensor_Object.md)) of this collection.

