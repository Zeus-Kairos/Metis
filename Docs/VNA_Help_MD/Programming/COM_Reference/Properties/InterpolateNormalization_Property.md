##### Write/Read

|

##### [About Receiver
Cal](../../../S0_Start/Traces_Channels_and_Windows.htm#trace)  
  
---|---  
  
## InterpolateNormalization Property Superseded

* * *

#### Description

|  Note: This property is replaced by [DoReceiverPowerCal
Method](../Methods/DoReceiverPowerCal_Method.htm). Turns ON and OFF
normalization interpolation which calculates new divisor data when stimulus
values change after normalization. When this property is ON and normalization
is being applied, the Normalization algorithm attempts to interpolate the
divisor data whenever the stimulus parameters are changed. When this property
is OFF under the same circumstances, normalization is turned OFF.
Normalization is currently supported only on measurements of unratioed power
for the purpose of performing a receiver power calibration.  
---|---  
  
####  VB Syntax

|  meas.InterpolateNormalization = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  (object) - A Measurement object  
value |  (boolean) False  Turns normalization interpolation OFF True  Turns normalization interpolation ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  False -OFF  
  
#### Examples

|  meas.InterpolateNormalization = False 'Write  
normalized = meas.InterpolateNormalization 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_InterpolateNormalization(VARIANT_BOOL bState); HRESULT
get_InterpolateNormalization(VARIANT_BOOL *bState);  
  
#### Interface

|  IMeasurement

