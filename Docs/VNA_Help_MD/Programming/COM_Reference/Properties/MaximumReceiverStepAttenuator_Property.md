##### Read only

|

##### [About VNA Options](../../../Support/Configurations.md)  
  
---|---  
  
## MaximumReceiverStepAttenuator Property

* * *

#### Description

|  Returns the maximum amount of receiver attenuation.  
---|---  
  
####  VB Syntax

|  value = cap.MaximumReceiverStepAttenuator (n)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Double) \- Variable to store the returned value of maximum receiver attenuation.  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (object)  
n |  (Long) - port number to query for step attenuators  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = cap.MaximumReceiverStepAttenuator'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MaximumReceiverStepAttenuator(long portNumber, double *
attenuation );  
  
#### Interface

|  ICapabilities

