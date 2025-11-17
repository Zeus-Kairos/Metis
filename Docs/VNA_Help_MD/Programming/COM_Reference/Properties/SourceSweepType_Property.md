##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
## SourceSweepType Property

* * *

#### Description

|  Set and read the source sweep type.  
---|---  
  
#### VB Syntax

|  sa.SourceSweepType (source) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
source |  (String) Source name enclosed in quotes. Use [SourcePortNames](SourcePortNames_Property.md) to read a list of available source port names. See also [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md).  
value |  (Enum as NASweepType) Choose from: 0 \- naLinearSweep \- SA source sweeps from Start to Stop in linear steps. 3 - naCWTimeSweep \- SA source is at a single frequency, set with [SourceCWFrequency Property](SourceCWFrequency_Property.md).  
  
#### Return Type

|  Enum  
  
#### Default

|  3 - naCWTimeSweep  
  
#### Examples

|  sa.SourceSweepType("Port 1")= naCWTimeSweep  'Write  
value = sa.SourceSweepType("Port 1") 'Read [See an example
program.](../../COM_Example_Programs/Spectrum_Analyzer.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_SourceSweepType(BSTR sourcename, tagNASweepTypes sweeptype);
HRESULT get_SourceSweepType(BSTR sourcename, tagNASweepTypes* sweeptype);  
  
#### Interface

|  ISpectrumAnalyzer  
  
* * *

