##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# TextFileEnabled Property

* * *

#### Description

|  Enables/disables text file (*.txt) output.  
---|---  
  
####  VB Syntax

|  sa.dft.TextFileEnabled = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.dft |  A [SpectrumAnalyzerDFT](../Objects/SpectrumAnalyzerDFT_Object.md) (object)  
value |  (Boolean) Choose from: 0 - OFF \- Disable text file output. 1 - ON \- Enable text file output.  
  
#### Return Type

|  Boolean  
  
#### Default

|  OFF  
  
#### Examples

|  sa.dft.TextFileEnabled = ON 'Write  
value = sa.dft.TextFileEnabled 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_TextFileEnabled(VARIANT_BOOL* enable)  
HRESULT put_TextFileEnabled(VARIANT_BOOL enable)  
  
#### Interface

|  ISpectrumAnalyzerDFT  
  
* * *

