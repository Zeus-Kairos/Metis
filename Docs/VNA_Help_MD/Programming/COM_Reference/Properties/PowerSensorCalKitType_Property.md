##### Write/Read

|

##### [About
GainCompressionCal](../../../Applications/GCA_Cal.htm#SelectDUTDiag)

##### [About
SweptIMDCal](../../../Applications/Swept_IMD.htm#CalSelectDUTConn)

##### [About Guided Power Cal](../../../S3_Cals/Guided_Power_Calibration.md)  
  
---|---  
  
## PowerSensorCalkitType Property

* * *

#### Description

|  Set and read the cal kit to be used for calibrating at the adapter when the
power sensor connector is different from the DUT. Use
[PowerSensorConnectorType](PowerSensorConnectorType_Property.md) to specify
the connector type of the adapter.  
---|---  
  
####  VB Syntax

|  object.PowerSensorCalkitType = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  A [GainCompressionCal](../Objects/GainCompressionCal_Object.md) (object) A [SweptIMDCal](../Objects/SweptIMDCal_Object.md) (object) A [GuidedCalibrationPowerSensor](../Objects/GuidedCalibrationPowerSensor_Object.md) (object)  
value |  (String) - Cal Kit. Use [CompatibleCalKits Property](CompatibleCalKits_Property.md) to return a list of valid cal kits.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  gca.PowerSensorCalkitType = "85052B" 'Write  
ctype = imd.PowerSensorCalkitType 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PowerSensorCalkitType(BSTR* Val) HRESULT
put_PowerSensorCalkitType(BSTR newVal)  
  
#### Interface

|  IGainCompressionCal2 ISweptIMD IGuidedCalibrationPowerSensor  
  
* * *

