##### Write/Read

|

##### [About IM Spectrum](../../../Applications/IMSpectrum.md)  
  
---|---  
  
## SpectrumSpanFrequency Property

* * *

#### Description

|  Sets and returns the Span of receiver frequencies for the IM Spectrum
measurement. Valid ONLY when Tracking is NOT enabled and when [Sweep
Type](SweepType_ims_Property.htm) = Linear. Otherwise, this setting is
ignored.  
---|---  
  
####  VB Syntax

|  ims.SpectrumSpanFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
ims |  An [IMSpectrum](../Objects/IMSpectrum_Object.md) Object  
value |  (Double) Frequency span in Hz. Choose a frequency within the range of the VNA.  
  
#### Return Type

|  Double  
  
#### Default

|  100 MHz  
  
#### Examples

|  ims.SpectrumSpanFrequency = 10e9 'Write  
value = ims.SpectrumSpanFrequency 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SpectrumSpanFrequency(double *pVal)  
HRESULT put_SpectrumSpanFrequency(double newVal)  
  
#### Interface

|  IIMSpectrum  
  
* * *

