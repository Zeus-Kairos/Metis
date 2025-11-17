##### Read only

|

##### [About VNA Options](../../../Support/Configurations.md)  
  
---|---  
  
## GPIBPortCount Property

* * *

#### Description

|  Returns the number of GPIB ports that are present on the VNA rear-panel.  
---|---  
  
####  VB Syntax

|  value = cap.GPIBPortCount  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Long) - Variable to store the returned integer value of the number of GPIB ports.  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (object)  
  
#### Return Type

|  Long  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = cap.GPIBPortCount 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_GPIBPortCount(long * gpibPorts );  
  
#### Interface

|  ICapabilities3  
  
* * *

