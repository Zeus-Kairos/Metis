##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# SourcePowerPointCount Property

#### Description

|  Set and read the number of steps the source will make across the specified
source power range. This setting is common to all sources.  
---|---  
  
#### VB Syntax

|  sa.SourcePowerPointCount = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Long)  Point count. Choose an integer value of 1 or higher.  
  
#### Return Type

|  Long  
  
#### Default

|  1  
  
#### Examples

|  sa.SourcePowerPointCount = 10  'Write  
value = sa.SourcePowerPointCount 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_SourcePowerPointCount(long points); HRESULT
get_SourcePowerPointCount(long* points);  
  
#### Interface

|  ISpectrumAnalyzer

