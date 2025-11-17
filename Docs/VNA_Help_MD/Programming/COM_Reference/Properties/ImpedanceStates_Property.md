##### Write/Read

|

##### [About Noise Figure](../../../Applications/Noise_Figure.md)  
  
---|---  
  
## ImpedanceStates Property

* * *

#### Description

|  Sets the number of impedance states to use during calibrated measurements.  
---|---  
  
####  VB Syntax

|  noise.ImpedanceStates = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
noise |  A [NoiseFigure](../Objects/NoiseFigure_Object.md) (object)  
value |  (double) - Impedance states. Choose between 4 and the maximum number allowed by the noise tuner device. If the specified number exceeds the capability of the device, the measurement will use the maximum number of states the device allows.  
  
#### Return Type

|  Double  
  
#### Default

|  4  
  
#### Examples

|  noise.ImpedanceStates = 10 'Write  
AvgNoise = noise.ImpedanceStates 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ImpedanceStates(double* pVal) HRESULT
put_ImpedanceStates(double newVal)  
  
#### Interface

|  INoiseFigure  
  
* * *

