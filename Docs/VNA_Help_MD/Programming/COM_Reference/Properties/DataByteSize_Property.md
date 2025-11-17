##### Read-only

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# DataByteSize Property

* * *

#### Description

|  Returns the byte size of the data to be exported in binary mode. Note:
Returned number can exceed the maximum integer number size. In that case, an
error will be raised. For that reason, we provide an access to larger numbers
with the same query and LSB or MSB suffixes.  
---|---  
  
#### VB Syntax

|  value = sa.dft.DataByteSize  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.dft |  A [SpectrumAnalyzerDFT](../Objects/SpectrumAnalyzerDFT_Object.md) (object)  
value |  (Variant) Variable to store the returned value.  
  
#### Return Type

|  Variant  
Example |  value = sa.dft.DataByteSize 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_DataByteSize(VARIANT* val);  
  
#### Interface

|  ISpectrumAnalyzerDFT  
  
* * *

