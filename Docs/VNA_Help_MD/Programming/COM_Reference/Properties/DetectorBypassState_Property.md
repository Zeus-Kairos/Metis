##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
## EnableDetectorBypass Property

* * *

#### Description

|  Set and read the ON/OFF state of the detector bypass setting.  
---|---  
  
#### VB Syntax

|  sa.EnableDetectorBypass = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Boolean) Choose from: 0 - OFF \- Detector bypass OFF. 1 - ON \- Detector bypass ON. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#FFT_Point_Mode).  
  
#### Return Type

|  Boolean  
  
#### Default

|  0  
  
#### Examples

|  sa.EnableDetectorBypass = ON  'Write  
value = sa.EnableDetectorBypass 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_EnableDetectorBypass(VARIANT_BOOL bEnable); HRESULT
get_EnableDetectorBypass(VARIANT_BOOL* bEnable);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

