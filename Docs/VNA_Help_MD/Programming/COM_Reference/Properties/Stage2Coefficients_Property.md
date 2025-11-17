##### Write/Read

|

##### [About PNA-X Pulsed
Capabilities](../../../Applications/Narrowband_Pulsed_Application.htm)  
  
---|---  
  
## Stage2Coefficients Property

* * *

#### Description

|  Sets and returns Stage2Coefficients. Note: Stage2 settings are ignored when
using DSP Version 5. [Learn more.](../../../S0_Start/HelpAbout.md#DSPchanges)  
---|---  
  
####  VB Syntax

|  spm4.Stage2Coefficients = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
spm4 |  A [SignalProcessingModuleFour](../Objects/SignalProcessingModuleFour_Object.md) (object)  
value |  (Variant) An array of real numbers. Filter coefficients  
  
#### Return Type

|  Variant  
  
#### Default

|  Not Applicable  
  
#### Examples

|  spm4.Stage2Coefficients = 'Write  
mode = spm4.Stage2Coefficients 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Stage2Coefficients(VARIANT* pCoefs); HRESULT
put_Stage2Coefficients(VARIANT pCoefs);  
  
#### Interface

|  ISignalProcessingModuleFour  
  
* * *

