##### Write/Read

|

##### [About Swept IMD](../../../Applications/Swept_IMD.md)  
  
---|---  
  
## FrequencyCenterSpan Property

* * *

#### Description

|  Sets and returns the frequency span when sweeping the main tones. Use with
sweep type = naIMDToneCenterFreqSweep.  
---|---  
  
####  VB Syntax

|  imd.FrequencyCenterSpan = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
imd |  A [SweptIMD](../Objects/SweptIMD_Object.md) Object  
value |  (Double) Frequency span in Hz. The F1 and F2 tones MUST be within the frequency range of the VNA.  
  
#### Return Type

|  Double  
  
#### Default

|  26.489 GHz  
  
#### Examples

|  imd.FrequencyCenterSpan = 10e9 'Write  
value = imd.FrequencyCenterSpan 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_FrequencyCenterSpan(double *pVal)  
HRESULT put_FrequencyCenterSpan(double newVal)  
  
#### Interface

|  ISweptIMD  
  
* * *

