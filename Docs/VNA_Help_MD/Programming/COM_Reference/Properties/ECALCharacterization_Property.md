##### Write/Read

## ECALCharacterization Property - Superseded

* * *

#### Description

|  Note: This property is replaced by [ECALCharacterizationEx
Property](ECALCharacterizationEx_Property.htm). Specifies the characterization
data within an ECal module to be used for the calibration. Learn more about
[ECal User Characterization](../../../S3_Cals/ECal_User_Characterization.md).  
---|---  
  
####  VB Syntax

|  cal.ECALCharacterization(mod) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal |  [Calibrator](../Objects/Calibrator_Object.md) (object)  
module |  1- ECal module  
value |  (Long)  Characterization data within the ECal module to be used for ECal operations. Choose from: 0  Factory Characterization 1  UserCharacterization1 2  UserCharacterization2 3  UserCharacterization3 4  UserCharacterization4 5  UserCharacterization5  
  
#### Return Type

|  Long  
  
#### Default

|  0 \- Factory Characterization  
  
#### Interface

|  ICalibrator2

