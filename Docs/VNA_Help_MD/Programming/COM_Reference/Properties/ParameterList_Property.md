##### Read-only

|

##### [About Diff I/Q App](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## ParameterList Property

* * *

#### Description

|  Returns a list of all existing parameters.  
---|---  
  
####  VB Syntax

|  params = DIQ.ParameterList  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
params |  (Variant Array) Comma-separated list of parameters, each parameter in the form name:expression.  
DIQ |  A [Differential I/Q](../Objects/DIQ_Object.md) (object)  
  
#### Return Type

|  (Variant Array)  
  
#### Default

|  Not Applicable  
Example |  params = diq.ParameterList 'Read 'Returns "IPwrF1:a1_F1","OPwrF1:b2_F1","GainF1:b2_F1/a1_F1"  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_ParameterList(VARIANT* params);  
  
#### Interface

|  IDIQ  
  
* * *

