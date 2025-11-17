##### Write/Read

|

##### [About Number of Points](../../../S1_Settings/DPoints.md)  
  
---|---  
  
## NumberOfPoints Property

* * *

#### Description

|  Sets or returns the Number of Points of the channel. Sets or returns the
Number of Points of the segment.

### See Also

  * [Measurement2 Interface](../Objects/Measurement_Object.md#IMeasurement2Interface) to learn how this method differs from [meas.NumberofPoints](NumberofPoints_meas_Property.md)
  * [Gain Compression Number of Points](NumberOfFrequencyPoints_Property.md).
  * [Swept IMD limitations](../../../Applications/Swept_IMD_and_IM_Spectrum_Concepts.md#LimitedAcq)

  
---|---  
  
####  VB Syntax

|  object.NumberOfPoints = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  Channel (object) or CalSet (object) - Read-only property  
value |  (long) \- Number of Points. For channel, choose any number from 1 to the [VNA max number of points](../../../S1_Settings/DPoints.md#PointsDiag). For segment, the total number of points in all segments cannot exceed the VNA maximum. A segment can have as few as 1 point.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  201 for channel 21 for segment  
  
#### Examples

|  chan.NumberOfPoints = 201 'sets the number of points for all measurements
in the channel. -Write  
numofpts = chan.NumberOfPoints 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_NumberOfPoints(long *pVal)  
HRESULT put_NumberOfPoints(long newVal)  
  
#### Interface

|  IChannel  
ISegment |CalSet3  
  
* * *

