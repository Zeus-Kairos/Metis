##### Write/Read

|

##### About VNA-Pulse Generators  
  
---|---  
  
# ModulatorDelay Property

* * *

#### Description

| Sets the time lag between the pulse drive signal and the actual RF output.  
---|---  
  
####  VB Syntax

| pulse.ModulatorDelay = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pulse | A [PulseGenerator](../Objects/PulseGenerator_Object.md) (object)  
value | (Double) \- Modulator delay value.  
  
#### Return Type

| Double  
  
#### Default

| 40 ns  
  
#### Examples

| pulse.ModulatorDelay = 40ns 'Write  
value = pulse.ModulatorDelay 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_ModulatorDelay(double* val); HRESULT put_ModulatorDelay(double
val);  
  
#### Interface

| IPulseGenerator5  
  
* * *

