##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# AutoBandwidth Property

* * *

#### Description

|  Set and read the default values for DFT bandwidth.  
---|---  
  
#### VB Syntax

|  sa.dft.AutoBandwidth = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.dft |  A [SpectrumAnalyzerDFT](../Objects/SpectrumAnalyzerDFT_Object.md) (object)  
value |  (Boolean) Choose from: 0 - OFF \- DFT minimum and maximum values are set manually: Narrow \- 500 kHz to 11 MHz Wide \- 500 kHz to 44 MHz 1 - ON \- DFT minimum and maximum values are set to their default values: Narrow \- 1 MHz to 10 MHz Wide \- 1 MHz to 34 MHz  
  
#### Return Type

|  Boolean  
  
#### Default

|  1  
  
#### Examples

|  sa.dft.AutoBandwidth = 0  'Write  
bwidth = sa.dft.AutoBandwidth 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_AutoBandwidth(VARIANT_BOOL bEnable); HRESULT
get_AutoBandwidth(VARIANT_BOOL* bEnable);  
  
#### Interface

|  ISpectrumAnalyzerDFT  
  
* * *

