##### Write/Read

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#Segment_Table)  
  
---|---  
  
# SAMTReferenceFreqOption Property

* * *

#### Description

| Specifies whether SA Reference Tone can be set independently for each
segment.  
---|---  
  
####  VB Syntax

| segs.SAMTReferenceFreqOption = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
segs | A [Segments](../Objects/Segments_Collection.md) collection (object)  
value | (boolean)  
True \- turns SA Reference Tone control ON. False \- turns SA Reference Tone
control OFF.  
  
#### Return Type

| Boolean  
  
#### Default

| False  
  
#### Examples

| segs.SAMTReferenceFreqOption = True 'Write  
value = SAMTReferenceFreqOption 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_SAMTReferenceFreqOption(VARIANT_BOOL *value) HRESULT
put_SAMTReferenceFreqOption(VARIANT_BOOL value)  
  
#### Interface

| ISegments7

