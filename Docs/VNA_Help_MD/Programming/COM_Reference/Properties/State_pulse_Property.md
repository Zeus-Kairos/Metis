##### Write/Read  
  
---  
  
## State Property

* * *

#### Description

|  Turns the specified pulse generator ON and OFF.  
---|---  
  
####  VB Syntax

|  pulse.State (n) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pulse |  A [PulseGenerator](../Objects/PulseGenerator_Object.md) (object)  
n |  (Integer) Pulse generator number. Choose from 0 to 4. Or use [PulseGeneratorID](PulseGeneratorID_Property.md) to refer to an external pulse generator. 0 is the generator that pulses the ADC.  
value |  True \- turns pulse output ON. False \- turns pulse output OFF.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  pulse.State(1) = True 'Write  
value = pulse.State(4) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_State(integer pulse, VARIANT_BOOL *pVal); HRESULT
put_State(integer pulse, VARIANT_BOOL newVal);  
  
#### Interface

|  IPulseGenerator  
  
* * *

