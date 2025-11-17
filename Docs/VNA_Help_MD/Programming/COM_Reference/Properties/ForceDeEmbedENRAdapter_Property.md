##### Write/Read

|

##### [About Noise Figure](../../../Applications/Noise_Figure.md)  
  
---|---  
  
## ForceDeEmbedENRAdapter Property

* * *

#### Description

|  Set and read the De-embedENRAdapter state. [Learn
more](../../../Applications/Noise_Cal.htm#DeEmbedAdapter).  
---|---  
  
####  VB Syntax

|  noiseCal.ForceDeEmbedENRAdapter = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
noiseCal |  A [NoiseCal](../Objects/NoiseCal_Object.md) (object)  
value |  (boolean) - ENR Adapter de-embed state. False - Do not Force de-embedding. True - Force de-embedding.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  noiseCal.ForceDeEmbedENRAdapter = False 'Write  
AdapterDembed = noiseCal.ForceDeEmbedENRAdapter 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ForceDeEmbedENRAdapter(VARIANT_BOOL* on); HRESULT
put_ForceDeEmbedENRAdapter(VARIANT_BOOL on);  
  
#### Interface

|  INoiseCal2  
  
* * *

