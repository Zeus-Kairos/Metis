##### Write/Read

|

##### [About External
Devices](../../../System/Configure_an_External_Device.htm)  
  
---|---  
  
## Driver Property

* * *

#### Description

|  Sets and returns the external device driver (model).  
---|---  
  
####  VB Syntax

|  extDevices.Driver = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDevices |  An [ExternalDevice](../Objects/ExternalDevice_Object.md) (object)  
value |  (String) External device driver (model). Choose from the following: "AGPM" for all power meters. "AGPULSEGEN" for supported pulse generators. "DCSource" for all supported DC Sources "DCMeter" for all supported DC Meters [See a list of supported external source drivers.](../../../System/Configure_an_External_Device.md#Supported)  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  extDevices.Driver = "AGESG" 'Write value = extDevices.Driver 'Read See
example program to configure [PMAR
device](../Objects/ExternalDevice_Object.htm) See example program to configure
[External Source](../Objects/ExternalSource_Object.md)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Driver( BSTR* value); HRESULT put_Driver( BSTR newVal);  
  
#### Interface

|  IExternalDevices  
  
* * *

