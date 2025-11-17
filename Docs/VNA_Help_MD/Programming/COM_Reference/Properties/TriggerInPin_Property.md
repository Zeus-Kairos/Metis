##### Write/Read

|

##### [About Ext DC Devices](../../../System/Configure_a_DC_Device.md)  
  
---|---  
  
## TriggerInPin Property

* * *

#### Description

|  When Trigger mode is set to Hardware List for SMU devices, this command
sets and returns the B2900 Digital IO pin to use for Trigger IN.  
---|---  
  
####  VB Syntax

|  extDC.TriggerInPin = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDC |  An [ExternalDCDevice](../Objects/ExternalDCDevice_Object.md) (object)  
value |  (Long) Pin number for Trigger IN. Choose a pin number from 1 to 14.  
  
#### Return Type

|  Long  
  
#### Default

|  1  
  
#### Examples

|  extDC.TriggerInPin = 3 'Write  
bool = extDC.TriggerInPin 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_TriggerInPin (Long *pValue) HRESULT put_TriggerInPin (long
newVal)  
  
#### Interface

|  IExternalDCDevice2  
  
* * *

