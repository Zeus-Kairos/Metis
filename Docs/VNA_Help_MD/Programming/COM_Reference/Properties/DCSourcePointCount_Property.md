##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# DCSourcePointCount Property

#### Description

|  Set and read the number of steps the source will make across the specified
source DC range. This setting is common to all sources.  
---|---  
  
#### VB Syntax

|  sa.DCSourcePointCount = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Long)  Point count. Choose an integer value of 1 or higher. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#SourceSetupTab)  
  
#### Return Type

|  Long  
  
#### Default

|  1  
  
#### Examples

|  sa.DCSourcePointCount = 10  'Write  
value = sa.DCSourcePointCount 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_DCSourcePointCount(long points); HRESULT
get_DCSourcePointCount(long* points);  
  
#### Interface

|  ISpectrumAnalyzer

