##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# BandwidthWideMax Property

* * *

#### Description

|  Set and read the maximum value for wide DFT bandwidth. The maximum wide DFT
bandwidth setting is 44 MHz. The [AutoBandwidth](AutoBandwidth_Property.md)
must be set to OFF to set this value manually.  
---|---  
  
#### VB Syntax

|  sa.dft.BandwidthWideMax = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.dft |  A [SpectrumAnalyzerDFT](../Objects/SpectrumAnalyzerDFT_Object.md) (object)  
  
#### Return Type

|  Double  
  
#### Examples

|  sa.dft.BandwidthWideMax = 44e6  'Write  
value = sa.dft.BandwidthWideMax 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_BandwidthWideMax(double maxbw); HRESULT
get_BandwidthWideMax(double* maxbw);  
  
#### Interface

|  ISpectrumAnalyzerDFT  
  
* * *

