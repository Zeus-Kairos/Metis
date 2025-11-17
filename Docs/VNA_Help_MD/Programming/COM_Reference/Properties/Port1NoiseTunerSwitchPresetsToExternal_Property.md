##### Write/Read

|

##### [See Noise Figure Block Diagram](../../../Applications/Noise_Figure.md)  
  
---|---  
  
## Port1NoiseTunerSwitchPresetsToExternal Property

* * *

#### Description

|  Sets the default setting for the Noise Tuner switch. [Learn
more.](../../../Applications/Noise_Figure.htm#blockDiag) This property returns
an error on VNA models with a built-in Noise tuner.  
---|---  
  
####  VB Syntax

|  pref.Port1NoiseTunerSwitchPresetsToExternal = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
bool |  (Boolean) \- Choose from: False \- Sets the default (preset) to INTERNAL True \- Sets the default (preset) to EXTERNAL  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  pref.Port1NoiseTunerSwitchPresetsToExternal = False 'Write  
prefer = pref.Port1NoiseTunerSwitchPresetsToExternal 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_Port1NoiseTunerSwitchPresetsToExternal( VARIANT_BOOL bValue)
HRESULT get_Port1NoiseTunerSwitchPresetsToExternal( VARIANT_BOOL *bValue)  
  
#### Interface

|  IPreferences8  
  
* * *

