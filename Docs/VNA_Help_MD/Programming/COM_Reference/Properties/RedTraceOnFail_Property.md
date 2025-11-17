##### Write/Read

|

##### [See Fail Limit
Lines](../../../S4_Collect/Use_Limits_to_Test_Devices.htm#dots)  
  
---|---  
  
## RedTraceOnFail Property

* * *

#### Description

|  Set and return whether to display limit line failures as red trace segments
or red data points (dots).  
---|---  
  
####  VB Syntax

|  pref.RedTraceOnFail = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
bool |  (Boolean) \- Choose from: False \- Display failures as red data points (dots). True \- Display failures as red trace segments. (Red Trace On Fail).  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  pref.RedTraceOnFail = False 'Write  
prefer = pref.RedTraceOnFail 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_RedTraceOnFail( VARIANT_BOOL bValue) HRESULT
get_RedTraceOnFail( VARIANT_BOOL *bValue)  
  
#### Interface

|  IPreferences10  
  
* * *

