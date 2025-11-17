##### Read only

|

##### [About VNA Options](../../../Support/Configurations.md)  
  
---|---  
  
## MaximumFrequency Property

* * *

#### Description

|  Returns the maximum frequency of the remote VNA, including any over-sweep.
Over-sweep frequencies can be set but are not specified.  
---|---  
  
####  VB Syntax

|  value = cap.MaximumFrequency  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Double) - Variable to store the returned maximum frequency of the VNA.  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (object)  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = cap.MaximumFrequency 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MaximumFrequency(&frequencyMax);  
  
#### Interface

|  ICapabilities

