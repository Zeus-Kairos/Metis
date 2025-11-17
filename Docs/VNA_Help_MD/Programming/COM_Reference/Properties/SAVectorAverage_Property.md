##### Write/Read

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#Segment_Table)  
  
---|---  
  
# SAVectorAverage Property

* * *

#### Description

| Sets or returns the SA vector average points.  
---|---  
  
####  VB Syntax

| seg.SAVectorAverage = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
seg | A [Segment](../Objects/Segment_Object.md) (object)  
value | (Long) Vector average points.  
  
#### Return Type

| Long  
  
#### Default

| 1  
  
#### Examples

| seg.SAVectorAverage = 10 'Write  
value = seg.SAVectorAverage 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_SAVectorAverage(long* pVal); HRESULT put_SAVectorAverage(long
pVal);  
  
#### Interface

| ISegment4

