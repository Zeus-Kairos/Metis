##### Read-Write

|

##### [About FOM](../../../FreqOffset/Frequency_Offset_Mode.md)  
  
---|---  
  
## Multiplier Property

* * *

#### Description

|  Sets and returns the multiplier value to be used when coupling this range
to the primary range. Learn more about multiplier value. This setting is valid
only if this range is [coupled](Coupled_Property.md) to the primary range.  
---|---  
  
####  VB Syntax

|  FOMRange.Multiplier = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  An [FOMRange](../Objects/FOMRange_Object.md) (object)  
value |  (Double) \- Multiplier value.-(Unitless)  
  
#### Return Type

|  Double  
  
#### Default

|  1  
  
#### Examples

|  fomRange.Multiplier = 2 'Write  
Mult = fomRange.Multiplier 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Multiplier(double *pVal)  
HRESULT put_Multiplier(double pVal)  
  
#### Interface

|  IFOMRange

