##### Read only

|

##### [About VNA Options](../../../Support/Configurations.md)  
  
---|---  
  
## SourceCount Property

* * *

#### Description

|  Returns the number of sources in the remote VNA.  
---|---  
  
####  VB Syntax

|  value = cap.SourceCount  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Long) - Variable to store the returned number of sources.  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (object)  
  
#### Return Type

|  Long  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = cap.SourceCount 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SourceCount(long * sourceCount );  
  
#### Interface

|  ICapabilities

