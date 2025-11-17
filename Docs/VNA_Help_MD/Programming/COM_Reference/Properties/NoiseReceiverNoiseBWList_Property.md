##### Read only

|

##### [About VNA Options](../../../Support/Configurations.md)  
  
---|---  
  
## NoiseReceiverNoiseBWList Property

* * *

#### Description

|  Returns the list of supported Noise Bandwidths values when using a noise
receiver (option 029). [Learn more about Opt.
029](../../../Applications/Noise_Figure.htm#OptionsExplained).  
---|---  
  
####  VB Syntax

|  value = cap.NoiseReceiverNoiseBWList  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  Variant containing one-dimensional array of long integers.  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (object)  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = cap.NoiseReceiverNoiseBWList 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_NoiseReceiverNoiseBWList (Variant *list);  
  
#### Interface

|  ICapabilities13  
  
* * *

