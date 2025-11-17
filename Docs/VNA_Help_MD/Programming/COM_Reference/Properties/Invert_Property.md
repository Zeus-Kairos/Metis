##### Write/Read  
  
---  
  
## Invert Property

* * *

#### Description

|  Sets whether to invert the polarity of the pulse.  
---|---  
  
####  VB Syntax

|  pulse.Invert (n) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pulse |  A [PulseGenerator](../Objects/PulseGenerator_Object.md) (object)  
n |  (Integer) Pulse generator number. Choose from 0 to 4. Or use [PulseGeneratorID](PulseGeneratorID_Property.md) to refer to an external pulse generator. 0 is the generator that pulses the ADC.  
value |  True \- Invert the pulse generator polarity. This causes the pulse ON time to be active low and OFF be active high. False \- Do NOT Invert the pulse generator polarity.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  pulse.Invert(1) = True 'Write  
value = pulse.Invert(4) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Invert(integer pulse, VARIANT_BOOL *pVal); HRESULT
put_Invert(integer pulse, VARIANT_BOOL newVal);  
  
#### Interface

|  IPulseGenerator4  
  
* * *

  

