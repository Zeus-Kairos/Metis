##### Write/Read

|

##### [About DC Sources](../../../S1_Settings/DC_Control.md)  
  
---|---  
  
## EnableAllOutput Property

* * *

#### Description

|  Sets and returns the ON / OFF state of all DC sources for the channel.  
---|---  
  
####  VB Syntax

|  dc.EnableAllOutput = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
dc |  An [DCStimulus](../Objects/DCStimulus_Object.md) (object)  
state |  (boolean) True \- All DC sources ON False \- All DC sources OFF  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  dc.EnableAllOutput = True 'Write  
value = dc.EnableAllOutput 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_EnableAllOutput(VARIANT_BOOL * pValue); HRESULT
put_EnableAllOutput(VARIANT_BOOL newValue);  
  
#### Interface

|  IDCStimulus  
  
* * *

* * *

