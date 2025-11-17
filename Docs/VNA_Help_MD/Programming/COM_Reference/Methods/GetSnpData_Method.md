##### Read-only

|

##### [Learn about Noise
Parameters](../../../Applications/Noise_Figure.htm#NoiseParams)  
  
---|---  
  
## GetSnPData Method

* * *

#### Description

|  Returns noise parameter and S-parameter S2P data for vector noise figure
measurements. Noise parameters are NOT valid for NFX or Scalar noise figure
measurements.  
---|---  
  
####  VB Syntax

|  data = nf.GetSnPData type  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
data |  Variant array to store the data.  
nf |  A [NoiseFigure](../Objects/NoiseFigure_Object.md) (object)  
type |  (string) \- Choose "NoiseParameter" \- Noise parameter data.  
  
#### Return Type

|  Variant  3 dimensional array. First dimension size is number of parameters
returned Second dimension size is number of points in the channel. Third
dimension size is 2; format is specified with [SnPFormat
Property](../Properties/SnPFormat_Property.htm) Data is returned in this
order: <real S11> <imag S11> <real S21> <imag S21> <real S12> <imag S12> <real
S22> <imag S22> Then noise parameters: <NFMin dB> <mag GammaOpt> <phase
GammaOpt> <Rn/Z0>  
  
#### Default

|  Not Applicable  
  
#### Examples

|  snp = nf.GetSnPData("NoiseParameter")  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT GetSnPData( BSTR type, VARIANT * response)  
  
#### Interface

|  INoiseFigure7  
  
* * *

