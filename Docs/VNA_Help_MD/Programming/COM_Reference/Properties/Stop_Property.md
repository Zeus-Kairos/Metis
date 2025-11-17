#### Write/Read

|

##### [About Time Domain](../../../Time/TimeDomain.md)  
  
---|---  
  
## Stop Property

* * *

#### Description

|  Sets or returns the Stop time of either Gating or Time Domain transform
windows  
---|---  
  
####  VB Syntax

|  object.Stop = value  
  
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

|  10 ns  
  
#### Examples

|  Trans.Stop = 4.5e-9 'sets the stop time of a transform window -Write  
Gate.Stop = 4.5e-9 'sets the stop time of a gating window -Write  
stp = Trans.Stop 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Stop(double *pVal)  
HRESULT put_Stop(double newVal)  
  
#### Interface

|  ITransform  
IGating

