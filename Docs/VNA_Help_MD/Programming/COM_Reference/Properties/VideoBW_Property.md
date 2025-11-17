##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
## VideoBW Property

* * *

#### Description

|  Set and read the Video bandwidth. Also set
[VideoBWMode](VideoBWMode_Property.md) to naManual.  
---|---  
  
#### VB Syntax

|  sa.VideoBW = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Double) Choose a value between 3 Hz and 3 MHz. Going outside this range places the trace into a hold mode. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#Video_Bandwidth).  
  
#### Return Type

|  Double  
  
#### Default

|  100 kHz  
  
#### Examples

|  sa.VideoBW = 1e5  Write  
value = sa.VideoBW 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_VideoBW(double freq); HRESULT get_VideoBW(double* freq);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

