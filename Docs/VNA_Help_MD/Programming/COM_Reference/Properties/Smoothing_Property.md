##### Write/Read

|

##### [About Smoothing](../../../S2_Opt/Trce_Noise.md#Smoothing)  
  
---|---  
  
## Smoothing Property

* * *

#### Description

|  Turns ON and OFF data smoothing.  
---|---  
  
####  VB Syntax

|  meas.Smoothing = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A Measurement (object)  
state |  (boolean)  
True \- Turns smoothing ON False \- Turns smoothing OFF  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  meas.Smoothing = False 'Write  
smooth = meas.Smoothing 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Smoothing(VARIANT_BOOL *pVal)  
HRESULT put_Smoothing(VARIANT_BOOL newVal)  
  
#### Interface

|  IMeasurement

