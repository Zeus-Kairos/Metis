##### Write/Read

|

##### [About Trigger Mode](../../../S1_Settings/Trigger.md#TriggerMode)  
  
---|---  
  
## TriggerMode Property

* * *

#### Description

|  These settings determine what EACH signal will trigger. Note: Setting Point
and EverySweep mode forces [Trigger.Scope](Scope_Property.md) =
naChannelTrigger.  
---|---  
  
####  VB Syntax

|  chan.TriggerMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A [Channel](../Objects/Channel_Object.md) (object)  
value |  (enum NATriggerMode) - Choose from: 0 - naTriggerModePoint \- Each Manual or External trigger signal causes one data point to be measured. 1 - naTriggerModeMeasurement (superseded \- still works but replaced with a more descriptive enum) 1 - naTriggerModeChannel \- Each trigger signal causes ALL traces in that channel to be swept. 2 \- naTriggerModeEverySweep - Each Manual or External trigger signal causes ALL traces that share a source port to be swept. 3 - naTriggerModeTrace \- Allowed ONLY when [PointSweepState](PointSweepState_Property.md) is enabled. Each trigger signal causes two identical measurements to be triggered separately - one trigger signal is required for each measurement. Other trigger mode settings cause two identical parameters to be measured simultaneously.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  1 \- naTriggerModeChannel  
  
#### Examples

|  chan.TriggerMode = naTriggerModePoint 'Write  
trigtyp = chan.TriggerMode 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_TriggerMode (tagNATriggerMode *pMode)  
HRESULT put_TriggerMode (tagNATriggerMode newMode)  
  
#### Interface

|  IChannel  
  
* * *

