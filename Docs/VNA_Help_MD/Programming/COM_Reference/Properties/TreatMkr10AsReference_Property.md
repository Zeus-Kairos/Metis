##### Write/Read

|

##### [About Reference Markers](../../../S4_Collect/Markers.md#reference)  
  
---|---  
  
## TreatMkr10AsReference Property

* * *

#### Description

|  Set and return whether to treat marker 10 as a reference marker.  
---|---  
  
####  VB Syntax

|  pref.TreatMkr10AsReference = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
value |  (Boolean) \- Choose from: True - Marker 10 is always a reference marker (Pre A.10.40 behavior). False - Marker 10 is just another marker. See [Reference Marker commands](../../XResponseTopic.md#Reference_Markers)  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  pref.TreatMkr10AsReference = True 'Write  
value = pref.TreatMkr10AsReference 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_TreatMkr10AsReference (VARIANT_BOOL* preference); HRESULT
put_TreatMkr10AsReference (VARIANT_BOOL val)  
  
#### Interface

|  IPreferences15  
  
* * *

