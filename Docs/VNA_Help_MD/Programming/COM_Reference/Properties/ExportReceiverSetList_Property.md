##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# ExportReceiverSetList Property

* * *

#### Description

|  Sets and returns the list of exported receivers. Note: This list can
contain receivers that are not currently measured in the channel. However,
this is not an issue. To get the current list of receivers that export data,
query [ExportReceiverList](ExportReceiverList_Property.md).  
---|---  
  
#### VB Syntax

|  sa.dft.ExportReceiverSetList = list  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.dft |  A [SpectrumAnalyzerDFT](../Objects/SpectrumAnalyzerDFT_Object.md) (object)  
list |  (String) Variable to store the returned list.  
  
#### Return Type

|  String  
Example |  sa.dft.ExportReceiverSetList = "B" 'Write  
list = sa.dft.ExportReceiverSetList 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ExportReceiverSetList(BSTR* ReceiverList); HRESULT
put_ExportReceiverSetList(BSTR ReceiverList);  
  
#### Interface

|  ISpectrumAnalyzerDFT  
  
* * *

