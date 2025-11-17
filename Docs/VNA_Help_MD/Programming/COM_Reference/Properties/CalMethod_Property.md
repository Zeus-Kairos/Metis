##### Write/Read

|

##### [About Noise Figure](../../../Applications/Noise_Figure.md)  
  
---|---  
  
## CalMethod Property

* * *

#### Description

|  Sets and returns the method for performing calibration on a noise channel.  
---|---  
  
####  VB Syntax

|  noise.CalMethod = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
noise |  A [NoiseCal](../Objects/NoiseCal_Object.md) (object)  
value |  (string) Cal Method. Choose from:

  * "VectorFull" or "Vector"
  * "SParameter" (Not available for NFX measurements)
  * "ScalarFull" or "Scalar"

  
  
#### Return Type

|  String  
  
#### Default

|  "VectorFull"  
  
#### Examples

|  noise.CalMethod = "VectorFull"'Write  
calMethod = noise.CalMethod 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CalMethod(BSTR* pValue) HRESULT put_CalMethod(BSTR pNewValue)  
  
#### Interface

|  INoiseCal  
  
* * *

  

