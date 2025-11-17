##### Write/Read

|

##### [About Guided Power Cal](../../../S3_Cals/Guided_Power_Calibration.md)

##### [About NFX Cal](../../../Applications/Noise_Cal.md)  
  
---|---  
  
## PowerCalibrationPowerLevel Property

* * *

#### Description

|  Set and read the power level at which to perform the source cal during an
Guided Power Cal or during an NFX Cal. When used with [Guided Power
Cal](../../../S3_Cals/Guided_Power_Calibration.htm), first enable a power cal
using [PerformPowerCalibration
Property](PerformPowerCalibration_Property.htm).  
---|---  
  
####  VB Syntax

|  object.PowerCalibrationPowerLevel (port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  A [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (Object)  
port |  (Long) VNA Port number to connect the power sensor.  
value |  (Double) - Power level in dB. Choose a value from +30 to (-30).  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  cal.PowerCalibrationPowerLevel(1) = -5 'Write  
pLevel = nfx.PowerCalibrationPowerLevel(1) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PowerCalibrationPowerLevel(long port, double* pVal) HRESULT
put_PowerCalibrationPowerLevel(long port, double* pVal)  
  
#### Interface

|  IGuidedCalibration6  
  
* * *

