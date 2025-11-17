##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# MemShareName Property

* * *

#### Description

|  Assigns a specified name to the Microsoft Windows shared data mechanism
when [MemShareEnabled](MemShareEnabled_Property.md) is enabled.  
---|---  
  
#### VB Syntax

|  sa.dft.MemShareName = MemFileName  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.dft |  A [SpectrumAnalyzerDFT](../Objects/SpectrumAnalyzerDFT_Object.md) (object)  
MemFileName |  (String) Memory file name.  
  
#### Return Type

|  String  
Example |  sa.dft.MemShareName = "Mem_Share" 'Write  
name = sa.dft.MemShareName 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MemShareName(BSTR* MemFileName); HRESULT put_MemShareName(BSTR
MemFileName);  
  
#### Interface

|  ISpectrumAnalyzerDFT  
  
* * *

