##### Write/Read

|

##### [About Active Match](../../../Applications/Active_Match.md)  
  
---|---  
  
# StopPowerIn3DSweep Property

* * *

#### Description

|  Set and read the stop power level for a 3D sweep.  
---|---  
  
####  VB Syntax

|  HotS22.StopPowerIn3DSweep = level  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
HotS22 |  A [ActiveParameterApp](../Objects/HotS22App_Object.md) (object)  
level |  (Double) - Stop power level in dBm. Choose a value from min power to max power of the hardware.  
  
#### Return Type

|  Double  
  
#### Default

|  0 dBm  
  
#### Examples

|  HotS22.StopPowerIn3DSweep = 0 'Write  
level = HotS22.StopPowerIn3DSweep 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_StopPowerIn3DSweep(double* level) HRESULT
put_StopPowerIn3DSweep(double level)  
  
#### Interface

|  IActiveChannelSettings  
  
* * *

