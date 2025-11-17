##### Write/Read

|

##### [About ADC Multiple
Recordings](../../../Applications/Spectrum_Analyzer.htm#Multiple_Recordings)  
  
---|---  
  
# ADCMultRecState Property

* * *

#### Description

|  Set and read the ON/OFF state of the multiple recording function. Multiple
recording allows the ADC Record Size to be divided and acquired in smaller
"chunks" and also to specify a wait period between these acquisitions.  
---|---  
  
#### VB Syntax

|  sa.ADCMultRecState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Boolean) Choose from: 0 - OFF \- ADC record size "chunking" OFF. 1 - ON \- ADC record size "chunking" ON. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#Multiple_Recordings).  
  
#### Return Type

|  Boolean  
  
#### Default

|  0  
  
#### Examples

|  sa.ADCMultRecState = OFF  Write  
value = sa.ADCMultRecState 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_ADCMultRecState(VARIANT_BOOL bEnable); HRESULT
get_ADCMultRecState(VARIANT_BOOL* bEnable);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

