##### Write/Read

|

##### [About RF power during sweep
retrace](../../../S1_Settings/Power_Level.htm#PowerONOFF)  
  
---|---  
  
## PowerOnDuringRetraceMode Property

* * *

#### Description

|  For single-band frequency or segment sweeps ONLY, specify whether to turn
RF power ON or OFF during a retrace. This setting remains until changed using
this command, or until the hard drive is changed or reformatted.  
---|---  
  
####  VB Syntax

|  pref.PowerOnDuringRetraceMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
value |  (Enum) \- Choose from: 0 - naRetracePowerMode_Auto Power is left ON during retrace of single-band frequency or segment sweeps ONLY. 1 - naRetracePowerMode_OFF Power is turned OFF during retrace of single-band frequency or segment sweeps ONLY.  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - naRetracePowerMode_Auto  
  
#### Examples

|  pref.PowerOnDuringRetraceMode = naPowerSweepRetraceMode_Start 'Write  
psMode = pref.naPowerOnDuringRetraceMode_Start 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PowerOnDuringRetraceMode (tagNARetracePowerMode* preference);  
HRESULT put_PowerOnDuringRetraceMode (tagNARetracePowerMode val)  
  
#### Interface

|  IPreferences4  
  
* * *

