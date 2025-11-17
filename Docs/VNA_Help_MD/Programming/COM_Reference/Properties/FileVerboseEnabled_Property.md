##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# FileVerboseEnabled Property

* * *

#### Description

|  Enables/disables exporting frequency and data for text files. Data is not
exported until the next new sweep occurs.  
---|---  
  
####  VB Syntax

|  sa.dft.FileVerboseEnabled = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.dft |  A [SpectrumAnalyzerDFT](../Objects/SpectrumAnalyzerDFT_Object.md) (object)  
value |  (Boolean) Choose from: 0 - OFF \- Disable verbose mode. 1 - ON \- Enable verbose mode.  
  
#### Return Type

|  Boolean  
  
#### Default

|  OFF  
  
#### Examples

|  sa.dft.FileVerboseEnabled = ON 'Write  
value = sa.dft.FileVerboseEnabled 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_FileVerboseEnabled(VARIANT_BOOL* enable)  
HRESULT put_FileVerboseEnabled(VARIANT_BOOL enable)  
  
#### Interface

|  ISpectrumAnalyzerDFT  
  
* * *

