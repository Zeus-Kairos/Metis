##### Write/Read

|

##### [About Phase Reference
Cals](../../../FreqOffset/Phase_Reference_Calibration.htm)  
  
---|---  
  
## DeembedCoupler Property

* * *

#### Description

|  Sets and returns the state of de-embedding (reversing) the port 2 coupler.  
---|---  
  
####  VB Syntax

|  phaseRef.DeembedCoupler = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  [PhaseReferenceCalibration](../Objects/PhaseReferenceCalibration_Object.md) (object)  
value |  (Boolean) Port 2 couple de-embed state. Choose from: True \- Configures the calibration to include additional measurements to de-embed the effects of reversing the coupler. (This is the same as clearing the Omit Coupler checkbox.) False \- Exclude additional measurements for de-embedding the effects of reversing the coupler.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  phaseRef.DeembedCoupler = True  
value = phaseRef.DeembedCoupler 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_DeembedCoupler(VARIANT_BOOL *value) HRESULT
put_DeembedCoupler(VARIANT_BOOL value)  
  
#### Interface

|  IPhaseReference2  
  
* * *

