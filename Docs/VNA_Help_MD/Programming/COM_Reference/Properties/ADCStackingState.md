##### Write/Read

|

##### [About ADC
Stacking](../../../Applications/Spectrum_Analyzer.htm#ADC_Stacking)  
  
---|---  
  
# ADCStackingState Property

* * *

#### Description

|  Set and read the ON/OFF state of the ADC sample stacking.  
---|---  
  
#### VB Syntax

|  sa.ADCStackingState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Boolean) Choose from: 0 - OFF \- ADC sample stacking is set to OFF. 1 - ON \- ADC sample stacking is set to ON. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#ADC_Stacking).  
  
#### Return Type

|  Boolean  
  
#### Default

|  0  
  
#### Examples

|  sa.ADCStackingState = OFF  Write  
value = sa.ADCStackingState 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_ADCStackingState(VARIANT_BOOL bEnable); HRESULT
get_ADCStackingState(VARIANT_BOOL* bEnable);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

