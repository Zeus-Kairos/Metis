##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# ADCEnableFIRFor25Mhz Property

* * *

#### Description

|  Set and read the FIR filter for 25 MHz decimation.  
---|---  
  
#### VB Syntax

|  sa.ADCEnableFIRFor25Mhz = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Boolean) Choose from: 0 - OFF \- Disable 25 MHz FIR filter. 1 - ON \- Enable 25 MHz FIR filter.  
  
#### Return Type

|  Boolean  
  
#### Default

|  0  
  
#### Examples

|  sa.ADCEnableFIRFor25Mhz = 0  'Write  
filter = sa.ADCEnableFIRFor25Mhz 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_ADCEnableFIRFor25Mhz(VARIANT_BOOL bEnable); HRESULT
get_ADCEnableFIRFor25Mhz(VARIANT_BOOL* bEnable);  
  
#### Interface

|  ISpectrumAnalyzer4  
  
* * *

