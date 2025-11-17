##### Write/Read

|

##### [About Gating](../../../Time/TimeDomain.md#Gating)  
  
---|---  
  
## Center Property

* * *

#### Description

|  Sets or returns the Center time of either Gating or Time Domain transform
windows  
---|---  
  
####  VB Syntax

|  object.Center = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  (object) As Gating  
or  
(object) As Transform  
value |  (double) - Center time in seconds. Choose any number between:  
± (points-1) / frequency span  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  trans.Center = 4.5e-9 'sets the Center time of a transform window -Write  
gate.Center = 4.5e-9 'sets the Center time of a gating window -Write  
cnt = trans.Center 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Center(double *pVal)  
HRESULT put_Center(double newVal)  
  
#### Interface

|  ITransform  
IGating

