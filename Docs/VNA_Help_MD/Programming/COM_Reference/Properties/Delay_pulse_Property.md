##### Write/Read

|

##### [About PNA-X Pulsed
Capabilities](../../../Applications/Narrowband_Pulsed_Application.htm)  
  
---|---  
  
## Delay (pulse) Property

* * *

#### Description

|  Sets the pulse delay - the amount of time before a new pulse begins.  
---|---  
  
####  VB Syntax

|  pulse.Delay(n) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pulse |  A [PulseGenerator](../Objects/PulseGenerator_Object.md) (object)  
n |  (Integer) Pulse generator number. Choose from 0 to 4. Or use [PulseGeneratorID](PulseGeneratorID_Property.md) to refer to an external pulse generator. 0 is the generator that pulses the ADC.  
value |  (Double) Delay value in seconds. Choose a value from about 33ns to about 70 seconds.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  pulse.Delay(1) = 1ms 'Write  
value = pulse.Delay(4) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Delay(integer pulse, double* delay); HRESULT put_Delay(integer
pulse, double delay);  
  
#### Interface

|  IPulseGenerator  
  
* * *

  

