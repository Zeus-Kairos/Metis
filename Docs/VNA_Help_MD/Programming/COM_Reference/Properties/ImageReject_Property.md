##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
## ImageRejectMethod Property

* * *

#### Description

|  Set and read the image reject value.  
---|---  
  
#### VB Syntax

|  sa.ImageRejectMethod = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Enum as NASAImageRejectMethod) Choose from: 0 - naIRNoneHigh 1 - naIRNoneLow 2 - naIRMin 3 - naIRNormal 4 - naIBetter 5 - naIRMax [Learn about these settings.](../../../Applications/Spectrum_Analyzer.md#Image_Reject)  
  
#### Return Type

|  Enum  
  
#### Default

|  3 - naIRNormal  
  
#### Examples

|  sa.ImageRejectMethod = naIRNormal  'Write  
value = sa.ImageRejectMethod 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_ImageReject(tagNASAImageRejectMethod algorithm); HRESULT
get_ImageReject(tagNASAImageRejectMethod* algorithm);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

