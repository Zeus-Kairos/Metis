##### Write/Read

|

##### [About Preferences](../../../System/Preferences.md#PresetPower)  
  
---|---  
  
## PresetPowerState Property

* * *

#### Description

|  Set and return the Preset Power ON/OFF state.  
---|---  
  
####  VB Syntax

|  pref.PresetPowerState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
value |  (Enum as NAPowerStates) - Choose from: naPowerON (0) \- Instrument Preset always turns RF power ON. naPowerAUTO (1):

  * When the current power setting is OFF, leave power OFF at Preset.
  * When the current power setting is ON, turn power ON at Preset.

  
  
#### Return Type

|  enum  
  
#### Default

|  naPowerON (0)  
  
#### Examples

|  pref.PresetPowerState = naPowerON 'Write  
pwrState = pref.PresetPowerState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PresetPowerState(tagNAPowerStates* pVal);  
HRESULT put_PresetPowerState(tagNAPowerStates pVal);  
  
#### Interface

|  IPreferences11  
  
* * *

