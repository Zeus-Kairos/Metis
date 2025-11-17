# DrawLimitLinesInRed Property

##### Write/Read

|

##### [About Limit Lines](../../../S4_Collect/Use_Limits_to_Test_Devices.md)  
  
---|---  
  
* * *

#### Description

|  Set and return whether to draw limits lines in Red or the trace color.  
---|---  
  
####  VB Syntax

|  pref.DrawLimitLinesInRed = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
value |  (Boolean) \- Choose from: True - All Limit lines are drawn in Red. False - Limit lines are drawn the same color as the trace.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  pref.DrawLimitLinesInRed = True 'Write  
value = pref.DrawLimitLinesInRed 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_DrawLimitLinesInRed (VARIANT_BOOL* preference); HRESULT
put_DrawLimitLinesInRed (VARIANT_BOOL val)  
  
#### Interface

|  IPreferences15  
  
* * *

