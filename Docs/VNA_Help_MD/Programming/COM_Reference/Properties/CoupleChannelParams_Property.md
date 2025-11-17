##### Write/Read

|

##### [About Time Domain Trace
Coupling](../../../Time/TimeDomain.htm#Coupling)  
  
---|---  
  
## CoupleChannelParams Property

* * *

#### Description

|  Turns ON and OFF Time Domain Trace Coupling. All of the measurements in the
specified channel are coupled.

  * To select Transform parameters to couple, use [Trans.CoupledParameters Property](CoupledParameters_Transform_Property.md)
  * To select Gating parameters to couple, use [Gate.CoupledParameters Property](CoupledParameters_Gate_Property.md)

  
---|---  
  
####  VB Syntax

|  chan.CoupleChannelParams = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A [Channel](../Objects/Channel_Object.md) (object)  
state |  (boolean)  
False \- Turns Trace Coupling OFF True \- Turns Trace Coupling ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  chan.CoupleChannelParams = False 'Write  
couple = chan.CoupleChannelParams 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_CoupleChannelParams(VARIANT_BOOL *isCoupled); HRESULT
put_CoupleChannelParams(VARIANT_BOOL isCoupled);  
  
#### Interface

|  IChannel5

