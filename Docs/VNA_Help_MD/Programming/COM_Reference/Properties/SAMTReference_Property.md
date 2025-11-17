##### Write/Read

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#Segment_Table)  
  
---|---  
  
# SAMTReference Property

* * *

#### Description

| Sets or returns the SA multitone reference.  
---|---  
  
####  VB Syntax

| seg.SAMTReference = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
seg | A [Segment](../Objects/Segment_Object.md) (object)  
value | (Double) Multitone reference (in dBm).  
  
#### Return Type

| Double  
  
#### Default

| 0  
  
#### Examples

| seg.SAMTReference = 0 'Write  
value = seg.SAMTReference 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_SAMTReference(double* pVal); HRESULT put_SAMTReference(double
pVal);  
  
#### Interface

| ISegment4

