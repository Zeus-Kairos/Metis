##### Read-only

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# SpanBinsCount Property

* * *

#### Description

|  Read the current span DFT bin count, the number of DFT points processed
across the total RF span. When the Detector is bypassed, this is the number of
points that are sent to the display.  
---|---  
  
#### VB Syntax

|  value = sa.SpanBinsCount  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Long) Variable to store the returned value.  
  
#### Return Type

|  Long  
Example |  value = sa.SpanBinsCount'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SpanBinsCount(long* val);  
  
#### Interface

|  ISpectrumAnalyzer4  
  
* * *

