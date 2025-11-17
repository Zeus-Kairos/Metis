##### Write-Read

|

##### [About PNA-X Pulsed
Capabilities](../../../Applications/Narrowband_Pulsed_Application.htm)  
  
---|---  
  
## Stage3FilterType Property

* * *

#### Description

|  Sets and returns the Stage 3 filter type. This command is only used when
[FilterMode](FilterMode_Property.md) is set to Manual.  
---|---  
  
####  VB Syntax

|  spm4.Stage3FilterType = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
spm4 |  A [SignalProcessingModuleFour](../Objects/SignalProcessingModuleFour_Object.md) (object)  
value |  (String) Filter type. Chose from:

  * "RECT" Rectangular Window Filter
  * "TUKEY" Tukey Filter
  * "PWIN" Pulse window filter

  
  
#### Default

|  TUKEY  
  
#### Examples

|  spm4.Stage3FilterType = "PWIN"  
mode = spm4.Stage3FilterType 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Stage3FilterType(BSTR* pFType); HRESULT
put_Stage3FilterType(BSTR GType);  
  
#### Interface

|  ISignalProcessingModuleFour  
  
* * *

