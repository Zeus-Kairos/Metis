##### Read-Write

## CharMixerReverse Property

* * *

#### Description

|  Specifies the direction in which to characterize the calibration mixer.
[Learn more about the calibration
mixer.](../../../FreqOffset/VMC_Measurements.htm#Measurement_direction)  
---|---  
  
#### VB Syntax

|  VMC.CharMixerReverse = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
VMC |  [VMCType](../Objects/VMC_Type_Object.md) (object)  
bool |  (Boolean) 0 \- Characterize the calibration mixer in the SAME direction as that specified in the mixer setup. 1 \- Characterize the calibration mixer in the REVERSE direction as that specified in the mixer setup.  
  
#### Return Type

|  Boolean  
  
#### Default

|  0  
  
#### Examples

|  VMC.CharMixerReverse = 0  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_CharMixerReverse(VARIANT_BOOL bcharReverse); HRESULT
get_CharMixerReverse(VARIANT_BOOL *bcharReverse);  
  
#### Interface

|  VMCType2

