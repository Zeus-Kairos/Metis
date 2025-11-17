##### Read-only

|

#####  
  
---|---  
  
## IsBlocked Property

* * *

#### Description

|  Reads whether the specified channel is currently 'blocked' from sweeping.
Learn more about the [Mechanical
Devices](../../../System/Mechanical_Devices.htm) dialog.  
---|---  
  
####  VB Syntax

|  value = chan.IsBlocked  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (boolean) - Choose either: False \- The channel IS blocked. True \- The channel is NOT blocked.  
chan |  Channel (object)  
  
#### Return Type

|  Boolean  
  
#### Default

|  Not Applicable  
  
#### Examples

|  block = chan.IsBlocked 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_IsBlocked (VARIANT_BOOL *bBlock);  
  
#### Interface

|  IChannel19  
  
* * *

