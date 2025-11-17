##### Write/Read

|

##### About [Mixer
Configuration](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
## LOFixedFrequency Property

* * *

#### Description

|  Sets or returns the LO frequency value. If you are changing several mixer
configuration settings, you can make all the changes first and then issue the
[Calculate](../Methods/Calculate_Method.md) and
[Apply](../Methods/Apply_Method.md) commands as you would do from the user
interface.  
---|---  
  
####  VB Syntax

|  obj.LOFixedFrequency (n) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Mixer Interface](../Objects/IMixer_Interface.md) pointer to the [Measurement](../Objects/Measurement_Object.md) (object) Or A [Converter Object](../Objects/Converter_Object.md)  
value |  (double) \- LO Frequency in Hertz.  
n |  (Long) \- LO stage number Choose from 1 or 2  
  
#### Return Type

|  Double  
  
#### Default

|  0 Hz  
  
#### Examples

|  Print mixer.LOFixedFrequency(1) 'prints the value of the first LO fixed
frequency  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_LOFixedFrequency(double *pVal) HRESULT
put_LOFixedFrequency(double newVal)  
  
#### Interface

|  IMixer IConverter  
  
* * *

