##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
## EnableRandomizedLO Property

* * *

#### Description

|  Set and read the LO randomize state.  
---|---  
  
#### VB Syntax

|  sa.EnableRandomizedLO = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Boolean) Choose from: 0 - OFF \- LO Randomize is set to OFF. 1 - ON \- LO Randomize is set to ON. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#Randomized_LO).  
  
#### Return Type

|  Boolean  
  
#### Default

|  1  
  
#### Examples

|  sa.EnbaleRandomizedLO = OFF  Write  
value = sa.EnbaleRandomizedLO 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_EnableRandomizedLO(VARIANT_BOOL bEnable); HRESULT
get_EnableRandomizedLO(VARIANT_BOOL* bEnable);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

