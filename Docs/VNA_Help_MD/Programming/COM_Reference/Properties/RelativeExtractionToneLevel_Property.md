##### Write/Read

|

##### [About Active Match](../../../Applications/Active_Match.md)  
  
---|---  
  
# RelativeExtractionToneLevel Property

* * *

#### Description

|  Set and read the tone power relative to the input power (dBc).  
---|---  
  
####  VB Syntax

|  HotS22.RelativeExtractionToneLevel = level  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
HotS22 |  A [ActiveParametersApp](../Objects/HotS22App_Object.md) (object)  
level |  (Double) - Relative tone power level  
  
#### Return Type

|  Double  
  
#### Default

|  -15 dBc  
  
#### Examples

|  HotS22.RelativeExtractionToneLevel = -5 'Write  
level = HotS22.RelativeExtractionToneLevel 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_RelativeExtractionToneLevel(double* level) HRESULT
put_RelativeExtractionToneLevel(double level)  
  
#### Interface

|  IActiveChannelSettings  
  
* * *

