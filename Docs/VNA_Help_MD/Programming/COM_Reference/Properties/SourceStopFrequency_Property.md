##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
## SourceStopFrequency Property

* * *

#### Description

|  Set and read the source stop frequency.  
---|---  
  
#### VB Syntax

|  sa.SourceStopFrequency (source) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
source |  (String) Source name enclosed in quotes. Use [SourcePortNames](SourcePortNames_Property.md) to read a list of available source port names. See also [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md).  
value |  (Double) Stop frequency in Hz. Choose a value within the frequency range of the analyzer.  
  
#### Return Type

|  Double  
  
#### Default

|  Stop frequency of the analyzer.  
  
#### Examples

|  sa.SourceStopFrequency("Port 1") = 1e9  'Write  
value = sa.SourceStopFrequency("Port 1") 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_SourceStopFrequency(BSTR sourcename, double frequency); HRESULT
get_SourceStopFrequency(BSTR sourcename, double* frequency);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

