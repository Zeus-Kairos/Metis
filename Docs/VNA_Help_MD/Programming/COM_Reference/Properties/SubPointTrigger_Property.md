##### Write/Read

|

##### [About VNA-Pulse
Generators](../../../IFAccess/IF_Path_Configuration.htm#PulseGens)  
  
---|---  
  
## SubPointTrigger Property

* * *

#### Description

|  Enables / Disables subpoint triggering. When enabled and performing [Point
Averaging](../../../S2_Opt/Trce_Noise.htm#averaging), Each rising edge of P0
triggers a subpoint (one of N acquisitions in an N point average). Must also
enable the P0 generator using [pulse.State(n)](State_pulse_Property.md).  
---|---  
  
####  VB Syntax

|  pulse.SubPointTrigger(n) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pulse |  A [PulseGenerator](../Objects/PulseGenerator_Object.md) (object)  
n |  (Integer) Pulse generator number. Must be 0 as this is the generator that triggers the ADC.  
value |  (Boolean) Enable or disable SubPointTrigger

  * True \- turns subpoint triggering ON.
  * False \- turns subpoint triggering OFF.

  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  pulse.SubPointTrigger(0) = True 'Write  
bool = pulse.SubPointTrigger(0) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_SubPointTrigger (integer pulse, VARIANT_BOOL* on_off);. HRESULT
put_SubPointTrigger (integer pulse, VARIANT_BOOL on_off);  
  
#### Interface

|  IPulseGenerator2  
  
* * *

