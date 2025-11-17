##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
## SourceStartFrequency Property

* * *

#### Description

|  Set and read the source start frequency.  
---|---  
  
#### VB Syntax

|  sa.SourceStartFrequency (source) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
source |  (String) Source name enclosed in quotes. Use [SourcePortNames](SourcePortNames_Property.md) to read a list of available source port names. See also [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md).  
value |  (Double)  Start frequency in Hz. Choose a value within the frequency range of the analyzer.  
  
#### Return Type

|  Double  
  
#### Default

|  Start frequency of the analyzer.  
  
#### Examples

|  sa.SourceStartFrequency("Port 1") = 1e9  'Write  
value = sa.SourceStartFrequency("Port 1") 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_SourceStartFrequency(BSTR sourcename, double frequency);
HRESULT get_SourceStartFrequency(BSTR sourcename, double* frequency);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

