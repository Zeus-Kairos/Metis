##### Write/Read

|

##### [About Source
Attenuation](../../../S1_Settings/Power_Level.htm#Source_Atten)  
  
---|---  
  
## OffsetSourceAttenuator Property

* * *

#### Description

|  Set and return whether to mathematically offset the reference receivers by
the amount of source attenuation. [Learn
more.](../../../S1_Settings/Power_Level.htm#Source_Atten) This setting remains
until changed or until the hard drive is changed or reformatted.  
---|---  
  
####  VB Syntax

|  pref.OffsetSourceAttenuator = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
value |  (Boolean) \- Choose from: False Do NOT offset the reference receivers. True Offset the reference receivers.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True PNA-X models False E836xB and PNA-L models  
  
#### Examples

|  pref.OffsetSourceAttenuator = 1 'Write  
Rcvroffset = pref.OffsetSourceAttenuator 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_OffsetSourceAttenuator(VARIANT_BOOL * val); HRESULT
put_OffsetSourceAttenuator(VARIANT_BOOL val);  
  
#### Interface

|  IPreferences6  
  
* * *

