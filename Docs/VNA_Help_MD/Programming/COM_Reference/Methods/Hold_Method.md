##### Write-only

|

##### [About Triggering](../../../S1_Settings/Trigger.md#state_hold)  
  
---|---  
  
## Hold Method

* * *

#### Description

|  Puts the channel in Hold - not sweeping. See
[chans.Hold](HoldChan_Method.md) to put ALL channels in hold.  
---|---  
  
####  VB Syntax

|  chan.Hold [sync]  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A [Channel](../Objects/Channel_Object.md) (object)  
[sync] |  The [sync] argument is ignored. Program control ALWAYS waits until the channel is in the Hold state.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  chan.Hold  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT Hold  
  
#### Interface

|  IChannel  
  
* * *

  

