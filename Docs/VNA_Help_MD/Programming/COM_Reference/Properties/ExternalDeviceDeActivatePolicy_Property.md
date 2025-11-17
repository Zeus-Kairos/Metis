##### Write/Read

|

##### [About
ExternalDevices](../../../System/Configure_an_External_Device.htm)  
  
---|---  
  
## ExternalDeviceDeActivatePolicy Property

* * *

#### Description

|  Set and return whether External Devices remain activated or are de-
activated when the VNA is Preset or when a Instrument State is recalled. This
setting remains until changed again using this command, or until the hard
drive is changed or reformatted. See the
[ExternalDevices](../Objects/ExternalDevices_Collection.md) collection.  
---|---  
  
####  VB Syntax

|  pref.ExternalDeviceDeActivatePolicy = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
value |  (Boolean) \- Choose from:

  * True \- External device are de-activated when the VNA is Preset or when a Instrument State is recalled.
  * False \- External devices remain active when the VNA is Preset or when a Instrument State is recalled.

  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  pref.ExternalDeviceDeActivatePolicy = 1 'Write  
dDevPolicy = pref.ExternalDeviceDeActivatePolicy 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ExternalDeviceDeActivatePolicy(VARIANT_BOOL * pref); HRESULT
put_ExternalDeviceDeActivatePolicy(VARIANT_BOOL pref);  
  
#### Interface

|  IPreferences10  
  
* * *

