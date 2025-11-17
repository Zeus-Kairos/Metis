##### Read only

|

##### [About VNA Options](../../../Support/Configurations.md)  
  
---|---  
  
## MinimumReceiverStepAttenuator Property

* * *

#### Description

|  Returns a value indicating the minimum amount of receiver attenuation.  
---|---  
  
####  VB Syntax

|  value = cap.MinimumReceiverStepAttenuator (n)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Double) \- Variable to store the returned minimum value of receiver attenuation.  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (object)  
n |  (Long) - port number to query for minimum value of receiver attenuation  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = cap.MinimumReceiverStepAttenuator'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULTget_ MinimumReceiverStepAttenuator(long portNumber, double *
attenuation );  
  
#### Interface

|  ICapabilities

