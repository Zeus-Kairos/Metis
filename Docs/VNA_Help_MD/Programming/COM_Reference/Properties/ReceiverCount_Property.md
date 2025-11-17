##### Read only

|

##### [About VNA Options](../../../Support/Configurations.md)  
  
---|---  
  
## ReceiverCount Property

* * *

#### Description

|  Returns the number of receivers in the remote VNA. The returned number
includes both test port receivers and reference receivers. [See the number of
reference receivers in your VNA.](../../../Support/Configurations.htm)  
---|---  
  
####  VB Syntax

|  value = cap.ReceiverCount  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Long) - Variable to store the returned number of receivers.  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (object)  
  
#### Return Type

|  Long  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = cap.ReceiverCount 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ReceiverCount(long * receiverCount );  
  
#### Interface

|  ICapabilities

