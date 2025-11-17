##### Write/Read

|

##### [About ECal
Extrapolation](../../../Applications/Swept_IMD.htm#ECalExtrap)  
  
---|---  
  
## IMDECalExtrapolation Property

* * *

#### Description

|  Sets whether a Swept IMD or IMDx calibration can exceed the stop frequency
limit of an ECal module.  
---|---  
  
####  VB Syntax

|  pref.IMDECalExtrapolation = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
bool |  (Boolean) \- Choose from: False \- Do NOT allow extrapolation. True \- Allow extrapolation.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  pref.IMDECalExtrapolation = False 'Write  
prefer = pref.IMDECalExtrapolation 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_IMDECalExtrapolation( VARIANT_BOOL bExtrap) HRESULT
get_IMDECalExtrapolation( VARIANT_BOOL *bExtrap)  
  
#### Interface

|  IPreferences14  
  
* * *

