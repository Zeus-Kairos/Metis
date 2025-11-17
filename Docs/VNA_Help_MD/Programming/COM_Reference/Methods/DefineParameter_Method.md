##### Write-only

|

##### [About Differential IQ](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## DefineParameter Method

* * *

#### Description

|  Create a new parameter for Differential IQ channel. Use
[CreateCustomMeasurementEx Method](CreateCustomMeasurementEx_Method.md) to
create a new trace with the new parameter. Use [Change Parameter
Method](Change_Parameter_Method.htm) to change the parameter of one of the
existing traces to the new parameter.  
---|---  
  
####  VB Syntax

|  DIQ.DefineParameter (name, expression)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
DIQ |  A [DIQ Object](../Objects/DIQ_Object.md)  
name |  (String) Parameter name. Note: Do not use underscores in the parameter name. For example, b2_f1 cannot be used as a parameter name. However, b2f1 is a valid parameter name.  
expression |  (String) Parameter expression using receiver names and mathematical expressions.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Diq.DefineParameter "myNewParam","(a1_F1+b1_F2)/c1"
app.ActiveMeasurement.ChangeParameter "myNewParam",1 [See example
program](../../COM_Example_Programs/Create_and_Cal_a_Diff_IQ_Measurement.htm.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT DefineParameter(BSTR name,BSTR expression);  
  
#### Interface

|  IDIQ  
  
* * *

