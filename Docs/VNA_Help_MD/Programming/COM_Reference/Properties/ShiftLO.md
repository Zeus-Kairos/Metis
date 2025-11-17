##### Write/Read

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#segment)  
  
---|---  
  
# ShiftLO Property (PNA does not support this setting)

* * *

#### Description

| Sets or returns the Shift LO Property of a Segment. Enable the Shift LO
Property setting using the [ShiftLOOption
Property](ShiftLOOption_Property.htm) of the Segments collection.  
---|---  
  
####  VB Syntax

| seg.ShiftLO = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
seg | A [Segment](../Objects/Segment_Object.md) (object)  
value | (boolean)  
True \- Enable shift LO state. False \- Disable shift LO state.  
  
#### Return Type

| Boolean  
  
#### Default

| False  
  
#### Examples

| seg.ShiftLO = True 'Write  
shiftstate = seg.ShiftLO 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_ShiftLO(VARIANT_BOOL* pVal) HRESULT put_ShiftLO(VARIANT_BOOL
pVal)  
  
#### Interface

| ISegment3

