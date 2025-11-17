#### Write-only

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#segment)  
  
---|---  
  
## SetAllSegments Method

* * *

#### Description

|  Uploads a segment table to the VNA replacing any existing segment table.
Segments must be ascending in frequency and non-overlapping. If they are not,
the segments are 'adjusted' as they are from the User Interface control. The
total number of points for all segments cannot exceed the VNA [maximum number
of points](../../../S1_Settings/DPoints.htm) for a sweep.  
---|---  
  
####  VB Syntax

|  Segs.SetAllSegments (segdata)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
segs |  A [Segments](../Objects/Segments_Collection.md) (Collection)  
segdata |  (Variant) A 2-dimensional array of Segment data:

  * dimension 0 is the number of elements in each segment.
  * dimension 1 is the number of segments that will be used.

The following is a list of dimension 0 elements for each segment: Note: All
elements must be dimensioned as either ALL Double or ALL Variant.

  * 0 = Segment state (Boolean True or False)
  * 1 = Number of Points in this segment (Integer)
  * 2 = Start Freq (Double)
  * 3 = Stop Freq (Double)
  * 4 = IFBW (Double) optional
  * 5 = Dwell Time (Double) optional
  * 6 + = Power (Double) optional; see table below.

The first four data elements must always be supplied. After those values, data
must be supplied for successive optional elements. For example, to set dwell
time values, you must also supply IFBW values, because IFBW (#4) precedes
dwell time (#5) in the array order. The
[IFBandwidthOption](../Properties/IF_Bandwidth_Option_Property.md),
[SweepTimeOption](../Properties/SweepTimeOption_Property.md), and
[SourePowerOption](../Properties/Source_Power_Option_Property.md) settings do
NOT affect the order in which elements are interpreted. The number of elements
to supply for Power depends on the following two settings:

  1. [SourcePowerOption](../Properties/Source_Power_Option_Property.md) = True allows segments to have independent power levels.
  2. [CouplePorts](../Properties/Couple_Ports_Property.md) = False allows different power levels for each test port.

|  CouplePorts |  SourcePowerOption |  Number of Elements  
---|---|---  
False |  False |  Each port has its own channel-wide power setting, which is set using [TestPortPower](../Properties/Test_Port_Power_Property.md). Provide exactly 7 elements per segment. The last element (power) is ignored.  
False |  True |  Provide 6 elements + total number of ports. The first 7 elements are still interpreted the same. The remaining elements (in-order) are interpreted as the power levels to set on that segment for Ports 2 through N, where N is the total number of ports currently enabled for the VNA or for a VNA with multiport external test set.  
True |  False |  Provide exactly 7 elements per segment. The last element (power) is ignored.  
True |  True |  Provide exactly 7 elements per segment. The last element (power) is honored.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  [See a VB example using this
command](../../COM_Example_Programs/Upload_Segment_Table_Example.htm) [See a
C++ example using this
command](../../COM_Example_Programs/Upload_Segment_Table_in_CPlus.htm)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT SetAllSegments (VARIANT Segments );  
  
#### Interface

|  ISegments2  
  
* * *

