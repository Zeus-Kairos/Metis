##### Write-Read

|

##### [About IO
Configuration](../../Learning_about_GPIB/How_to_Configure_for_GPIB_SCPI_and_SICL.htm)  
  
---|---  
  
## HiSLIPPort Property

* * *

#### Description

|  Set and returns the TCPIP port for HiSLIP communication.  
---|---  
  
####  VB Syntax

|  IOConfig.HiSLIPPort = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
IOConfig |  An [IOConfiguration](../Objects/IOConfiguration_Object.md) object.  
value |  (Long) HiSlip port number.  
  
#### Return Type

|  Long  
  
#### Default

|  4880  
  
#### Examples

|  IOConfig.HiSLIPPort = 4880 'Write value = IOConfig.HiSLIPPort 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get HiSLIPPort(long port); HRESULT put HiSLIPPort(long * port);  
  
#### Interface

|  IIOConfiguration  
  
* * *

