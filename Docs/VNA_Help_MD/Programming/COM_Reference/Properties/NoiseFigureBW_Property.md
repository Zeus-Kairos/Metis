##### Write/Read

|

##### [About Segment Sweep](../../../S1_Settings/Sweep.md#segment)  
  
---|---  
  
# NoiseFigureBW Property

* * *

#### Description

| Sets or returns the noise figure bandwidth.  
---|---  
  
####  VB Syntax

| seg.NoiseFigureBW = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
seg | A [Segment](../Objects/Segment_Object.md) (object)  
value | (Double) Noise figure bandwidth.  
  
#### Return Type

| Double  
  
#### Default

| Not Applicable  
  
#### Examples

| seg.NoiseFigureBW = 1000 'Write  
value = seg.NoiseFigureBW 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_NoiseFigureBW(double* pVal); HRESULT put_NoiseFigureBW(double
pVal);  
  
#### Interface

| ISegment4

