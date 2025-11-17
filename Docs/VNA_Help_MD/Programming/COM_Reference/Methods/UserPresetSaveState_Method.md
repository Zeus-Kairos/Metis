##### Write-only

|

##### [About User Preset](../../Using_Macros.md)  
  
---|---  
  
## UserPresetSaveState Method

* * *

#### Description

|  Saves the current instrument settings as UserPreset.sta. Subsequent
execution of [app.UserPreset](UserPreset_Method.md) will cause the VNA to
assume this instrument state. Regardless of the state of the [User Preset
Enable](../../../S1_Settings/Preset_the_Analyzer.htm#UserDiag) checkbox, the
[app.Preset](Preset_Method.md) command will always preset the VNA to the
factory preset settings, and [app.UserPreset](UserPreset_Method.md) will
always perform a User Preset.  
---|---  
  
####  VB Syntax

|  app.UserPresetSaveState  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  app.UserPresetSaveState  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT UserPresetSaveState()  
  
#### Interface

|  IApplication6

