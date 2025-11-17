##### Write/Read

|

##### [About Noise Figure](../../../Applications/Noise_Figure.md)  
  
---|---  
  
## NoiseSourceCalKitType Property

* * *

#### Description

|  Set and read the Cal Kit that will be used for the Noise Source adapter. An
adapter is always necessary to connect a 346C Noise Source to the VNA port 2.
Select a Cal Kit that is the same type and gender as the noise source
connector. If the Noise Source mates directly to VNA port 2, then set this
type to "None".  
---|---  
  
####  VB Syntax

|  noise.NoiseSourceCalKitType = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
noise |  A [NoiseCal](../Objects/NoiseCal_Object.md) (object)  
value |  (string) Cal Kit type. To read possible cal kit strings for the adapter:

  1. Change the port connector type to that of the noise source using: [ConnectorType](ConnectorType_Property.md)
  2. Then read the possible cal kit strings for that port using: [CompatibleCalKits](CompatibleCalKits_Property.md)

  
  
#### Return Type

|  String  
  
#### Default

|  Not applicable  
  
#### Examples

|  noise.NoiseSourceCalKitType = "N4691-60004 ECAL"'Write  
calkit = noise.NoiseSourceCalKitType 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_NoiseSourceCalKitType(BSTR* pValue) HRESULT
put_NoiseSourceCalKitType(BSTR pNewValue)  
  
#### Interface

|  INoiseCal  
  
* * *

