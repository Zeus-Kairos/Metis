##### Write / Read

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## Locator Property

* * *

#### Description

|  Specifies the location, address, or ID string of the power meter / sensor
that is used during a source power calibration. Use [Path
Property](Path_Property.htm) to specify the type of interface.  
---|---  
  
#### VB Syntax

|  pwrMtrInterface.Locator = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pwrMtrInterface |  (object) - A [PowerMeterInterface](../Objects/PowerMeterInterface_Object.md) (object)  
value |  (string) Location of the power meter / sensor, depending on the type of interface ([Path Property](Path_Property.md))

  * For naGPIB, address of the power meter. Choose any integer between 0 and 30.
  * For naUSB, the ID string of the power sensor. Use [USBPowerMeterCatalog Property](USBPowerMeterCatalog_Property.md) to see a list of ID strings of connected power sensors.
  * For naLAN, the hostname or IP address of the power meter.
  * For naANY, any VISA resource string or a VISA alias.

  
  
#### Return Type

|  String  
  
#### Default

|  Not applicable  
  
#### Examples

|  pwrMeterInterface.Locator = "13" 'GPIB address pwrMeterInterface.Locator =
"Keysight Technologies,U2000A,MY12345678 'USB ID string
pwrMeterInterface.Locator = "mymeter.Keysight.com" 'LAN
pwrMeterInterface.Locator = "TCPIP0::mymeter.Keysight.com::5025::SOCKET" ' Any  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_Locator( BSTR pValue ); HRESULT get_Locator(BSTR* pValue );  
  
#### Locator

|  IPowerMeterInterface  
  
* * *

