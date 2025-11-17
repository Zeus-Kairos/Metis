##### Write-only

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#segment)  
  
---|---  
  
## Add (segment) Method

* * *

#### Description

|  Adds segments to the Segments collection, but does not turn the segments
ON.  
---|---  
  
#### VB Syntax

|  segs.Add (item, [size])  
segs |  A [segments](../Objects/Segments_Collection.md) collection (object)  
item |  (variant) Number of the new segment. If it already exists, a new segment is inserted at the requested position.  
size |  (long integer) Optional argument. The number of segments to add, starting with item. If unspecified, value is set to 1.  
  
#### Return Type

|  None  
  
#### Default

|  None  
  
#### Examples

|  Segs.Add 1, 4 'Adds segments 1,2,3,and 4. (does NOT automatically turn
segments ON)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT Add(VARIANT index, long size);  
  
#### Interface

|  ISegments  
  
#### Remarks

|  To ensure predictable results, it is best to remove all segments before
defining a segment list. For each segment in the collection, do a
seg.[Remove](Remove_Method.md).

