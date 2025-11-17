##### Read-only

|  
---|---  
  
## get_InputVoltage Method Superseded

* * *

#### Description

|  This command is replaced with [get InputVoltageEX
Method](../Properties/InputVoltageEX_Property.htm) Reads the ADC input voltage
from Analog IN (pin 14) of the AUX IO connector.  
---|---  
  
####  VB Syntax

|  volts = AuxIO.get_InputVoltage  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
volts |  (double) - variable to store the return value  
AuxIO |  (object) - A Hardware Auxiliary Input / Output object  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  Dim aux as HWAuxIO Set aux = PNA.getAuxIO  
volts = aux.get_InputVoltage 'read voltage on Analog In (pin 14)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_InputVoltage ( double* Voltage );  
  
#### Interface

|  HWAuxIO  
  
* * *

