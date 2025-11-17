##### Write/Read

|

##### [About Noise Figure](../../../Applications/Noise_Figure.md)  
  
---|---  
  
## ForceDeEmbedSensorAdapter Property

* * *

#### Description

|  Set and read the state of power sensor adapter de-embedding. [Learn
more](../../../Applications/Noise_Cal.htm#DeEmbedAdapter).  
---|---  
  
####  VB Syntax

|  noiseCal.ForceDeEmbedSensorAdapter = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
noiseCal |  A [NoiseCal](../Objects/NoiseCal_Object.md) (object)  
value |  (boolean) - Power sensor adapter de-embed state. False - Do not Force de-embedding. True - Force de-embedding.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  noiseCal.ForceDeEmbedSensorAdapter = False 'Write  
AdapterDembed = noiseCal.ForceDeEmbedSensorAdapter 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ForceDeEmbedSensorAdapter(VARIANT_BOOL* on); HRESULT
put_ForceDeEmbedSensorAdapter(VARIANT_BOOL on);  
  
#### Interface

|  INoiseCal2  
  
* * *

