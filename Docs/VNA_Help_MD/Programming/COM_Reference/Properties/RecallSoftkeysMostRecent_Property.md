##### Write/Read

|

##### [About Preferences](../../../System/Preferences.md#PresetPower)  
  
---|---  
  
## RecallSoftkeysMostRecent Property

* * *

#### Description

|  Set and return whether to list files for recall on softkeys by most-
recently used or alphabetically.  
---|---  
  
####  VB Syntax

|  pref.RecallSoftkeysMostRecent = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
value |  (Boolean)  Choose from: True  Recall softkeys show most recently-used files. False  Recall softkeys show alphabetically-ordered files.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  pref.RecallSoftkeysMostRecent = False 'Write  
recallPref = pref.RecallSoftkeysMostRecent 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_RecallSoftkeysMostRecent(VARIANT_BOOL * pVal); HRESULT
put_RecallSoftkeysMostRecent(VARIANT_BOOL pVal);  
  
#### Interface

|  IPreferences13  
  
* * *

