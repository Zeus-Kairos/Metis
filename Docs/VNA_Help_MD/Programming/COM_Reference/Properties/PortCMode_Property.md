##### Read/Write

|  
---|---  
  
## PortCMode Property

* * *

#### Description

|  Sets and reads whether Port C is setup for writing or reading data on the
Handler IO connector.  
---|---  
  
####  VB Syntax

|  AuxIO.PortCMode = _value_  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
AuxIO |  (object) - A Hardware Aux I/O object  
value |  (enum as NaPortMode) \- Choose from: 0 - naInput \- set the port for reading 1 - naOutput \- set the port for writing  
  
#### Return Type

|  Enum as NaPortMode  
  
#### Default

|  1 - naInput  
  
#### Examples

|  auxIo.get_PortCMode = naInput 'Write value = auxIo.get_PortCMode 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PortCMode( tagNAPortMode* pMode ); HRESULT put_PortCMode(
tagNAPortMode pMode );  
  
#### Interface

|  IHWAuxIO

