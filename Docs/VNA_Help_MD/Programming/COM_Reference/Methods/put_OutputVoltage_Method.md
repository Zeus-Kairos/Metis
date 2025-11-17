##### Write-only

|  
---|---  
  
## put_OutputVoltage Method

* * *

#### Description

| E836x and PNA-L: Sets voltages on the DAC/Analog Output 1|2 of the Auxiliary
IO connector. PNA-X: Sets voltage on the [Power I/O
connector](../../../Rear_Panel/XPwrIO.htm) AnalogOut1|2. Read output voltages
using [get OutputVoltage Method](get_OutputVoltage_Method.md). Note: The
9-pin PWR I/O (Power I/O) D connector on the rear-panel replaces much of the
functionality of the AUX I/O connector on older VNA models. The Power I/O
voltages can be set using the following methods:  
  
\- [CONTrol:AUXiliary:OUTPut:VOLTage](../../GP-
IB_Command_Finder/ControlAux.htm#output) or put_OutputVoltage Method (no GUI
equivalent, global scoped, and settings not saved as part of the instrument
state)  
\- [SOURce:DC:START](../../GP-IB_Command_Finder/SourceDC.md#start) and
[SOURce:DC:STOP](../../GP-IB_Command_Finder/SourceDC.md#stop) ([DC Source
dialog](../../../S1_Settings/DC_Control.htm#DCControl) is the GUI equivalent,
channel scoped, and settings saved as part of the instrument state)  
\- [Interface Control dialog](../../../System/Interface_Control.md#Aux) (no
remote equivalent, channel scoped, and settings saved as part of the
instrument state)  
  
To avoid unexpected behavior, choose one method only to set the Power I/O
voltages.  
---|---  
  
####  VB Syntax

| AuxIO.put_OutputVoltage output, voltage  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
AuxIO | (object) - A Hardware Auxiliary Input / Output object  
output | (variant) Number of the output DAC to write voltage to. Choose from: 1 Output 1 (Aux I/O pin 3) and (Power I/O pin 3) 2 Output 2 (Aux I/O pin 2) and (Power I/O pin 4)  
voltage | (double) Voltage to write to the output DAC. Choose a voltage from -10 to 10  
  
#### Return Type

| None  
  
#### Default

| None  
  
#### Examples

| HWAuxIO.put_OutputVoltage 1,9 'set Analog Out1 to +9v  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT put_OutputVoltage (VARIANT Output, double Voltage );  
  
#### Interface

| IHWAuxIO  
  
* * *

