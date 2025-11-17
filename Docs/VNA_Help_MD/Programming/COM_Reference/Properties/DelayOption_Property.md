##### Write/Read

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#segment)  
  
---|---  
  
# DelayOption Property

* * *

#### Description

| Enables or disables segment delay. Value is set using the [Delay (Segment
Sweep) Property](Delay_\(Segment_Sweep\)_Property.htm) on a Segment.  
---|---  
  
####  VB Syntax

| segs.DelayOption = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
segs | A [Segments](../Objects/Segments_Collection.md) collection (object)  
value | (boolean)  
True \- Enable delay. False \- Disable delay.  
  
#### Return Type

| Boolean  
  
#### Default

| False  
  
#### Examples

| segs.DelayOption = True 'Write  
delaystate = segs.DelayOption 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_DelayOption(VARIANT_BOOL* pVal) HRESULT
put_DelayOption(VARIANT_BOOL pVal)  
  
#### Interface

| ISegments6

