##### Write-only

|

##### [About External
Devices](../../../System/Configure_an_External_Device.htm)  
  
---|---  
  
## Add (External Device) Method

* * *

#### Description

|  Adds an external device to the system. This is the same as clicking the New
button and editing the name on the Configure an External Device dialog. Upon
creation, all settings on the new device are set to the defaults. The device
is not active until set using
[Ext.Dev.Active.](../Properties/Active_ExtDev_Property.md)  
---|---  
  
#### VB Syntax

|  extDevices.Add name  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDevices |  An [ExternalDevices](../Objects/ExternalDevices_Collection.md) (collection)  
name |  (String) - Name of the new external device.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  extDevices.Add 'MySource' 'Creates a new external device  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT Add (BSTR name)  
  
#### Interface

|  IExternalDevices  
  
* * *

