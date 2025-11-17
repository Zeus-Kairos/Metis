##### Write/Read

|

##### [About Active Match](../../../Applications/Active_Match.md)  
  
---|---  
  
# DisplayInterpolationState Property

* * *

#### Description

|  Sets whether or not interpolation is on for display. Frequency, power, and
phase X axis are supported for display. Interpolation may be applied in the
trace.  
---|---  
  
####  VB Syntax

|  HotS22.DisplayInterpolationState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
HotS22 |  A [ActiveParametersApp](../Objects/HotS22App_Object.md) (object)  
value |  (boolean) - Choose from: True \- Turns interpolation ON False \- Turns interpolation OFF  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  HotS22.DisplayInterpolationState = False  
value = HotS22.DisplayInterpolationState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_DisplayInterpolationState(VARIANT_BOOL* value);  
HRESULT put_DisplayInterpolationState(VARIANT_BOOL value);  
  
#### Interface

|  IActiveChannelSettings  
  
* * *

