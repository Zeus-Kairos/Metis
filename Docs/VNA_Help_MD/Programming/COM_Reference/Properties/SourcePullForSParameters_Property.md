##### Write/Read

|

##### [About NFX](../../../Applications/Noise_Cal.md)  
  
---|---  
  
## SourcePullForSParameters Property

* * *

#### Description

|  Enables and disables the use of source pull technique to compute S22 on
Noise Figure on Converters. [Learn
more.](../../../Applications/Noise_Figure_on_Converters.htm#SourcePulling)  
---|---  
  
####  VB Syntax

|  nfx.SourcePullForSParameters = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
nfx |  A [NoiseFigure](../Objects/NoiseFigure_Object.md) (object)  
value |  (Boolean) Source pull technique state. Choose from: False \- Disable use of source pull technique. True \- Enable use of source pull technique.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  nfx.SourcePullForSParameters = true 'Write  
sourcePull = nfx.SourcePullForSParameters 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SourcePullForSParameters (VARIANT_BOOL * Val) HRESULT
put_SourcePullForSParameters (VARIANT_BOOL newVal)  
  
#### Interface

|  INoiseFigure4  
  
* * *

