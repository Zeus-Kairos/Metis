##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# FilePrefix Property

* * *

#### Description

|  Sets and returns the file name prefix for the data file. The receivers
selected in [ExportReceiverSetList](ExportReceiverSetList_Property.md) will
be appended to the specified prefix name with either "_X.txt" if a text file
is exported ([TextFileEnabled](TextFileEnabled_Property.md)) or "_X.bin" if a
binary file is exported ([BinaryFileEnabled](BinaryFileEnabled_Property.md)).
X is the receiver name.  
---|---  
  
#### VB Syntax

|  sa.dft.FilePrefix = prefix  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.dft |  A [SpectrumAnalyzerDFT](../Objects/SpectrumAnalyzerDFT_Object.md) (object)  
prefix |  (String) Specified prefix.  
  
#### Return Type

|  String  
Example |  sa.dft.FilePrefix = "C:\TEMP\SA_DATA_OUT" 'Write  
value = sa.dft.FilePrefix 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_FilePrefix(BSTR* prefix); HRESULT put_FilePrefix(BSTR prefix);  
  
#### Interface

|  ISpectrumAnalyzerDFT  
  
* * *

