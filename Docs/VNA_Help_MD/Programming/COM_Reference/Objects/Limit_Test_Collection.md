# Limit Test Collection

* * *

Description

Child of the Measurement Object. A collection that provides a mechanism for
iterating through the Measurement's Limit Segment objects (Limit Lines). The
collection has 100 limit lines by default.

### Accessing the LimitTest collection

Get a handle to an individual limit segment by specifying an item of the
LimitTest collection.

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim limSegs As LimitTest  
Set limSegs = app.ActiveMeasurement.LimitTest  
limSegs.Item(1).BeginStimulus = 1000000000  
limSegs.Item(1).EndStimulus = 1000000000  
limSegs.Item(1).BeginResponse = 3.5  
limSegs.Item(1).EndResponse = 3.5

### See Also:

  * [LimitSegment Object](LimitSegment_Object.md)

  * [Collections in the Analyzer](../../Learning_about_COM/Collections_in_the_Analyzer.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Limit Line Testing Example](../../COM_Example_Programs/Limit_Line_Testing_Example_with_COM.md)

### Methods

|

### Description  
  
---|---  
[GetTestResult](../Methods/Get_Test_Result_Method.md) |  Retrieves the Pass/Fail results of the Limit Test (State).  
[Item](../Methods/Item_Method.md) |  Use to get a handle on a limit line in the collection.  
  
### Properties

|

### Description  
  
[Count](../Properties/Count_Property.md) |  Returns the number of limit lines used in the measurement.  
[LineDisplay](../Properties/LineDisplay_Property.md) |  Displays the limit lines on the screen.  
[SegmentCount](../Properties/LimitTest_SegmentCount.md) |  Returns the number of segments used in a limit test.  
[SoundOnFail](../Properties/SoundOnFail_Property.md) |  Enables a beep on Limit Test fails.  
[State](../Properties/State_Property.md) |  Turns ON and OFF limit testing.  
  
### LimitTest History

Interface |  Introduced with VNA Rev:  
---|---  
ILimitTest |  1.0

