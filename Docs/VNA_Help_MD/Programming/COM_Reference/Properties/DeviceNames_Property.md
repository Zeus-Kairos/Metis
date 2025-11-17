##### Read-Only

|

##### [About External
Devices](../../../System/Configure_an_External_Device.htm)  
  
---|---  
  
## DeviceNames Property

* * *

#### Description

|  Returns a list of configured device names of the specified device type.  
---|---  
  
####  VB Syntax

|  value = extDevices.DeviceNames(devType)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Variant) Variable to store the device names.  
extDevices |  An [ExternalDevices](../Objects/ExternalDevices_Collection.md) (collection)  
devType |  (String) Device Type such as "Source" and "Power Meter". See a [complete list of valid device types](../../../System/Configure_an_External_Device.md#ExtDevConfig).  
  
#### Return Type

|  Variant Array  
  
#### Default

|  Not Applicable  
  
#### Examples

|  devices = extDevices.DeviceNames("Power Meter" ) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_DeviceNames(VARIANT *names);  
  
#### Interface

|  IExternalDevices2  
  
* * *

