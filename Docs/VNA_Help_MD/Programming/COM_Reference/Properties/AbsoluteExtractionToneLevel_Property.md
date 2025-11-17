##### Write/Read

|

##### [About Active Match](../../../Applications/Active_Match.md)  
  
---|---  
  
# AbsoluteExtractionToneLevel Property

* * *

#### Description

|  Set and read the absolute tone power level.  
---|---  
  
####  VB Syntax

|  HotS22.AbsoluteExtractionToneLevel = level  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
HotS22 |  A [ActiveParametersApp](../Objects/HotS22App_Object.md) (object)  
level |  (Double) - Absolute tone power level  
  
#### Return Type

|  Double  
  
#### Default

|  -5 dBm  
  
#### Examples

|  HotS22.AbsoluteExtractionToneLevel = -5 'Write  
level = HotS22.AbsoluteExtractionToneLevel 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_AbsoluteExtractionToneLevel(double* level) HRESULT
put_AbsoluteExtractionToneLevel(double level)  
  
#### Interface

|  IActiveChannelSettings  
  
* * *

