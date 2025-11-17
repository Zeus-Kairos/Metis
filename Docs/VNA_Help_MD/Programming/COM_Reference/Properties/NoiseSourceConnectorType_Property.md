##### Write/Read

|

##### [About Noise Figure](../../../Applications/Noise_Figure.md)  
  
---|---  
  
## NoiseSourceConnectorType Property

* * *

#### Description

|  Set and read the Noise Source connector type and gender. The Keysight 346C
has an "APC 3.5 male" connector.  
---|---  
  
####  VB Syntax

|  noise.NoiseSourceConnectorType = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
noise |  A [NoiseCal](../Objects/NoiseCal_Object.md) (object)  
value |  (string) Connector type. Use [ValidConnectorType](ValidConnectorType_Property.md) to return a list of valid connector types.  
  
#### Return Type

|  String  
  
#### Default

|  Not applicable  
  
#### Examples

|  noise.NoiseSourceConnectorType = "APC 3.5 male"'Write  
connector = noise.NoiseSourceConnectorType 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_NoiseSourceConnectorType(BSTR* pConnectorType) HRESULT
put_NoiseSourceConnectorType(BSTR pConnectorType)  
  
#### Interface

|  INoiseCal  
  
* * *

