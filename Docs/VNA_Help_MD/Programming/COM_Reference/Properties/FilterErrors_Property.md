##### Read-only

|

##### [About PNA-X Pulsed
Capabilities](../../../Applications/Narrowband_Pulsed_Application.htm)  
  
---|---  
  
## FilterErrors Property

* * *

#### Description

|  Returns the error string associated with the digital filters. The return
string has three fields separated by commas: "stage1 status, stage2 status,
stage3 status" Each of these fields can contain one or more of the following
error codes:

  * NO ERROR
  * *NUMBER-OF-COEFFICIENTS \- the number of coefficients is excessive for that filter-stage
  * *COEFFICIENT VALUE \- one or more coefficients are out of range for that filter-stage
  * *SUM-OF-COEFFICIENTS \- the sum of all coefficients is excessive for that filter-stage,
  * *FREQUENCY \- the frequency for Stage 1 is out of range (only applies stage1 field),
  * *PARAMETER \- one or more parameters are out of range (only applies to stage 3 field)

  
---|---  
  
####  VB Syntax

|  value = spm4.FilterErrors  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  Variable to store the returned errors.  
spm4 |  A [SignalProcessingModuleFour](../Objects/SignalProcessingModuleFour_Object.md) (object)  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  mode = spm4.FilterErrors 'Read 'example return strings" NO ERROR, NO ERROR,
NO ERROR  
indicates no errors, *SUM-OF-COEFFICIENTS, NO ERROR, NO ERROR  
indicates that the sum of all filter coefficients exceed the maximum value for
the Stage-1 filter, *COEFFICIENT *SUM-OF-COEFFICIENTS, NO ERROR, *PARAMETER  
indicates a problems with Stage 1 coefficients and a problem with one or more
of the parameters associated with the Stage 3 filter.  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_FilterErrors(BSTR* dspErrors);  
  
#### Interface

|  ISignalProcessingModuleFour  
  
* * *

