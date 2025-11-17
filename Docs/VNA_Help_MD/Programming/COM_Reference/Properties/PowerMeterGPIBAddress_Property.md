##### Write / Read

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## PowerMeterGPIBAddress Property Superseded

* * *

#### Description

|  This command is replaced with [PowerMeterInterface
Object](../Objects/PowerMeterInterface_Object.htm). Specifies the GPIB address
of the power meter that will be referenced by the SourcePowerCalibrator
object. When performing a source power cal, the VNA will search VISA
interfaces that are configured in the Keysight IO LIbraries on the VNA.  
---|---  
  
#### VB Syntax

|  powerCalibrator.PowerMeterGPIBAddress = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
powerCalibrator |  (object) - A SourcePowerCalibrator (object)  
value |  (long integer)  Power meter GPIB address. Choose any number between 0 and 30.  
  
#### Return Type

|  Long integer  
  
#### Default

|  13  
  
#### Examples

|  Set powerCalibrator = pna.SourcePowerCalibrator  
powerCalibrator.PowerMeterGPIBAddress = 13 'Write  
  
pwrMtrAddress = powerCalibrator.PowerMeterGPIBAddress 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_PowerMeterGPIBAddress(long newVal); HRESULT
get_PowerMeterGPIBAddress(long *pVal);  
  
#### Interface

|  ISourcePowerCalibrator  
  
* * *

