##### Write-Read

|

##### [About PNA-X Pulsed
Capabilities](../../../Applications/Narrowband_Pulsed_Application.htm)  
  
---|---  
  
## Stage3Parameter Property

* * *

#### Description

|  Sets and returns the Stage 3 filter parameters. Must first select the
filter type using [Stage3FilterType](Stage3FilterType_Property.md) before
setting these parameters Use [Stage3Parameters](Stage3Parameters_Property.md)
to return a list of the available parameters for the currently selected filter
type.  
---|---  
  
####  VB Syntax

|  spm4.Stage3Parameter(param) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
spm4 |  A [SignalProcessingModuleFour](../Objects/SignalProcessingModuleFour_Object.md) (object)  
param |  (String) Filter parameter. Choose from: "C" - Tap count (Tukey, RECT, PWIN) "P" \- Period (PWIN ONLY) "D" \- Delay (PWIN ONLY) "W" \- Width (PWIN ONLY) "R" - Ramp Count (PWIN ONLY) "M" \- Number of times to repeat the user-supplied array for each data point (COEF ONLY)  
value |  (String) Parameter Value for the specified stage 3 parameter. Use [Stage3ParameterMaximum](Stage3ParameterMaximum_Property.md) and [Stage3ParameterMinimum](Stage3ParameterMinimum_Property.md) to return a range of values for the specified parameter.  
  
#### Default

|  RECT: C = 1 PWIN: C=1E6, P=10ms, D=50us, W=50us, R=7 TUKEY: C=1  
  
#### Examples

|  spm4.Stage3Parameter("C") = 2  
mode = spm4.Stage3Parameter("pwin") 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Stage3Parameter(BSTR pName, double* pVal); HRESULT
put_Stage3Parameter(BSTR pName, double pVal);  
  
#### Interface

|  ISignalProcessingModuleFour  
  
* * *

