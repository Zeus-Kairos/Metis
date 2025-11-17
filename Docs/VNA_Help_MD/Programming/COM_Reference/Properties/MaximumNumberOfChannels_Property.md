##### Read only

|

##### [About VNA Options](../../../Support/Configurations.md)  
  
---|---  
  
## MaximumNumberOfChannels Property

* * *

#### Description

|  Returns the maximum possible number of channels that can be used in the
VNA.  
---|---  
  
####  VB Syntax

|  value = cap.MaximumNumberOfChannels  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Long) \- Variable to store the returned maximum value for number of channels.  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (object)  
  
#### Return Type

|  Long  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = cap.MaximumNumberOfChannels 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MaximumNumberOfChannels(long * maximumNumberOfChans );  
  
#### Interface

|  ICapabilities2

