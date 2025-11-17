##### Write/Read

|

##### [About External
Devices](../../../System/Configure_an_External_Device.htm)  
  
---|---  
  
## IOConfiguration Property

* * *

#### Description

|  Sets and returns the method of communication and address for the external
device.  
---|---  
  
####  VB Syntax

|  extDevices.IOConfiguration = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDevices |  An [ExternalDevice](../Objects/ExternalDevice_Object.md) (object)  
value |  (String) Configuration path. Any valid VISA resource shown in the IO Configuration field of the [External Devices dialog](../../../System/Configure_an_External_Device.md#ExtDevConfig), enclosed in quotes. Do NOT use the ID string of a PMAR USB power sensor as the resource string. The ID string is returned by the [USBPowerMeterCatalog Property](USBPowerMeterCatalog_Property.md)  
  
#### Return Type

|  String  
  
#### Default

|  " " Empty String  
  
#### Examples

|  extDevices.IOConfiguration = "TCPIP::141.121.76.239::inst0::INSTR" Write
value = extDevices.IOConfiguration 'Read See example program to configure
[PMAR device](../Objects/ExternalDevice_Object.md) See example program to
configure [External Source](../Objects/ExternalSource_Object.md)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_IOConfiguration( BSTR* value); HRESULT put_IOConfiguration(
BSTR newVal);  
  
#### Interface

|  IExternalDevices  
  
* * *

