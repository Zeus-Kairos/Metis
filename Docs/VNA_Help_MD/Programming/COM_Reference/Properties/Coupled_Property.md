##### Read-Write

|

##### [About FOM](../../../FreqOffset/Frequency_Offset_Mode.md)  
  
---|---  
  
## Coupled Property

* * *

#### Description

|  Sets and returns the state of coupling (ON or OFF) of this range to the
primary range.  
---|---  
  
####  VB Syntax

|  FOMRange.Coupled = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  An [FOMRange](../Objects/FOMRange_Object.md) (object)  
value |  (boolean) \- State of coupling. True \- Couple range to primary range. False \- Do NOT couple to primary range.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  fomRange.Coupled = False 'this range is NOT coupled to the primary range.  
coupl = fomRange.Coupled 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Coupled(VARIANT_BOOL *pVal)  
HRESULT put_Coupled(VARIANT_BOOL pVal)  
  
#### Interface

|  IFOMRange

