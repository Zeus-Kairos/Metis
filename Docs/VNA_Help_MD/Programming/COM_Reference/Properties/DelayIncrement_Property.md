##### Write/Read

|

##### [About PNA-X Pulsed
Capabilities](../../../Applications/Narrowband_Pulsed_Application.htm)  
  
---|---  
  
## DelayIncrement Property

* * *

#### Description

|  Sets the pulse delay increment. The delay increments with each pulse by the
<value> amount. For example, in this diagram the delay starts as 1. On the
second pulse, delay=2. On the third pulse, delay=3. Important: If D + W is
greater than P, then undefined VNA behavior results. There is NO error message
or warning. Delay includes the incremented value. This is useful for pulse
profiling. ![](../../../assets/images/Programming/PulseDinc.gif)  
---|---  
  
####  VB Syntax

|  pulse.DelayIncrement(n) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pulse |  A [PulseGenerator](../Objects/PulseGenerator_Object.md) (object)  
n |  (Integer) Pulse generator number. Choose from 0 to 4. Or use [PulseGeneratorID](PulseGeneratorID_Property.md) to refer to an external pulse generator. 0 is the generator that pulses the ADC.  
value |  (Double) Delay increment value in seconds.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  pulse.DelayIncrement(1) = 1ms 'Write  
value = pulse.DelayIncrement(4) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_DelayIncrement(integer pulse, double* dIncre); HRESULT
put_DelayIncrement(integer pulse, double dIncre);  
  
#### Interface

|  IPulseGenerator  
  
* * *

  

