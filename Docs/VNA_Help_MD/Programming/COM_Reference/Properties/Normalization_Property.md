##### Write/Read

|

##### [About Receiver
Cal](../../../S0_Start/Traces_Channels_and_Windows.htm#trace)  
  
---|---  
  
## Normalization Property Superseded

* * *

#### Description

|  Note: This property is replaced by [DoReceiverPowerCal
Method](../Methods/DoReceiverPowerCal_Method.htm). Sets or returns
normalization ON or OFF for the measurement. Normalization is currently
supported only on measurements of unratioed power for the purpose of
performing a receiver power calibration. If this property is set to ON for a
ratioed measurement (such as S-parameter), it will return an error. This
property will also return an error when set to ON if the divisor buffer
doesnt yet exist.  
---|---  
  
####  VB Syntax

|  meas.Normalization = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  (object) - A Measurement object  
value |  (boolean) False  Turns normalization OFF True  Turns normalization ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  meas.Normalization = False 'Write  
normalized = meas.Normalization 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_Normalization(VARIANT_BOOL bState); HRESULT
get_Normalization(VARIANT_BOOL *bState);  
  
#### Interface

|  IMeasurement

