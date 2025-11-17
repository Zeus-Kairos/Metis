##### Write/Read

|

##### [About PNA-X Pulsed
Capabilities](../../../Applications/Narrowband_Pulsed_Application.htm)  
  
---|---  
  
## Stage3Coefficients Property

* * *

#### Description

|  Sets and returns Stage3Coefficients.  
---|---  
  
####  VB Syntax

|  spm4.Stage3Coefficients = values  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
spm4 |  A [SignalProcessingModuleFour](../Objects/SignalProcessingModuleFour_Object.md) (object)  
values |  (Float array) Filter coefficients  
  
#### Return Type

|  Variant  
  
#### Default

|  Not Applicable  
  
#### Examples

|  spm4.Stage3Coefficients = +0.0E+000,+6.4E+001,+2.56E+002 'Write  
mode = spm4.Stage3Coefficients 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Stage3Coefficients(Float* pCoefs); HRESULT
put_Stage3Coefficients(Float pCoefs);  
  
#### Interface

|  ISignalProcessingModuleFour2  
  
* * *

