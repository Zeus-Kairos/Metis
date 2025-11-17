##### Write/Read

|

##### [About IM Spectrum](../../../Applications/IMSpectrum.md)  
  
---|---  
  
## SpectrumStopFrequency Property

* * *

#### Description

|  Sets and returns the receiver Stop frequency for the IM Spectrum
measurement. Valid ONLY when Tracking is NOT enabled and when Sweep Type =
Linear. Otherwise, this setting is ignored.  
---|---  
  
####  VB Syntax

|  ims.SpectrumStopFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
ims |  An [IMSpectrum](../Objects/IMSpectrum_Object.md) Object  
value |  (Double) Stop frequency in Hz. Choose a frequency within the range of the VNA.  
  
#### Return Type

|  Double  
  
#### Default

|  950 MHz  
  
#### Examples

|  ims.SpectrumStopFrequency = 10e9 'Write  
value = ims.SpectrumStopFrequency 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SpectrumStopFrequency(double *pVal)  
HRESULT put_SpectrumStopFrequency(double newVal)  
  
#### Interface

|  IIMSpectrum  
  
* * *

