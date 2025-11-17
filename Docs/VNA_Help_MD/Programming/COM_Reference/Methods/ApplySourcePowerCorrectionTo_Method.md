##### Write-only

|

##### [About Source Power Calibration](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## ApplySourcePowerCalibrationTo Method

* * *

#### Description

|  Copies and applies an existing Source Power Calibration to another channel.  
---|---  
  
####  VB Syntax

|  chan.ApplySourcePowerCalibrationTo (fromPortNum, targetChan,
targetPortNum);  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A [Channel](../Objects/Channel_Object.md) (object)  
fromPortNum |  (Long) Port number of the existing source power correction.  
targetChan |  (Long) Channel number to which the source power correction will be copied.  
targetPortNum |  (Long) Port number to which the source power correction will be applied.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  chan.ApplySourcePowerCalibrationTo 1,2,1  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT ApplySourcePowerCalibrationTo (long fromPortNumber, long
otherChannelNumber, long portNumber);  
  
#### Interface

|  IChannel11  
  
* * *

