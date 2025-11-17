##### Read only

|

##### [About VNA Options](../../../Support/Configurations.md)  
  
---|---  
  
## IsFrequencyOffsetPresent Property

* * *

#### Description

|  Returns a value indicating the presence of Frequency Offset Option S93080A
in the remote VNA.  
---|---  
  
####  VB Syntax

|  value = cap.IsFrequencyOffsetPresent  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Boolean) - Variable to store the returned value True - Frequency Offset Option S93080A is present False - Frequency Offset Option S93080A is not present  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (object)  
  
#### Return Type

|  Boolean  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = cap.isFrequencyOffsetPresent(1) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_IsFrequencyOffsetPresent(VARIANT_BOOL * present );  
  
#### Interface

|  ICapabilities

