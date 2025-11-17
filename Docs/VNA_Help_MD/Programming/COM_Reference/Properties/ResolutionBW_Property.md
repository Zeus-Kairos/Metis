##### Write/Read

|

##### [About IM Spectrum](../../../Applications/IMSpectrum.md)  
  
---|---  
  
## ResolutionBW Property

* * *

#### Description

|  Sets and returns the Resolution Bandwidth for the IM Spectrum measurement.  
---|---  
  
####  VB Syntax

|  ims.ResolutionBW = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
ims |  An [IMSpectrum](../Objects/IMSpectrum_Object.md) Object  
value |  (Double) Resolution BW in Hz. Choose from: 60k | 100k | 150k | 300k, 600k | 1.0M | 3.0M If an invalid number is specified, the VNA will round up to the closest valid number.  
  
#### Return Type

|  Double  
  
#### Default

|  600 kHz  
  
#### Examples

|  ims.ResolutionBW = 150e3 'Write  
value = ims.ResolutionBW 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ResolutionBW(double *pVal)  
HRESULT put_ResolutionBW(double newVal)  
  
#### Interface

|  IIMSpectrum  
  
* * *

