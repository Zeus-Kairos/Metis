##### Write/Read

|

##### [About External
Devices](../../../System/Configure_an_External_Device.htm)  
  
---|---  
  
## Name (ExternalDevice) Property

* * *

#### Description

|  Sets and returns the name of the External Device.  
---|---  
  
####  VB Syntax

|  extDev.Name = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
extDev |  A [ExternalDevice Object](../Objects/ExternalDevice_Object.md) (object).  
value |  (string) \- External Device name. Any string name limited to alpha-numeric characters.  
  
#### Return Type

|  String  
  
#### Default

|  Device<n>  
  
#### Examples

|  extDev.Name = "MySource" 'Write  
extDevName = extDev.Name 'Read See example program to configure [PMAR
device](../Objects/ExternalDevice_Object.htm) See example program to configure
[External Source](../Objects/ExternalSource_Object.md)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Name(BSTR *pVal) HRESULT put_Name(BSTR newVal)  
  
#### Interface

|  IExternalDevice  
  
* * *

