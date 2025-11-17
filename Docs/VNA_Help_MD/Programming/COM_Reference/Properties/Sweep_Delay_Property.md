##### Write/Read

|

##### [About Sweep Delay](../../../S1_Settings/Sweep.md#SweepSetupDiag)  
  
---|---  
  
## Sweep Delay Property

* * *

#### Description

|  Specifies the time to wait just before acquisition begins for each sweep.
This delay is in addition to [Dwell Time](Dwell_Time_Property.md) and the
following two External Trigger delays if enabled.

  * [TriggerDelay](TriggerDelay_Property.md) (global scope)
  * [ExternalTriggerDelay](ExternalTriggerDelay_Property.md) (channel scope)

  
---|---  
  
####  VB Syntax

|  chan.SweepDelay = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  [Channel](../Objects/Channel_Object.md) (object)  
value |  (double) \- Sweep delay in seconds.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  chan.SweepDelay = 3e-3 'Write  
swpdelay = chan.SweepDelay 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SweepDelay(double *pVal) HRESULT put_SweepDelay(double newVal)  
  
#### Interface

|  IChannel  
  
* * *

  

