##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# DCSourceSweepState

#### Description

|  Set and read the ON/OFF state of the DC sources. If ON, the DC sources
sweep between their start and stop voltages.  
---|---  
  
#### VB Syntax

|  sa.DCSourceSweepState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Boolean) Choose from: 0 - OFF \- DC sweep OFF. 1 - ON \- DC sweep ON. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#SourceSetupTab)  
  
#### Return Type

|  Boolean  
  
#### Default

|  0  
  
#### Examples

|  sa.DCSourceSweepState = OFF  Write  
value = sa.DCSourceSweepState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_DCSourceSweepState(VARIANT_BOOL bEnable); HRESULT
get_DCSourceSweepState(VARIANT_BOOL* bEnable);  
  
#### Interface

|  ISpectrumAnalyzer

