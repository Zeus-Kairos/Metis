##### Read-only

|

##### [About Gain
Compression](../../../Applications/Gain_Compression_Application.htm)  
  
---|---  
  
## DeviceInputPort Property

* * *

#### Description

|  Read the VNA port number which is connected to the DUT input. Use
[SetPortMap Method](../Methods/SetPortMap_Method.md) to change the port
mapping.  
---|---  
  
####  VB Syntax

|  obj.DeviceInputPort  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Converter](../Objects/Converter_Object.md) (object) or A [GainCompression](../Objects/GainCompression_Object.md) (object) or A [SweptIMD](../Objects/SweptIMD_Object.md) (object) or An [IMSpectrum](../Objects/IMSpectrum_Object.md) (object) A [NoiseFigure](../Objects/NoiseFigure_Object.md) (object)  
  
#### Return Type

|  Integer  
  
#### Default

|  1  
  
#### Examples

|  inPort = gca.DeviceInputPort 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_DeviceInputPort(int* pVal)  
  
#### Interface

|  IGainCompression ISweptIMD IMSpectrum INoiseFigure6 IConverter6  
  
* * *

