##### Write-only

|

##### [About Triggering](../../../S1_Settings/Trigger.md)  
  
---|---  
  
## ManualTrigger Method

* * *

#### Description

|  Triggers the analyzer when
[TriggerSetup.Source](../Properties/Source_Property.md) = naTriggerManual.
Note: An SMC Fixed Output measurement cannot be triggered using this command.
For more information, see the [example
program](../../COM_Example_Programs/Create_an_SMC_Fixed_Output_Meas.htm).  
---|---  
  
####  VB Syntax

|  app.ManualTrigger [sync],[timeout]  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
[sync] |  (boolean) - Optional argument.  
A variable set to either True or False. True \- The analyzer waits until the
trigger is completed to process subsequent commands.  
False \- Subsequent commands are processed immediately (the default setting).  
timeout |  (long) - Optional argument.   
If sync is true, timeout sets the amount of time the VNA will wait until
continuing program execution. Units are milliseconds. A value of -1 (the
default setting) causes the VNA to wait indefinitely. If sync is False, the
timeout setting is ignored.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  ' After Manual trigger is executed, the VNA will wait 1 second to continue
program execution  
Dim wait as Boolean  
wait = True  
app.ManualTrigger wait, 1000  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT ManualTrigger(VARIANT_BOOL bSynchronize, long timeout)  
  
#### Interface

|  IApplication  
  
* * *

