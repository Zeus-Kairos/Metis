##### Write/Read

|

##### [About Calsets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
# PreferSourcePowerCalFromCalset Property

* * *

#### Description

|  Specifies if the source power cal in the calset linked to a measurement cal
should be enabled or disabled with that cal.  
---|---  
  
####  VB Syntax

|  pref.PreferSourcePowerCalFromCalset = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
bool |  (Boolean) \- Choose from: 0 - False \- Disable source power cal in calset. 1 - True \- Enable source power cal in calset.  
  
#### Return Type

|  Boolean  
  
#### Default

|  0 - False  
  
#### Examples

|  pref.PreferSourcePowerCalFromCalset = False 'Write  
prefer = pref.PreferSourcePowerCalFromCalset 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_PrefeSourcePowerCalFromCalset( VARIANT_BOOL prefPowerCal)
HRESULT get_PrefeSourcePowerCalFromCalset( VARIANT_BOOL *prefPowerCal)  
  
#### Interface

|  IPreferences

