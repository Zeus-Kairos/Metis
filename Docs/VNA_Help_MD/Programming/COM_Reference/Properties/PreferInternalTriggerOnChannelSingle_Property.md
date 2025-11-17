##### Write/Read

|

##### [About Triggering](../../../S1_Settings/Trigger.md)  
  
---|---  
  
## PreferInternalTriggerOnChannelSingle Property

* * *

#### Description

|  Set and read the preference for the
[chan.Single](../Methods/Single_Method.md) trigger behavior. This setting
persists until changed. These preferences are important when performing a
Guided calibration, as the VNA uses the chan.Single trigger command to measure
standards.

  * set PreferInternalTriggerOnChannelSingle = False to use an External trigger sweep to measure a cal standard.
  * set PreferInternalTriggerOnChannelSingle = True to use an External sweep for the measurement, but rely on the VNA to send Internal trigger signals for calibrating.

To set this preference for an Unguided Calibration, use
[PreferInternalTriggerOnUnguidedCal
Property](PreferInternalTriggerOnUnguidedCal_Property.htm) The chan.Single
trigger command NEVER respects the Trigger Source = Manual setting. It always
switches to Internal for one trigger, then back to Manual, regardless of this
preference command.  
---|---  
  
####  VB Syntax

|  pref.PreferInternalTriggerOnChannelSingle = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
bool |  (Boolean) \- Choose from: 0 - False \- the Single trigger property does respect the Trigger Source = External setting. For example, if [Trigger source = External](Source_Property.md), the single trigger method will wait for the External trigger signal and then allow only one sweep. 1 - True \- the Single trigger command does NOT respect the Trigger Source = External setting. For example, when the Single method is sent, the VNA immediately switches to Internal sweep, responds to one trigger signal, then switches back to External.  
  
#### Return Type

|  Boolean  
  
#### Default

|  0 - False  
  
#### Examples

|  pref.PreferInternalTriggerOnChannelSingle = False 'Write  
prefer = pref.PreferInternalTriggerOnChannelSingle 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_PreferInternalTriggerOnChannelSingle( VARIANT_BOOL bprefSingle)
HRESULT get_PreferInternalTriggerOnChannelSingle( VARIANT_BOOL *bprefSingle)  
  
#### Interface

|  IPreferences2

