##### Write/Read

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#Segment_Table)  
  
---|---  
  
# SAVideoBandwidth Property

* * *

#### Description

| Sets or returns the SA video bandwidth.  
---|---  
  
####  VB Syntax

| seg.SAVideoBandwidth = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
seg | A [Segment](../Objects/Segment_Object.md) (object)  
value | (Double) Video bandwidth (in Hz).  
  
#### Return Type

| Double  
  
#### Default

| 1E6 Hz  
  
#### Examples

| seg.SAVideoBandwidth = 1E6 'Write  
value = seg.SAVideoBandwidth 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_SAVideoBandwidth(double* pVal); HRESULT
put_SAVideoBandwidth(double pVal);  
  
#### Interface

| ISegment5

