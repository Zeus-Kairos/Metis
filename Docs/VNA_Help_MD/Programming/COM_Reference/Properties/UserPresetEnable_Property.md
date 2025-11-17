##### Write/Read

|

##### [About User
Preset](../../../S1_Settings/Preset_the_Analyzer.htm#PresetUserDefined)  
  
---|---  
  
## UserPresetEnable Property

* * *

#### Description

|  'Checks' and 'clears' the enable box on the User Preset dialog box. This
only affects subsequent Presets from the front panel user interface.
Regardless of the state of the User Preset Enable checkbox, the
[app.Preset](../Methods/Preset_Method.md) command will always preset the VNA
to the factory preset settings, and
[app.UserPreset](../Methods/UserPreset_Method.md) will always perform a User
Preset.  
---|---  
  
####  VB Syntax

|  app.UserPresetEnable = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
state |  (boolean) Front Panel User Preset State. Choose from: False  User Preset OFF True  User Preset ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  app.UserPresetEnable = True 'Write  
upreset = app.UserPresetEnable 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_UserPresetEnable(VARIANT_BOOL *pVal)  
HRESULT put_UserPresetEnable(VARIANT_BOOL newVal)  
  
#### Interface

|  IApplication6

