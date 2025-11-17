##### Write-only

|

##### [About Calibration](../../../S3_Cals/Select_Cal.md)  
  
---|---  
  
## DoECAL2PortEx Method

* * *

#### Description

|  This method replaces [DoECAL2Port Method](DoECAL2Port_Method.md). Does a
2-port calibration using an ECal module. 2-port refers to the number of ports
to calibrate; NOT to the number of ECal module ports. You must first have a
measurement active to perform the calibration. The characterization within the
ECal module that will be used for the calibration is specified by
[ECalCharacterizationEx](../Properties/ECALCharacterizationEx_Property.md).
The default value is 0.  
---|---  
  
#### VB Syntax

|  cal.DoECAL2PortEx [portA][,portB][,module]  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal |  A Calibrator (object)  
portA |  (long integer) Optional argument - Number of the receive port to calibrate. Choose from:  
1 - Calibrate port 1 (default, if unspecified)  
2 - Calibrate port 2  
3 - Calibrate port 3 And so forth for all available VNA / test set ports.  
portB |  (long integer) Optional argument - Number of the source port to calibrate. Choose from:  
1 - Calibrate port 1  
2 - Calibrate port 2 (default, if unspecified)  
3 - Calibrate port 3 And so forth for all available VNA / test set ports.  
module |  (long integer) Optional argument. ECal module. Choose from modules 1 through 8 Use [IsECALModuleFoundEx](../Properties/IsECALModuleFoundEx_Property.md) to determine the number of modules connected to the VNA Use [GetECALModuleInfoEx](Get_ECALModuleInfoEx_Method.md) to returns the model and serial number of each module.  
  
#### Return Type

|  None  
  
#### Default

|  Not Applicable  
  
#### Examples

|  cal.DoECAL2PortEx,1,2,3  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT DoECAL2PortEx( long portA = 1, long portB =2, long moduleNumber =
1);  
  
#### Interface

|  ICalibrator4  
  
* * *

