##### Write/Read

|

##### [About Enhanced Power
Cal](../../../S3_Cals/Guided_Power_Calibration.htm)

##### [About NF Cal](../../../Applications/Noise_Cal.md)  
  
---|---  
  
## PowerCalibrationLevel Property

* * *

#### Description

|  Set and read the power level at which to perform the source cal during an
Enhanced Power Cal or during the power cal portion of some Noise Figure Cals.  
---|---  
  
####  VB Syntax

|  object.PowerCalibrationLevel (port) = value  
  
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

|  cal.PowerCalibrationLevel(1) = -5 'Write  
pLevel = nfx.PowerCalibrationLevel(1) 'Read [See enhanced power cal
example](../../COM_Example_Programs/Perform_a_Guided_Cal_using_COM.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PowerCalibrationLevel(long port, double* pVal) HRESULT
put_PowerCalibrationLevel(long port, double* pVal)  
  
#### Interface

|  IGuidedCalibration6  
  
* * *

  

