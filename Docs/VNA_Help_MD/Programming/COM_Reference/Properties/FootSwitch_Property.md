##### Read-only

## FootSwitch Property

* * *

#### Description

|  Reads the Footswitch Input (pin 20 of the AUX IO connector).  
---|---  
  
####  VB Syntax

|  value = AuxIO.Footswitch  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (boolean) - Variable to store the returned value **False** \- foot switch is released **True** \- footswitch is depressed  
AuxIO |  (object) - A Hardware Aux I/O object  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  fs = aux.Footswitch  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_FootSwitch ( VARIANT_BOOL* State );  
  
#### Interface

|  IHWAuxIO

