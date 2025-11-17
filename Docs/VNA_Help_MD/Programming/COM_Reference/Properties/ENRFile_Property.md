##### Write/Read

|

##### [About Noise Figure](../../../Applications/Noise_Figure.md)  
  
---|---  
  
## ENRFile Property

* * *

#### Description

|  Sets and returns the name of the ENR file associated with the noise source.  
---|---  
  
####  VB Syntax

|  noise.ENRFile = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
noise |  A [NoiseCal](../Objects/NoiseCal_Object.md) (object)  
value |  (string) Full path and ENR filename.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  noise.ENRFile = "c:/ProgramFiles/Keysight/Network
Analyzer/Documents/ENR/346C.enr"'Write  
ENR = noise.ENRFile 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ENRFile(BSTR* pValue) HRESULT put_ENRFile(BSTR pNewValue)  
  
#### Interface

|  INoiseCal  
  
* * *

