##### Write / Read

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## Path Property

* * *

#### Description

|  Specifies an interface to use for the power meter / sensor during a source
power calibration.  
---|---  
  
#### VB Syntax

|  pwrMtrInterface.Path = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pwrMtrInterface |  (object) - A [PowerMeterInterface](../Objects/PowerMeterInterface_Object.md) (object)  
value |  (enum as NACommunicationPath) Choose from: 0 - naGPIB \- GPIB interface 1 - naUSB \- USB interface 2 - naLAN \- LAN interface 3 - naAny \- Any VISA resource string or a visa alias  
  
#### Return Type

|  Enum  
  
#### Default

|  naGPIB  
  
#### Examples

|  [See example](../Objects/PowerMeterInterface_Object.md#Accessing)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_Path(tagNACommunicationPath pNewVal); HRESULT
get_Path(tagNACommunicationPath *pVal);  
  
#### Interface

|  IPowerMeterInterface  
  
* * *

