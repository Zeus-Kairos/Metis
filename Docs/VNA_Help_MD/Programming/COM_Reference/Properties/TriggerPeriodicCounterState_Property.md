##### Write/Read

|

##### [About Periodic
Counter](../../../Applications/Spectrum_Analyzer.htm#Periodic_Counter)  
  
---|---  
  
# TriggerPeriodicCounterState Property

* * *

#### Description

|  Set and read the ON/OFF state of a measurement trigger event based on the
specified period set using the TriggerPeriodicCounterValue command.  
---|---  
  
#### VB Syntax

|  sa.TriggerPeriodicCounterState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Boolean) Choose from: 0 - OFF \- Periodic counter OFF. 1 - ON \- Periodic counter ON. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#Periodic_Counter).  
  
#### Return Type

|  Boolean  
  
#### Default

|  0  
  
#### Examples

|  sa.TriggerPeriodicCounterState = OFF  Write  
value = sa.TriggerPeriodicCounterState 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_TriggerPeriodicCounterState(VARIANT_BOOL bEnable); HRESULT
get_TriggerPeriodicCounterState(VARIANT_BOOL* bEnable);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

