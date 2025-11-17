##### Read-only

## GetECALModuleInfoEx Method

* * *

#### Description

|  This property replaces [Get ECALModuleInfo
Method](Get_ECAL_Module_Info_Method.htm). Returns the following information
about the connected ECAL module: model number, serial number, connector type,
calibration date, min and max frequency. The characterization within the ECal
module that this information will be read from is specified by
[ECALCharacterizationEx](../Properties/ECALCharacterizationEx_Property.md).
The default value is 0.  
---|---  
  
####  VB Syntax

|  moduleInfo = cal.GetECALModuleInfoEx (module)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
moduleInfo |  (string) \- variable to store the module information  
cal |  A Calibrator (object)  
module |  (long integer)  ECal module. Choose from modules 1 through 8 Use [IsECALModuleFoundEx](../Properties/IsECALModuleFoundEx_Property.md) to determine the number of modules connected to the VNA  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  info = cal.GetECALModuleInfoEx(2) Example return string: ModelNumber:
85092-60007, SerialNumber: 01386, ConnectorType: N5FN5F, PortAConnector: Type
N (50) female, PortBConnector: Type N (50) female, MinFreq: 30000, MaxFreq:
9100000000, NumberOfPoints: 250, Calibrated: July 4 2002  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetECALModuleInfoEx(long moduleNumber, BSTR* info);  
  
#### Interface

|  ICalibrator4

