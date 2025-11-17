# MarkCoupMethPresetIsChan Property

##### Write/Read

|

##### [About Limit Lines](../../../S4_Collect/Use_Limits_to_Test_Devices.md)  
  
---|---  
  
* * *

#### Description

|  Set and return whether Coupled Markers is set to Channel or All after
Preset. [Learn more about Coupled
Markers](../../../S4_Collect/Markers.htm#Coupled_Markers). Refer also to
[CoupledMarkers Property](CoupledMarkers_Property.md) and
[MarkCoupPresetIsOn](MarkCoupPresetIsOn_Property.md).  
---|---  
  
####  VB Syntax

|  pref.MarkCoupMethPresetIsChan = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
value |  (Boolean) \- Choose from: True - Marker Coupling Method is set to Channel after Preset. False -  Marker Coupling Method is set to ALL after Preset.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  pref.MarkCoupMethPresetIsChan = True 'Write  
value = pref.MarkCoupMethPresetIsChan 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MarkCoupMethPresetIsChan (VARIANT_BOOL* preference); HRESULT
put_MarkCoupMethPresetIsChan (VARIANT_BOOL val)  
  
#### Interface

|  IPreferences15  
  
* * *

