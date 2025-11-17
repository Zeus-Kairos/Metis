##### Write only  
  
---  
  
## LoadFile Method

* * *

#### Description

|  Recalls an external device configuration file from the VNA hard drive.
Currently, only DC Supply and DC Meter configuration files are supported. See
more [DC Device commands](../Objects/ExternalDCDevice_Object.md).  
---|---  
  
####  VB Syntax

|  extDev.LoadFile (filename)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDev |  An [ExternalDevice](../Objects/ExternalDevice_Object.md) Object  
filename |  (String) File name and .xml extension of the external device configuration file. Currently, only DC Supply and DC Meter configuration files are supported. See more [DC Device commands](../Objects/ExternalDCDevice_Object.md).  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  extDev.LoadFile "MyDCSupply"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT LoadFile(BSTR newVal)  
  
#### Interface

|  IExternalDevice  
  
* * *

* * *

