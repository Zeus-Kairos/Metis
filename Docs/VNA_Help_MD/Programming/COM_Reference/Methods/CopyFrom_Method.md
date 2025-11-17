##### Write-only

|

##### [About Path Configuration](../../../S1_Settings/Path_Configurator.md)  
  
---|---  
  
## CopyFrom Method

* * *

#### Description

|  Copies the mechanical switch and attenuator settings from the specified
channel to the calling channel. To avoid potential conflicts, all port
couplings in the calling channel will be turned OFF and all port attenuator
settings will be set to manual before copying the switch or attenuator
settings. The two channels CAN be of different measurement classes. Use
[CopyToChannel](CopyToChannel_Method.md) to copy ALL settings from one
channel to another.  
---|---  
  
####  VB Syntax

|  pathConfig.CopyFrom (chanNum)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pathConfig |  A [PathConfiguration](../Objects/PathConfiguration_Object.md) (object)  
chanNum |  (long integer) Channel number to copy to the calling channel.  
  
#### Return Type

|  None  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim chan,pathConfig Set chan = app.ActiveChannel Set pathConfig =
chan.PathConfiguration pathConfig.CopyFrom 2  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT CopyFrom(long chanNum);  
  
#### Interface

|  IPathConfiguration2  
  
* * *

Last modified:

New topic  
---  
  
* * *

