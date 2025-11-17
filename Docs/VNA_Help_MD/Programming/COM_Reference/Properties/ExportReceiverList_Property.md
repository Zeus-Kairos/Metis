##### Read-only

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# ExportReceiverList Property

* * *

#### Description

|  Returns the currently exported receiver list. Note: The list is set with
[ExportReceiverSetList](ExportReceiverSetList_Property.md) can contain more
receivers, this query will only return the ones that are currently measured
and that are in the receiver list.  
---|---  
  
#### VB Syntax

|  list = sa.dft.ExportReceiverList  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.dft |  A [SpectrumAnalyzerDFT](../Objects/SpectrumAnalyzerDFT_Object.md) (object)  
list |  (String) Variable to store the returned list.  
  
#### Return Type

|  String  
Example |  list = sa.dft.ExportReceiverList 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ExportReceiverList(BSTR* ReceiverList);  
  
#### Interface

|  ISpectrumAnalyzerDFT  
  
* * *

