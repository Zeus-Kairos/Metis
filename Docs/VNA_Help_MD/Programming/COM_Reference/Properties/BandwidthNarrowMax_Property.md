##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# BandwidthNarrowMax Property

* * *

#### Description

|  Set and read the maximum value for narrow DFT bandwidth. The maximum narrow
DFT bandwidth setting is 11 MHz. The
[AutoBandwidth](AutoBandwidth_Property.md) must be set to OFF to set this
value manually.  
---|---  
  
#### VB Syntax

|  sa.dft.BandwidthNarrowMax = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.dft |  A [SpectrumAnalyzerDFT](../Objects/SpectrumAnalyzerDFT_Object.md) (object)  
  
#### Return Type

|  Double  
  
#### Examples

|  sa.dft.BandwidthNarrowMax = 11e6  'Write  
value = sa.dft.BandwidthNarrowMax 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_BandwidthNarrowMax(double maxbw); HRESULT
get_BandwidthNarrowMax(double* maxbw);  
  
#### Interface

|  ISpectrumAnalyzerDFT  
  
* * *

