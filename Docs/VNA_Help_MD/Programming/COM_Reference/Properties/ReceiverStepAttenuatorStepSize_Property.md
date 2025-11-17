##### Read only

|

##### [About VNA Options](../../../Support/Configurations.md)  
  
---|---  
  
## ReceiverStepAttenuatorStepSize Property

* * *

#### Description

|  Returns a value indicating the step size of the attenuator.  
---|---  
  
####  VB Syntax

|  value = cap.ReceiverStepAttenuatorStepSize (n)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Double) \- Variable to store the returned value of the attenuator step size.  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (object)  
n |  (Long) - port number to query for the value of the attenuator step size.  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = cap.ReceiverStepAttenuatorStepSize(1)'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ReceiverStepAttenuatorStepSize(long portNumber, double *
stepSize );  
  
#### Interface

|  ICapabilities

