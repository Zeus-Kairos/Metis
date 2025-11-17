##### Read only

|

#####  
  
---|---  
  
## ValidConnectorTypes Property

* * *

#### Description

|  Returns a list of all connector types for which there are calibration kits. Looks for connector types in mechanical cal kits, within VNA disk memory, and within the attached ECal Module memory. Here are the more common connector types: |  W-band waveguide V-band waveguide U-band waveguide R-band waveguide Q-band waveguide K-band waveguide P-band waveguide X-band waveguide 7-16 female 7-16 male |  Type B Type A (50) female Type A (50) male Type F (75) female Type F (75) male Type N (75) female Type N (75) male Type N (50) female Type N (50) male |  1.00 mm female 1.00 mm male 1.85 mm male 1.85 mm female 2.92 mm female 2.92 mm male APC 2.4 female APC 2.4 male APC 3.5 female APC 3.5 male APC 7  
---|---|---  
  
#### VB Syntax

|  value = obj.ValidConnectorTypes  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Variant) List of connector types  
obj |  Any of the following: [ECalUserCharacterizer](../Objects/ECalUserCharacterizer_Object.md) (object) [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object) [SMCType](../Objects/SMC_Type_Object.md) (object) [VMCType](../Objects/VMC_Type_Object.md) (object)  
  
#### Return Type

|  Variant  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = SMC.ValidConnectorTypes  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_ValidConnectorTypes(VARIANT* connectorTypes);  
  
#### Interface

|  IGuidedCalibration SMCType VMCType  
  
* * *

