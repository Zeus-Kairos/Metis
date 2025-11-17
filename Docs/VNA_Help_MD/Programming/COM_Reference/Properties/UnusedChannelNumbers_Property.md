##### Read-only

|

#####  
  
---|---  
  
## UnusedChannelNumbers Property

* * *

#### Description

|  Returns an array of channel numbers that are NOT in use. An unused channel
has NO measurements subscribed to it.  
---|---  
  
#### VB Syntax

|  chanNumbers = chans.UnusedChannelNumbers (NumberOfChannels)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chanNumbers |  Variable array to store the returned channel numbers  
chans |  A [Channel collection](../Objects/Channels_Collection.md) (object)  
NumberOfChannels |  (Long Integer) Number of channels that you are requesting.  
  
#### Return Type

|  One-dimensional array of long integers. The size of the array is specified
by the NumberOfChannels parameter.  
  
#### Default

|  Not Applicable  
  
#### Examples

|  chanNumbers = chans.UnusedChannelNumbers(5)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_UnusedChannelNumbers(long numberRequested,VARIANT*
channelNumbers);  
  
#### Interface

|  IChannels2

