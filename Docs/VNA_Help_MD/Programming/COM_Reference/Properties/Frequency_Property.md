##### Write / Read

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)

##### [About PMAR](../../../System/Configure_a_Power_Meter_As_Receiver.md)  
  
---|---  
  
## Frequency Property

* * *

#### Description

|  Sets or returns the frequency associated with a Power Sensor CalFactor
Segment or Sets or returns the frequency associated with a Power Loss Segment.  
---|---  
  
#### VB Syntax

|  object.Frequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  One of the following objects: [PowerSensorCalFactorSegment](../Objects/PowerSensorCalFactorSegment_Object.md) [PowerSensorCalFactorSegmentPMAR](../Objects/PowerSensorCalFactorSegmentPMAR_Object.md) [PowerLossSegment](../Objects/PowerLossSegment_Object.md) [PowerLossSegmentPMAR](../Objects/PowerLossSegmentPMAR_Object.md)  
value |  (double)  Frequency in units of Hz. This can be any non-negative value (limited by the maximum value of double).  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  seg.Frequency = 6e9 'Write  
freq = seg.Frequency 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_Frequency(double newVal); HRESULT get_Frequency(double *pVal);  
  
#### Interface

|  One of the above objects.  
  
* * *

