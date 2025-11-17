##### Write/Read

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#Segment_Table)  
  
---|---  
  
# SADataThresholdOption Property

* * *

#### Description

| Specifies whether SA Data Threshold can be set independently for each
segment.  
---|---  
  
####  VB Syntax

| segs.SADataThresholdOption = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
segs | A [Segments](../Objects/Segments_Collection.md) collection (object)  
value | (boolean)  
True \- turns SA Data Threshold control ON. False \- turns SA Data Threshold
control OFF.  
  
#### Return Type

| Boolean  
  
#### Default

| False  
  
#### Examples

| segs.SADataThresholdOption = True 'Write  
value = SADataThresholdOption 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_SADataThresholdOption(VARIANT_BOOL *value) HRESULT
put_SADataThresholdOption(VARIANT_BOOL value)  
  
#### Interface

| ISegments8

