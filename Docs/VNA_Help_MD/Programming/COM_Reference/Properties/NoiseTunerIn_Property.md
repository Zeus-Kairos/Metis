##### Write/Read

|

##### [About Noise Figure](../../../Applications/Noise_Figure.md)  
  
---|---  
  
## NoiseTunerIn Property

* * *

#### Description

|  Sets and returns the port identifier of the ECal noise tuner that is
connected to the VNA Source.  
---|---  
  
####  VB Syntax

|  noise.NoiseTunerIn = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
noise |  A [NoiseFigure](../Objects/NoiseFigure_Object.md) (object)  
value |  (string) Noise Tuner port identifier that is connected to the VNA source, as it is labeled on the ECal module. For example, for 2-port ECal modules, choose either "A" or "B".  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  noise.NoiseTunerIn = "A"'Write  
EcalPort = noise.NoiseTunerIn 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_NoiseTunerIn(BSTR* pValue) HRESULT put_NoiseTunerIn(BSTR
pNewValue)  
  
#### Interface

|  INoiseFigure  
  
* * *

