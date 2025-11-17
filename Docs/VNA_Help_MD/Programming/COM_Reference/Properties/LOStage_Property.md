##### Write/Read

|

##### About [Mixer
Configuration](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
## LOStage Property

* * *

#### Description

|  Sets or returns the number of LO stages present in the mixer.  
---|---  
  
####  VB Syntax

|  obj.LOStage = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Mixer Interface](../Objects/IMixer_Interface.md) pointer to the [Measurement](../Objects/Measurement_Object.md) (object) Or A [Converter Object](../Objects/Converter_Object.md)  
value |  (Long) \- Number of LO stages. Choose from 1 or 2  
  
#### Return Type

|  Long  
  
#### Default

|  1  
  
#### Examples

|  mixer.LOStage = 1 'sets the LO Stage value to 1  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_LOStage(long *pVal) HRESULT put_LOStage(long newVal)  
  
#### Interface

|  IMixer IConverter  
  
* * *

