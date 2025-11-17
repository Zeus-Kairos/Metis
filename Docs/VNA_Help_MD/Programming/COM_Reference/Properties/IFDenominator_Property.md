##### Write/Read

|

##### About [Mixer
Configuration](../../../Applications/MixerConverter_Setup.htm)  
  
---|---  
  
## IFDenominator Property

* * *

#### Description

|  Sets or returns the denominator value of the IF Fractional Multiplier. Only
applies to 2 stage mixers. If you are changing several mixer configuration
settings, you can make all the changes first and then issue the
[Calculate](../Methods/Calculate_Method.md) and
[Apply](../Methods/Apply_Method.md) commands as you would do from the user
interface.  
---|---  
  
####  VB Syntax

|  conv.IFDenominator = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
conv |  A  [Converter](../Objects/Converter_Object.md) (object)  
value |  (long) IF Denominator value.  
  
#### Return Type

|  Long  
  
#### Default

|  1  
  
#### Examples

|  Print mixer.IFDenominator 'prints the value of the IFDenominator  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_IFDenominator(long *pVal) HRESULT put_IFDenominator(long
newVal)  
  
#### Interface

|  IConverter4  
  
* * *

