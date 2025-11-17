##### Write/Read

|

##### [About External
Devices](../../../System/Configure_an_External_Device.htm)  
  
---|---  
  
## TimeOut Property

* * *

#### Description

|  Sets and returns the Time out value for communication with the external
device. An error is returned if communication with the device is not
successful within this period of time.  
---|---  
  
####  VB Syntax

|  extDevices.TimeOut = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDevices |  An [ExternalDevice](../Objects/ExternalDevice_Object.md) (object)  
value |  (Double) Time out in milliseconds.  
  
#### Return Type

|  Double  
  
#### Default

|  20000 milliseconds (20 seconds)  
  
#### Examples

|  extDevices.TimeOut = 1000 Write value = extDevices.TimeOut 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_TimeOut(Double* value); HRESULT put_TimeOut(Double newVal);  
  
#### Interface

|  IExternalDevices  
  
* * *

