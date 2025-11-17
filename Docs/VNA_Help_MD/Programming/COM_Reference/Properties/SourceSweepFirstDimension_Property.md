##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# SourceSweepFirstDimension Property

#### Description

|  Set and read the sweep order. This command applies whenever frequency and
power are being swept (sweep type set using the
[SourceSweepType2](SourceSweepType2_Property.md) command). Otherwise, this
setting is ignored. For example, if all the active sources are set to CW
and/or linear sweep type, or if all the active sources are set to CW and/or
power sweep type, the sweep order is ignored. If any active source is set to
linear and power sweep type, or if an active source is set to linear sweep
type and another active source is set to power sweep type, then the sweep
order setting will be used.  
---|---  
  
#### VB Syntax

|  sa.SourceSweepFirstDimension (source) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Enum as NASASweepFirstTypes) Choose from: 0 - naSAFreqFirst \- Sweep from Start to Stop frequency first followed by a power sweep. 1 - naSAPowerFirst \- Sweep power first then sweep from Start to Stop frequency.  
  
#### Return Type

|  Enum  
  
#### Default

|  naSAFreqFirst  
  
#### Examples

|  sa.SourceSweepFirstDimension("Port 1")= naSAPowerFirst  'Write  
value = sa.SourceSweepFirstDimension("Port 1") 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_SourceSweepFirstDimension(tagNASASweepFirstTypes first);
HRESULT get_SourceSweepFirstDimension(tagNASASweepFirstTypes* first);  
  
#### Interface

|  ISpectrumAnalyzer

