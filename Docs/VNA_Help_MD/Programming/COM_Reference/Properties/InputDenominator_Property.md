##### Write/Read

|

##### About [Mixer
Configuration](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
## InputDenominator Property

* * *

#### Description

|  Sets or returns the denominator value of the Input Fractional Multiplier.
If you are changing several mixer configuration settings, you can make all the
changes first and then issue the [Calculate](../Methods/Calculate_Method.md)
and [Apply](../Methods/Apply_Method.md) commands as you would do from the
user interface.  
---|---  
  
####  VB Syntax

|  obj.InputDenominator = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Mixer Interface](../Objects/IMixer_Interface.md) pointer to the [Measurement](../Objects/Measurement_Object.md) (object) Or A [Converter Object](../Objects/Converter_Object.md)  
value |  (Long) \- Input denominator value.  
  
#### Return Type

|  Long  
  
#### Default

|  1  
  
#### Examples

|  Print mixer.InputDenominator 'prints the value of the InputDenominator  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_InputDenominator(long *pVal) HRESULT put_InputDenominator(long
newVal)  
  
#### Interface

|  IMixer IConverter  
  
* * *

