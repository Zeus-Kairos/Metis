# MarkCoupPresetIsOn Property

##### Write/Read

|

##### [About Limit Lines](../../../S4_Collect/Use_Limits_to_Test_Devices.md)  
  
---|---  
  
* * *

#### Description

|  Set and return whether Coupled Markers is set to ON or OFF after Preset.
[Learn more about Coupled
Markers](../../../S4_Collect/Markers.htm#Coupled_Markers).  
---|---  
  
####  VB Syntax

|  pref.MarkCoupPresetIsOn = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
value |  (Boolean) \- Choose from: True - Coupled Markers is ON after Preset.  False - Coupled Markers is OFF after Preset.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  pref.MarkCoupPresetIsOn = True 'Write  
value = pref.MarkCoupPresetIsOn 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MarkCoupPresetIsOn (VARIANT_BOOL* preference); HRESULT
put_MarkCoupPresetIsOn (VARIANT_BOOL val)  
  
#### Interface

|  IPreferences15  
  
* * *

