##### Write/Read

|

##### [About User Ranges](../../../S4_Collect/Markers.md#domain)  
  
---|---  
  
## StatisticsRange Property

* * *

#### Description

|  Sets the User Range number for calculating measurement statistics. Set the
start and stop values for a User Range with
[UserRangeMin](User_Range_Min_Property.md) and
[UserRangeMax.](User_Range_Max_Property.md) There are 16 User Ranges per
channel. User ranges are applied independently to any measurement.  
---|---  
  
####  VB Syntax

|  meas.StatisticsRange = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A Measurement (object)  
value |  (long integer) \- Range Number. Choose any number between 0 and 16 0 is Full Span 1 - 16 are user-defined ranges  
  
#### Return Type

|  Long Integer  
  
#### Default

|  0  
  
#### Examples

|  meas.StatisticsRange = 2 'Write  
statrange = meas.StatisticsRange 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_StatisticsRange(long* rangeNumber)  
HRESULT put_StatisticsRange(long rangeNumber)  
  
#### Interface

|  IMeasurement  
  
* * *

