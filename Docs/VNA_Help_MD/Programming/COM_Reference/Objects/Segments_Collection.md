# Segments Collection

* * *

### Description

The segment collection provides a mechanism for iterating through the sweep
segments of a channel. Sweep segments are a potentially faster method of
sweeping the analyzer through only the frequencies of interest. Learn more
about [Segment Sweep](../../../S1_Settings/Sweep.md#segment).

### Accessing the Segments collection

There are two paths to the Segments Collection:

  1. From the [Channel](Channel_Object.md) object

  2. From the [FOMRange](FOMRange_Object.md) object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim segs As ISegments  
Set segs = app.ActiveChannel.Segments

or

Set segs = app.ActiveChannel.FOM.FOMRange(1).Segments

### See Also:

  * [Segment Object](Segment_Object.md) to learn how to set the properties for individual segments.

  * [Collections in the Analyzer](../../Learning_about_COM/Collections_in_the_Analyzer.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Interface

[See History](Segments_Collection.md#history) | 

### Description  
  
---|---|---  
[Add](../Methods/Add_segments_Method.md) | ISegments | Adds an item to either the Segments collection.  
[ExportCSVfile](../Methods/ExportCSVfile_Method.md) | ISegments6 | Export CSV file  
[GetAllSegments](../Methods/GetAllSegments_Method.md) | ISegments5 | Downloads a segment table from the VNA  
[ImportCSVfile](../Methods/ImportCSVfile_Method.md) | ISegments6 | Import CSV file  
[Item](../Methods/Item_Method.md) | ISegments | Use to get a handle to a segment in the collection..  
[Remove](../Methods/Remove_Method.md) | ISegments | Removes an item from a collection of objects.  
[SetAllSegments](../Methods/SetAllSegments_Method.md) | ISegments2 | Uploads a segment table to the VNA.  
  
### Properties

|

###

|

### Description  
  
[AllowArbitrarySegments](../Properties/AllowArbitrarySegments_Property.md) | ISegments3 | Enables the setup of arbitrary segment sweep  
[Count](../Properties/Count_Property.md) | ISegments | Returns the number of items in a collection of objects.  
[DelayOption](../Properties/DelayOption_Property.md) | ISegments6 | Enables delay.  
[IFBandwidthOption](../Properties/IF_Bandwidth_Option_Property.md) | ISegments | Enables the IFBandwidth to be set on individual sweep segments.  
[NoiseFigureBWOption](../Properties/NoiseFigureBWOption_Property.md) | ISegments7 | Enables noise figure bandwidth setting.  
[Parent](../Properties/Parent_Property.md) | ISegments | Returns a handle to the current naNetworkAnalyzer application..  
[PortIFBandwidthOption](../Properties/PortIFBandwidthOption_Property.md) | ISegments6 | Enables port IF bandwidth.  
[SADataThresholdOption](../Properties/SADataThresholdOption_Property.md) | ISegments8 | Specifies whether SA Data Threshold can be set independently for each segment.  
[SAMTReferenceFreqOption](../Properties/SAMTReferenceFreqOption_Property.md) | ISegments7 | Specifies whether SA Reference Tone can be set independently for each segment.  
[SAVectorAverageOption](../Properties/SAVectorAverageOption_Property.md) | ISegments7 | Specifies whether SA Vector Averaging can be set independently for each segment.  
[SAVideoAverageOption](../Properties/SAVectorAverageOption_Property.md) | ISegments8 | Specifies whether SA Video Bandwidth can be set independently for each segment.  
[ShiftLOOption](../Properties/ShiftLOOption_Property.md) | ISegments6 | Sets or returns the Shift LO state of each segment in the segment sweep table.  
[SourcePowerOption](../Properties/Source_Power_Option_Property.md) | ISegments | Enables setting the Source Power for a segment.  
[SweepModeOption](../Properties/SweepModeOption_Property.md) | ISegments6 | Enables analog or stepped sweep mode.  
[SweepTimeOption](../Properties/SweepTimeOption_Property.md) | ISegments4 | Enables the [Sweep time](../Properties/Sweep_Time_Property.md) or [Dwell time](../Properties/Dwell_Time_Property.md) to be set independently on sweep segments.  
  
###  ISegments History

Interface | Introduced with VNA Rev:  
---|---  
ISegments | 1.0  
ISegments2 | 3.5  
ISegments3 | 4.2  
ISegments4 | 7.1  
ISegments5 | 8.6  
ISegments6 | 12.85  
ISegments7 | 13.50  
ISegments8 | 13.50  
  
* * *

