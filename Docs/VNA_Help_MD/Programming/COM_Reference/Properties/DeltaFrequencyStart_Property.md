##### Write/Read

|

##### [About Swept IMD](../../../Applications/Swept_IMD.md)  
  
---|---  
  
## DeltaFrequencyStart Property

* * *

#### Description

|  Sets and returns the starting main tone separation for [sweep
type](SweepType_imd_Property.htm)= naIMDDeltaFrequencySweep  
---|---  
  
####  VB Syntax

|  imd.DeltaFrequencyStart = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
imd |  A [SweptIMD](../Objects/SweptIMD_Object.md) Object  
value |  (Double) - Starting tone separation between F1 and F2 in Hz. Both F1 and F2 tones MUST be within the frequency range of the VNA where: F1 (start) = imd.FrequencyCenter  imd.DeltaFrequencyStart / 2 F2 (start) = imd.FrequencyCenter + imd.DeltaFrequencyStart / 2  
  
#### Return Type

|  Double  
  
#### Default

|  1 MHz  
  
#### Examples

|  imd.DeltaFrequencyStart = 5e6 'Write  
value = imd.DeltaFrequencyStart 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_DeltaFrequencyStart(double *pVal))  
HRESULT put_DeltaFrequencyStart(double newVal)  
  
#### Interface

|  ISweptIMD  
  
* * *

