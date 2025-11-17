##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# DCSourceSweepFirstDimension Property

#### Description

|  Set and read the DC sweep order. The SA may be programmed to loop through a
series of spectrum measurements at multiple RF source frequencies, multiple RF
source powers, and multiple DC voltages. These settings determine whether the
DC sources are swept before the RF power and frequencies are swept, or whether
the DC sources are swept after the RF power and frequencies are swept.  
---|---  
  
#### VB Syntax

|  sa.DCSourceSweepFirstDimension (source) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (Enum as NASADCSweepFirstTypes) Choose from: 0 - naSADCFirst \- Sweep through each DC voltage step first then sweep through the next frequency. 1 - naSARFFirst \- Sweep through each frequency step first then sweep through the next DC voltage. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#SourceSetupTab)  
  
#### Return Type

|  Enum  
  
#### Default

|  naSADCFirst  
  
#### Examples

|  sa.DCSourceSweepFirstDimension("Port 1")= naSADCFirst  'Write  
value = sa.DCSourceSweepFirstDimension("Port 1") 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_DCSourceSweepFirstDimension(tagNASADCSweepFirstTypes first);
HRESULT get_DCSourceSweepFirstDimension(tagNASADCSweepFirstTypes* first);  
  
#### Interface

|  ISpectrumAnalyzer

