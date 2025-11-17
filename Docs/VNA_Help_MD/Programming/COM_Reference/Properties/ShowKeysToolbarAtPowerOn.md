# ShowKeysToolbarAtPowerOn Property

##### Write/Read

|  
---|---  
  
* * *

#### Description

|  This command controls the on/off state of the preference, "On Power-on show
Keys toolbar".  
---|---  
  
####  VB Syntax

|  pref.ShowKeysToolbarAtPowerOn = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
value |  (Boolean) \- Choose from: True - Display the keys toolbar on power-on. False - Do not display the keys toolbar on power-on.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  pref.ShowKeysToolbarAtPowerOn = True 'Write  
value = pref.ShowKeysToolbarAtPowerOn 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ShowKeysToolbarAtPowerOn (VARIANT_BOOL* preference); HRESULT
put_ShowKeysToolbarAtPowerOn (VARIANT_BOOL val);  
  
#### Interface

|  IPreferences16  
  
* * *

