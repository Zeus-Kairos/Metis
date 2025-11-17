##### Write-only

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## SetCalInfoEx Method (for source power cals)

* * *

#### Description

|  This command replaces [SetCalInfo2
Method](SetCalInfo2_\(power\)_Method.htm). Specifies the channel and the
source port to be used for the source power calibration about to be performed.  
---|---  
  
####  VB Syntax

|  powerCalibrator.SetCalInfoEx channel, srcPort, [powerOffset,] [display]  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
powerCalibrator |  (object) \- A [SourcePowerCalibrator](../Objects/SourcePowerCalibrator_Object.md) object  
channel |  (long integer) - Number of the VNA channel (not power meter channel) on which the source power cal will be performed. If the channel does not already exist, it will be created.  
srcPort |  (long integer) - Port number on which the source power cal will be performed. Note: If the port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source VNA-x model, then you must use [chan.getPortNumber](GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md).  
[powerOffset] |  (double) - Optional argument. Sets or returns a power level offset from the VNA test port power. This can be a gain or loss value (in dB) to account for components you connect between the source and the reference plane of your measurement. For example, specify 10 dB to account for a 10 dB amplifier at the input of your DUT. Following the calibration, the VNA power readouts are adjusted by this value. This argument performs the same function as [chan.SourcePowerCalPowerOffset Property](../Properties/SourcePowerCalPowerOffset_Property.md)  
[display] |  (boolean) Optional argument. Enables and disables the display of power readings on the VNA screen. After the source power cal data is acquired, this setting is reset to ON. If unspecified, value is set to ON. True \- Display of power readings is ON False \- Display of power readings is OFF  
  
#### Return Type

|  None  
  
#### Default

|  Not Applicable  
  
#### Examples

|  powerCalibrator.SetCalInfoEx 1, 1, -10, True  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT SetCalInfoEx( long Channel, long SourcePort, double PowerOffset =
0., VARIANT_BOOL bDisplay = VARIANT_TRUE);  
  
#### Interface

|  ISourcePowerCalibrator4  
  
* * *

