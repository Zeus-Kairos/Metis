##### Read-only

## GetECALModuleInfo Method - Superseded

* * *

#### Description

|  Note: This property is replaced by [GetECALModuleInfoEx
Method](Get_ECALModuleInfoEx_Method.htm) Returns the following information
about the connected ECAL module: model number, serial number, connector type,
calibration date, min and max frequency. The characterization within the ECal
module that this information will be read from is specified by the
[ECALCharacterization
property](../Properties/ECALCharacterization_vmc_Property.htm) on the
ICalibrator2 interface. The default value of the ECALCharacterization property
is naECALFactoryCharacterization.  
---|---  
  
####  VB Syntax

|  moduleInfo = cal.GetECALModuleInfo (module)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
moduleInfo |  (string) \- variable to store the module information  
cal |  A Calibrator (object)  
module |  (enum NAECALModule)  ECAL module. Choose from: 0 - naECALModule_A 1 - naECALModule_B  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  info = cal.GetECALModuleInfo(naECALModule_A) Example return string:
ModelNumber: 85092-60007, SerialNumber: 01386, ConnectorType: N5FN5F,
PortAConnector: Type N (50) female, PortBConnector: Type N (50) female,
MinFreq: 30000, MaxFreq: 9100000000, NumberOfPoints: 250, Calibrated: July 4
2002  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetECALModuleInfo(tagNAECALModule ecalModule, BSTR* info);  
  
#### Interface

|  ICalibrator

