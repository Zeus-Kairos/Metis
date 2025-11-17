##### Read-only

|

##### [About PNA-X Pulsed
Capabilities](../../../Applications/Narrowband_Pulsed_Application.htm)  
  
---|---  
  
## Stage3ParameterMaximum Property

* * *

#### Description

|  Returns maximum parameter value for the current filter type.  
---|---  
  
####  VB Syntax

|  value= spm4.Stage3ParameterMaximum (parameter)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Variant) Variable to store the maximum parameter value.  
spm4 |  A [SignalProcessingModuleFour](../Objects/SignalProcessingModuleFour_Object.md) (object)  
parameter |  (String) Parameter name. See [Stage3Parameter Property](Stage3Parameter_Property.md) for a list of parameters.  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
Examples |  mode = spm4.Stage3ParameterMaximum ("c") 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Stage3ParameterMaximum(BSTR pName, double* pVal);  
  
#### Interface

|  ISignalProcessingModuleFour  
  
* * *

