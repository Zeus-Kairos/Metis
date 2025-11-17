##### Write/Read

|

##### [About External
Devices](../../../System/Configure_an_External_Device.htm)  
  
---|---  
  
## IOEnable Property

* * *

#### Description

|  Sets and returns whether an external device is enabled for IO communication
with the VNA. When disabled (False), the VNA will NOT attempt to connect to
the external device regardless of the instrument state
([Active)](Active_ExtDev_Property.md).property. Therefore, no errors will be
produced if the device is not connected. This command is useful for debugging
and testing states when the external device is not connected. This command is
unnecessary in ordinary operation (when the device is connected).  
---|---  
  
####  VB Syntax

|  extDevices.IOEnable = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDevices |  An [ExternalDevice](../Objects/ExternalDevice_Object.md) (object)  
value |  (Boolean) Choose from: True \- Device is available for IO communication. False \- Device is NOT available for IO communication.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  extDevices.IOEnable = True 'Write bool = extDevices.IOEnable 'Read See
example program to configure [PMAR
device](../Objects/ExternalDevice_Object.htm) See example program to configure
[External Source](../Objects/ExternalSource_Object.md)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_IOEnable( VARIANT_BOOL* value); HRESULT put_IOEnable(
VARIANT_BOOL newVal);  
  
#### Interface

|  IExternalDevices  
  
* * *

