##### Read-only

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# RecordSize Property

* * *

#### Description

|  Read the current DFT record size. This value is based on the
[ForceADCRecordSize](ForceADCRecordSize_Property.md) and
[dft.Type](Type_Property.md) settings.  
---|---  
  
#### VB Syntax

|  value = sa.dft.RecordSize  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.dft |  A [SpectrumAnalyzerDFT](../Objects/SpectrumAnalyzerDFT_Object.md) (object)  
value |  (Long) Variable to store the returned value.  
  
#### Return Type

|  Long  
Example |  value = sa.dft.RecordSize 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_RecordSize(long* val);  
  
#### Interface

|  ISpectrumAnalyzerDFT  
  
* * *

