##### Read-Only

|

##### [About LO
Count](../../../Applications/Spectrum_Analyzer.htm#Number_of_LOs)  
  
---|---  
  
# LOCount Property

* * *

#### Description

|  Returns the number of LO acquisitions determined by the Image Reject
selection and the span.  
---|---  
  
#### VB Syntax

|  value = sa.LOCount  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Long) Variable to store the returned number of LOs. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#Number_of_LOs).  
  
#### Return Type

|  Long  
  
#### Default

|  N/A  
  
#### Examples

|  value = sa.LOCount 'Read  
[See an example program.](../../COM_Example_Programs/Spectrum_Analyzer.md)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_LOCount(long* val);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

