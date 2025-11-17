##### Read-only

|

##### [About PNA-X Pulsed
Capabilities](../../../Applications/Narrowband_Pulsed_Application.htm)  
  
---|---  
  
## Stage3ParameterMinimum Property

* * *

#### Description

|  Returns minimum parameter value for the current filter type.  
---|---  
  
####  VB Syntax

|  value= spm4.Stage3ParameterMinimum (parameter)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Variant) Variable to store the minimum parameter value.  
spm4 |  A [SignalProcessingModuleFour](../Objects/SignalProcessingModuleFour_Object.md) (object)  
parameter |  (String) Parameter name. See [Stage3Parameter Property](Stage3Parameter_Property.md) for a list of parameters.  
  
#### Return Type

|  Double  
  
#### Default

|  Not applicable  
Examples |  mode = spm4.Stage3ParameterMinimum ("c") 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Stage3ParameterMinimum(BSTR pName, double* pVal);  
  
#### Interface

|  ISignalProcessingModuleFour  
  
* * *

