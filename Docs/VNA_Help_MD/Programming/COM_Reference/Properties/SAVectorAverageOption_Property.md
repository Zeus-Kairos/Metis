##### Write/Read

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#Segment_Table)  
  
---|---  
  
# SAVectorAverageOption Property

* * *

#### Description

| Specifies whether SA Video Bandwidth can be set independently for each
segment.  
---|---  
  
####  VB Syntax

| segs.SAVectorAverageOption = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
segs | A [Segments](../Objects/Segments_Collection.md) collection (object)  
value | (boolean)  
True \- turns SA Vector Averaging control ON. False \- turns SA Vector
Averaging control OFF.  
  
#### Return Type

| Boolean  
  
#### Default

| False  
  
#### Examples

| segs.SAVectorAverageOption = True 'Write  
value = SAVectorAverageOption 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_SAVectorAverageOption(VARIANT_BOOL *value) HRESULT
put_SAVectorAverageOption(VARIANT_BOOL value)  
  
#### Interface

| ISegments7

