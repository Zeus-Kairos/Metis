##### Read-only

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#segment)

##### [About PMAR](../../../System/Configure_a_Power_Meter_As_Receiver.md)  
  
---|---  
  
## SegmentNumber Property

* * *

#### Description

| Returns the number of the current segment, PowerSensorCalFactorSegment or
PowerLossSegment object.  
---|---  
  
####  VB Syntax

| seg.SegmentNumber  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
seg | Any of the following objects: A [Segment](../Objects/Segment_Object.md) (Object) A [PowerSensorCalFactorSegment](../Objects/PowerSensorCalFactorSegment_Object.md) (Object) A [PowerSensorCalFactorSegmentPMAR Object](../Objects/PowerSensorCalFactorSegmentPMAR_Object.md) (Object) A [PowerLossSegment](../Objects/PowerLossSegment_Object.md) (Object) A [PowerLossSegmentPMAR](../Objects/PowerLossSegmentPMAR_Object.md) (Object)  
  
#### Return Type

| Long Integer  
  
#### Default

| Not Applicable  
  
#### Examples

| segNum = seg.SegmentNumber 'returns the segment number -Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT get_SegmentNumber(long *pVal)  
  
#### Interface

| ISegment  
IPowerSensorCalFactorSegment IPowerLossSegment  
  
* * *

