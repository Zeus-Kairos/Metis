##### Write/Read

|

##### [About Time Domain](../../../Time/TimeDomain.md)  
  
---|---  
  
## KaiserBeta Property

* * *

#### Description

|  Sets or returns the Kaiser Beta of Time Domain transform windows  
---|---  
  
####  VB Syntax

|  trans.KaiserBeta = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
trans |  A Transform (object)  
value |  (single) - Kaiser Beta. Choose any number between 0 and 13.  
  
#### Return Type

|  Single  
  
#### Default

|  0  
  
#### Examples

|  trans.KaiserBeta = 6 'sets the Kaiser Beta of a transform window -Write  
KB = trans.KaiserBeta 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_KaiserBeta(float *pVal)  
HRESULT put_KaiserBeta(float newVal)  
  
#### Interface

|  ITransform

