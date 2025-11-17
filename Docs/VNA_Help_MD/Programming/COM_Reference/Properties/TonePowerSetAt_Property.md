##### Write/Read

|

##### [About Tone Power](../../../Applications/Swept_IMD.md#PowerTabDiag)  
  
---|---  
  
## TonePowerSetAt Property - Superseded

* * *

#### Description

|  Note: This command is replaced with [LevelingMethod
Property](LevelingMethod_Property.htm) Sets and returns whether tone power is
specified at the DUT input or output.  
---|---  
  
####  VB Syntax

|  object.TonePowerSetAt = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  A [SweptIMD](../Objects/SweptIMD_Object.md) Object or [IMSpectrum](../Objects/IMSpectrum_Object.md) Object  
value |  (Enum as NAPortMode) 0 - naInput \- Specified power level is set at the DUT input. 1 - naOutput \- Specified power level is set at the DUT output.  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - naInput  
  
#### Examples

|  imd.TonePowerSetAt = naOutput 'Write  
value = ims.TonePowerSetAt 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_TonePowerSetAt(tagNAPortMode *pVal) HRESULT
put_TonePowerSetAt(tagNAPortMode pVal)  
  
#### Interface

|  ISweptIMD2 IImSpectrum2  
  
* * *

* * *

