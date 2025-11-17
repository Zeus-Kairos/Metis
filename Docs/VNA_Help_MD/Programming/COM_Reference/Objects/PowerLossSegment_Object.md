# PowerLossSegment Object

* * *

### Description

Contains the properties describing a segment of the power loss table used in
source power calibration.

You can get a handle to one of these segments through the
[segments.Item](../Methods/Item_Method.md) Method of the PowerLossSegments
collection.

### Accessing the PowerLossSegment object

You can get a handle to one of these segments through
PowerLossSegments.Item(n)

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim PwrLossSeg As PowerLossSegment  
Set PwrLossSeg = app.SourcePowerCalibrator.PowerLossSegments(1)

### See Also:

  * [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

##  
  
---|---  
None |   
  
### Properties

|

### Description  
  
[Frequency](../Properties/Frequency_Property.md) |  The frequency (Hz) associated with this segment.  
[Loss](../Properties/Loss_sourceCal_Property.md) |  The loss value (dB) associated with this segment.  
[SegmentNumber](../Properties/Segment_Number_Property.md) |  Returns the number of this segment  
  
###  IPowerLossSegment History

Interface |  Introduced with VNA Rev:  
---|---  
IPowerLossSegment |  2.0

