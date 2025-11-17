##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
## VideoBWMode Property

* * *

#### Description

|  Set and read how the video bandwidth is set. When ON, video bandwidth is
set based on RBW/VBW ratio.  
---|---  
  
#### VB Syntax

|  sa.VideoBWMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Enum as NAModes) Choose from: 1 - naMANUAL \- Video BW is set manually using [VideoBW Property](VideoBW_Property.md) 0 - naAUTO \- Video BW is set automatically. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#Video_Bandwidth_Auto).  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - naAUTO  
  
#### Examples

|  sa.VideoBWMode = naMANUAL  Write  
value = sa.VideoBWMode 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_VideoBWMode(tagNAModes mode); HRESULT
get_VideoBWMode(tagNAModes* mode);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

