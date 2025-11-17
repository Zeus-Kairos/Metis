#### Read-only

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#segment)  
  
---|---  
  
## GetAllSegments Method

* * *

#### Description

|  Downloads a segment table from the VNA.  
---|---  
  
####  VB Syntax

|  segdata = Segs.GetAllSegments  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
segs |  A [Segments](../Objects/Segments_Collection.md) (Collection)  
segdata |  (Variant) A 2-dimensional array of Segment data:

  * Dimension 0 is the number of elements in each segment.
  * Dimension 1 is the number of segments that will be used.

All elements in the returned array are Variant. The type inside each Variant
will be as is listed below.  The returned array will contain values for all
elements regardless of the settings of
[IFBandwidthOption](../Properties/IF_Bandwidth_Option_Property.md),
[SweepTimeOption](../Properties/SweepTimeOption_Property.md),
[SourcePowerOption](../Properties/Source_Power_Option_Property.md) and
[CouplePorts](../Properties/Couple_Ports_Property.md) properties. Ignore the
values for the properties that are set to false. The following is a list of
dimension 0 elements for each segment:

  * 0 = Segment state (Boolean True or False)
  * 1 = Number of Points in this segment (Integer)
  * 2 = Start Freq (Double)
  * 3 = Stop Freq (Double)
  * 4 = IFBW (Double)
  * 5 = Dwell Time (Double)
  * 6 + N = Power (Double) where N is the number of source ports of the VNA. For example, with a 4-port, 1-source VNA, indices 6 through 9 correspond to the per-segment power levels for Ports 1 to 4. Use [SourcePortCount Property](../Properties/SourcePortCount_Property.md) and [SourcePortNames Property](../Properties/SourcePortNames_Property.md) to see the available source ports for the VNA.

  
  
#### Return Type

|  Variant, containing an array.  
  
#### Default

|  Not Applicable  
  
#### Examples

|  [See a VB example using this
command](../../COM_Example_Programs/Upload_Segment_Table_Example.htm)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetAllSegments (VARIANT *pSegments );  
  
#### Interface

|  ISegments5  
  
* * *

