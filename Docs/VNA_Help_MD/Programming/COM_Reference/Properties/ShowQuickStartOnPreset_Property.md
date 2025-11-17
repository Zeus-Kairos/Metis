# ShowQuickStartOnPreset Property

##### Write/Read

|  
---|---  
  
* * *

#### Description

|  This command controls the on/off state of the preference, "On PRESET show
Quick Start dialog".  
---|---  
  
####  VB Syntax

|  pref.ShowQuickStartOnPreset = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
value |  (Boolean) \- Choose from: True - Display the Quick Start dialog on PRESET. False - Do not display the Quick Start dialog on PRESET.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  pref.ShowQuickStartOnPreset = True 'Write  
value = pref.ShowQuickStartOnPreset 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ShowQuickStartOnPreset (VARIANT_BOOL* preference); HRESULT
put_ShowQuickStartOnPreset (VARIANT_BOOL val);  
  
#### Interface

|  IPreferences13  
  
* * *

