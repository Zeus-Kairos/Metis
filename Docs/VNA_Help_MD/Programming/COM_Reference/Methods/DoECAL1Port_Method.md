##### Write-only

|

##### [About Calibration](../../../S3_Cals/Select_Cal.md)  
  
---|---  
  
## DoECAL1Port Method - Superseded

* * *

#### Description

|  Note: This property is replaced by [DoECAL1PortEx
Method](DoECAL1PortEx_Method.htm). Does a 1-Port calibration using an ECAL
module. You must first have a 1-port measurement active to perform the
calibration. The characterization within the ECal module that will be used for
the calibration is specified by the [ECALCharacterization
property](../Properties/ECALCharacterization_vmc_Property.htm) on the
ICalibrator2 interface. The default value of the ECALCharacterization property
is naECALFactoryCharacterization.  
---|---  
  
####  VB Syntax

|  cal.DoECAL1Port [port][,module]  
  
* * *  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal |  A Calibrator (object)  
port |  (long integer) Optional argument - Port number to calibrate. Choose from:  
1 - Calibrate port 1 (default if unspecified)  
2 - Calibrate port 2  
module |  (enum NAEcalModule) Optional argument - ECAL module. Choose from:  
  
0 - naECALModule_A - (default if unspecified)  
1 - naECALModule_B  
  
#### Return Type

|  None  
  
#### Default

|  Not Applicable  
  
* * *  
  
#### Examples

|  cal.DoECAL1Port,2,naECALModule_B  
  
* * *  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT DoECAL1Port(long port, tagNAECALModule ecalModule);  
  
#### Interface

|  ICalibrator

