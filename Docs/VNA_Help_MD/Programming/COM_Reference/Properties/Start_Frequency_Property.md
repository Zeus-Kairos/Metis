##### Write/Read

|

##### [About Linear Frequency Sweep](../../../S1_Settings/Sweep.md#lin_freq)  
  
---|---  
  
## StartFrequency Property

* * *

#### Description

|  Sets or returns the start frequency of the channel. (Channel Object) Sets
or returns the start frequency of the segment. (Segment Object) Sets or
returns the start frequency of the FOM Range. (FOMRange Object Sets or returns
the start frequency of the Power Sensor coverage (GuidedCalibrationPowerSensor
Object) See also
[Measurement2](../Objects/Measurement_Object.md#IMeasurement2Interface)
interface  
---|---  
  
####  VB Syntax

|  object.StartFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  Any of the following: [Channel](../Objects/Channel_Object.md) (object) [Segment](../Objects/Segment_Object.md) (object) [FOMRange](../Objects/FOMRange_Object.md) (object) [GuidedCalibrationPowerSensor](../Objects/GuidedCalibrationPowerSensor_Object.md) (object)  
value |  (double) - Start frequency in Hertz. Choose any number between the minimum and maximum frequencies of the analyzer. If start frequency is set greater than the stop frequency, then the stop frequency is set to the start frequency + frequency span.  
  
#### Return Type

|  Double  
  
#### Default

|  Channel - Minimum frequency of the analyzer Segment - 0 FOMRange - Minimum
frequency of the analyzer PowerSensor - Minimum frequency of the analyzer  
  
#### Examples

|  chan.StartFrequency = 4.5e9 'sets the start frequency of a linear sweep for
the channel object -Write  
startfreq = Chan.StartFrequency 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_StartFrequency(double *pVal) HRESULT put_StartFrequency(double
newVal)  
  
#### Interface

|  IChannel ISegment IFOMRange IGuidedCalibrationPowerSensor  
  
* * *

