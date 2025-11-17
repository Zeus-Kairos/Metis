##### Write/Read

|

##### [About Guided Power Cal](../../../S3_Cals/Guided_Power_Calibration.md)

##### [About NFXCal](../../../Applications/Swept_IMD.md#CalOverview)  
  
---|---  
  
## PowerSensorCalKitType Property

* * *

#### Description

|  Set and read the cal kit to be used for calibrating at the reference plane
when the power sensor connector is different from the DUT port. When used with
[Guided Power Cal](../../../S3_Cals/Guided_Power_Calibration.md), first
enable a power cal using [PerformPowerCalibration
Property](PerformPowerCalibration_Property.htm).  
---|---  
  
####  VB Syntax

|  object.PowerSensorCalkitType (n) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  A [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object)  
n |  (Long) VNA port number for which cal kit is specified.  
value |  (String) - Cal Kit. Use [CompatibleCalKits Property](CompatibleCalKits_Property.md) to return a list of valid cal kits.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  gguided.PowerSensorCalkitType(1) = "85052B" 'Write  
ctype =guided.PowerSensorCalkitType(1) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PowerSensorCalkitType(long port, BSTR* Val) HRESULT
put_PowerSensorCalkitType(long port, BSTR newVal)  
  
#### Interface

|  IGuidedCalibration6  
  
* * *

