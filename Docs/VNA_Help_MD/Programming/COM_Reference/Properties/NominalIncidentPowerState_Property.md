##### Write/Read

|

##### About [Mixer
Configuration](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
## NominalIncidentPowerState Property

* * *

#### Description

|  Toggles the Nominal Incident Power setting ON and OFF. This setting is ONLY
to be used with SMC measurements, not VMC. [Learn more about Nominal Incident
Power.](../../../FreqOffset/SMC_Measurements.htm#UseNominal)  
---|---  
  
####  VB Syntax

|  mixer.NominalIncidentPowerState = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mixer |  A Mixer  (object)  
bool |  (boolean) \- Nominal Incident Power State. Choose from: 1 -(True) Turn nominal incident power ON 0 -(False) Turn nominal incident power OFF  
  
#### Return Type

|  Boolean  
  
#### Default

|  0 -(False)  
  
#### Examples

|  mixer.NominalIncidentPowerState = True 'sets NominalIncidentPowerState to
ON  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_NominalIncidentPowerState(VARIANT_BOOL *pVal) HRESULT
put_NominalIncidentPowerState(VARIANT_BOOL val );  
  
#### Interface

|  IMixer4

