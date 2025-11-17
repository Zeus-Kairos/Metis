##### Write/Read

|

##### [About Noise CAL](../../../Applications/Noise_Cal.md)  
  
---|---  
  
## AutoOrientTunerTuner Property

* * *

#### Description

|  Sets the state of auto orientation for a noise tuner during Noise Figure
for NFX.  
---|---  
  
####  VB Syntax

|  nfCal.AutoOrientTuner = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
nfCal |  A [NoiseCal](../Objects/NoiseCal_Object.md) (object)  
  
#### bool

|  (Boolean) True \- Set AutoOrientTuneration ON False \- Set
AutoOrientTuneration OFF  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  nfCal.AutoOrientTuner = True  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_AutoOrientTuner(VARIANT_BOOL bEnable); HRESULT
get_AutoOrientTuner(VARIANT_BOOL *bEnable);  
  
#### Interface

|  INoiseCal2  
  
* * *

