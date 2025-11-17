##### Write/Read

|

##### [About PNA-X Pulsed
Capabilities](../../../Applications/Narrowband_Pulsed_Application.htm)  
  
---|---  
  
## Period Property

* * *

#### Description

|  Sets the pulse-period (1/PRF) for ALL PNA-X internal pulse generators. The
resolution of the period is 16.667nS.  
---|---  
  
####  VB Syntax

|  pulse.Period = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pulse |  A [PulseGenerator](../Objects/PulseGenerator_Object.md) (object)  
value |  (Double) Pulse period in seconds. Choose a value from about 33ns to about 70 seconds.  
  
#### Return Type

|  Double  
  
#### Default

|  1e-3 sec  
  
#### Examples

|  pulse.Period = 1ms 'Write  
value = pulse.Period 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Period(double* period); HRESULT put_Period(double period);  
  
#### Interface

|  IPulseGenerator  
  
* * *

