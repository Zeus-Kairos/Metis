##### Write/Read

|

##### [About GPIB Fundamentals](../../Learning_about_GPIB/GP-
IB_Fundamentals.htm)  
  
---|---  
  
## GPIBMode Property

* * *

#### Description

|  Changes the analyzer to a GPIB system controller or a talker/listener on
the bus. The analyzer must be the controller if you want to use it to send
commands to other instruments. The analyzer must be a talker/listener if you
want to send it commands from another PC. Note: This command has no affect in
VNAs with dedicated Controller and Talker/Listener GPIB connectors.  
---|---  
  
####  VB Syntax

|  app.GPIBMode value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
value |  (enum NAGPIBMode) -Choose either:  
0 - naTalkerListener \- the analyzer is a talker / listener  
1 - naSystemController - the analyzer is the system controller  
  
#### Return Type

|  Long Integer  
  
#### Default

|  0 - naTalkerListener  
  
#### Examples

|  app.GPIBMode = naTalkerListener 'Write  
mode = app.GPIBMode 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_GPIBMode(tagGPIBModeEnum* eGpibMode)  
HRESULT put_GPIBMode(tagGPIBModeEnum eGpibMode)  
  
#### Interface

|  IApplication  
  
* * *

