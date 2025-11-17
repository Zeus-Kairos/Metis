##### Write/Read

|

##### About [Mixer
Configuration](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
## InputFixedFrequency Property

* * *

#### Description

|  Sets or returns the mixer fixed Input frequency value. If you are changing
several mixer configuration settings, you can make all the changes first and
then issue the [Calculate](../Methods/Calculate_Method.md) and
[Apply](../Methods/Apply_Method.md) commands as you would do from the user
interface.  
---|---  
  
####  VB Syntax

|  obj.InputFixedFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Mixer Interface](../Objects/IMixer_Interface.md) pointer to the [Measurement](../Objects/Measurement_Object.md) (object) Or A [Converter Object](../Objects/Converter_Object.md)  
value |  (double) \- Input Fixed Frequency in Hertz.  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  mixer.InputFixedFrequency = 1e9  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_InputFixedFrequency(double *pVal) HRESULT
put_InputFixedFrequency(double newVal)  
  
#### Interface

|  IMixer6 IConverter  
  
* * *

