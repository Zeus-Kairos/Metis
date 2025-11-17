##### Write/Read

|

##### About [Mixer
Configuration](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
## IFNumerator Property

* * *

#### Description

|  Sets or returns the numerator value of the IF Fractional Multiplier. Only
applies to 2 stage mixers. If you are changing several mixer configuration
settings, you can make all the changes first and then issue the
[Calculate](../Methods/Calculate_Method.md) and
[Apply](../Methods/Apply_Method.md) commands as you would do from the user
interface.  
---|---  
  
####  VB Syntax

|  conv.IFNumerator = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
conv |  A [Converter](../Objects/Converter_Object.md) (object)  
value |  (Long) IF Numerator value.  
  
#### Return Type

|  long  
  
#### Default

|  1  
  
#### Examples

|  Print mixer.IFNumerator 'prints the value of the IFNumerator  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_IFNumerator(long *pVal) HRESULT put_IFNumerator(long newVal)  
  
#### Interface

|  IConverter4  
  
* * *

