##### Write/Read

|

##### [About PNA-X Pulsed
Capabilities](../../../Applications/Narrowband_Pulsed_Application.htm)  
  
---|---  
  
## ADCCaptureMode Property

* * *

#### Description

|  Sets and returns the ADC capture mode modeled as a 2-pole switch in the
diagram on the
[SignalProcessingModuleFour](../Objects/SignalProcessingModuleFour_Object.md)
page. The switch either bypasses or routes the IF through the 3-stage digital
filter.  
---|---  
  
####  VB Syntax

|  spm4.ADCCaptureMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
spm4 |  A [SignalProcessingModuleFour](../Objects/SignalProcessingModuleFour_Object.md) (object)  
value |  (Enum as NAStates) Capture mode. naOFF (0) - The digital filters are used to process IF information. The filters can be configured automatically or manually using [FilterMode Property](FilterMode_Property.md). naON (1) - The digital filters are bypassed and the raw ADC readings are taken directly. With DSP 4 versions, a maximum of 4096 data points per sweep can be acquired. With DSP 5 versions, the [VNA maximum data points](../../../S1_Settings/DPoints.md#PointsDiag) per sweep can be acquired. [Learn more about DSP Versions.](../../../S0_Start/HelpAbout.md#DSPchanges)  
  
#### Return Type

|  Enum  
  
#### Default

|  OFF  
  
#### Examples

|  spm4.ADCCaptureMode = 0 'Write  
mode = spm4.ADCCaptureMode 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ADCCaptureMode(tagNAStates* pCaptureMode); HRESULT
put_ADCCaptureMode(tagNAStates pCaptureMode);  
  
#### Interface

|  ISignalProcessingModuleFour  
  
* * *

