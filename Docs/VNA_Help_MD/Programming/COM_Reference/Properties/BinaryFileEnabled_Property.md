##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# BinaryFileEnabled Property

* * *

#### Description

|  Enables/disables binary file (*.bin) output.  
---|---  
  
####  VB Syntax

|  sa.dft.BinaryFileEnabled = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.dft |  A [SpectrumAnalyzerDFT](../Objects/SpectrumAnalyzerDFT_Object.md) (object)  
value |  (Boolean) Choose from: 0 - OFF \- Disable binary file output. 1 - ON \- Enable binary file output.  
  
#### Return Type

|  Boolean  
  
#### Default

|  OFF  
  
#### Examples

|  sa.dft.BinaryFileEnabled = ON 'Write  
value = sa.dft.BinaryFileEnabled 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_BinaryFileEnabled(VARIANT_BOOL* enable)  
HRESULT put_BinaryFileEnabled(VARIANT_BOOL enable)  
  
#### Interface

|  ISpectrumAnalyzerDFT  
  
* * *

