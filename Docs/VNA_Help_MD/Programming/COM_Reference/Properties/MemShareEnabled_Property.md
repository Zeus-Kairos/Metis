##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# MemShareEnabled Property

* * *

#### Description

|  Enables/disables exporting data to shared memory, which is the fastest way
to transfer data between applications.  
---|---  
  
####  VB Syntax

|  sa.dft.MemShareEnabled = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.dft |  A [SpectrumAnalyzerDFT](../Objects/SpectrumAnalyzerDFT_Object.md) (object)  
value |  (Boolean) Choose from: 0 - OFF \- Disable memory sharing. 1 - ON \- Enable memory sharing.  
  
#### Return Type

|  Boolean  
  
#### Default

|  OFF  
  
#### Examples

|  sa.dft.MemShareEnabled = ON 'Write  
value = sa.dft.MemShareEnabled 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MemShareEnabled(VARIANT_BOOL* enable)  
HRESULT put_MemShareEnabled(VARIANT_BOOL enable)  
  
#### Interface

|  ISpectrumAnalyzerDFT  
  
* * *

