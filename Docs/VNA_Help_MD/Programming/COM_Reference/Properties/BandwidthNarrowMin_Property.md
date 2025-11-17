##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# BandwidthNarrowMin Property

* * *

#### Description

|  Set and read the minimum value for narrow DFT bandwidth. The minimum narrow
DFT bandwidth setting is 500 kHz. The
[AutoBandwidth](AutoBandwidth_Property.md) must be set to OFF to set this
value manually.  
---|---  
  
#### VB Syntax

|  sa.dft.BandwidthNarrowMin = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.dft |  A [SpectrumAnalyzerDFT](../Objects/SpectrumAnalyzerDFT_Object.md) (object)  
  
#### Return Type

|  Double  
  
#### Examples

|  sa.dft.BandwidthNarrowMin = 5e5  'Write  
value = sa.dft.BandwidthNarrowMin 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_BandwidthNarrowMin(double minbw); HRESULT
get_BandwidthNarrowMin(double* minbw);  
  
#### Interface

|  ISpectrumAnalyzerDFT  
  
* * *

