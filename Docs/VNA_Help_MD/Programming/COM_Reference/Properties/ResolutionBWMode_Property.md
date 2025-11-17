##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
## ResolutionBWMode Property

* * *

#### Description

|  Set and read how the resolution bandwidth is set. When ON, resolution
bandwidth is set based on Span/RBW ratio.  
---|---  
  
#### VB Syntax

|  sa.ResolutionBWMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Enum as NAModes) Choose from: 1 - naMANUAL \- Res. BW is set manually using [ResolutionBW Property](ResolutionBW_\(SA\)_Property.md) 0 - naAUTO \- Res. BW is set automatically and will not set resolution bandwidth above 300 kHz. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#Resolution_Bandwidth_Auto).  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - naAUTO  
  
#### Examples

|  sa.ResolutionBWMode = 1  'Write  
value = sa.ResolutionBWMode 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_ResolutionBWMode(tagNAModes mode); HRESULT
get_ResolutionBWMode(tagNAModes* mode);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

