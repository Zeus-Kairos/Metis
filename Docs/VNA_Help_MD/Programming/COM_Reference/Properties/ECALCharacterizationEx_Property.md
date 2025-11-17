##### Write/Read

## ECALCharacterizationEx Property

* * *

#### Description

|  This property replaces [ECALCharacterization
Property](ECALCharacterization_Property.htm). Specifies the characterization
data within an ECal module to be used for the calibration. Learn more about
[ECal User Characterization](../../../S3_Cals/ECal_User_Characterization.md).  
---|---  
  
####  VB Syntax

|  cal.ECALCharacterizationEx (module) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal |  [Calibrator](../Objects/Calibrator_Object.md) (object)  
module |  (long integer)  Optional argument. ECal module. Choose from modules 1 through 8 Use [IsECALModuleFoundEx](IsECALModuleFoundEx_Property.md) to determine the number of modules connected to the VNA Use [GetECALModuleInfoEx](../Methods/Get_ECALModuleInfoEx_Method.md) to returns the model and serial number of each module.  
value |  (Long)  Characterization data within the ECal module to be used for ECal operations. Choose from: 0  Factory Characterization 1  UserCharacterization1 2  UserCharacterization2 ..and so forth up to... 12  UserCharacterization12  
  
#### Return Type

|  Long  
  
#### Default

|  0 \- Factory Characterization  
  
#### Examples

|  cal.ECALCharacterizationEx (4) = 2  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_ECALCharacterizationEx( long moduleNumber, long
characterization); HRESULT get_ECALCharacterizationEx( long moduleNumber,
long* characterization);  
  
#### Interface

|  ICalibrator4  
  
* * *

  

