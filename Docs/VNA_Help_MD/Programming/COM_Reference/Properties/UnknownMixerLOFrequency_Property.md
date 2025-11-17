##### Write/Read

|

##### [About Phase Reference
Cals](../../../FreqOffset/Phase_Reference_Calibration.htm)  
  
---|---  
  
## UnknownMixerLOFrequency Property

* * *

#### Description

|  Sets and returns the LO Frequency to the unknown mixer.  
---|---  
  
####  VB Syntax

|  phaseRef.UnknownMixerLOFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  [PhaseReferenceCalibration](../Objects/PhaseReferenceCalibration_Object.md) (object)  
value |  (Double) LO frequency in Hz. Choose a value between 3 GHz and (Max Frequency minus 1GHz). For a 26.5 GHz VNA, the range is 3 GHz to 25.5 GHz. For best results, use the default LO frequency. 3.351Ghz. This frequency produces no spurs from the input/LO frequency. And also the Input frequency will have no band breaks.  
  
#### Return Type

|  Double  
  
#### Default

|  3.351 GHz  
  
#### Examples

|  phaseRef.UnknownMixerLOFrequency = 3.351e9  
value = phaseRef.UnknownMixerLOFrequency 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_UnknownMixerLOFrequency(double *value) HRESULT
put_UnknownMixerLOFrequency(double value)  
  
#### Interface

|  IPhaseReference2  
  
* * *

