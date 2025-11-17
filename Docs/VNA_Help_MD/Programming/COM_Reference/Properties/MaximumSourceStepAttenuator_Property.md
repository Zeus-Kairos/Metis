##### Read only

|

##### [About VNA Options](../../../Support/Configurations.md)  
  
---|---  
  
## MaximumSourceStepAttenuator Property

* * *

#### Description

|  Returns a value for the maximum amount of source attenuation.  
---|---  
  
####  VB Syntax

|  value = cap.MaximumSourceStepAttenuator (n)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Double) \- Variable to store the returned value for the maximum amount of source attenuation.  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (object)  
n |  (Long) - port number to query for the maximum amount of source attenuation  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = cap.MaximumSourceStepAttenuator 2'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MaximumSourceStepAttenuator(long portNumber, double *
attenuation );  
  
#### Interface

|  ICapabilities  
  
* * *

