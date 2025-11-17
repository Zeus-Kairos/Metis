##### Write-only

|

##### [About ECAL Confidence Check](../../../S3_Cals/Quest_Cal.md#AboutECal)  
  
---|---  
  
## AcquireCalConfidenceCheckECAL Method - Superseded

* * *

#### Description

|  Note: This property is replaced by [AcquireCalConfidenceCheckECALex
Method](AcquireCalConfidenceCheckECALex_Method.htm) Transfers confidence data
from the specified ECal module into the measurement's memory trace. The data
is transferred to the specified S-parameter on the same channel as this
Calibrator object. The characterization within the ECal module that the
confidence data will be read from is specified by the [ECALCharacterization
property](../Properties/ECALCharacterization_vmc_Property.htm) on the
ICalibrator2 interface. The default value of the ECALCharacterization property
is naECALFactoryCharacterization.  
---|---  
  
####  VB Syntax

|  cal.AcquireCalConfidenceCheckECAL Sparam[,ecalModule]  
  
* * *  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal |  A Calibrator (object)  
Sparam |  (String) S-parameter to transfer confidence data to. This parameter must be present on the same channel as the calibrator object.  
ecalModule |  (enum NAECALModule)  Optional argument. ECal module. Choose from: 0 - naECALModule_A (default, if unspecified) 1 - naECALModule_B  
  
#### Return Type

|  None  
  
#### Default

|  Not applicable  
  
* * *  
  
#### Examples

|  Cal.AcquireCalConfidenceCheckECAL "S11", naECALModule_A  
  
* * *  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT AcquireCalConfidenceCheckECAL( _bstr_t strParameter, enum
NAECALModule ecalModule );  
  
#### Interface

|  ICalibrator

