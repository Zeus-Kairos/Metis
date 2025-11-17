##### Write/Read

|

##### [About Noise Figure](../../../Applications/Noise_Figure.md)  
  
---|---  
  
## NoiseTuner Property

* * *

#### Description

|  Sets and returns the noise tuner identifier, which is an ECal model and
serial number string.  
---|---  
  
####  VB Syntax

|  noise.NoiseTuner = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
noise |  A [NoiseFigure](../Objects/NoiseFigure_Object.md) (object)  
value |  (string) Noise Tuner. Return the connected ECal identifiers by sending GetCalKitTypeString and passing the module number.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  noise.NoiseTuner = "N4691-60004 ECal 02822"'Write  
noiseT = noise.NoiseTuner 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_NoiseTuner(BSTR* pValue) HRESULT put_NoiseTuner(BSTR pNewValue)  
  
#### Interface

|  INoiseFigure  
  
* * *

