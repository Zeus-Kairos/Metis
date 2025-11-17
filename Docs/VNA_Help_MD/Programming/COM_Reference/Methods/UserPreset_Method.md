##### Write-only

|

##### [About User Preset](../../Using_Macros.md)  
  
---|---  
  
## UserPreset Method

* * *

#### Description

|  Performs a User Preset. There must be an active User Preset state file (see
[UserPresetLoadFile](UserPresetLoadFile_Method.md) and
[UserPresetSaveState](UserPresetSaveState_Method.md)) or an error will be
returned. Regardless of the state of the [User Preset
Enable](../../../S1_Settings/Preset_the_Analyzer.htm#UserDiag) checkbox, the
[app.Preset](Preset_Method.md) command will always preset the VNA to the
factory preset settings, and [app.UserPreset](UserPreset_Method.md) will
always perform a User Preset.  
---|---  
  
####  VB Syntax

|  app.UserPreset  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  app.UserPreset  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT UserPreset()  
  
#### Interface

|  IApplication6

