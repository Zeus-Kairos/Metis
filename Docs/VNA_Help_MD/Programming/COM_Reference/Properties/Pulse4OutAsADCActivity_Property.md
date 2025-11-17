##### Write/Read

|

##### [About VNA-Pulse
Generators](../../../IFAccess/IF_Path_Configuration.htm#PulseGens)  
  
---|---  
  
# Pulse4OutAsADCActivity Property

* * *

#### Description

| Turns pulse4 output ON and OFF. Enable pulse4 to use an oscilloscope
connected to pin 13 of the [PULSE I/O
connector](../../../Rear_Panel/XPulseIO.htm) on the rear panel of the VNA to
display when the ADC is making measurements.  
---|---  
  
####  VB Syntax

| pulse.Pulse4OutAsADCActivity = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pulse | A [PulseGenerator](../Objects/PulseGenerator_Object.md) (object)  
value | (Boolean)  Choose from: ON (or 1) - Pulse 4 output pin indicates ADC activity. OFF (or 0) - Pulse 4 output pin indicates legacy behavior (pulse generator number 4 output).  
  
#### Return Type

| Boolean  
  
#### Default

| False  
  
#### Examples

| pulse.Pulse4OutAsADCActivity = True 'Write  
bool = pulse.Pulse4OutAsADCActivity 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_Pulse4OutAsADCActivity(VARIANT_BOOL* ADCActivity);. HRESULT
put_Pulse4OutAsADCActivit (VARIANT_BOOL ADCActivity);  
  
#### Interface

| IPulseGenerator5  
  
* * *

