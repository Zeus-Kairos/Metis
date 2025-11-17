##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# SourcePowerRepeatCount Property

#### Description

|  Set and read the number of SA (receiver) sweeps for each Source Step. This
setting is common to all sources.  
---|---  
  
#### VB Syntax

|  sa.SourcePowerRepeatCount = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Long)  Repeat count. Choose an integer value of 1 or higher.  
  
#### Return Type

|  Long  
  
#### Default

|  1  
  
#### Examples

|  sa.SourcePowerRepeatCount = 10  'Write  
value = sa.SourcePowerRepeatCount 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_SourcePowerRepeatCount(long count); HRESULT
get_SourcePowerRepeatCount(long* count);  
  
#### Interface

|  ISpectrumAnalyzer

