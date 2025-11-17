##### Read-only

|  
---|---  
  
## get_OutputVoltage Method

* * *

#### Description

|  E836x and PNA-L: Reads voltages on the DAC/Analog Output 1|2 of the
Auxiliary IO connector. PNA-X: Reads voltage on the [Power I/O
connector](../../../Rear_Panel/XPwrIO.htm) AnalogOut1|2.  
---|---  
  
####  VB Syntax

|  volts = AuxIO.get_OutputVoltage (output)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
volts |  (double) - variable to store the return value  
AuxIO |  (object) - A Hardware Auxiliary Input / Output object  
output |  (variant) Number of the output DAC from which to read voltage. Choose from: 1 Output 1 (Aux I/O pin 3) and (Power I/O pin 3) 2 Output 2 (Aux I/O pin 2) and (Power I/O pin 4)  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim aux as HWAuxIO Set aux = PNA.getAuxIO volts = aux.get_OutputVoltage(1)
'read voltage from Analog Out 1 (Aux I/O pin3) or (Power I/O pin 3)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_OutputVoltage( VARIANT Output, double* Voltage );  
  
#### Interface

|  IHWAuxIO  
  
* * *

