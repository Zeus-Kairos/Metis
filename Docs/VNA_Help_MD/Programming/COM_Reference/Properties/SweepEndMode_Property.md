##### Read/Write

## SweepEndMode Property

* * *

#### Description

|  Sets and reads the event that will cause the Sweep End line to go to a low
state. The line will return to a high state after the appropriate calculations
are complete. Note: This line is connected to the [HANDLER IO
connector](../../HandlerIO_Connector.htm).  
---|---  
  
####  VB Syntax

|  object.SweepEndMode = _value_  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  (object) - A HandlerIO or AuxIO object  
value |  (enum as NASweepEndMode ) Choose from: 0 - naSweep - the line goes low when each sweep is complete 1 - naChannelSweep - the line goes low when all the sweeps for each channel is complete. 2 - naGlobalSweep - the line goes low when all sweeps for all [triggerable](JavaScript:hhctrl.TextPopup\('a channel that is not in Hold','Arial,8',10,10,00000000,0xc0ffff\)) channels are complete.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  0 - naSweep  
  
#### Examples

|  HWAuxIO.PassFailMode = naSweep 'Write value = HWAuxIO.PassFailMode 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_SweepEndMode ( tagNASweepEndMode Mode ); HRESULT
get_SweepEndMode ( tagNASweepEndMode* Mode );  
  
#### Interface

|  IHWAuxIO IHWMaterialHandlerIO

