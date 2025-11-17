##### Write/Read

|

##### [About Guided Power Cal](../../../S3_Cals/Guided_Power_Calibration.md)

##### [About NFX Cal](../../../Applications/Noise_Cal.md#SelectDutConn)  
  
---|---  
  
## PowerSensorConnectorType Property

* * *

#### Description

|  Set and read the power sensor connector type which is used to perform a
Power Cal during an S-parameter calibration or during an NFX Cal. When used
with [Guided Power Cal](../../../S3_Cals/Guided_Power_Calibration.md), first
enable a power cal using [PerformPowerCalibration
Property](PerformPowerCalibration_Property.htm).  
---|---  
  
####  VB Syntax

|  guided.PowerSensorConnectorType (n) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
guided |  A [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object )  
n |  (Long) VNA port number to connect power sensor to.  
value |  (String) - Power sensor connector type. Use [ValidConnectorType Property](ValidConnectorType_Property.md) to return a list of valid connector types. Set to "Ignored" to NOT compensate for the adapter.  
  
#### Return Type

|  String  
  
#### Default

|  Not applicable.  
  
#### Examples

|  guided.PowerSensorConnectorType(1) = "APC3.5 male" 'Write  
ctype = guided.PowerSensorConnectorType(1) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PowerSensorConnectorType (long port, BSTR* val); HRESULT
put_PowerSensorConnectorType (long port, BSTR newVal);  
  
#### Interface

|  IGuidedCalibration6  
  
* * *

  

