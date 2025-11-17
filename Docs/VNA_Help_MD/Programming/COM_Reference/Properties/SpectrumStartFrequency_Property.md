##### Write/Read

|

##### [About IM Spectrum](../../../Applications/IMSpectrum.md)  
  
---|---  
  
## SpectrumStartFrequency Property

* * *

#### Description

|  Sets and returns the receiver Start frequency for the IM Spectrum
measurement. Valid ONLY when Tracking is NOT enabled and when Sweep Type =
Linear. Otherwise, this setting is ignored.  
---|---  
  
####  VB Syntax

|  ims.SpectrumStartFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
ims |  An [IMSpectrum](../Objects/IMSpectrum_Object.md) Object  
value |  (Double) Start frequency in Hz. Choose a frequency within the range of the VNA.  
  
#### Return Type

|  Double  
  
#### Default

|  950 MHz  
  
#### Examples

|  ims.SpectrumStartFrequency = 10e9 'Write  
value = ims.SpectrumStartFrequency 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SpectrumStartFrequency(double *pVal)  
HRESULT put_SpectrumStartFrequency(double newVal)  
  
#### Interface

|  IIMSpectrum  
  
* * *

