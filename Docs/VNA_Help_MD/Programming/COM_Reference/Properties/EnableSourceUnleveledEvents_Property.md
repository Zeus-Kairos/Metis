##### Write/Read

|

##### [About Source Unleveled](../../../S1_Settings/Power_Level.md#Unleveled)  
  
---|---  
  
## EnableSourceUnleveledEvents Property

* * *

#### Description

|  Specifies whether or not to report [Source
Unleveled](../../../S1_Settings/Power_Level.htm#Unleveled) errors as system
events. These events can trigger an
[OnSystemEvent](../Events/OnSystemEvent.md) call. This setting will revert to
the default (False) setting on Instrument Preset.  
---|---  
  
####  VB Syntax

|  pref.EnableSourceUnleveledEvents = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
bool |  (Boolean) \- Choose from: False \- Do NOT report Source Unleveled Errors. True \- Report Source Unleveled Errors.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  pref.EnableSourceUnleveledEvents = False 'Write  
prefer = pref.EnableSourceUnleveledEvents 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_EnableSourceUnleveledEvents( VARIANT_BOOL bsourcUnlEnable)
HRESULT get_EnableSourceUnleveledEvents( VARIANT_BOOL *bsourcUnlEnable)  
  
#### Interface

|  IPreferences3  
  
* * *

