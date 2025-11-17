##### Read-only

|

##### [About Trigger](../../../S1_Settings/Trigger.md)  
  
---|---  
  
## IsContinuous Property

* * *

#### Description

|  Returns whether or not a channel is in continuous mode. To set the channel
to continuous mode, use [Continuous Method](../Methods/Continuous_Method.md).  
---|---  
  
####  VB Syntax

|  value = chan.IsContinuous  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (boolean) - Choose either: False \- Channel trigger is NOT set to continuous. True \- Channel trigger IS set to continuous.  
chan |  Channel (object)  
  
#### Return Type

|  Boolean  
  
#### Default

|  Not Applicable  
  
#### Examples

|  trig = chan.IsContinuous 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_IsContinuous ( VARIANT_BOOL *bContinuous);  
  
#### Interface

|  IChannel4  
  
* * *

