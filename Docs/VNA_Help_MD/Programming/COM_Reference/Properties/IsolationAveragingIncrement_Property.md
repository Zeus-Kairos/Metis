##### Read/Write

|

##### [About ECAL](../../../S3_Cals/ModifyCalKits.md)  
  
---|---  
  
## IsolationIncrementAveraging Property

* * *

#### Description

|  Value by which to increment (increase) the channel's averaging factor
during measurement of isolation in an ECal calibration. Note: If <value> is
greater than 1 and the channel currently has averaging turned OFF, averaging
will be turned ON only during the isolation measurements and with the
averaging factor equal to <value>.  
---|---  
  
####  VB Syntax

|  cal.IsolationIncrementAveraging = _value_  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal |  A [Calibrator](../Objects/Calibrator_Object.md) (object)  
value |  (Long) Incremental Averaging factor. The maximum averaging factor is 65536 (2^16).  
  
#### Return Type

|  Long Integer  
  
#### Default

|  8  
  
#### Examples

|  oCal.IsolationAveragingIncrement = 16 'Write  
avgIncr = oCal.IsolationAveragingIncrement ' Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_IsolationAveragingIncrement(long *pVal); HRESULT
put_IsolationAveragingIncrement(long newVal);  
  
#### Interface

|  ICalibrator7  
  
* * *

