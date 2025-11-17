##### Write/Read

|

##### [About IM Spectrum](../../../Applications/IMSpectrum.md)  
  
---|---  
  
## SpectrumCenterFrequency Property

* * *

#### Description

|  Sets and returns the receiver Center frequency for the IM Spectrum
measurement. Valid ONLY when Tracking is NOT enabled and when [Sweep
Type](SweepType_ims_Property.htm) = Linear. Otherwise, this setting is
ignored.  
---|---  
  
####  VB Syntax

|  ims.SpectrumCenterFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
ims |  An [IMSpectrum](../Objects/IMSpectrum_Object.md) Object  
value |  (Double) Center frequency in Hz. Choose a frequency within the range of the VNA.  
  
#### Return Type

|  Double  
  
#### Default

|  1.0 GHz  
  
#### Examples

|  ims.SpectrumCenterFrequency = 10e9 'Write  
value = ims.SpectrumCenterFrequency 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SpectrumCenterFrequency(double *pVal)  
HRESULT put_SpectrumCenterFrequency(double newVal)  
  
#### Interface

|  IIMSpectrum  
  
* * *

