##### Write/Read

|

##### [About Equal Tone
Power](../../../Applications/Swept_IMD.htm#PowerTabDiag)  
  
---|---  
  
## EqualTonePower Property - Superseded

* * *

#### Description

|  Note: This command is replaced with [LevelingMethod Property](LevelingMethod_Property.md) Sets and returns the ON | OFF state of Equal Tone Power for the Swept IMD or IMSpectrum measurement.  
---|---  
  
####  VB Syntax

|  object.EqualTonePower = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  A [SweptIMD](../Objects/SweptIMD_Object.md) or [IMSpectrum](../Objects/IMSpectrum_Object.md) Object  
value |  (Boolean) - Choose from: True \- Set equal tone power. False \- Do NOT set equal tone power.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  ims.EqualTonePower = true 'Write  
value = imd.EqualTonePower 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_EqualTonePower(VARIANT_BOOL* val) HRESULT
put_EqualTonePower(VARIANT_BOOL val)  
  
#### Interface

|  ISweptIMD2 IIMSpectrum2  
  
* * *

* * *

