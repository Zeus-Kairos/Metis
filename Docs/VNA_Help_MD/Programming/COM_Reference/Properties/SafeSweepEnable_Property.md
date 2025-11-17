##### Write/Read

|

##### [About Safe
Sweep](../../../Applications/Gain_Compression_Application.htm#Safe)  
  
---|---  
  
## SafeSweepEnable Property

* * *

#### Description

|  Set and read the (ON | OFF) state of Safe Sweep mode.  
---|---  
  
####  VB Syntax

|  gca.SafeSweepEnable = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value |  (Boolean)  Safe Sweep state. Choose from: False \- Disable Safe Sweep True - Enable Safe Sweep  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  gca.SafeSweepEnable = True 'Write  
SSEnable = gca.SafeSweepEnable 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SafeSweepEnable(VARIANT_BOOL* value) HRESULT
put_SafeSweepEnable(VARIANT_BOOL value)  
  
#### Interface

|  IGainCompression  
  
* * *

