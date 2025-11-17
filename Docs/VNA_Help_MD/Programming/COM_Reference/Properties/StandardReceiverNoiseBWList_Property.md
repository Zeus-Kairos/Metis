##### Read only

|

##### [About VNA Options](../../../Support/Configurations.md)  
  
---|---  
  
## StandardReceiverNoiseBWList Property

* * *

#### Description

|  Returns the list of supported Noise Bandwidths values when using the NA
receiver for noise measurements (option 028). [Learn more about Opt.
028](../../../Applications/Noise_Figure.htm#OptionsExplained).  
---|---  
  
####  VB Syntax

|  value = cap.StandardReceiverNoiseBWList  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  Variant containing one-dimensional array of long integers.  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (object)  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = cap.StandardReceiverNoiseBWList 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_StandardReceiverNoiseBWList (Variant *list);  
  
#### Interface

|  ICapabilities12  
  
* * *

