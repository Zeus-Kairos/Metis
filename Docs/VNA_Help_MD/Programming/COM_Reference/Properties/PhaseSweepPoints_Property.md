##### Write/Read

|

##### [About Active Match](../../../Applications/Active_Match.md)  
  
---|---  
  
# PhaseSweepPoints Property

* * *

#### Description

|  Set and read the number of phase points. For the tuning tone at the output,
a phase sweep is done for each point.  
---|---  
  
####  VB Syntax

|  HotS22.PhaseSweepPoints = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
HotS22 |  A [ActiveParametersApp](../Objects/HotS22App_Object.md) (object)  
value |  (Long) - Number of phase points. Do not exceed the max number of phase points (50).  
  
#### Return Type

|  Long  
  
#### Default

|  8  
  
#### Examples

|  HotS22.PhaseSweepPoints = 201 'Write  
value = HotS22.PhaseSweepPoints 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PhaseSweepPoints(long* value) HRESULT put_PhaseSweepPoints(long
value)  
  
#### Interface

|  IActiveChannelSettings  
  
* * *

