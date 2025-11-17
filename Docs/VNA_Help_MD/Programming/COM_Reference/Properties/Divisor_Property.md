##### Read-Write

|

##### [About FOM](../../../FreqOffset/Frequency_Offset_Mode.md)  
  
---|---  
  
## Divisor Property

* * *

#### Description

|  Sets and returns the Divisor value to be used when coupling this range to
the primary range. This setting is valid only if the specified range is
[coupled](Coupled_Property.md) to the primary range.  
---|---  
  
####  VB Syntax

|  FOMRange.Divisor = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  An [FOMRange](../Objects/FOMRange_Object.md) (object)  
value |  (Double) \- Divisor value.-(Unitless)  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  fomRange.Divisor = .5 'Write  
Div = fomRange.Divisor 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Divisor(double *pVal)  
HRESULT put_Divisor(double *pVal)  
  
#### Interface

|  IFOMRange

