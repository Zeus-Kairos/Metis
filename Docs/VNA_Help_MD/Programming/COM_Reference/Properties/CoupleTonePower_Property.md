##### Write/Read

|

##### [About Swept IMD](../../../Applications/Swept_IMD.md)  
  
---|---  
  
## CoupleTonePower Property

* * *

#### Description

|  Sets and returns the ON | OFF state of power coupling for F1 and F2.  
---|---  
  
####  VB Syntax

|  object.CoupleTonePower = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  A [SweptIMD](../Objects/SweptIMD_Object.md) or [IMSpectrum](../Objects/IMSpectrum_Object.md) Object  
value |  (Boolean) - Choose from: True \- F1 and F2 power is coupled. False \- F1 and F2 power is NOT coupled. Set power levels individually.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  ims.CoupleTonePower = true 'Write  
value = ims.CoupleTonePower 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CoupleTonePower(VARIANT_BOOL* val)  
HRESULT put_CoupleTonePower(VARIANT_BOOL val)  
  
#### Interface

|  ISweptIMD IIMSpectrum  
  
* * *

