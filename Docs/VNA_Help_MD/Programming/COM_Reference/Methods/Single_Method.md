##### Write-only

|

##### [About Triggering](../../../S1_Settings/Trigger.md)  
  
---|---  
  
## Single Method

* * *

#### Description

|  Sets the trigger count to 1 which will cause the channel to respond once to
the [trigger source](../Properties/Source_Property.md). How the channel
responds to a single trigger depends on the [trigger
mode](../Properties/Trigger_Mode_Property.htm) (point, trace, and so forth.)
With the exception of the 'sync' argument, this command behaves like the
[channel 'single' setting](../../../S1_Settings/Trigger.md#state_single) from
the user interface. This setting has implications on Calibration. [Learn
more.](../Properties/PreferInternalTriggerOnChannelSingle_Property.htm)  
---|---  
  
####  VB Syntax

|  chan.Single [sync]  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A Channel (object)  
[sync] |  (boolean) -Optional argument.

  * True \- The VNA waits (blocks execution) until the entire acquisition process is completed.
  * False \- The VNA returns immediately - does NOT wait for acquisition to complete (non-blocking). Default setting.

When trigger source is set to Manual:

  * with sync = True, trigger source automatically changes to Internal which sends AND allows one trigger signal, then changes back to Manual.
  * with sync = False, a trigger signal must also be sent using [app.ManualTrigger Method](Manual_Trigger_Method.md).

  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  sync = True  
chan.Single sync  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT Single(VARIANT_BOOL bWait)  
  
#### Interface

|  IChannel  
  
* * *

