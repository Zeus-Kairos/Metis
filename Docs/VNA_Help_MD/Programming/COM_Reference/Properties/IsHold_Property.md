##### Read-only

|

##### [About Trigger](../../../S1_Settings/Trigger.md)  
  
---|---  
  
## IsHold Property

* * *

#### Description

|  Returns whether or not a channel is in hold mode. To set the channel to
hold mode, use [Hold Method](../Methods/Hold_Method.md).  
---|---  
  
####  VB Syntax

|  value = chan.IsHold  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (boolean) - Choose either: False \- Channel trigger is NOT set to hold. True \- Channel trigger IS set to hold.  
chan |  Channel (object)  
  
#### Return Type

|  Boolean  
  
#### Default

|  Not Applicable  
  
#### Examples

|  trig = chan.IsHold 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_IsHold ( VARIANT_BOOL *bHold);  
  
#### Interface

|  IChannel4  
  
* * *

