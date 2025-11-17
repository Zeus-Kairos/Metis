##### Write/Read

|

#####  
  
---|---  
  
# ConfirmPreset Property

* * *

#### Description

|  Set and return preset confirmation. If preset confirmation is OFF, pressing
the green PRESET key presets the instrument and opens the Preset softkey menu.
If preset confirmation is ON, pressing the green PRESET causes the Preset menu
to appear.  
---|---  
  
####  VB Syntax

|  pref.ConfirmPreset = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
bool |  (boolean)  
False \- Set preset confirmation to OFF as the default. True - Set preset
confirmation to ON as the default.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  pref.ConfirmPreset = True 'Write  
prefer = pref.ConfirmPreset 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ConfirmPreset(VARIANT_BOOL *presetState)  
HRESULT put_ConfirmPreset(VARIANT_BOOL presetState)  
  
#### Interface

|  IPreferences18

