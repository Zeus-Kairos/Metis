##### Write-only

|

##### [About
Channels](../../../S0_Start/Traces_Channels_and_Windows.htm#channel)  
  
---|---  
  
## Add (channels) Method

* * *

#### Description

|  Creates a channel and returns a handle to it. If the channel already
exists, it returns the handle to the existing channel.  
---|---  
  
#### VB Syntax

|  chans.Add (item)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chans |  A [Channel collection](../Objects/Channels_Collection.md) (object)  
item |  (variant) - Channel number.  
  
#### Return Type

|  Channel  
  
#### Default

|  Not Applicable  
  
#### Examples

|  chans.Add 3 'Creates channel 3  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT Add(VARIANT numVal, IChannel** pChannel)  
  
#### Interface

|  IChannels

