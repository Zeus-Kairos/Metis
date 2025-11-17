##### Write-Read

|

##### [About IO
Configuration](../../Learning_about_GPIB/How_to_Configure_for_GPIB_SCPI_and_SICL.htm)  
  
---|---  
  
## HiSLIPAddress Property

* * *

#### Description

|  Set and returns HiSLIP instrument number.  
---|---  
  
####  VB Syntax

|  IOConfig.HiSLIPAddress = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
IOConfig |  An [IOConfiguration](../Objects/IOConfiguration_Object.md) object.  
value |  (Long) HiSLIP instrument number.  
  
#### Return Type

|  Long  
  
#### Default

|  0 (which renders "inst0")  
  
#### Examples

|  IOConfig.HiSLIPAddress = 1 'Write value = IOConfig.HiSLIPAddress 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get HiSLIPAddress(long Address); HRESULT put HiSLIPAddress(long *
Address);  
  
#### Interface

|  IIOConfiguration  
  
* * *

