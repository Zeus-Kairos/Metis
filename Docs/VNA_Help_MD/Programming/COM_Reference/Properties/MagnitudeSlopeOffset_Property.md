##### Write/Read

|

##### [About Magnitude Offset](../../../S1_Settings/Scale.md#Magnitude)  
  
---|---  
  
## MagnitudeSlopeOffset Property

* * *

#### Description

|  Offsets the data trace magnitude to a value that changes linearly with
frequency. The offset slope begins at 0 Hz. To offset the entire data trace
magnitude by a specified value, use [MagnitudeOffset
Property](MagnitudeOffset_Property.htm).  
---|---  
  
####  VB Syntax

|  meas.MagnitudeSlopeOffset = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  (object) - A [Measurement](../Objects/Measurement_Object.md) object  
value |  (double) - Offset slope value in dB / 1GHz.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  meas.MagnitudeSlopeOffset = 4 'Writes a slope offset of 4dB/1GHz.  
offs = meas.MagnitudeSlopeOffset 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_MagnitudeSlopeOffset(double newVal); HRESULT
get_MagnitudeSlopeOffset(double *pVal);  
  
#### Interface

|  IMeasurement4

