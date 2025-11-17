##### Write/Read

|

##### [About SA Application](../../../Applications/Spectrum_Analyzer.md)  
  
---|---  
  
# ImageRejectStrength Property

* * *

#### Description

|  Sets and returns the image rejection strength. During the image rejection
process, several LO acquisitions overlap at the same RF frequency. As a
result, different RF signal values can be returned. This command sets the
acceptable power differences between LOs in determining actual signals.  
---|---  
  
####  VB Syntax

|  sa.ImageRejectStrength = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa |  A [SpectrumAnalyzer](../Objects/SpectrumAnalyzer_Object.md) (object)  
value |  (enum NASAStrength) \- Choose from: 0 naSAWeak: 3 dB (approximate value, depends on RBW) 1 naSANormal: 1 dB (approximate value, depends on RBW) 2 naSAStrong: 0.5 dB (approximate value, depends on RBW)  
  
#### Return Type

|  Enum as NASAStrength  
  
#### Default

|  naSANormal  
  
#### Examples

|  sa.ImageRejectStrength = naSAStrong 'Write  
Strength = sa.ImageRejectStrength 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ImageRejectStrength(tagNASAStrength* pVal)  
HRESULT put_ImageRejectStrength(tagNASAStrength newVal)  
  
#### Interface

|  ISpectrumAnalyzer4  
  
* * *

