##### Read-only

|

#####  
  
---|---  
  
## CustomCalConfiguration Property

* * *

#### Description

|  Calibration for the following VNA Applications is performed using the [GuidedCalibration Object](../Objects/GuidedCalibration_Object.md). This command provides access to additional Properties and Methods which extends the GuidedCal Object. |  Meas Type |  Custom Cal Interface  
---|---  
Gain Compression |  [IGainCompressionCal Object](../Objects/GainCompressionCal_Object.md)  
Noise Figure |  [INoiseCal Object](../Objects/NoiseCal_Object.md)  
Swept IMD |  [ISweptIMD Cal Object](../Objects/SweptIMDCal_Object.md)  
  
####  VB Syntax

|  set custCal = cal.CustomCalConfiguration()  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
custCal |  (object) The handle to an interface that provides application-specific calibration properties..  
cal |  [GuidedCalibration Object](../Objects/GuidedCalibration_Object.md).  
  
#### Return Type

|  Depends on the MeasType. See above table.  
  
#### Default

|  None  
  
#### Examples

|  See
examples:[NoiseFigure](../../COM_Example_Programs/Create_and_Cal_a_NoiseFigure_Measurement.md)
[GainCompression](../../COM_Example_Programs/Create_and_Cal_a_Gain_Compression_Measurement.md)
[SweptIMD](../../COM_Example_Programs/Create_and_Cal_a_Swept_IMD_Measurement.md)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT CustomCalConfiguration(IDispatch** value);  
  
#### Interface

|  IGuidedCalibration4  
  
* * *

