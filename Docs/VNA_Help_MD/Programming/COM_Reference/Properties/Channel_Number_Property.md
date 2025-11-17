##### Read-only

|

##### [About
Channels](../../../S0_Start/Traces_Channels_and_Windows.htm#channel)  
  
---|---  
  
## ChannelNumber Property

* * *

#### Description

|  Returns the Channel number of the Channel or Measurement object.  
---|---  
  
####  VB Syntax

|  object.ChannelNumber  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  A Channel (object)  
or  
A Measurement (object)  
  
#### Return Type

|  Long Integer  
  
#### Default

|  Not applicable  
  
#### Examples

|  chanNum = chan.ChannelNumber 'returns the channel number  
chanNum = meas.ChannelNumber 'returns the channel number of the measurement  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_ChannelNumber(long *pVal)  
  
#### Interface

|  IChannel  
IMeasurement

