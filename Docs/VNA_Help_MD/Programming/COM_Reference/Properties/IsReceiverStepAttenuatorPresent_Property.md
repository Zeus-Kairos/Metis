##### Read only

|

##### [About VNA Options](../../../Support/Configurations.md)  
  
---|---  
  
## IsReceiverStepAttenuatorPresent Property

* * *

#### Description

|  Returns a value indicating the presence of Receiver step attenuators in the
remote VNA.  
---|---  
  
####  VB Syntax

|  value = cap.IsReceiverStepAttenuatorPresent (n)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Boolean) \- Variable to store the returned value. True - Receiver step attenuators are present. False - Receiver step attenuators are not present.  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (object)  
n |  (Long) - port number to query for step attenuators  
  
#### Return Type

|  Boolean  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = cap.IsReceiverStepAttenuatorPresent(1)'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_IsReceiverStepAttenuatorPresent(long portNumber, VARIANT_BOOL *
present );  
  
#### Interface

|  ICapabilities

