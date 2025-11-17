##### Read-only

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# DataExportWindowingFactor Property

* * *

#### Description

| Returns the windowing factor for band power computation. This factor is
derived from the window type (Gaussian, flat top, etc.). When doing the sum of
linear power over a band, use this factor to compensate the side lobe effect
of windowing to get an accurate band power value.  
---|---  
  
#### VB Syntax

| value = sa.dft.DataExportWindowingFactor  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.dft | A [SpectrumAnalyzerDFT](../Objects/SpectrumAnalyzerDFT_Object.md) (object)  
value | (Double) Variable to store the returned value.  
  
#### Return Type

| Double  
Example | value = sa.dft.DataExportWindowingFactor 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_DataExportWindowingFactor(double* WindowingFactor);  
  
#### Interface

| ISpectrumAnalyzerDFT2  
  
* * *

