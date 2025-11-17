##### Write/Read

|

##### [About Receiver
Attenuation](../../../S1_Settings/Power_Level.htm#Receiver_Atten)  
  
---|---  
  
## OffsetReceiverAttenuator Property

* * *

#### Description

|  Set and return whether to offset the reference receiver by the amount of
receiver attenuation. [Learn
more.](../../../S1_Settings/Power_Level.htm#Receiver_Atten) This setting
remains until changed or until the hard drive is changed or reformatted.  
---|---  
  
####  VB Syntax

|  pref.OffsetReceiverAttenuator = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
value |  (Boolean) \- Choose from: False Do NOT offset the test port receivers. True Offset the test port receivers.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True PNA-X models False E836xB and PNA-L models  
  
#### Examples

|  pref.OffsetReceiverAttenuator = 1 'Write  
Rcvroffset = pref.OffsetReceiverAttenuator 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_OffsetReceiverAttenuator(VARIANT_BOOL * val); HRESULT
put_OffsetReceiverAttenuator(VARIANT_BOOL val);  
  
#### Interface

|  IPreferences6  
  
* * *

