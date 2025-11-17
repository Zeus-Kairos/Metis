##### Read-only

|

#####  
  
---|---  
  
## CustomMeasurementConfiguration Property

* * *

#### Description

|  Returns a handle to a custom measurement object on the active channel. You
can use the handle to access custom measurement properties and methods.
Currently, the custom measurement objects to which this property provides
access is:

  * [GainCompressionMeas Object](../Objects/GainCompression_Object.md)

  
---|---  
  
####  VB Syntax

|  Set custMeas = meas.CustomMeasurementConfiguration  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
custMeas |  A variable in which the handle to a custom measurement is returned. (object)  
chan |  A [Measurement](../Objects/Measurement_Object.md) (object)  
  
#### Return Type

|  Custom Measurement object  
  
#### Default

|  None  
  
#### Examples

|  See
examples:[GainCompression](../../COM_Example_Programs/Create_and_Cal_a_Gain_Compression_Measurement.md)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT CustomMeasurementConfiguration(IDispatch** value);  
  
#### Interface

|  IMeaurement12  
  
* * *

