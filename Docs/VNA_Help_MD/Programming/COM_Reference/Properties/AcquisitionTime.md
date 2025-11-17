##### Read-Only

|

##### [About Acquisition
Time](../../../Applications/Spectrum_Analyzer.htm#Acquisition_Time)  
  
---|---  
  
# AcquisitionTime Property

* * *

#### Description

|  Returns the LO acquisition time which is the ADC Record Size x ADC Sampling
Frequency (10 nsec or 40 nsec) x (1 + Stacking) x (Video Average.Coefficient).  
---|---  
  
#### VB Syntax

|  value = sa.AcquisitionTime  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Double) Variable to store the returned number of LOs. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#Acquisition_Time).  
  
#### Return Type

|  Double  
  
#### Default

|  N/A  
  
#### Examples

|  value = sa.AcquisitionTime 'Read  
[See an example program.](../../COM_Example_Programs/Spectrum_Analyzer.md)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_AcquisitionTime(double* val);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

