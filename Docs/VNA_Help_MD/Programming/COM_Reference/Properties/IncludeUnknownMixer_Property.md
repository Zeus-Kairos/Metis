##### Write/Read

|

##### [About Phase Reference
Cals](../../../FreqOffset/Phase_Reference_Calibration.htm)  
  
---|---  
  
## IncludeUnknownMixer Property

* * *

#### Description

|  Sets and returns the state of Unknown Mixer calibration.  
---|---  
  
####  VB Syntax

|  phaseRef.IncludeUnknownMixer = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  [PhaseReferenceCalibration](../Objects/PhaseReferenceCalibration_Object.md) (object)  
value |  (Boolean) Unknown Mixer cal state. Choose from: True \- Enable Unknown Mixer cal. The start frequency becomes 10 MHz and can NOT be changed. False \- Disable Unknown Mixer cal.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  phaseRef.IncludeUnknownMixer = True  
value = phaseRef.IncludeUnknownMixer 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_IncludeUnknownMixer(VARIANT_BOOL *value) HRESULT
put_IncludeUnknownMixer(VARIANT_BOOL value)  
  
#### Interface

|  IPhaseReference2  
  
* * *

