##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# SearchOccupiedBWMinFreq Property

* * *

#### Description

|  Set and read the minimum search frequency to use during an Occupied BW
search measurement. Power below this frequency is ignored.  
---|---  
  
#### VB Syntax

|  sa.SearchOccupiedBWMinFreq = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Double) Minimum search frequency value. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#Occupied_BW_search_min).  
  
#### Return Type

|  Double  
  
#### Default

|  250 MHz  
  
#### Examples

|  sa.SearchOccupiedBWMinFreq = 300e6  Write  
value = sa.SearchOccupiedBWMinFreq 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_SearchOccupiedBWMinFreq(double minfreq); HRESULT
get_SearchOccupiedBWMinFreq(double* minfreq);  
  
#### Interface

|  ISpectrumAnalyzer4  
  
* * *

