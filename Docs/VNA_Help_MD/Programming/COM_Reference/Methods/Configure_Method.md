##### Write-only

|

##### [Learn more about Multiport Test Set
Restart](../../../System/External_Testset_Control.htm#Restart)  
  
---|---  
  
## Configure Method

* * *

#### Description

|  Restarts as an "N-port" VNA using the specified multiport test set. [See
other commands to configure multiport test
sets.](../Objects/TestsetControl_Object.htm)  
---|---  
  
####  VB Syntax

|  app.Configure (model, address)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
model |  String \- Model of the test set with which to restart. Use "Native" to restart without a test set. To see a list of supported test sets, use  
address |  Integer \- GPIB Address of the test set. Use 0 for native restart.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  [See an example using this
command.](../../COM_Example_Programs/External_Testset_Control.htm)
app.Configure ("N44xx",18)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT Configure(BSTR model, long address);  
  
#### Interface

|  IApplication10

