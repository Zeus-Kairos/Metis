##### Write-only

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)

##### [About PMAR](../../../System/Configure_a_Power_Meter_As_Receiver.md)  
  
---|---  
  
## Add (PowerSensorCalFactorSegment) Method

* * *

#### Description

|  Adds a PowerSensorCalFactorSegment to the CalFactorSegments collection.
Also Adds a PowerSensorCalFactorSegmentPMAR to the CalFactorSegmentsPMAR
collection. To ensure predictable results, it is best to remove all segments
before defining a new list of segments. For each segment in the collection, do
a seg.[Remove.](Remove_Method.md)  
---|---  
  
#### VB Syntax

|  segs.Add (item [ size])  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
segs |  A [CalFactorSegments](../Objects/CalFactorSegments_Collection.md) (collection) or A [CalFactorSegmentsPMAR](../Objects/CalFactorSegmentsPMAR_Collection.md) (collection)  
item |  (variant) \- Number of the new segment. If it already exists, a new segment is inserted at the requested position.  
size |  (long integer) - Optional argument. The number of segments to add, starting with item. If unspecified, value is set to 1.  
  
#### Return Type

|  None  
  
#### Default

|  Not Applicable  
  
#### Examples

|  segs.Add 1, 4 'Adds segments 1,2,3 and 4  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT Add(VARIANT index, long size);  
  
#### Interface

|  ICalFactorSegments ICalFactorSegmentsPMAR  
  
* * *

  

