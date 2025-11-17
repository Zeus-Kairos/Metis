##### Write/Read

|

##### About [Mixer
Configuration](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
## InputNumerator Property

* * *

#### Description

|  Sets or returns the numerator value of the Input Fractional Multiplier. If
you are changing several mixer configuration settings, you can make all the
changes first and then issue the [Calculate](../Methods/Calculate_Method.md)
and [Apply](../Methods/Apply_Method.md) commands as you would do from the
user interface.  
---|---  
  
####  VB Syntax

|  obj.InputNumerator = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Mixer Interface](../Objects/IMixer_Interface.md) pointer to the [Measurement](../Objects/Measurement_Object.md) (object) Or A [Converter Object](../Objects/Converter_Object.md)  
value |  (Long) \- Input numerator value.  
  
#### Return Type

|  Long  
  
#### Default

|  1  
  
#### Examples

|  Print mixer.InputNumerator 'prints the value of the InputNumerator  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_InputNumerator(long *pVal) HRESULT put_InputNumerator(long
newVal)  
  
#### Interface

|  IMixer IConverter  
  
* * *

