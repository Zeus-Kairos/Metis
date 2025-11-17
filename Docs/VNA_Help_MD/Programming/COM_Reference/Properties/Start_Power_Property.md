##### Write/Read

|

##### [About Power Sweep](../../../S1_Settings/Sweep.md#power)  
  
---|---  
  
## StartPower Property

* * *

#### Description

|  Sets the start power of the analyzer when [sweep
type](Sweep_Type_Property.htm) is set to Power Sweep. Frequency of the
measurement is set with chan.[CWFrequency](CW_Frequency_Property.md).  
---|---  
  
####  VB Syntax

|  object.StartPower = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  One of the following:

  * [Channel](../Objects/Channel_Object.md) (object)
  * [CalSet](../Objects/CalSet_Object.md) (object) - Read-only property

  
value |  (double) \- Start Power in dBm. Note: The range of settable power values depends on the VNA model and if source attenuators are installed. To determine the range of values, use [cap.MaximumSourceALCPower](MaximumSourceALCPower_Property.md) and [cap.MinimumSourceALCPower](MinimumSourceALCPower_Property.md) Auto attenuation is not allowed in Power Sweep.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  Chan.StartPower = -10 'Write  
strtpwr = Chan.StartPower 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_StartPower(double *pVal)  
HRESULT put_StartPower(double newVal)  
  
#### Interface

|  IChannel |CalSet3  
  
* * *

