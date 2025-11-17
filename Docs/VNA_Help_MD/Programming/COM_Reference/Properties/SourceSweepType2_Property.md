##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# SourceSweepType2 Property

#### Description

|  Set and read the source sweep type.  
---|---  
  
#### VB Syntax

|  sa.SourceSweepType2 (source) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
source |  (String) Source name enclosed in quotes. Use [SourcePortNames](SourcePortNames_Property.md) to read a list of available source port names. See also [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md).  
value |  (Enum as NASASourceSweepTypes) Choose from: 0 - naSASourceFreqSweep \- SA source sweeps from Start to Stop in linear steps. 1 - naSASourceFreqAndPowerSweep \- The source is set to sweep from the Start to Stop frequency and power sweep. The order is determined by the [SourceSweepFirstDimension](SourceSweepFirstDimension_Property.md) command. 2 - naSASourcePowerSweep \- SA source is set to a power sweep. 3 - naSASourceCWFreqSweep \- SA source is at a single frequency, set with [SourceCWFrequency Property](SourceCWFrequency_Property.md).  
  
#### Return Type

|  Enum  
  
#### Default

|  3 - naSASourceCWFreqSweep  
  
#### Examples

|  sa.SourceSweepType2("Port 1")= naSASourceCWFreqSweep'Write  
value = sa.SourceSweepType2("Port 1") 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_SourceSweepType2(BSTR sourcename, tagNASASourceSweepTypes
sweeptype); HRESULT get_SourceSweepType2(BSTR sourcename,
tagNASASourceSweepTypes* sweeptype);  
  
#### Interface

|  ISpectrumAnalyzer

