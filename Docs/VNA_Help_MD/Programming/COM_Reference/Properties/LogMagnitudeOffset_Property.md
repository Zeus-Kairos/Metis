##### Write/Read

|

##### [About Receiver
Cal](../../../S3_Cals/PwrCalibration.htm#ReceiverPowerCal)  
  
---|---  
  
## LogMagnitudeOffset Property Superseded

* * *

#### Description

|  Note: This property is replaced by [DoReceiverPowerCal
Method](../Methods/DoReceiverPowerCal_Method.htm). For Receiver Calibration \-
Sets or returns the value to offset the normalized unratioed power measurement
data. The unratioed power measurement is effectively calibrated to the power
level specified by the value of LogMagnitudeOffset as soon as the
[Normalization property](Normalization_Property.md) is set to ON after
calling the [DataToDivisor](../Methods/DataToDivisor_Method.md) method. To
offset the data trace magnitude a specified value, use [MagnitudeOffset
Property](MagnitudeOffset_Property.htm)  
---|---  
  
####  VB Syntax

|  meas.LogMagnitudeOffset = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  (object) - A [Measurement](../Objects/Measurement_Object.md) object  
value |  (double) - Offset value in dBm.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  meas.LogMagnitudeOffset = -10 'Write (-10 dBm)  
calpower = meas.LogMagnitudeOffset 'Read  
meas.DataToDivisor 'Store meas data as measurement divisor  
meas.Normalize = 1 'Measurement is now calibrated to 10 dBm  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_LogMagnitudeOffset(double newVal); HRESULT
get_LogMagnitudeOffset(double *pVal);  
  
#### Interface

|  IMeasurement

