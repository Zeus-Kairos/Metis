##### Write/Read

|

##### [About PNA-X Pulsed
Capabilities](../../../Applications/Narrowband_Pulsed_Application.htm)  
  
---|---  
  
## Stage1Coefficients Property

* * *

#### Description

|  Sets and returns the digital filter coefficients of stage1.  
---|---  
  
####  VB Syntax

|  spm4.Stage1Coefficients = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
spm4 |  A [SignalProcessingModuleFour](../Objects/SignalProcessingModuleFour_Object.md) (object)  
value |  (Variant Array) Coefficients. An array of real values.  
  
#### Return Type

|  Variant  
  
#### Default

|  Stage dependent.  
  
#### Examples

|  spm4.Stage1Coefficients = 0,0.1,0.7,0.7,0.1 'Write  
mode = spm4.Stage1Coefficients 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Stage1Coefficients(VARIANT* pCoefs); HRESULT
put_Stage1Coefficients(VARIANT pCoefs);  
  
#### Interface

|  ISignalProcessingModuleFour  
  
* * *

