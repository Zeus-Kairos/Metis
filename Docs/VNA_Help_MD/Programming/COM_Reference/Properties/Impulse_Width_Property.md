##### Write/Read

|

##### [About Time Domain](../../../Time/TimeDomain.md)  
  
---|---  
  
## ImpulseWidth Property

* * *

#### Description

|  Sets or returns the Impulse Width of Time Domain transform windows  
---|---  
  
####  VB Syntax

|  trans.ImpulseWidth = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
trans |  A [Transform](../Objects/Transform_Object.md) (object)  
value |  (double) - Impulse Width in seconds. Range of settings depends on the frequency range of your analyzer.  
  
#### Return Type

|  Double  
  
#### Default

|  .98 / Default Span  
  
#### Examples

|  trans.ImpulseWidth = 200e-12 'sets the Impulse width of a transform window
-Write  
IW = trans.ImpulseWidth 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_ImpulseWidth(double *pVal)  
HRESULT put_ImpulseWidth(double newVal)  
  
#### Interface

|  ITransform

