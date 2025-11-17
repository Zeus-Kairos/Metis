##### Write/Read

|

##### [About Magnitude Offset](../../../S1_Settings/Scale.md#Magnitude)  
  
---|---  
  
## MagnitudeOffset Property

* * *

#### Description

|  Offsets the data trace magnitude by the specified value. To offset the data
trace magnitude to a slope value that changes with frequency, use
[MagnitudeSlopeOffset Property](MagnitudeSlopeOffset_Property.md). To
implement a Receiver Cal offset, use [LogMagnitudeOffset
property](LogMagnitudeOffset_Property.htm).  
---|---  
  
####  VB Syntax

|  meas.MagnitudeOffset = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  (object) - A [Measurement](../Objects/Measurement_Object.md) object  
value |  (double) - Offset value in dB.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  meas.MagnitudeOffset = 4 'Write  
offs = meas.MagnitudeOffset 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_MagnitudeOffset(double newVal); HRESULT
get_MagnitudeOffset(double *pVal);  
  
#### Interface

|  IMeasurement4

