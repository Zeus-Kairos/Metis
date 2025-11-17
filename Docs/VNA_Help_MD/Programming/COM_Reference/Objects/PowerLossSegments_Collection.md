# PowerLossSegments Collection

* * *

### Description

A collection object that provides a mechanism for iterating through the
segments of the power loss table used in source power calibration. The power
loss table can contain up to 9999 segments.

### Accessing the PowerLossSegments collection

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim PwrLossSegs As PowerLossSegments  
Set PwrLossSegs = app.SourcePowerCalibrator.PowerLossSegments

See Also:

  * [PowerLossSegment Object](PowerLossSegment_Object.md)

  * [Collections in the Analyzer](../../Learning_about_COM/Collections_in_the_Analyzer.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Description  
  
---|---  
[Add](../Methods/Add_PowerLossSegment_Method.md) |  Adds a PowerLossSegment object to the collection.  
[Item](../Methods/Item_Method.md) |  Use to get a handle to a PowerLossSegment object in the collection.  
[Remove](../Methods/Remove_Method.md) |  Removes an object from the collection.  
  
### Properties

|

### Description  
  
[Count](../Properties/Count_Property.md) |  Returns the number of objects in the collection.  
[Parent](../Properties/Parent_Property.md) |  Returns a handle to the Parent object (SourcePowerCalibrator) of this collection.  
  
* * *

