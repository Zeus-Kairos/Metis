##### Write/Read

|

##### [About Active Match](../../../Applications/Active_Match.md)  
  
---|---  
  
# PowerStepsIn3DSweep Property

* * *

#### Description

|  Set and read the number of power steps for a 3D sweep.  
---|---  
  
####  VB Syntax

|  HotS22.PowerStepsIn3DSweep = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
HotS22 |  A [ActiveParametersApp](../Objects/HotS22App_Object.md) (object)  
value |  (Long) - Number of power steps. The range is 2 to 20001.  
  
#### Return Type

|  Long  
  
#### Default

|  201  
  
#### Examples

|  HotS22.PowerStepsIn3DSweep = 201 'Write  
value = HotS22.PowerStepsIn3DSweep 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PowerStepsIn3DSweep(long* value) HRESULT
put_PowerStepsIn3DSweep(long value)  
  
#### Interface

|  IActiveChannelSettings  
  
* * *

