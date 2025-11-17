##### Write-only

# put_OutputVoltageMode Method

* * *

#### Description

|  This command sets the mode of the selected "Analog Out" line on the [Power
I/O connector](../../../Rear_Panel/XPwrIO.htm). The modes give the user the
option to have the requested voltage applied immediately or not until the
sweep is done. To read the mode on each output use [get_OutputVoltageMode
Method](get_OutputVoltageMode_Method.htm).  
---|---  
  
####  VB Syntax

|  auxIo.put_OutputVoltageMode (output, mode)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
auxIo |  (Object) An AuxIO object  
output |  Analog Output to receive mode setting. Choose from 1 or 2  
mode |  (enum NAOutputVoltageMode ) naWaitEOS \- While in this mode any voltage changes sent to the selected analog out will only get applied to the output between sweeps. naNoWait \- While in this mode any voltage changes sent to the selected analog out will occur right away without waiting until the end of a sweep, the voltage gets applied immediately.  
  
#### Return Type

|  NAOutputVoltageMode  
  
#### Default

|  naWaitEOS  
  
#### Examples

|  auxIo.put_OutputVoltageMode 1, naWaitEOS 'Write  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_OutputVoltageMode(VARIANT Output, tagNAOutputVoltageMode
dNewMode);  
  
#### Interface

|  IHWAuxIO  
  
* * *

