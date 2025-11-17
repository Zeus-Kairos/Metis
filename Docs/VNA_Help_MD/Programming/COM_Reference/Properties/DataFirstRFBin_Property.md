##### Read-only

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# DataFirstRFBin Property

* * *

#### Description

|  Returns the frequency of the first RF bin. Note: This value can differ
slightly from the SA Sweep start frequency, the frequency of the first RF bin
is aligned with the current DFT grid.  
---|---  
  
#### VB Syntax

|  value = sa.dft.DataFirstRFBin  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.dft |  A [SpectrumAnalyzerDFT](../Objects/SpectrumAnalyzerDFT_Object.md) (object)  
value |  (Double) Variable to store the returned value.  
  
#### Return Type

|  Double  
Example |  value = sa.dft.DataFirstRFBin 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_DataFirstRFBin(double* val);  
  
#### Interface

|  ISpectrumAnalyzerDFT  
  
* * *

