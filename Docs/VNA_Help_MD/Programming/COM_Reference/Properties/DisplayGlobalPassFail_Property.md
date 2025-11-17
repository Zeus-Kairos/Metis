##### Write-Read

## DisplayGlobalPassFail Property

* * *

#### Description

|  Shows or hides the dialog which displays global pass/fail results. [Learn
more about Global
Pass/Fail.](../../../S4_Collect/Use_Limits_to_Test_Devices.htm#Limitdiag)  
---|---  
  
####  VB Syntax

|  app.DisplayGlobalPassFail = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
value |  (Boolean) True \- displays the pass/fail dialog. False - hides the pass/fail dialog.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  Dim app As Application Set app = New Application app.DisplayGlobalPassFail
= true 'shows dialog  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_DisplayGlobalPassFail(VARIANT_BOOL * Val); HRESULT
put_DisplayGlobalPassFail(VARIANT_BOOL Val);  
  
#### Interface

|  IApplication6

