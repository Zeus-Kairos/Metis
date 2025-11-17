##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
## EnableImageRejectTraces Property

* * *

#### Description

|  Set and read the show / hide state of the image reject traces in the
measurement parameters dialog.  
---|---  
  
#### VB Syntax

|  sa.EnableImageRejectTraces = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Boolean) Choose from: 0 - OFF -Disable image reject traces. 1 - ON \- Enable image reject traces and set mode using [ImageReject](ImageReject_Property.md). [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#Enable_Image_Reject_Traces).  
  
#### Return Type

|  Boolean  
  
#### Default

|  0  
  
#### Examples

|  sa.EnableImageRejectTraces = 0 'Write  
value = sa.EnableImageRejectTraces 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_EnableImageRejectTraces(VARIANT_BOOL bEnable); HRESULT
get_EnableImageRejectTracesVARIANT_BOOL* bEnable);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

