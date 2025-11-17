##### Write/Read

|

##### [About Noise Figure](../../../Applications/Noise_Figure.md)  
  
---|---  
  
# ForceDeEmbedThruAdapter Property

* * *

#### Description

| Sets and reads the state of Thru adapter de-embedding. [Learn
more](../../../Applications/Noise_Cal.htm#DeEmbedAdapter).  
---|---  
  
####  VB Syntax

| noiseCal.ForceDeEmbedThruAdapter = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
noiseCal | A [NoiseCal](../Objects/NoiseCal_Object.md) (object)  
value | (boolean) \- Thru Adapter de-embed state. False \- Do not Force de-embedding. True \- Force de-embedding.  
  
#### Return Type

| Boolean  
  
#### Default

| False  
  
#### Examples

| noiseCal.ForceDeEmbedThruAdapter = False 'Write  
AdapterDembed = noiseCal.ForceDeEmbedThruAdapter 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_ForceDeEmbedThruAdapter(VARIANT_BOOL* on); HRESULT
put_ForceDeEmbedThruAdapter(VARIANT_BOOL on);  
  
#### Interface

| INoiseCal4

