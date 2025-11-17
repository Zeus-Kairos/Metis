##### Read/Write

|

##### [About ECAL](../../../S3_Cals/ModifyCalKits.md)  
  
---|---  
  
## RemoteCalStoragePreference Property

* * *

#### Description

|  Specifies the default manner in which calibrations performed using COM or
SCPI are to be stored. Cal data is always stored to the channels Cal Register
regardless of this setting. This setting survives instrument preset and
reboot. It remains until changed by another invocation of this property.  
---|---  
  
####  VB Syntax

|  pref.RemoteCalStoragePreference = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal |  A [Preferences](../Objects/Preferences_Object.md) (object)  
value |  (Enum) \- Choose from: 0 - naPreferCalRegister \- Cal is saved ONLY to the channels Cal Register. 1 - naPreferNewUserCalSet \- Cal is automatically saved to a new User Cal Set file when performing a calibration using COM. The Cal Set name is automatically generated. This corresponds to pre-6.0 behavior. Use the [Name](Name_Calset_Property.md) property to change the name after the cal is complete. 2 - naPreferReuseCurrentCalSet \- The cal is saved to the Cal Set is that is currently selected on the specific channel. This could be the channels Cal Register. If the channel does not yet have a selected Cal Set, the cal will be saved to a new User Cal Set with an automatically-generated name.  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - naPreferCalRegister  
  
#### Examples

|  pref.RemoteCalStoragePreference = naPreferNewUserCalSet 'Write  
calStorageMode = pref.RemoteCalStoragePreference ' Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_RemoteCalStoragePreference(enum NARemoteCalStoragePreference*
preference); HRESULT put_RemoteCalStoragePreference(enum
NARemoteCalStoragePreference val);  
  
#### Interface

|  IPreferences7  
  
* * *

