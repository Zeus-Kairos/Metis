##### Read-only

|

##### [About PNA-X Pulsed
Capabilities](../../../Applications/Narrowband_Pulsed_Application.htm)  
  
---|---  
  
## Stage3Parameters Property

* * *

#### Description

|  Returns the names of parameters for the current filter type. Use
[Stage3FilterType Property](Stage3FilterType_Property.md) to set the filter
type.  
---|---  
  
####  VB Syntax

|  values= spm4.Stage3Parameters  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Variant) Variable to store the returned parameter names.  
spm4 |  A [SignalProcessingModuleFour](../Objects/SignalProcessingModuleFour_Object.md) (object)  
  
#### Return Type

|  Variant  
  
#### Default

|  Not Applicable  
Examples |  mode = spm4.Stage3Parameters 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Stage3Parameters(VARIANT* pNames);  
  
#### Interface

|  ISignalProcessingModuleFour  
  
* * *

