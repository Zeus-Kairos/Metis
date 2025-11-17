##### Write/Read

|

##### [About PNA-X Pulsed
Capabilities](../../../Applications/Narrowband_Pulsed_Application.htm)  
  
---|---  
  
## Width Property

* * *

#### Description

|  Sets the pulse width - the amount of time that the pulse is ON.  
---|---  
  
####  VB Syntax

|  pulse.Width (n) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pulse |  A [PulseGenerator](../Objects/PulseGenerator_Object.md) (object)  
n |  (Integer) Pulse generator number. Choose from 0 to 4. 0 is the generator that pulses the ADC.  
value |  (Double) Pulse width in seconds. Choose a value from about 33ns to about 70 seconds.  
  
#### Return Type

|  Double  
  
#### Default

|  1e-4 sec  
  
#### Examples

|  pulse.Width = 1ms 'Write  
value = pulse.Width 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Width (integer pulse, double* width); HRESULT put_Width
(integer pulse, double width);  
  
#### Interface

|  IPulseGenerator  
  
* * *

  

