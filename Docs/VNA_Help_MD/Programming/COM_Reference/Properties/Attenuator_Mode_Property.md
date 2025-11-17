##### Write/Read

|

##### [About Attenuation](../../../S1_Settings/Power_Level.md#Atten_Manual)  
  
---|---  
  
## AttenuatorMode Property

* * *

#### Description

|  Sets or returns the mode of operation of the attenuator control for the
specified port number. This command is automatically set to Manual when an
Attenuator value is set.  
---|---  
  
####  VB Syntax

|  object.AttenuatorMode(portNum) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  [Channel](../Objects/Channel_Object.md) (object) or [CalSet](../Objects/CalSet_Object.md) (object) - Read-only property  
portNum |  (long) -Port number of attenuator control to be changed.  
value |  (enum NAModes) - Choose from: 0 - naAuto \- Attenuator control set to automatic. The analyzer will set the attenuator control appropriately to deliver the specified power at the source. 1 - naManual - Specify the attenuator setting using chan.[Attenuator](Attenuator_Property.md) (which automatically sets AttenuatorMode = naManual.  
  
#### Return Type

|  NAModes  
  
#### Default

|  0 - Auto  
  
#### Examples

|  chan.AttenuatorMode(1) = naAuto 'Write  
attn = chan.AttenuatorMode(1) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_AttenuatorMode(long port, tagNAModes* pVal)  
HRESULT put_AttenuatorMode(long port, tagNAModes newVal)  
  
#### Interface

|  IChannel ICalSet3

