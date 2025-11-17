##### Write/Read

|

##### [About Active Match](../../../Applications/Active_Match.md)  
  
---|---  
  
# ExtractionToneMode Property

* * *

#### Description

|  Set and read the tuning tone mode. The tuning tone is the source at the
output port to extract the X parameters.  
---|---  
  
####  VB Syntax

|  HotS22.ExtractionToneMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
HotS22 |  A [ActiveParametersApp](../Objects/HotS22App_Object.md) (object)  
value |  (Enum as NAExtractionToneMode) - Choose from:

  * 0 - naRelative Tone power is a dBc power relative to the input power.
  * 1 - naAbsolute  Tone power is an absolute power.

  
  
#### Return Type

|  Enum  
  
#### Default

|  naAbsolute  
  
#### Examples

|  HotS22.ExtractionToneMode = naAbsolute 'Write  
value = HotS22.ExtractionToneMode 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ExtractionToneMode(tagNAExtractionToneMode* value)  
HRESULT put_ExtractionToneMode(tagNAExtractionToneMode value)  
  
#### Interface

|  IActiveChannelSettings  
  
* * *

