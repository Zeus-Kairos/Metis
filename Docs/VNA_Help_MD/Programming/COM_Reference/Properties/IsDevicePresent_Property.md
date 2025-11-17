##### Read-Only

|

##### [About External
Devices](../../../System/Configure_an_External_Device.htm)  
  
---|---  
  
## IsDevicePresent Property

* * *

#### Description

|  Returns whether the named device is present on the bus for which it is
configured.  
---|---  
  
####  VB Syntax

|  value = extDevices.IsDevicePresent(devName)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Boolean) Variable to store the returned value:

  * False \- The device is not in the collection or the device fails to respond and times out when communication is attempted.
  * True \- The device responds when communication is attempted.

  
extDevices |  An [ExternalDevices](../Objects/ExternalDevices_Collection.md) (collection)  
devName |  (String) Name of the device with which you want to communicate.  
  
#### Return Type

|  Boolean  
  
#### Default

|  Not Applicable  
  
#### Examples

|  present = extDevices.IsDevicePresent("MyPowerMeter" ) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_IsDevicePresent(VARIANT_BOOL *present);  
  
#### Interface

|  IExternalDevices2  
  
* * *

