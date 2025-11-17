##### Write/Read

|

##### About [Mixer
Configuration](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
## InputPower Property

* * *

#### Description

|  Sets or returns the value of the Input Power. If you are changing several
mixer configuration settings, you can make all the changes first and then
issue the [Calculate](../Methods/Calculate_Method.md) and
[Apply](../Methods/Apply_Method.md) commands as you would do from the user
interface.  
---|---  
  
####  VB Syntax

|  obj.InputPower = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Mixer Interface](../Objects/IMixer_Interface.md) pointer to the [Measurement](../Objects/Measurement_Object.md) (object) Or A [Converter Object](../Objects/Converter_Object.md)  
value |  (double) \- Input power in dBm.  
  
#### Return Type

|  Double  
  
#### Default

|  -15 dBm for IMixer -20 dBm for IConverter  
  
#### Examples

|  Print mixer.InputPower 'prints the value of the InputPower  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_InputPower(double *pVal) HRESULT put_InputPower(double newVal)  
  
#### Interface

|  IMixer IConverter  
  
* * *

