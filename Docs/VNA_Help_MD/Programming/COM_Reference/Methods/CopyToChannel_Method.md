##### Write-only

|

##### [About Copy Channels](../../../S1_Settings/CopyChannels.md)  
  
---|---  
  
## CopyToChannel Method

* * *

#### Description

|  Copies ALL settings from this channel to the specified channel. Use
[CopyFrom](CopyFrom_Method.md) to copy ONLY the mechanical switch and
attenuator settings.  
---|---  
  
####  VB Syntax

|  chan.CopyToChannel(lChanNum)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A [Channel](../Objects/Channel_Object.md) (object)  
IChanNum |  (long integer)  Number of the channel to become a copy of <chan>.  
  
#### Return Type

|  None  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim chan Set chan = PNAapp.ActiveChannel chan.CopyToChannel 2  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT CopyToChannel(long lChanNum);  
  
#### Interface

|  IChannel2  
  
* * *

