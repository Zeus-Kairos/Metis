##### Read-only

|

#####  
  
---|---  
  
## UsedChannelNumbers Property

* * *

#### Description

|  Returns an array of channel numbers that are in use. A used channel has at
least one measurement subscribed to it  
---|---  
  
#### VB Syntax

|  chanNumbers = chans.UsedChannelNumbers  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chanNumbers |  Variable array to store the returned channel numbers  
chans |  A [Channel collection](../Objects/Channels_Collection.md) (object)  
  
#### Return Type

|  One-dimensional array of long integers  
  
#### Default

|  Not Applicable  
  
#### Examples

|  chanNumbers = chans.UsedChannelNumbers  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_UsedChannelNumbers(VARIANT* channelNumbers);  
  
#### Interface

|  IChannels2

