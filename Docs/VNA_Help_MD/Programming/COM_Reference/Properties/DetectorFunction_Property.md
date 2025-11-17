##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
## DetectorFunction Property

* * *

#### Description

|  Set and read the detector type.  
---|---  
  
#### VB Syntax

|  sa.DetectorFunction = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Enum as NASADetectorFunction) Choose from: 0 - naDTAverage 1 - naDTSample 2 - naDTPeak 3 - naDTNormal 4 - naDTNegPeak 5 - naDTPeakSample 6 - naDTPeakAverage [Learn more about these settings.](../../../Applications/Spectrum_Analyzer.md#Detector_Type)  
  
#### Return Type

|  Enum  
  
#### Default

|  2 - naDTPeak  
  
#### Examples

|  sa.DetectorFunction = naDTAverage 'Write  
value = sa.DetectorFunction 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_DetectorFunction(tagNASADetectorType type); HRESULT
get_DetectorFunction(tagNASADetectorType* type);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

