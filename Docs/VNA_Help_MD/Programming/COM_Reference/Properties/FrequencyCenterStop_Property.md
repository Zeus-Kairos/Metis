##### Write/Read

|

##### [About Swept IMD](../../../Applications/Swept_IMD.md)  
  
---|---  
  
## FrequencyCenterStop Property

* * *

#### Description

|  Sets and returns the stop frequency when sweeping the main tones. Use with
sweep type = naIMDToneCenterFreqSweep.  
---|---  
  
####  VB Syntax

|  imd.FrequencyCenterStop = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
imd |  A [SweptIMD](../Objects/SweptIMD_Object.md) Object  
value |  (Double) Stop frequency in Hz. The F1 and F2 tones MUST be within the frequency range of the VNA.  
  
#### Return Type

|  Double  
  
#### Default

|  26.4995 MHz  
  
#### Examples

|  imd.FrequencyCenterStop = 20e9 'Write  
value = imd.FrequencyCenterStop 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_FrequencyCenterStop(double *pVal)  
HRESULT put_FrequencyCenterStop(double newVal)  
  
#### Interface

|  ISweptIMD  
  
* * *

