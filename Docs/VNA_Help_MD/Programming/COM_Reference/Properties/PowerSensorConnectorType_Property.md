##### Write/Read

|

##### [About GainCompressionCal](../../../Applications/GCA_Cal.md)

##### [About SweptIMDCal](../../../Applications/Swept_IMD.md#CalOverview)

##### [About Guided Power Cal](../../../S3_Cals/Guided_Power_Calibration.md)  
  
---|---  
  
## PowerSensorConnectorType Property

* * *

#### Description

|  Set and read the power sensor connector type which is used to perform the
Source Power Cal. Use
[PowerSensorCalKitType](PowerSensorCalKitType_Property.md) to specify the Cal
Kit to use for the cal.  
---|---  
  
####  VB Syntax

|  object.PowerSensorConnectorType = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object. |  A [GainCompressionCal](../Objects/GainCompressionCal_Object.md) (object) A [SweptIMDCal](../Objects/SweptIMDCal_Object.md) (object) A [GuidedCalibrationPowerSensor](../Objects/GuidedCalibrationPowerSensor_Object.md) (object)  
value |  (String) - Power sensor connector type. Use [ValidConnectorType Property](ValidConnectorType_Property.md) to return a list of valid connector types. Select "Ignored" to NOT compensate for the adapter.  
  
#### Return Type

|  String  
  
#### Default

|  Not applicable  
  
#### Examples

|  gca.PowerSensorConnectorType = "APC3.5 male" 'Write  
ctype = imd.PowerSensorConnectorType 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PowerSensorConnectorType(BSTR* Val) HRESULT
put_PowerSensorConnectorType(BSTR newVal)  
  
#### Interface

|  IGainCompressionCal2 ISweptIMDCal IGuidedPowerCalPowerSensor  
  
* * *

  

