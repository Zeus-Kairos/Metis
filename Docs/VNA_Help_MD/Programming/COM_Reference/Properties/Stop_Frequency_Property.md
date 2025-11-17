##### Write/Read

|

##### [About Linear Frequency Sweep](../../../S1_Settings/Sweep.md#lin_freq)  
  
---|---  
  
## StopFrequency Property

* * *

#### Description

|  Sets or returns the stop frequency of the channel. (Channel Object) Sets or
returns the stop frequency of the segment. (Segment Object) Sets or returns
the stop frequency of the FOM Range. (FOMRange Object Sets or returns the stop
frequency of the Power Sensor coverage (GuidedCalibrationPowerSensor Object)
Sets or returns the stop frequency of the Phase Reference Calibration. See
also [Measurement2](../Objects/Measurement_Object.md#IMeasurement2Interface)
interface.  
---|---  
  
####  VB Syntax

|  object.StopFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  Any of the following: [Channel](../Objects/Channel_Object.md) (object) [Segment](../Objects/Segment_Object.md) (object) [FOMRange](../Objects/FOMRange_Object.md) (object) [GuidedCalibrationPowerSensor](../Objects/GuidedCalibrationPowerSensor_Object.md) (object) [PhaseReferenceCalibration](../Objects/PhaseReferenceCalibration_Object.md) (object)  
value |  (double) - Stop frequency in Hertz. Choose any number between 70 (minimum) and maximum frequency limits of the analyzer. If the stop frequency is set less than the start frequency, then the start frequency is set to the stop frequency - frequency span.  
  
#### Return Type

|  Double  
  
#### Default

|  Channel - Maximum frequency of the analyzer. Segment - 0 FOMRange - Maximum
frequency of the analyzer. GuidedCalibrationPowerSensor - Maximum frequency of
the analyzer. PhaseReferenceCalibration - Maximum frequency of the analyzer.  
  
#### Examples

|  chan.StopFrequency = 4.5e9 'sets the stop frequency for the channel object
-Write  
stopfreq = Chan.StopFrequency 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_StopFrequency(double *pVal) HRESULT put_StopFrequency(double
newVal)  
  
#### Interface

|  IChannel ISegment IFOMRange IGuidedCalibrationPowerSensor  
  
* * *

