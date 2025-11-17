# Segment Object

* * *

### Description

Contains the methods and properties that affect a sweep segment.

Note: All of these properties are shared with at least one of the following
objects: Channel, Cal Set, PowerSensorCalFactorSegment, or PowerLossSegment.

### Accessing a Segment object and setting Segment Properties

You can get a handle to a sweep segment through the segments collection.

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim segs As ISegments  
Set segs = app.ActiveChannel.Segments  
  
segs.Add(1)  
segs(1).NumberOfPoints = 30

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Segment Sweep](../../../S1_Settings/Sweep.md#segment)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|  |   
---|---|---  
None |  |   
  
### Properties

|

### Interface

|

### Description  
  
[centerFrequency](../Properties/CenterFreq_Property.md) | ISegment | Sets or returns the center frequency of the segment. Shared with the Channel Object  
[Delay](../Properties/Delay_\(Segment_Sweep\)_Property.md) | ISegment3 | Sets or returns the delay value.  
[DwellTime](../Properties/Dwell_Time_Property.md) | ISegment | Dwell time value. Shared with the Channel Object  
[FrequencySpan](../Properties/Frequency_Span_Property.md) | ISegment | Sets or returns the frequency span of the segment. Shared with the Channel Object  
[IFBandwidth](../Properties/IF_Bandwidth_Property.md) | ISegment | Sets or returns the IF Bandwidth of the segment. Shared with the Channel Object and Cal Set object.  
[NoiseFigureBW](../Properties/NoiseFigureBW_Property.md) | ISegment4 | Sets or returns the noise figure bandwidth.  
[NumberOfPoints](../Properties/Number_of__Points_Property.md) | ISegment | Sets or returns the Number of Points of the segment. Shared with the Channel Object  
[PortIFBandwidth](../Properties/PortIFBandwidth_Property.md) | ISegment3 | Sets or returns the port IF bandwidth.  
[SADataThreshold](../Properties/SADataThreshold_Property.md) | ISegment5 | Sets or returns the SA data threshold.  
[SAMTReference](../Properties/SAMTReference_Property.md) | ISegment4 | Sets or returns the SA multitone reference.  
[SAVectorAverage](../Properties/SAVectorAverage_Property.md) | ISegment4 | Sets or returns the SA vector average.  
[SAVideoBandwidth](../Properties/SAVideoBandwidth_Property.md) | ISegment5 | Sets or returns the SA video bandwidth.  
[SegmentNumber](../Properties/Segment_Number_Property.md) | ISegment | Returns the number of the current segment.  
[ShiftLO](../Properties/ShiftLO.md) | ISegment3 | Enable or disable shift LO.  
[StartFrequency](../Properties/Start_Frequency_Property.md) | ISegment | Sets or returns the start frequency of the segment. Shared with the Channel Object  
[State](../Properties/State_Property.md) | ISegment | Turns On or OFF a segment.  
[StopFrequency](../Properties/Stop_Frequency_Property.md) | ISegment | Sets or returns the stop frequency of the segment. Shared with the Channel Object  
[SweepMode](../Properties/SweepMode_Property.md) | ISegment3 | Sets or returns the sweep mode.  
[SweepTime](../Properties/Sweep_Time_Property.md) | ISegment2 | Sets or returns the sweep time of the segment. Shared with the Channel Object  
[TestPortPower](../Properties/Test_Port_Power_Property.md) | ISegment | Sets or returns the RF power level of the segment. Shared with the Channel Object  
  
###  ISegment History

Interface | Introduced with VNA Rev:  
---|---  
ISegment | 1.0  
ISegment2 | 7.1  
ISegment3 | 12.85  
ISegment4 | 13.50  
ISegment5 | 13.50  
  
* * *

