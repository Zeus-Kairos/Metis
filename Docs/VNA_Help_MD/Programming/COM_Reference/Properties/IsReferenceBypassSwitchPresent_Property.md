##### Read only

|

##### [About VNA Options](../../../Support/Configurations.md)  
  
---|---  
  
## IsReferenceBypassSwitchPresent Property

* * *

#### Description

|  Returns a value indicating the presence of a Reference Bypass Switch in the
remote VNA.  
---|---  
  
####  VB Syntax

|  value = cap.IsReferenceBypassSwitchPresent (n)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Boolean) - Variable to store the returned value. True - Reference Bypass Switch is present. False - Reference Bypass Switch is not present.  
cap n |  A [Capabilities](../Objects/Capabilities_Object.md) (object) (Long) - port number to query for reference bypass switch  
  
#### Return Type

|  Boolean  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = cap.IsReferenceBypassSwitchPresent(1) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_IsReferenceBypassSwitchPresent(long portNumber, VARIANT_BOOL *
present );  
  
#### Interface

|  ICapabilities

