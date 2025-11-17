##### Write/Read

|

##### [About Swept IMD](../../../Applications/Swept_IMD.md)  
  
---|---  
  
## FrequencyCenterCenter Property

* * *

#### Description

|  Sets and returns the sweep center frequency when sweeping the main tones.
Use with sweep type = naIMDToneCenterFreqSweep.  
---|---  
  
####  VB Syntax

|  imd.FrequencyCenterCenter = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
imd |  A [SweptIMD](../Objects/SweptIMD_Object.md) Object  
value |  (Double) Center frequency in Hz. The F1 and F2 tones MUST be within the frequency range of the VNA.  
  
#### Return Type

|  Double  
  
#### Default

|  13.255 GHz  
  
#### Examples

|  imd.FrequencyCenterCenter = 10e9 'Write  
value = imd.FrequencyCenterCenter 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_FrequencyCenterCenter(double *pVal)  
HRESULT put_FrequencyCenterCenter(double newVal)  
  
#### Interface

|  ISweptIMD  
  
* * *

