##### Write/Read

|

##### [About Triggering
ADC](../../../Applications/Spectrum_Analyzer.htm#Advanced_Trigger_Modes)  
  
---|---  
  
# TriggerADCLevelState Property

* * *

#### Description

|  Set and read the ON/OFF state of a measurement trigger event that will
occur whenever the ADC level is greater than the value specified using the
TriggerADCLevelValue command.  
---|---  
  
#### VB Syntax

|  sa.TriggerADCLevelState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Boolean) Choose from: 0 - OFF \- ADC measurement trigger OFF. 1 - ON \- ADC measurement trigger ON. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#Advanced_Trigger_Modes).  
  
#### Return Type

|  Boolean  
  
#### Default

|  0  
  
#### Examples

|  sa.TriggerADCLevelState = OFF  Write  
value = sa.TriggerADCLevelState 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_TriggerADCLevelState(VARIANT_BOOL bEnable); HRESULT
get_TriggerADCLevelState(VARIANT_BOOL* bEnable);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

