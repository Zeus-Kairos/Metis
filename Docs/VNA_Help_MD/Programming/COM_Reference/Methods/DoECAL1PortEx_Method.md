##### Write-only

|

##### [About Calibration](../../../S3_Cals/Select_Cal.md)  
  
---|---  
  
## DoECAL1PortEx Method

* * *

#### Description

|  This method replaces [DoECAL1Port Method](DoECAL1Port_Method.md). Does a
1-Port calibration using an ECAL module. You must first have a 1-port
measurement active to perform the calibration. The characterization within the
ECal module that will be used for the calibration is specified by
[ECALCharacterizationEx](../Properties/ECALCharacterizationEx_Property.md).
The default value is 0.  
---|---  
  
####  VB Syntax

|  cal.DoECAL1PortEx [port][,module]  
  
* * *  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal |  A Calibrator (object)  
port |  (long integer) Optional argument - Port number to calibrate. Choose from:  
1 - Calibrate port 1 (default if unspecified)  
2 - Calibrate port 2  
module |  (long integer)  Optional argument. ECal module. Choose from modules 1 through 8 Use [IsECALModuleFoundEx](../Properties/IsECALModuleFoundEx_Property.md) to determine the number of modules connected to the VNA Use [GetECALModuleInfoEx](Get_ECALModuleInfoEx_Method.md) to returns the model and serial number of each module.  
  
#### Return Type

|  None  
  
#### Default

|  Not Applicable  
  
* * *  
  
#### Examples

|  cal.DoECAL1PortEx,2,2  
  
* * *  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT DoECAL1PortEx(long port, long moduleNumber = 1);  
  
#### Interface

|  ICalibrator4

