##### Read-only

|

##### [About PNA-X Pulsed
Capabilities](../../../Applications/Narrowband_Pulsed_Application.htm)  
  
---|---  
  
## Stage2MaximumCoefficientSum Property

* * *

#### Description

|  Returns the maximum sum of all Stage2 coefficients. Note: Stage2 settings
are ignored when using DSP Version 5. [Learn
more.](../../../S0_Start/HelpAbout.htm#DSPchanges)  
---|---  
  
####  VB Syntax

|  value = spm4.Stage2MaximumCoefficientSum  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (__int64* val) Variable to store the returned Max sum of all coefficients.  
spm4 |  A [SignalProcessingModuleFour](../Objects/SignalProcessingModuleFour_Object.md) (object)  
  
#### Default

|  Not Applicable  
Examples |  mode = spm4.Stage2MaximumCoefficientSum 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Stage2MaximumCoefficientSum(__int64* val);  
  
#### Interface

|  ISignalProcessingModuleFour  
  
* * *

