# PowerSensorCalFactorSegment Object

* * *

Description

Contains the properties describing a segment of a power sensor cal factor
table.

### Accessing the PowerSensorCalFactorSegment object

You can get a handle to one of these segments through
[CalFactorSegments](CalFactorSegments_Collection.md).Item(n)

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim calFactSeg As CalFactorSegments  
Set calFactSeg =
app.SourcePowerCalibrator.PowerSensors(1).CalFactorSegments(1)

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|  
---|---  
None |   
  
### Properties

|

### Description  
  
[Frequency](../Properties/Frequency_Property.md) |  The frequency (Hz) associated with this segment. Shared with the PowerLossSegment Object  
[CalFactor](../Properties/CalFactor_Property.md) |  The cal factor (%) associated with this segment.  
[SegmentNumber](../Properties/Segment_Number_Property.md) |  Returns the number of this segment. Shared with the PowerLossSegment Object  
  
###  IPowerSensorCalFactorSegment History

Interface |  Introduced with VNA Rev:  
---|---  
IPowerSensorCalFactorSegment |  2.0

