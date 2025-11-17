##### Write/Read

|

##### [About Phase Reference
Cals](../../../FreqOffset/Phase_Reference_Calibration.htm)  
  
---|---  
  
## CalKitType Property

* * *

#### Description

|  Sets and returns the Cal Kit to be used during the S-parameter portion of a
Phase Reference calibration.  
---|---  
  
####  VB Syntax

|  phaseRef.CalKitType = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  Any of the following: [PhaseReferenceCalibration](../Objects/PhaseReferenceCalibration_Object.md) (object)  
value |  (string) \- Calibration Kit type. Case-sensitive. Use [GetCompatibleCalKits](../Methods/GetCompatibleCalKits_Method.md) to return a list of valid Cal Kits.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  phaseRef.CalKitType = "85052C"  
value = phaseRef.CalKitType 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CalKitType(BSTR *calkit) HRESULT put_CalKitType(BSTR calkit)  
  
#### Interface

|  IPhaseReference2  
  
* * *

