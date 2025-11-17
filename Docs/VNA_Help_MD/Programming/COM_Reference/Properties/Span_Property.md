##### Write/Read

|

##### [About Time Domain](../../../Time/TimeDomain.md)  
  
---|---  
  
## Span Property

* * *

#### Description

|  Sets or returns the Span time of either Gating or Time Domain transform
windows  
---|---  
  
####  VB Syntax

|  object.Span = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  (object) As Gating  
or  
(object) As Transform  
value |  (double) - Span time in seconds. Choose any number between: 2*[(number of points-1) / frequency span] and 0  
  
#### Return Type

|  Double  
  
#### Default

|  20ns  
  
#### Examples

|  Trans.Span = 4.5e-9 'sets the time span of a transform window -Write  
Gate.Span = 4.5e-9 'sets the Span time of a gating window -Write  
span = Trans.Span 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Span(double *pVal)  
HRESULT put_Span(double newVal)  
  
#### Interface

|  ITransform  
IGating

