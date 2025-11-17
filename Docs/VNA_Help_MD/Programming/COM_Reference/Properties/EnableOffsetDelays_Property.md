##### Write/Read

|

##### About VNA-Pulse Generators  
  
---|---  
  
# EnableOffsetDelays Property

* * *

#### Description

| Enables/disables modulator and ADC delays for pulse measurements.  
---|---  
  
####  VB Syntax

| pulse.EnableOffsetDelays = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pulse | A [PulseGenerator](../Objects/PulseGenerator_Object.md) (object)  
value | (Boolean)  Choose from: ON (or 1) - Enable delays. OFF (or 0) - Disable delays.  
  
#### Return Type

| Boolean  
  
#### Default

| False  
  
#### Examples

| pulse.EnableOffsetDelays = True 'Write  
bool = pulse.EnableOffsetDelays 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_EnableOffsetDelays(VARIANT_BOOL* enable); HRESULT
put_EnableOffsetDelays(VARIANT_BOOL enable);  
  
#### Interface

| IPulseGenerator5  
  
* * *

