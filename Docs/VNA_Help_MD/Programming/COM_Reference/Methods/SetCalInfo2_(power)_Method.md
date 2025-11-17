##### Write-only

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## SetCalInfo2 Method (for source power cals) - Superseded

* * *

#### Description

|  This command is replaced by [SetCalInfoEx Method](SetCalInfoEx_Method.md)
Specifies the technique, the channel, and the source port to be used for the
source power calibration about to be performed.  
---|---  
  
####  VB Syntax

|  powerCalibrator.SetCalInfo2 calMethod, channel, sourcePort, [powerOffset,]
[display]  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
powerCalibrator |  (object) \- A [SourcePowerCalibrator3](../Objects/SourcePowerCalibrator_Object.md) object  
calMethod |  (enum NASourcePowerCalMethod) Selects the calibration method to be used for the source power cal acquisition. 0 - naPowerMeter Power Meter is used for all readings. (same as ["fast iteration" box](../../../S3_Cals/PwrCalibration.md#SourceDiag) not checked on dialog box) 1 - naPowerMeterAndReceiver Power meter for the first iteration; then use the reference receiver for remaining readings if necessary (same as ["fast iteration" box](../../../S3_Cals/PwrCalibration.md#SourceDiag) checked on dialog box)  
channel |  (long integer) - Number of the VNA channel (not power meter channel) on which the source power cal will be performed. If the channel does not already exist, it will be created.  
sourcePort |  (long integer) - Port number on which the source power cal will be performed.  
[powerOffset] |  (double) - Optional argument. Sets or returns a power level offset from the VNA test port power. This can be a gain or loss value (in dB) to account for components you connect between the source and the reference plane of your measurement. For example, specify 10 dB to account for a 10 dB amplifier at the input of your DUT. Following the calibration, the VNA power readouts are adjusted by this value. This argument performs the same function as [chan.SourcePowerCalPowerOffset Property](../Properties/SourcePowerCalPowerOffset_Property.md)  
[display] |  (boolean) Optional argument. Enables and disables the display of power readings on the VNA screen. After the source power cal data is acquired, this setting is reset to ON. If unspecified, value is set to ON. True \- Display of power readings is ON False \- Display of power readings is OFF  
  
#### Return Type

|  None  
  
#### Default

|  Not Applicable  
  
#### Examples

|  powerCalibrator.SetCalInfo2 naPowerMeter, 1, 1, -10, True  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT SetCalInfo2( tagNASourcePowerCalMethod enumCalMethod, long Channel,
long SourcePort, double PowerOffset = 0., VARIANT_BOOL bDisplay =
VARIANT_TRUE);  
  
#### Interface

|  ISourcePowerCalibrator3

