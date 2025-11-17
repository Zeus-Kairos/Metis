##### Write-only

|

##### [About Triggering](../../../S1_Settings/Trigger.md)  
  
---|---  
  
## Abort Method

* * *

#### Description

| Ends the current measurement sweep on the channel.  
---|---  
  
####  VB Syntax

| chan.Abort [sync]  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan | (object) \- A [Channel](../Objects/Channel_Object.md) object  
sync | (boolean) \- wait (or not) for the analyzer to stop before processing subsequent commands. Optional argument; if unspecified, value is set to False. Choose from:  
True \- synchronize - the analyzer will not process subsequent commands until
the current measurement is aborted.  
False \- continue processing commands immediately  
  
#### Return Type

| None  
  
#### Default

| None  
  
#### Examples

| chan.abort True  
chan.abort  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT Abort(VARIANT_BOOL bSynchronize);  
  
#### Interface

| IChannel

