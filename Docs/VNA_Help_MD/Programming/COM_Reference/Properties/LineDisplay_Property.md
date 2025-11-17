##### Write/Read

|

##### [About Limits](../../../S4_Collect/Use_Limits_to_Test_Devices.md)  
  
---|---  
  
## LineDisplay Property

* * *

#### Description

|  Turns the display of limit lines ON or OFF. To turn limit TESTING On and
OFF, use [State Property.](State_Property.md) Note: Trace data must be ON to
view limit lines  
---|---  
  
####  VB Syntax

|  limitst.LineDisplay = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
limitst |  A LimitTest (object)  
state |  (boolean)  
False \- Turns the display of limit lines OFF True \- Turns the display of
limit lines ON  
  
#### Return Type

|  Long Integer  
  
#### Default

|  True  
  
#### Examples

|  Limttest.LineDisplay = true 'Write  
lineDsp = Limttest.LineDisplay 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_LineDisplay(VARIANT_BOOL *pVal)  
HRESULT put_LineDisplay(VARIANT_BOOL newVal)  
  
#### Interface

|  ILimitTest

