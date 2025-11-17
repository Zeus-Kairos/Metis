##### Write-only

|

##### [About Triggering](../../../S1_Settings/Trigger.md)  
  
---|---  
  
## Resume Method

* * *

#### Description

|  Resumes the trigger mode of all channels that was in effect before sending
the [channels.Hold](HoldChan_Method.md) method. Channels.Hold must be sent
before channels.Resume, using the same instance of the Channels object.  
---|---  
  
#### VB Syntax

|  chans.Resume  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chans |  A [Channel collection](../Objects/Channels_Collection.md) (object)  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  chans.Resume  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT Resume();  
  
#### Interface

|  IChannels2

