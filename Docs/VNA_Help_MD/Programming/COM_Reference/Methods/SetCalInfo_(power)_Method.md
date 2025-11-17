##### Write-only

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## SetCalInfo Method (for source power cals) - Superseded

* * *

#### Description

|  This command is replaced by [SetCalInfoEx Method](SetCalInfoEx_Method.md)
Specifies the technique to be used for the source power calibration about to
be performed, and the channel and source port for which it is to be performed.  
---|---  
  
####  VB Syntax

|  powerCalibrator.SetCalInfo calMethod, channel, sourcePort, calPower  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
powerCalibrator |  (object) \- A SourcePowerCalibrator object  
calMethod |  (enum NASourcePowerCalMethod) The method of gathering the source power correction data. 0  naPowerMeter (the only method currently supported)  
channel |  (long integer) - Number of the VNA channel (not power meter channel) on which the source power cal will be performed. If the channel doesnt already exist, it will be created.  
sourcePort |  (long integer) - Port number on which the source power cal will be performed.  
calPower |  (double) - Specifies the power level that is expected at the desired reference plane (input or output of DUT) following the source power cal.  
  
#### Return Type

|  None  
  
#### Default

|  Not Applicable  
  
#### Examples

|  powerCalibrator.SetCalInfo naPowerMeter, 1, 1, -10  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT SetCalInfo(tagNASourcePowerCalMethod calMethod, long channel, long
sourcePort, double calPower);  
  
#### Interface

|  ISourcePowerCalibrator

