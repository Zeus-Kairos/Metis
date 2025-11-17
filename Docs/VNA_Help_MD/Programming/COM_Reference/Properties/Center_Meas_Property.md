##### Read-only

|

#####  
  
---|---  
  
## Center Property

* * *

#### Description

|  Returns the stimulus value of the center data point for the measurement.
This function does NOT work for segment sweep measurements. To understand how
this property is useful, see [IMeasurement2
Interface](../Objects/Measurement_Object.htm#IMeasurement2Interface).  
---|---  
  
####  VB Syntax

|  value = meas.Center  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Double) \- Variable to store the returned value.  
meas |  A Measurement (object)  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Print meas.Center 'prints the center data point  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Center(double * Val);  
  
#### Interface

|  IMeasurement2

