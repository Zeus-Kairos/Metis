##### Write/Read

|

##### [About Power Leveling](../../../Applications/IMSpectrum.md#PowerTab)  
  
---|---  
  
## LevelingMethod Property

* * *

#### Description

|  Sets and returns the tone power leveling mode.  
---|---  
  
####  VB Syntax

|  object.LevelingMethod = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  One of the following:

  * [IMSpectrum Object](../Objects/IMSpectrum_Object.md)
  * [SweptIMD Object](../Objects/SweptIMD_Object.md)

  
value |  (enum NAIMDLevelMethod) \- Choose from: 0 - naNOLevel 1 - naLevelInput 2 - naEqualizeOutput 3 - naLevelOutput  
  
#### Return Type

|  Enum  
  
#### Default

|  naNOLevel  
  
#### Examples

|  imd.LevelingMethod = naEqualizeOutput 'Write  
levMode = ims.LevelingMethod 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_LevelingMethod(tagNALevelingMethods* pVal) HRESULT
put_LevelingMethod(tagNALevelingMethods newVal)  
  
#### Interface

|  IIMSpectrum ISweptIMD  
  
* * *

