##### Write/Read

|

##### [About Triggering](../../../S1_Settings/Trigger.md)  
  
---|---  
  
## PreferInternalTriggerOnUnguidedCal Property

* * *

#### Description

|  Set and read the preference for the trigger behavior when performing an
Unguided calibration.  
---|---  
  
####  VB Syntax

|  pref.PreferInternalTriggerOnUnguidedCal = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
bool |  (Boolean) \- Choose from: 0 - False \- The trigger behavior during an Unguided calibration DOES respect the setting of the [Trigger source](Source_Property.md) command. For example, during an Unguided Cal, when Trigger source = External, the VNA will wait for the External trigger signal and then allow only one sweep. 1 - True -The trigger behavior during an Unguided calibration does NOT respect the Trigger Source = External setting. For example, during an Unguided Cal, when Trigger source = External, the VNA immediately switches to Internal sweep, measures the standard with one trigger signal, then switches back to External trigger. Note: When Trigger Source = Manual during a calibration, the VNA ALWAYS switches to Internal for one trigger to measure a standard, then back to Manual, regardless of this preference command.  
  
#### Return Type

|  Boolean  
  
#### Default

|  0 - False  
  
#### Examples

|  pref.PreferInternalTriggerOnUnguidedCal = False 'Write  
prefer = pref.PreferInternalTriggerOnUnguidedCal 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_PreferInternalTriggerOnUnguidedCal( VARIANT_BOOL bprefUnguided)
HRESULT get_PreferInternalTriggerOnUnguidedCal( VARIANT_BOOL *bprefUnguided)  
  
#### Interface

|  IPreferences2

