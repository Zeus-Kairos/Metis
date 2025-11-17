##### Write/Read

|

##### [About User Ranges](../../../S4_Collect/Markers.md#domain)  
  
---|---  
  
## UserRangeMax Property

* * *

#### Description

|  Note: This property on the Channel Object is superseded by the same
property on the Measurement Object. Sets the stimulus stop value for the
specified User Range.  
---|---  
  
####  VB Syntax

|  chan.UserRangeMax(domainType,Rnum) = value - Superseded
meas.UserRangeMax(Rnum) = value mark.UserRangeMax(Rnum) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A [Channel](../Objects/Channel_Object.md) (object) - Superseded  
meas |  A [Measurement](../Objects/Measurement_Object.md) (object)  
mark |  A [Marker](../Objects/Marker_Object.md) (object) To assign a marker to a User Range, use the [UserRange Property](User_Range_Property.md).  
domainType |  This argument is no longer required. The domain type is inferred by the measurement or marker. (enum NADomainType) \- Choose from: 0 - naDomainFrequency 1 - naDomainTime 2 - naDomainPower  
Rnum |  (long integer) - User Range number. Choose any number between 1 and 16 (0=Full Span)  
value |  (double) - Stop value. Choose any number within the full span of the channel.  
  
#### Return Type

|  Double  
  
#### Default

|  The current stimulus setting for the channel  
  
#### Examples

|  mark.UserRangeMax(1) = 3e9 'Write meas.UserRangeMax(1) = 3e9 'Write  
UseRngeMax = mark.UserRangeMax(1) 'Read UseRngeMax = meas.UserRangeMax(2)
'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_UserRangeMax(long rangeNumber, double maxValue) HRESULT
get_UserRangeMax(long rangeNumber, double *maxValue)  
  
#### Interface

|  IMeasurement IMarker  
  
* * *

