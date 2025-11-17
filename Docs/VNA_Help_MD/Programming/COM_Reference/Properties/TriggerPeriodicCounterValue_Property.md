##### Write/Read

|

##### [About Periodic
Counter](../../../Applications/Spectrum_Analyzer.htm#Periodic_Counter)  
  
---|---  
  
# TriggerPeriodicCounterValue Property

* * *

#### Description

|  Set and read the periodic counter value. This command initiates a
measurement trigger event based on the specified period.  
---|---  
  
#### VB Syntax

|  sa.TriggerPeriodicCounterValue = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Long) Choose a value between 0 and 2147483647. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#Periodic_Counter).  
  
#### Return Type

|  Long  
  
#### Default

|  256  
  
#### Examples

|  sa.TriggerPeriodicCounterValue = 256  'Write  
value = sa.TriggerPeriodicCounterValue 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_TriggerPeriodicCounterValue(long val); HRESULT
get_TriggerPeriodicCounterValue(long* val);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

