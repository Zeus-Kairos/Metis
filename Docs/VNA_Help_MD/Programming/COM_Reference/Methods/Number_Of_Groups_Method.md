##### Write-only

|

##### [About Triggering](../../../S1_Settings/Trigger.md#state_group)  
  
---|---  
  
## NumberOfGroups Method

* * *

#### Description

| Sets the number of trigger signals the channel will receive. After the
channel has received that number of trigger signals, the channel switches to
Hold mode.  
---|---  
  
####  VB Syntax

| chan.NumberOfGroups num, sync  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan | A [Channel](../Objects/Channel_Object.md) (object)  
num | (long integer) Number of trigger signals the channel will receive. Choose any number greater than 0.  
sync | (boolean) Variable set to either: True - subsequent commands are not processed until the groups are complete. Do not use with manual trigger. False - subsequent commands are processed immediately.  
  
#### Return Type

| Not Applicable  
  
#### Default

| Not Applicable  
  
#### Examples

| chan.NumberOfGroups 5,False  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT NumberOfGroups(long count, VARIANT_BOOL bWait)  
  
#### Interface

| IChannel

