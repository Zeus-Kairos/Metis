##### Write/Read

|

##### [About Attenuation](../../../S1_Settings/Power_Level.md#Atten_Manual)  
  
---|---  
  
## Attenuator Property

* * *

#### Description

|  Sets or returns the value of the source attenuator for the specified port
number. Sending this command automatically sets
[AttenuatorMode](Attenuator_Mode_Property.md) to Manual.  
---|---  
  
####  VB Syntax

|  object.Attenuator(portNum) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  [Channel](../Objects/Channel_Object.md) (object) or [CalSet](../Objects/CalSet_Object.md) (object) \- Read-only property  
portNum |  (long integer) - Port number of source attenuator to be changed.  
value |  (double) \- Attenuation value. The range of settable values depends on the VNA model. To determine the valid settings, do one of the following:

  * See [VNA models and options](../../../Support/Configurations.md) to see the range and step size for each model / option.
  * To determine the maximum attenuator value use [MaximumSourceStepAttenuator](MaximumSourceStepAttenuator_Property.md).

If an invalid attenuation setting is entered, the VNA will select the next
lower valid value. For example, if 19 is entered, then for an E8361A, 10 dB
attenuation will be selected.  
  
#### Return Type

|  Double  
  
#### Default

|  20 dB  
  
#### Examples

|  chan.Attenuator(1) = 20 'Write  
attn = chan.Attenuator(cnum) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Attenuator(long port, double *pVal)  
HRESULT put_Attenuator(long port, double newVal)  
  
#### Interface

|  IChannel ICalSet3  
  
* * *

