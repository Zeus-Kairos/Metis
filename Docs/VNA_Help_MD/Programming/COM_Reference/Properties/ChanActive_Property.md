##### Write/Read

|

##### [About External SMU
Devices](../../../System/Configure_an_External_SMU.htm)  
  
---|---  
  
# ChanActive Property

* * *

#### Description

|  Set and return the state of activation of the SMU device.  
---|---  
  
####  VB Syntax

|  extSMU.ChanActive <chanNum>,<value>  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extSMU |  An [ExteranlSMUDevice](../Objects/ExternalSMUDevice_Object.md) (object)  
<chanNum> |  Channel number for the external SMU  
<value> |  (Boolean) Choose from: True \- Channel is active. False \- Channel is NOT active.  
  
#### Return Type

|  Boolean  
  
#### Default

|  Not applicable  
  
#### Examples

|  extSMU.ChanActive = 2,True 'Write  
variable = extSMU.ChanActive 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ChanActive( long chanNum, VARIANT_BOOL* value) HRESULT
put_ChanActive( long chanNum, VARIANT_BOOL value)  
  
#### Interface

|  IExternalSMUDevice

