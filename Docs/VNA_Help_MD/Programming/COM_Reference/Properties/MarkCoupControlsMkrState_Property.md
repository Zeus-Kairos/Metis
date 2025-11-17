# MarkCoupControlsMkrState Property

##### Write/Read

|

##### [About Limit Lines](../../../S4_Collect/Use_Limits_to_Test_Devices.md)  
  
---|---  
  
* * *

#### Description

|  Set and return whether the Coupled Markers setting controls the ON|OFF
state of markers that are coupled. [Learn more about Coupled
Markers](../../../S4_Collect/Markers.htm#Coupled_Markers). Refer also to
[CoupledMarkers Property](CoupledMarkers_Property.md).  
---|---  
  
####  VB Syntax

|  pref.MarkCoupControlsMkrState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
value |  (Boolean) \- Choose from: True - With Coupled Markers ON, when a marker is turned on, the same-numbered marker on all coupled traces will also be turned on. Likewise, turning off a marker will turn it off on all coupled traces. False - Turning a marker on or off will have no effect on the markers on other traces.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  pref.MarkCoupControlsMkrState = True 'Write  
value = pref.MarkCoupControlsMkrState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MarkCoupControlsMkrState (VARIANT_BOOL* preference); HRESULT
put_MarkCoupControlsMkrState (VARIANT_BOOL val)  
  
#### Interface

|  IPreferences15  
  
* * *

