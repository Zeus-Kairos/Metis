##### Write-only

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## putSourcePowerCalData Method Superseded

* * *

#### Description

|  Inputs source power calibration data (as variant data type) to this channel
for a specific source port. Note: This method is Superseded. It is replaced by
[PutSourcePowerCalDataEx Method](Put_SourcePowerCalDataEx_Method.md)  
---|---  
  
####  VB Syntax

|  chan.putSourcePowerCalData sourcePort, data  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  (object)  A Channel object  
sourcePort |  (long integer)  The source port for which calibration data is being requested.  
data |  (variant)  Array of source power cal data being input.  
  
#### Return Type

|  None  
  
#### Default

|  Not Applicable  
  
#### Examples

|  chan.putSourcePowerCalData 1, varData  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT putSourcePowerCalData(long sourcePort, VARIANT varData);  
  
#### Interface

|  IChannel

