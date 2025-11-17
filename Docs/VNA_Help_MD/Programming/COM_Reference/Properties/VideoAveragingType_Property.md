##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
## VideoAveragingType Property

* * *

#### Description

|  Set and read the video averaging type.  
---|---  
  
#### VB Syntax

|  sa.VideoAveragingType = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Enum as NASAVideoAveragingType) Choose from: 0 - naPower 1 - naLog 2 - naVoltage 3 - naVoltageMax 4 - naVoltageMin [Learn about these settings.](../../../Applications/Spectrum_Analyzer.md#VideoAverType)  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - naPower  
  
#### Examples

|  sa.VideoAveragingType = naLog  'Write  
value = sa.VideoAveragingType 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_VideoAveragingType(tagNASAVideoAveragingType type); HRESULT
get_VideoAveragingType(tagNASAVideoAveragingType* type);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

