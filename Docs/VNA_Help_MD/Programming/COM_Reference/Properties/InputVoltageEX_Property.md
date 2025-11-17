##### Read-only

|  
---|---  
  
## InputVoltageEX Property

* * *

#### Description

|  This command replaces [get InputVoltage
Method](../Methods/get_InputVoltage_Method.htm) Reads the ADC voltage from the
specified location.  
---|---  
  
####  VB Syntax

|  volts = AuxIO.InputVoltageEX loc  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
volts |  (double) - variable to store the return value  
AuxIO |  (object) - A [Hardware Auxiliary Input / Output](../Objects/HWauxIO_Object.md) object  
loc |  (Long) Location from which to read data. For PNA-X models:, reads ADC voltages from the [Power I/O connector](../../../Rear_Panel/XPwrIO.md). Choose from: 1 Reads voltage on Analog In 1 port (pin 7). 2 Reads voltage on Analog In 2 port (pin 8). 3 Reads voltage on GndSens (pin 6). 4 Reads voltage on Analog Out 1 port (pin 3). 5 Reads voltage on Analog Out 2 port (pin 4). For all other VNA models: 1 Reads voltage on the Analog IN (pin 14) of the AUX IO connector. 4 Reads voltage on Analog Out 1 port (pin 3). 5 Reads voltage on Analog Out 2 port (pin 2).  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim aux as HWAuxIO Set aux = PNA.getAuxIO  
volts = aux.InputVoltageEX 1 'for PNA-X, read voltage on PowerI/O pin 7 'for
all other models, reads voltage on Aux I/O Analog In (pin 14)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_InputVoltageEX (long muxLoc, double* vtVoltage );  
  
#### Interface

|  HWAuxIO2  
  
* * *

