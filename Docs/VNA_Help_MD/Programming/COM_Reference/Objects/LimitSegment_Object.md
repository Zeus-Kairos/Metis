# LimitSegment Object

* * *

Description

The LimitSegment object is an individual limit line.

### Accessing the LimitSegment object

Get a handle to an individual limit line by using the LimitTest collection.

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim limSegs As LimitTest  
Set limSegs = app.ActiveMeasurement.LimitTest  
limSegs(1).BeginResponse = 1000000000#

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Description  
  
---|---  
None |   
  
### Properties

|

### Description  
  
[BeginResponse](../Properties/Begin_Response_Property.md) |  Specifies the Y-axis value that corresponds with Begin Stimulus (X-axis) value.  
[BeginStimulus](../Properties/Begin_Stimulus_Property.md) |  Specifies the beginning X-axis value of the Limit Line.  
[EndResponse](../Properties/End_Response_Property.md) |  Specifies the Y-axis value that corresponds with End Stimulus (X-axis) value.  
[EndStimulus](../Properties/End_Stimulus_Value.md) |  Specifies the End X-axis value of the Limit Line.  
[Type](../Properties/Type_limit_Property.md) |  Specifies the Limit Line type.  
  
### LimitSegment History

Interface |  Introduced with VNA Rev:  
---|---  
ILimitSegment |  1.0

