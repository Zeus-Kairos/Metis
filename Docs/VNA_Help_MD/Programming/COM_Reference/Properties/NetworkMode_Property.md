##### Read-Write

|

##### [About FCA
embed/deembed](../../../FreqOffset/VMC_Measurements.htm#Waveguide)  
  
---|---  
  
## NetworkMode Property

* * *

#### Description

|  Allows you to embed (add) or de-embed (remove) circuit network effects on
the input and output of your mixer measurement.  
---|---  
  
#### VB Syntax

|  object.NetworkMode(n) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  [SMCType](../Objects/SMC_Type_Object.md) (object) or [VMCType](../Objects/VMC_Type_Object.md) (object)  
n |  (Integer) Apply network to input or output of mixer. Choose from: 1 \- Input of mixer 2 \- Output of mixer  
value |  (ENum as ENetworkMode) Choose from: NO_NETWORK Do nothing with effects of S2P file EMBED_NETWORK \- Add effects of S2P file from the measurement results. DEEMBED_NETWORK \- Remove effects of S2P file from the measurement results.  
  
#### Return Type

|  Enum  
  
#### Default

|  NO_NETWORK  
  
#### Examples

|  VMC.NetworkMode = EMBED_NETWORK  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_NetworkMode(short networkNum, enum ENetworkMode networkMode);
HRESULT get_NetworkMode(short networkNum, enum ENetworkMode *networkMode);  
  
#### Interface

|  SMCType2 VMCType2

