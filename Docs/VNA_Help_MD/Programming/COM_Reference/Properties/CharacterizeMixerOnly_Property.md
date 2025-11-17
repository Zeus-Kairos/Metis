##### Read/Write

|

##### [About
CharacterizeMixer](../../../FreqOffset/VMC_Measurements.htm#calibrationMixer)  
  
---|---  
  
## CharacterizeMixerOnly Property

* * *

#### Description

|  Sets and returns whether to perform ONLY a mixer characterization.  
---|---  
  
#### VB Syntax

|  VMC.CharacterizeMixerOnly = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) - Description  
  
VMC |  [VMCType](../Objects/VMC_Type_Object.md) (object)  
bool |  (Boolean) True \- Perform ONLY mixer characterization. False \- Perform both mixer characterization and calibration.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  value = VMC.CharacterizeMixerOnly  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_CharacterizeMixerOnly(VARIANT_BOOL bCharMixerOnly); HRESULT
get_CharacterizeMixerOnly(VARIANT_BOOL *bCharMixerOnly);  
  
#### Interface

|  VMCType

