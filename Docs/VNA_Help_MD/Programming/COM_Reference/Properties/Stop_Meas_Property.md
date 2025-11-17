##### Read- only

|  
---|---  
  
## Stop Property

* * *

#### Description

|  Returns the stimulus value of the last data point for the measurement. To
understand how this property is useful, see [IMeasurement2
Interface](../Objects/Measurement_Object.htm#IMeasurement2Interface).  
---|---  
  
####  VB Syntax

|  value = meas.Stop  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Double) Variable to store the returned value  
meas |  A Measurement (object)  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Print meas.Stop 'prints the stimulus value of the last data point  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Stop(double * Val);  
  
#### Interface

|  IMeasurement2

