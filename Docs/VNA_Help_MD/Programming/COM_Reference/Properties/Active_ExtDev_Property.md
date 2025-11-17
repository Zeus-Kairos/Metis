##### Write/Read

|

##### [About External
Devices](../../../System/Configure_an_External_Device.htm)  
  
---|---  
  
## Active (ExtDev) Property

* * *

#### Description

|  Set and return the state of activation of the device. When
[extDev.IOEnable](IOEnable_Property.md) = True, and this command is set to
True, the VNA will attempt communication with the external device. An error is
returned if communication cannot be verified. Note: Send this command AFTER
sending other External Device settings to avoid communicating with the device
before it has been fully configured. See Also [ExternalDeviceDeActivatePolicy
Property](ExternalDeviceDeActivatePolicy_Property.htm) \- Determines whether
External Devices remain activated or are de-activated when the VNA is Preset
or when a Instrument State is recalled.  
---|---  
  
####  VB Syntax

|  extDevices.Active = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDevices |  An [ExternalDevice](../Objects/ExternalDevice_Object.md) (object)  
value |  (Boolean) Choose from: True \- Device is active. False \- Device is NOT active.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False - When configured using the front panel user interface, the device is
ON (activated) by default.  
  
#### Examples

|  extDevices.Active = True 'Write bool = extDevices.Active 'Read See example
program to configure [PMAR device](../Objects/ExternalDevice_Object.md) See
example program to configure [External
Source](../Objects/ExternalSource_Object.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Active( VARIANT_BOOL* value); HRESULT put_Active( VARIANT_BOOL
newVal);  
  
#### Interface

|  IExternalDevices  
  
* * *

  

