##### Read only

|

##### [About VNA Options](../../../Support/Configurations.md)  
  
---|---  
  
## InternalTestsetPortCount Property

* * *

#### Description

|  Returns the number of VNA test ports. This does not include the ports on an
[external test set](../../../System/External_Testset_Control.md).  
---|---  
  
####  VB Syntax

|  value = cap.InternalTestsetPortCount  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Long) - Variable to store the returned number of VNA test ports.  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (object)  
  
#### Return Type

|  Long  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = cap.InternalTestsetPortCount 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_InternalTestsetPortCount(long *numPorts );  
  
#### Interface

|  ICapabilities

