##### Write-only

|

##### [About Calibration](../../../S3_Cals/Select_Cal.md)  
  
---|---  
  
## DoECAL2Port Method - Superseded

* * *

#### Description

|  Note: This property is replaced by [DoECAL2PortEx
Method](DoECAL2PortEx_Method.htm). Does a 2-Port calibration using an ECAL
module. You must first have a 2-port measurement active to perform the
calibration. The characterization within the ECal module that will be used for
the calibration is specified by the [ECALCharacterization
property](../Properties/ECALCharacterization_vmc_Property.htm) on the
ICalibrator2 interface. The default value of the ECALCharacterization property
is naECALFactoryCharacterization.  
---|---  
  
####  VB Syntax

|  cal.DoECAL2Port[portA][,portB][,module]  
  
* * *  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal |  A Calibrator (object)  
portA |  (long integer) Optional argument - Number of the receive port to calibrate.  
Choose from:  
1 - Calibrate port 1 (default, if unspecified)  
2 - Calibrate port 2  
3 - Calibrate port 3 (if the VNA has 3 ports)  
portB |  (long integer) Optional argument - Number of the source port to calibrate. Choose from:  
1 - Calibrate port 1 (default, if unspecified)  
2 - Calibrate port 2  
3 - Calibrate port 3 (if the VNA has 3 ports)  
module |  (enum NAECALModule)  Optional argument. ECal module. Choose from:  
0 - naECALModule_A (default, if unspecified)  
1 - naECALModule_B  
  
#### Return Type

|  None  
  
#### Default

|  Not Applicable  
  
* * *  
  
#### Examples

|  cal.DoECAL2Port,1,2,naECALModule_B  
  
* * *  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT DoECAL2Port(long rcvport, long srcPort, tagNAECALModule
ecalModule);  
  
#### Interface

|  ICalibrator

