##### Write/Read

|

##### [About Swept IMD](../../../Applications/Swept_IMD.md)  
  
---|---  
  
## DeltaFrequencyStop Property

* * *

#### Description

|  Sets and returns the stop spacing of the main tones. Use with [sweep
type](SweepType_imd_Property.htm)= naIMDDeltaFrequencySweep  
---|---  
  
####  VB Syntax

|  imd.DeltaFrequencyStop = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
imd |  A [SweptIMD](../Objects/SweptIMD_Object.md) Object  
value |  (Double) - Stopping tone separation between F1 and F2 in Hz. Both F1 and F2 tones MUST be within the frequency range of the VNA where: F1 (stop) = imd.FrequencyCenter  imd.DeltaFrequencyStop / 2 F2 (stop) = imd.FrequencyCenter + imd.DeltaFrequencyStop / 2  
  
#### Return Type

|  Double  
  
#### Default

|  10 MHz  
  
#### Examples

|  imd.DeltaFrequencyStop = 20e6 'Write  
value = imd.DeltaFrequencyStop 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_DeltaFrequencyStop(double *pVal))  
HRESULT put_DeltaFrequencyStop(double newVal)  
  
#### Interface

|  ISweptIMD  
  
* * *

