##### Write/Read

|

##### [About SMC Phase](../../../FreqOffset/SMC_plus_Phase.md)  
  
---|---  
  
## EnablePhase Property

* * *

#### Description

|  Sets and returns the state of SMC Phase measurements. In the User
Interface, there are two "enable phase" checkboxes: in the [Phase Settings
dialog](../../../FreqOffset/SMC_plus_Phase.htm) and in the [Calibration
Wizard](../../../FreqOffset/SMC_Measurements.htm#CalWizard). Checking one
enables both. This single command also enables both.  
---|---  
  
####  VB Syntax

|  obj.EnablePhase = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Mixer Interface](../Objects/IMixer_Interface.md) pointer to the [Measurement](../Objects/Measurement_Object.md) (object) A [Converter](../Objects/Converter_Object.md) (Object)  
bool |  (Boolean) - True \- Include phase in SMC measurements False \- Do NOT include phase in SMC measurements  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  mixer.EnablePhase = True  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_EnablePhase(VARIANT_BOOL * val); HRESULT
put_EnablePhase(VARIANT_BOOL val);  
  
#### Interface

|  IMixer13  
  
* * *

