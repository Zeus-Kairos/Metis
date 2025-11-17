##### Write/Read

|

##### [About External
Devices](../../../System/Configure_an_External_Device.htm)  
  
---|---  
  
## DeviceType Property

* * *

#### Description

|  Sets and returns the DeviceType for the external device.  
---|---  
  
####  VB Syntax

|  extDevices.DeviceType = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDevices |  An [ExternalDevice](../Objects/ExternalDevice_Object.md) (object)  
value |  (String) Device Type. "Source" \- external source "Power Meter" \- power meter "DC Meter" \- DC voltmeter "DC Source" \- DC power supply "Pulse Generator" \- external pulse generator  
  
#### Return Type

|  String  
  
#### Default

|  "Unknown"  
  
#### Examples

|  extDevices.DeviceType = "source" Write value = extDevices.DeviceType 'Read
See example program to configure [PMAR
device](../Objects/ExternalDevice_Object.htm) See example program to configure
[External Source](../Objects/ExternalSource_Object.md)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_DeviceType( BSTR* value); HRESULT put_DeviceType( BSTR newVal);  
  
#### Interface

|  IExternalDevices  
  
* * *

