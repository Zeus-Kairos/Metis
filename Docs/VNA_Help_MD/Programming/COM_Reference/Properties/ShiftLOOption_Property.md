##### Write/Read

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#segment)  
  
---|---  
  
# ShiftLOOption Property (This command is not supported on PNA-L, PNA, PNA-X)

* * *

#### Description

| Enables or disables ShiftLO per segment. Value is set using [ShiftLO
Property](ShiftLO.htm) of a segment.  
---|---  
  
####  VB Syntax

| segs.ShiftLOOption = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
segs | A [Segments](../Objects/Segments_Collection.md) collection (object)  
value | (boolean)  
True \- Enable shift LO state. False \- Disable shift LO state.  
  
#### Return Type

| Boolean  
  
#### Default

| False  
  
#### Examples

| segs.ShiftLOOption = True 'Write  
shiftstate = segs.ShiftLOOption 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_ShiftLOOption(VARIANT_BOOL* pVal) HRESULT
put_ShiftLOOption(VARIANT_BOOL pVal)  
  
#### Interface

| ISegments6

