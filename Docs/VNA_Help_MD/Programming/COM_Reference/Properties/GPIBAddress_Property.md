##### Write-Read

|

##### [About GPIB Fundamentals](../../Learning_about_GPIB/GP-
IB_Fundamentals.htm)  
  
---|---  
  
## GPIBAddress Property

* * *

#### Description

|  Sets and returns the VNA GPIB address on the talker/listener bus.  
---|---  
  
####  VB Syntax

|  app.GPIBAddress (bus) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
bus |  (Short Integer) GPIB bus. MUST be set to 0 - the talker/listener bus.  
value |  (Short Integer) GPIB Address on the VNA. Choose a value between 0 and 30.  
  
#### Return Type

|  Short Integer  
  
#### Default

|  16  
  
#### Examples

|  address=app.GPIBAddress(0) 'Read  
app.GPIBAddress(0)=16 'Write  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_GPIBAddress(short busIndex, short* address); HRESULT
put_GPIBAddress(short busIndex,short address);  
  
#### Interface

|  IApplication8  
  
* * *

* * *

