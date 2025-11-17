##### Read only

|

##### [About VNA Options](../../../Support/Configurations.md)  
  
---|---  
  
## HasDirectReceiverAccess Property

* * *

#### Description

|  Returns whether or not the analyzer has direct receiver access (front-panel
jumpers).  
---|---  
  
####  VB Syntax

|  value = cap.HasDirectReceiverAccess  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Boolean) - Variable to store the returned value True - VNA has direct receiver access. False - VNA does NOT have direct receiver access.  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (object)  
  
#### Return Type

|  Boolean  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = cap.HasDirectReceiverAccess 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_HasDirectReceiverAccess(VARIANT_BOOL *present );  
  
#### Interface

|  ICapabilities12  
  
* * *

