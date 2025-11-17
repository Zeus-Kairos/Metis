##### Write-only

|

##### [About User Preset](../../Using_Macros.md)  
  
---|---  
  
## UserPresetLoadFile Method

* * *

#### Description

| Loads an existing instrument state file (.sta or .cst) to be used for User
Preset. Subsequent execution of [app.UserPreset](UserPreset_Method.md) will
cause the VNA to assume this instrument state. Regardless of the state of the
[User Preset Enable](../../../S1_Settings/Preset_the_Analyzer.md#UserDiag)
checkbox, the [app.Preset](Preset_Method.md) command will always preset the
VNA to the factory preset settings, and
[app.UserPreset](UserPreset_Method.md) will always perform a User Preset.  
---|---  
  
####  VB Syntax

| app.UserPresetLoadFile (file)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app | An [Application](../Objects/Application_Object.md) (object)  
file | (String) Full path, name, and extension of the file to be loaded.  
  
#### Return Type

| Not Applicable  
  
#### Default

| Not Applicable  
  
#### Examples

| app.UserPresetLoadFile ("C:\Program Files\Keysight\Network
Analyzer\Documents\10MHzto20GHz.sta")  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT UserPresetLoadFile (BSTR bstrFile)  
  
#### Interface

| IApplication6

