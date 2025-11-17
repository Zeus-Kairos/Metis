##### Write-only

|

##### [About Receiver Cal](../../../S4_Collect/Markers.md)  
  
---|---  
  
## DataToDivisor Method Superseded

* * *

#### Description

|  Note: This property is replaced by [DoReceiverPowerCal
Method](DoReceiverPowerCal_Method.htm). Stores the measurements data to the
measurements divisor buffer for use by the Normalization data processing
algorithm. Normalization is currently supported only on measurements of
unratioed power, for purpose of receiver power calibration. If DataToDivisor
is called on a ratioed measurement (such as an S-parameter), it will return an
error.  
---|---  
  
####  VB Syntax

|  meas.DataToDivisor  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  (object) - A Measurement object  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  meas.DataToDivisor  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT DataToDivisor();  
  
#### Interface

|  IMeasurement

