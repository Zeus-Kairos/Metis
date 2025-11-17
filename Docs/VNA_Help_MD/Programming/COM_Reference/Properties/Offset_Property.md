##### Read-Write

|

##### [About FOM](../../../FreqOffset/Frequency_Offset_Mode.md)  
  
---|---  
  
## Offset Property

* * *

#### Description

|  Sets and returns the offset value to be used when coupling this range to
the primary range. This setting is valid only if the specified range is
[coupled](Coupled_Property.md) to the primary range.  
---|---  
  
####  VB Syntax

|  FOMRange.Offset = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  An [FOMRange](../Objects/FOMRange_Object.md) (object)  
value |  (Double) \- Offset value.-(Unitless)  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  fomRange.Offset = 1e9 'Write  
Offs = fomRange.Offset 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Offset(double *pVal)  
HRESULT put_Offset(double pVal)  
  
#### Interface

|  IFOMRange  
  
* * *

