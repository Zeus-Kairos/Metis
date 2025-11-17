##### Write/Read

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#Segment_Table)  
  
---|---  
  
# SADataThreshold Property

* * *

#### Description

| Sets or returns the SA data threshold.  
---|---  
  
####  VB Syntax

| seg.SADataThreshold = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
seg | A [Segment](../Objects/Segment_Object.md) (object)  
value | (Double) Data threshold (in dBm).  
  
#### Return Type

| Double  
  
#### Default

| -60 dBm  
  
#### Examples

| seg.SADataThreshold = -60 'Write  
value = seg.SADataThreshold 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_SADataThreshold(double* pVal); HRESULT
put_SADataThreshold(double pVal);  
  
#### Interface

| ISegment5

