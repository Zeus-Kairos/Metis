##### Write/Read

|

##### [About External
Triggering](../../../S1_Settings/External_Triggering.htm#ExternalAuxConcepts)  
  
---|---  
  
## AuxTriggerScopeIsGlobal Property

* * *

#### Description

|  Sets the Trigger OUT behavior to either Global or Channel. [Learn more
about this setting.](../../../S1_Settings/External_Triggering.htm#Output) This
command will cause the VNA to
[Preset.](../../../S1_Settings/Preset_the_Analyzer.md) This setting remains
until changed again using this command, or until the hard drive is changed or
reformatted. See the [AuxTrigger Object](../Objects/AuxTrigger_Object.md).  
---|---  
  
####  VB Syntax

|  pref.AuxTriggerScopeIsGlobal = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
value |  (Boolean) \- Choose from:

  * True \- Trigger properties apply to ALL channels (Global).
  *     * Default setting for E836x and PNA-L models.
    * Allows use of command to configure the external trigger properties.
    * "Per Point" trigger property is not settable. Use the channel's [Point trigger](Trigger_Mode_Property.md) setting. 
  * False \- External Trigger properties apply to each channel independently.
  *     * Default setting for PNA-X models.
    * Must use [AuxTrigger](../Objects/AuxTrigger_Object.md) commands to configure the external trigger properties. [ExternalTriggerConnectionBehavior Property](ExternalTriggerConnectionBehavior_Property.md) will NOT work.
    * "Per Point" trigger output property is set using the channel's [Point trigger](Trigger_Mode_Property.md) setting AND [TriggerOutInterval Property](TriggerOutInterval_Property.md).

  
  
#### Return Type

|  Boolean  
  
#### Default

|  True \- E836xB and PNA-L models False \- PNA-X models  
  
#### Examples

|  pref.AuxTriggerScopeIsGlobal = 1 'Write  
auxTrigPref = pref.AuxTriggerScopeIsGlobal 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_AuxTriggerScopeIsGlobal(VARIANT_BOOL * pref); HRESULT
put_AuxTriggerScopeIsGlobal(VARIANT_BOOL pref);  
  
#### Interface

|  IPreferences5  
  
* * *

