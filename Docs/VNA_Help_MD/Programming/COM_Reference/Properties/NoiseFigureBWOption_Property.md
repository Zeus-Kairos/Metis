##### Write/Read

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#segment)  
  
---|---  
  
# NoiseFigureBWOption Property

* * *

#### Description

| Enables or disables noise figure bandwidth setting.  
---|---  
  
####  VB Syntax

| segs.NoiseFigureBWOption = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
segs | A [Segments](../Objects/Segments_Collection.md) collection (object)  
value | (boolean)  
True \- Enable noise figure bandwidth setting. False \- Disable noise figure
bandwidth setting.  
  
#### Return Type

| Boolean  
  
#### Default

| False  
  
#### Examples

| segs.NoiseFigureBWOption = True 'Write  
IFBWstate = segs.NoiseFigureBWOption 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_NoiseFigureBWOption(VARIANT_BOOL* pVal) HRESULT
put_NoiseFigureBWOption(VARIANT_BOOL pVal)  
  
#### Interface

| ISegments7

