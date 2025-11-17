##### Write/Read

|

##### [About Smoothing](../../../S2_Opt/Trce_Noise.md#Smoothing)  
  
---|---  
  
## SmoothingAperture Property

* * *

#### Description

|  Specifies or returns the amount of smoothing as a ratio of the number of
data points in the measurement trace. There is no COM command for specifying
smoothing by number of aperture points.  
---|---  
  
####  VB Syntax

|  meas.SmoothingAperture = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A [Measurement](../Objects/Measurement_Object.md) (object)  
value |  (double) - Smoothing Aperture. A ratio of (aperture points / trace points). Choose any number between .01 and .25.  
  
#### Return Type

|  Double  
  
#### Default

|  .25  
  
#### Examples

|  meas.SmoothingAperture = .10 'Write  
saperture = meas.SmoothingAperture 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_SmoothingAperture(double *pVal)  
HRESULT put_SmoothingAperture(double newVal)  
  
#### Interface

|  IMeasurement  
  
* * *

