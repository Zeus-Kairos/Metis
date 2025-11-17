##### Write/Read

|

##### [About Time Domain](../../../Time/TimeDomain.md)  
  
---|---  
  
## Start Property

* * *

#### Description

|  Sets or returns the start time of either Gating or Time Domain transform
windows  
---|---  
  
####  VB Syntax

|  object.Start = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  (object) As Gating  
or  
(object) As Transform  
value |  (double) - Start time in seconds. Choose any number between:  
± (number of points-1) / frequency span  
  
#### Return Type

|  Double  
  
#### Default

|  -10ns  
  
#### Examples

|  Trans.Start = 4.5e-9 'sets the start time of a transform window -Write  
Gate.Start = 4.5e-9 'sets the start time of a gating window -Write  
strt = Trans.Start 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Start(double *pVal)  
HRESULT put_Start(double newVal)  
  
#### Interface

|  ITransform  
IGating

