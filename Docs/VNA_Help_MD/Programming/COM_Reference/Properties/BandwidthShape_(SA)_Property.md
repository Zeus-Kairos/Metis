##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
## BandwidthShape Property

* * *

#### Description

|  Set and read the resolution bandwidth shape.  
---|---  
  
#### VB Syntax

|  sa.BandwidthShape = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Enum as NASABandwidthShape) Choose from: 0 - naNoWindow 1 - naWindowFlatTop 2 - naWindowGaussian 3 - naWindowBlackman 4 - naWindowKaiser [Learn about these choices.](../../../Applications/Spectrum_Analyzer.md#RBW_Shape)  
  
#### Return Type

|  Enum  
  
#### Default

|  2 - naWindowGaussian  
  
#### Examples

|  sa.BandwidthShape = naWindowFlatTop  'Write  
value = sa.BandwidthShape 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_BandwidthShape(tagNASABandwidthShape shape); HRESULT
get_BandwidthShape(tagNASABandwidthShape* shape);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

