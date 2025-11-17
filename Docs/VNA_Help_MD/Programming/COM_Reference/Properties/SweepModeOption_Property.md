##### Write/Read

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#segment)  
  
---|---  
  
# SweepModeOption Property

* * *

#### Description

| Enables or disables sweep mode per segment. Value is set using the
[SweepMode Property](SweepMode_Property.md) of a Segment.  
---|---  
  
####  VB Syntax

| segs.SweepModeOption = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
segs | A [Segments](../Objects/Segments_Collection.md) collection (object)  
value | (boolean)  
True \- Enable sweep mode. False \- Disable sweep mode.  
  
#### Return Type

| Boolean  
  
#### Default

| False  
  
#### Examples

| segs.SweepModeOption = True 'Write  
sweepstate = segs.SweepModeOption 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_SweepModeOption(VARIANT_BOOL* pVal) HRESULT
put_SweepModeOption(VARIANT_BOOL pVal)  
  
#### Interface

| ISegments6

