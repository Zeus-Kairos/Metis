# Measurement Collection

* * *

### Description

A collection object that provides a mechanism for iterating through the
Application measurements.

### Accessing the Measurements collection

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim measments As Measurements  
Set measments = app.Measurements

### See Also:

  * [Measurement Object](Measurement_Object.md)

  * [Collections in the Analyzer](../../Learning_about_COM/Collections_in_the_Analyzer.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Description  
  
---|---  
[Add](../Methods/Add_measurement_Method.md) |  Adds a Measurement to the collection.  
[Item](../Methods/Item_Method.md) |  Use to get a handle on a measurement in the collection.  
[Remove](../Methods/Remove_Method.md) |  Removes a measurement from the measurements collection.  
  
### Properties

|

### Description  
  
[Count](../Properties/Count_Property.md) |  Returns the number of measurements in the analyzer.  
[Parent](../Properties/Parent_Property.md) |  Returns a handle to the current Application.

