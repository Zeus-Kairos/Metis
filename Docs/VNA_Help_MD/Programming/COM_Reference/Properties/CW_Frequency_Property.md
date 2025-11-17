##### Write/Read

|

##### [About CW Frequency](../../../S1_Settings/Frequency_Range.md#cw_freq)  
  
---|---  
  
## CWFrequency Property

* * *

#### Description

|  Set the Continuous Wave (CW) frequency. Must first send chan.SweepType =
naCWTimeSweep. See Also: [calset.CWFrequency
Property](CWFrequency_CS_Property.htm)  
---|---  
  
####  VB Syntax

|  object.CWFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  One of the following:

  * [Channel](../Objects/Channel_Object.md) (object)
  * [FOMRange](../Objects/FOMRange_Object.md) (object) Range must be [UNCOUPLED](Coupled_Property.md).

See also
[Measurement2](../Objects/Measurement_Object.md#IMeasurement2Interface)
interface.  
value |  (double) CW frequency. Choose any number between:  
the minimum and maximum frequency limits of the analyzer  
Units are Hz  
  
#### Return Type

|  Double  
  
#### Default

|  1e9  
  
#### Examples

|  chan.CWFrequency = 5e9 'Write  
cwfreq = chan.CWFrequency 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_CWFrequency(double newVal)  
HRESULT get_CWFrequency(double *pVal)  
  
#### Interface

|  IChannel IFOMRange

