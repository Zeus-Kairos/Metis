##### Write/Read

|

##### [About Swept IMD](../../../Applications/Swept_IMD.md)  
  
---|---  
  
## FrequencyCenterStart Property

* * *

#### Description

|  Sets and returns the start frequency when sweeping the main tones. Use with
sweep type = naIMDToneCenterFreqSweep.  
---|---  
  
####  VB Syntax

|  imd.FrequencyCenterStart = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
imd |  A [SweptIMD](../Objects/SweptIMD_Object.md) Object  
value |  (Double) Start frequency in Hz. The F1 and F2 tones MUST be within the frequency range of the VNA.  
  
#### Return Type

|  Double  
  
#### Default

|  10.5 MHz  
  
#### Examples

|  imd.FrequencyCenterStart = 20e6 'Write  
value = imd.FrequencyCenterStart 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_FrequencyCenterStart(double *pVal)  
HRESULT put_FrequencyCenterStart(double newVal)  
  
#### Interface

|  ISweptIMD  
  
* * *

