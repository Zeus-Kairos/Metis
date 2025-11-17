##### Write/Read

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## RangeIFBW Property

* * *

#### Description

|  Sets and reads the receiver IF bandwidth setting. On the [Frequency
Range](../../../Applications/Differential_IQ.htm#RangeDiag) dialog under
Frequency, this is the IFBW setting.  
---|---  
  
####  VB Syntax

|  DIQ.RangeIFBW (n) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
n |  (Long Integer) Frequency range number.  
value |  (Double) IF Bandwidth in Hz. The list of valid IF Bandwidths is different depending on the analyzer model. ([See the list](../../../S2_Opt/Trce_Noise.md#IFDiag).) If an invalid number is specified, the analyzer will round up to the closest valid number.  
  
#### Return Type

|  Double  
  
#### Default

|  1e5  
  
#### Examples

|  diq.RangeIFBW 1 = 1e3 'Write  
value = diq.RangeIFBW 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_RangeIFBW(long range, double* RangeIFBW); HRESULT
put_RangeIFBW(long range, double RangeIFBW);  
  
#### Interface

|  IDIQ  
  
* * *

