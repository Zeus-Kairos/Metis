##### Read-only

## get OutputVoltageMode Method

* * *

#### Description

|  This command returns the mode of the selected "Analog Out" line on the
[Power I/O connector](../../../Rear_Panel/XPwrIO.md). The modes give the user
the option to have the requested voltage applied immediately or not until the
sweep is done. To set the mode, use [put_OutputVoltageMode
Method](put_OutputVoltageMode_Method.htm).  
---|---  
  
####  VB Syntax

|  mode = auxIo.get_OutputVoltageMode (output)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mode |  (enum NAOutputVoltageMode ) - variable to store the returned mode. naWaitEOS \- While in this mode any voltage changes sent to the selected analog out will only get applied to the output between sweeps. naNoWait \- While in this mode any voltage changes sent to the selected analog out will occur right away without waiting until the end of a sweep, the voltage gets applied immediately.  
auxIo |  (object) - A Hardware Auxiliary Input / Output object  
output |  (double) Analog Output. Choose from 1 or 2  
  
#### Return Type

|  enum as NAOutputVoltageMode  
  
#### Default

|  naWaitEOS  
  
#### Examples

|  vOutMode = auxIo.get_OutputVoltageMode (1)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_OutputVoltageMode(VARIANT Output, tagNAOutputVoltageMode*
pMode);  
  
#### Interface

|  IHWAuxIO  
  
* * *

