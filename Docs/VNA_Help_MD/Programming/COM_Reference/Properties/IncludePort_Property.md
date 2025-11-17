##### Write/Read

|

##### [About Phase Reference
Cals](../../../FreqOffset/Phase_Reference_Calibration.htm)  
  
---|---  
  
## IncludePort Property

* * *

#### Description

|  Sets and returns the enable state for the specified port.  
---|---  
  
####  VB Syntax

|  phaseRef.IncludePort (n)= value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  [PhaseReferenceCalibration](../Objects/PhaseReferenceCalibration_Object.md) (object)  
n |  (Long) Port number to enable or disable.  
value |  (Boolean) Port enable state. Choose from: True \- Enable port <n> False \- Disable port <n>  
  
#### Return Type

|  Boolean  
  
#### Default

|  Ports 1 and 2 are enabled. Ports 3 and 4 (if present) are disabled  
  
#### Examples

|  phaseRef.IncludePort(3) = True  
value = phaseRef.IncludePort(3) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_IncludePort(Long port, VARIANT_BOOL *value) HRESULT
put_IncludePort(Long port, VARIANT_BOOL value)  
  
#### Interface

|  IPhaseReference2  
  
* * *

