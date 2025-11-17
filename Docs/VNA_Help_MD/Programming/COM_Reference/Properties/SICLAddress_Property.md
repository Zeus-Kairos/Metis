##### Write-Read

|

##### [Configuring the analyzer for
SICL/VISA](../../Learning_about_GPIB/Configure_for_VISA_and_SICL.htm)  
  
---|---  
  
## SICLAddress Property

* * *

#### Description

|  Sets and returns the VNA SICL address. This is the address used for SICL
over LAN.  
---|---  
  
####  VB Syntax

|  app.SICLAddress = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
value |  (Integer) SICL Address of the VNA. Choose a value between 0 and 30.  
  
#### Return Type

|  Short Integer  
  
#### Default

|  16  
  
#### Examples

|  address=app.SICLAddress 'Read  
app.SICLAddress=16 'Write  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SICLAddress(short busIndex, short* address); HRESULT
put_SICLAddress(short busIndex,short address);  
  
#### Interface

|  IApplication8

