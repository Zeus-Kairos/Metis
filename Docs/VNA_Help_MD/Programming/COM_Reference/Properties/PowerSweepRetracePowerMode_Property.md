##### Write/Read

|

##### [About Power Sweep](../../../S1_Settings/Sweep.md#power)  
  
---|---  
  
## PowerSweepRetracePowerMode Property

* * *

#### Description

|  At the end of a power sweep, while waiting to trigger the next sweep,
maintain source power at either the start power level or at the stop power
level.  
---|---  
  
####  VB Syntax

|  pref.PowerSweepRetracePowerMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
value |  (Enum) \- Choose from: 0 - naPowerSweepRetraceMode_Start \- maintain source at start power level. 1 - naPowerSweepRetraceMode_Stop \- maintain source at stop power level.  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - naPowerSweepRetraceMode_Start  
  
#### Examples

|  pref.PowerSweepRetracePowerMode = naPowerSweepRetraceMode_Start 'Write  
psMode = pref.PowerSweepRetracePowerMode 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PowerSweepRetracePowerMode (tagNAPowerSweepRetraceMode*
preference);  
HRESULT put_PowerSweepRetracePowerMode (tagNAPowerSweepRetraceMode val)  
  
#### Interface

|  IPreferences3  
  
* * *

