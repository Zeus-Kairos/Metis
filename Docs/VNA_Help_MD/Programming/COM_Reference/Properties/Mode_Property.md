##### Write/Read

|

##### [About Time Domain](../../../Time/TimeDomain.md)  
  
---|---  
  
## Mode Property

* * *

#### Description

|  Sets the type of transform.  
---|---  
  
####  VB Syntax

|  trans.Mode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
trans |  A Transform (object)  
value |  (enum NATransformMode) - Choose from: 0 \- naTransformBandpassImpulse  
1 \- naTransformLowpassImpulse  
2 \- naTransformLowpassStep  
  
#### Return Type

|  NATransformMode  
  
#### Default

|  0 \- naTransformBandpassImpulse  
  
#### Examples

|  trans.Mode = naTransformLowpassStep 'Write  
transmode = trans.Mode 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Mode(tagNATransformMode *pVal)  
HRESULT put_Mode(tagNATransformMode newVal)  
  
#### Interface

|  ITransform

