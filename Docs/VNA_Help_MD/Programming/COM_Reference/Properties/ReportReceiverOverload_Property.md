##### Write/Read

|

##### [About Receiver Overload](../../../System/Preferences.md#RcvrOverload)  
  
---|---  
  
## ReportReceiverOverload Property

* * *

#### Description

|  Set and return whether to display receiver overload warnings.  
---|---  
  
####  VB Syntax

|  pref.ReportReceiverOverload = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pref |  A [Preferences](../Objects/Preferences_Object.md) (object)  
value |  (Boolean) \- Choose from: True Display overload warnings. False Do NOT display overload warnings.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  pref.ReportReceiverOverload = True 'Write  
value = pref.ReportReceiverOverload 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ReportReceiverOverload (VARIANT_BOOL PowerSweepRetraceMode*
preference);  
HRESULT put_ReportReceiverOverload (VARIANT_BOOL PowerSweepRetraceMode val)  
  
#### Interface

|  IPreferences12  
  
* * *

